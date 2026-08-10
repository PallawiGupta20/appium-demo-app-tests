# Appium Mobile Test Automation — Sauce Labs Demo App

Automated UI tests for the Sauce Labs "My Demo App RN" Android app, written in Python using Appium and pytest.

## Setup
1. python3 -m venv venv && source venv/bin/activate
2. pip install -r requirements.txt
3. adb install path/to/app.apk
4. Run appium in a separate terminal
5. Make sure emulator is running (adb devices)

## Run tests
pytest tests/ -v
