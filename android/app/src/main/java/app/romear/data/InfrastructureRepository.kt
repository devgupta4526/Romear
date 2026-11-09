package app.romear.data

import java.io.IOException
import java.util.concurrent.TimeUnit
import javax.inject.Inject
import javax.inject.Singleton
import app.romear.BuildConfig
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import okhttp3.OkHttpClient
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET

data class ReadyResponse(val status: String?)

interface InfrastructureApi {
    @GET("ready")
    suspend fun ready(): retrofit2.Response<ReadyResponse>
}

enum class ConnectionResult { READY, UNAVAILABLE, OFFLINE }

class InfrastructureRepository @Inject constructor(private val api: InfrastructureApi) {
    suspend fun check(): ConnectionResult = try {
        val response = api.ready()
        if (response.isSuccessful && response.body()?.status == "ready") ConnectionResult.READY
        else ConnectionResult.UNAVAILABLE
    } catch (_: com.google.gson.stream.MalformedJsonException) {
        ConnectionResult.UNAVAILABLE
    } catch (_: com.google.gson.JsonParseException) {
        ConnectionResult.UNAVAILABLE
    } catch (_: IOException) {
        ConnectionResult.OFFLINE
    }
}

@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {
    @Provides
    @Singleton
    fun api(): InfrastructureApi {
        check(!BuildConfig.ALLOW_TEST_DATA || (BuildConfig.DEBUG && BuildConfig.ENVIRONMENT == "dev"))
        val client = OkHttpClient.Builder()
            .connectTimeout(5, TimeUnit.SECONDS)
            .readTimeout(5, TimeUnit.SECONDS)
            .callTimeout(10, TimeUnit.SECONDS)
            .retryOnConnectionFailure(false)
            .build()
        return Retrofit.Builder().baseUrl(BuildConfig.API_BASE_URL).client(client)
            .addConverterFactory(GsonConverterFactory.create()).build()
            .create(InfrastructureApi::class.java)
    }
}
