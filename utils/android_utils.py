import subprocess


class DevicesNotFoundException(Exception):
    pass


def get_udid() -> str:
    devices = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    try:
        return devices.stdout.split()[4]
    except Exception:
        raise DevicesNotFoundException("There is no devices connected to your machine")


def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': get_udid(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }
