package app.romear

import androidx.test.core.app.ActivityScenario
import androidx.test.espresso.Espresso.onView
import androidx.test.espresso.assertion.ViewAssertions.matches
import androidx.test.espresso.matcher.ViewMatchers.isDisplayed
import androidx.test.espresso.matcher.ViewMatchers.withId
import androidx.test.ext.junit.runners.AndroidJUnit4
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class ShellSmokeTest {
    @Test
    fun shellLaunchesAndSurvivesRecreation() {
        ActivityScenario.launch(MainActivity::class.java).use { scenario ->
            onView(withId(R.id.shell_title)).check(matches(isDisplayed()))
            onView(withId(R.id.check_connection)).check(matches(isDisplayed()))
            scenario.recreate()
            onView(withId(R.id.connection_status)).check(matches(isDisplayed()))
        }
    }
}
