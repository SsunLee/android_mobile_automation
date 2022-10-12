blackButton = '//android.view.View[6]/android.view.View/android.view.View/android.view.View/android.widget.Button' # 검정색 버튼 모두
gotoHomeButton = '//android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.Button' # 홈으로 가기
courseButton = '//androidx.compose.ui.platform.ComposeView[2]/android.view.View/android.view.View[1]' # 추천 학습 셀
courseTitleText = '//androidx.compose.ui.platform.ComposeView[2]/android.view.View/android.view.View[1]/android.view.View[3]' # 추천 학습 셀 타이틀
anwserTest = '//android.view.View[5]/android.view.View/android.view.View[6]'
startSoundCheck = '//android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.widget.Button'
startTestPrep = '//android.view.View/android.view.View[3]/android.view.View/android.view.View[3]/android.widget.Button'
soundPlayWhenLCblack = '//android.view.View/android.view.View[1]/android.view.View/android.view.View[6]/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'
testPrepPopup = '//android.widget.Button'

device_cap_aws = {
                "platformName": "Android",
                "appium:deviceName": "Android Emulator",
                "appium:automationName": "Appium",
                "appium:newCommandTimeout": "1000",
                "appium:appPackage": "co.riiid.vida.staging",
                "appium:appActivity": "co.riiid.vida.ui.splash.SplashActivity"
            }


def getPath(usrName, filename):  
    appPath = f"/Users/{usrName}/Downloads/{filename}.apk"
    device_cap = {
                    "platformName": "Android",
                    "appium:platformVersion": "11.0",
                    "appium:deviceName": "Android Emulator",
                    "appium:app": appPath,
                    "appium:automationName": "Appium",
                    "appium:newCommandTimeout": "1000",
                    "appium:appPackage": "co.riiid.vida.staging",
                    "appium:appActivity": "co.riiid.vida.ui.splash.SplashActivity"
                }

    return device_cap

print(getPath('sunbae', '27777.apk'))