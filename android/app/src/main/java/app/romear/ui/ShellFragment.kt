package app.romear.ui

import android.os.Bundle
import android.view.View
import androidx.core.view.isVisible
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.lifecycleScope
import androidx.lifecycle.repeatOnLifecycle
import app.romear.R
import app.romear.databinding.FragmentShellBinding
import dagger.hilt.android.AndroidEntryPoint
import kotlinx.coroutines.launch

@AndroidEntryPoint
class ShellFragment : Fragment(R.layout.fragment_shell) {
    private var binding: FragmentShellBinding? = null
    private val model: ShellViewModel by viewModels()

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val views = FragmentShellBinding.bind(view)
        binding = views
        views.checkConnection.setOnClickListener { model.checkConnection() }
        viewLifecycleOwner.lifecycleScope.launch {
            viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
                model.state.collect { state ->
                    views.progress.isVisible = state == ShellState.CHECKING
                    views.checkConnection.isEnabled = state != ShellState.CHECKING
                    views.connectionStatus.setText(when (state) {
                        ShellState.EMPTY -> R.string.connection_empty
                        ShellState.CHECKING -> R.string.connection_checking
                        ShellState.READY -> R.string.connection_ready
                        ShellState.UNAVAILABLE -> R.string.connection_unavailable
                        ShellState.OFFLINE -> R.string.connection_offline
                    })
                }
            }
        }
    }

    override fun onDestroyView() {
        binding = null
        super.onDestroyView()
    }
}
