package app.romear.ui

import app.romear.data.InfrastructureApi
import app.romear.data.InfrastructureRepository
import app.romear.data.ReadyResponse
import kotlinx.coroutines.CompletableDeferred
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.test.StandardTestDispatcher
import kotlinx.coroutines.test.advanceUntilIdle
import kotlinx.coroutines.test.resetMain
import kotlinx.coroutines.test.runTest
import kotlinx.coroutines.test.setMain
import org.junit.Assert.assertEquals
import org.junit.Test
import retrofit2.Response

@OptIn(ExperimentalCoroutinesApi::class)
class ShellViewModelTest {
    @Test
    fun duplicateTapIsIgnoredAndFailureCanRetry() = runTest {
        Dispatchers.setMain(StandardTestDispatcher(testScheduler))
        try {
            var calls = 0
            val gate = CompletableDeferred<Unit>()
            val api = object : InfrastructureApi {
                override suspend fun ready(): Response<ReadyResponse> {
                    calls++
                    gate.await()
                    return if (calls == 1) Response.success(ReadyResponse("stale"))
                    else Response.success(ReadyResponse("ready"))
                }
            }
            val model = ShellViewModel(InfrastructureRepository(api))
            assertEquals(ShellState.EMPTY, model.state.value)
            model.checkConnection()
            model.checkConnection()
            assertEquals(ShellState.CHECKING, model.state.value)
            gate.complete(Unit)
            advanceUntilIdle()
            assertEquals(1, calls)
            assertEquals(ShellState.UNAVAILABLE, model.state.value)
            model.checkConnection()
            advanceUntilIdle()
            assertEquals(ShellState.READY, model.state.value)
        } finally {
            Dispatchers.resetMain()
        }
    }
}
