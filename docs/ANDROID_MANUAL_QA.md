# Stage 00 device checks — owner to run

Device/emulator testing was explicitly delegated to the owner on 10 November 2026.
No current-build emulator screenshot, visual approval, TalkBack pass or device test
pass is claimed by Codex.

1. Start/migrate the local API as in README.md. Confirm `/ready` returns HTTP 200.
2. In `android/`, run `./gradlew.bat :app:assembleDebug`, then install the actual build:

   ```powershell
   adb devices -l
   adb install -r app/build/outputs/apk/debug/app-debug.apk
   adb shell dumpsys package app.romear.dev
   adb shell am start -n app.romear.dev/app.romear.MainActivity
   ```

   On the emulator the default API host is `10.0.2.2:8000`. For a USB device, use
   `adb reverse tcp:8000 tcp:8000` and rebuild with
   `-PDEV_API_URL=http://127.0.0.1:8000/`.
3. Confirm the cream/forest branded empty shell appears. No feed, accounts, bookings,
   fake activity or bottom navigation is expected in Stage 00.
4. Tap **Check connection**. The button disables while checking. A successful real
   `/ready` response shows that the service and DB are ready. Repeated fast taps
   must not start duplicate checks. Rotate while checking/after a result and retry.
5. Stop the development DB while keeping the API running. `/health` should still
   work; `/ready` should fail with 503, and the app must show the service unavailable
   state. Restart the DB; retry must recover. Stop the API to test the connection
   failure message. Neither failure can become a local success.
6. Test compact portrait, landscape, large font and TalkBack: all text remains
   readable/scrollable, the button remains reachable and >=48dp, content avoids
   system bars, status changes are announced, and Back exits this sole root route.
   There is no keyboard or runtime permission prompt in this stage.

Optional automated device smoke check (launch and Activity recreation only):

```powershell
./gradlew.bat :app:connectedDebugAndroidTest
```

Record results/screenshots in BUILD_STATUS.md before declaring the device gate passed.
