package app.romear.data

import kotlinx.coroutines.test.runTest
import okhttp3.mockwebserver.MockResponse
import okhttp3.mockwebserver.MockWebServer
import org.junit.Assert.assertEquals
import org.junit.Test
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class InfrastructureRepositoryTest {
    @Test
    fun onlyServerReadinessConfirmsSuccess() = runTest {
        val server = MockWebServer()
        server.start()
        try {
            val api = Retrofit.Builder().baseUrl(server.url("/"))
                .addConverterFactory(GsonConverterFactory.create()).build()
                .create(InfrastructureApi::class.java)
            val repository = InfrastructureRepository(api)
            for ((body, code, expected) in listOf(
                Triple("{\"status\":\"ready\"}", 200, ConnectionResult.READY),
                Triple("{\"status\":\"ok\"}", 200, ConnectionResult.UNAVAILABLE),
                Triple("{}", 200, ConnectionResult.UNAVAILABLE),
                Triple("{\"error\":{\"code\":\"database_unavailable\"}}", 503, ConnectionResult.UNAVAILABLE),
                Triple("{}", 401, ConnectionResult.UNAVAILABLE),
                Triple("invalid-json", 200, ConnectionResult.UNAVAILABLE),
            )) {
                server.enqueue(MockResponse().setResponseCode(code).setBody(body))
                assertEquals(expected, repository.check())
                assertEquals("/ready", server.takeRequest().path)
            }
        } finally {
            server.shutdown()
        }
    }

    @Test
    fun ioFailureDoesNotBecomeSuccess() = runTest {
        val api = object : InfrastructureApi {
            override suspend fun ready(): retrofit2.Response<ReadyResponse> {
                throw java.io.IOException("offline")
            }
        }
        assertEquals(ConnectionResult.OFFLINE, InfrastructureRepository(api).check())
    }
}
