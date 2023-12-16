from appium.webdriver.common.appiumby import AppiumBy


LOGIN_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/authHelloLogin")
LOGIN_AND_PASSWORD_FIELDS = (AppiumBy.XPATH,
                             "//android.widget.EditText[@resource-id=\"defaultAutomationId\"]")
PERFORM_LOGIN_BUTTON = (AppiumBy.XPATH,
                        "//*[@resource-id=\"com.ajaxsystems:id/text\" and @text=\"Вхід\"]")
ADD_HUB_BUTTON = (AppiumBy.ID,
                  "com.ajaxsystems:id/hubAdd")
