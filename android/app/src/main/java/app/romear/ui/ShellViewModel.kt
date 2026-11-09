package app.romear.ui

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import app.romear.data.ConnectionResult
import app.romear.data.InfrastructureRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import javax.inject.Inject
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

enum class ShellState { EMPTY, CHECKING, READY, UNAVAILABLE, OFFLINE }

@HiltViewModel
class ShellViewModel @Inject constructor(private val repository: InfrastructureRepository) : ViewModel() {
    private val mutableState = MutableStateFlow(ShellState.EMPTY)
    val state = mutableState.asStateFlow()

    fun checkConnection() {
        if (mutableState.value == ShellState.CHECKING) return
        mutableState.value = ShellState.CHECKING
        viewModelScope.launch {
            mutableState.value = when (repository.check()) {
                ConnectionResult.READY -> ShellState.READY
                ConnectionResult.UNAVAILABLE -> ShellState.UNAVAILABLE
                ConnectionResult.OFFLINE -> ShellState.OFFLINE
            }
        }
    }
}
