import random
import unittest
import os
from unittest import suite
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class TableSearchTest(unittest.TestCase):
    blackButton = '//android.view.View[6]/android.view.View/android.view.View/android.view.View/android.widget.Button' # 검정색 버튼 모두
    gotoHomeButton = '//android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.Button' # 홈으로 가기
    courseButton = '//androidx.compose.ui.platform.ComposeView[2]/android.view.View/android.view.View[1]' # 추천 학습 셀
    courseTitleText = '//androidx.compose.ui.platform.ComposeView[2]/android.view.View/android.view.View[1]/android.view.View[3]' # 추천 학습 셀 타이틀
    anwserTest = '//android.view.View[5]/android.view.View/android.view.View[6]'
    startSoundCheck = '//android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.widget.Button'
    startTestPrep = '//android.view.View/android.view.View[3]/android.view.View/android.view.View[3]/android.widget.Button'
    soundPlayWhenLCblack = '//android.view.View/android.view.View[1]/android.view.View/android.view.View[6]/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'
    testPrepPopup = '//android.widget.Button'
    def setUp(self):
        
        cmd = 'adb shell su 0 setprop gsm.sim.operator.iso-country kr'
        os.popen(cmd)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                "platformName": "Android",
                "appium:platformVersion": "11.0",
                "appium:deviceName": "Android Emulator",
                "appium:app": "Users/riiid/Downloads/27688948.apk",
                "appium:automationName": "Appium",
                "appium:newCommandTimeout": "1000",
                "appium:appPackage": "co.riiid.vida",
                "appium:appActivity": "co.riiid.vida.ui.splash.SplashActivity"
            })

    def test_addToAsset(self):
        driver = self.driver
        driver.implicitly_wait(10)

        # Email login 
        self.email_login() 

        try:
            getTitle = driver.find_element(By.XPATH, self.courseTitleText).get_attribute('text')
            recommended_cell = driver.find_element(By.XPATH, self.courseButton)
            recommended_cell.click()
            print(f'{getTitle}')
            sleep(2.9)

            if getTitle.find('쪽지') >= 0:
                self.selectAnswer(True)
            elif getTitle.find('어휘 암기') >= 0:
                self.VocaTest()
            else:
                self.selectAnswer()
        except Exception as e:
            print(f'Exception : {e}')
        


    def selectAnswer(self, isReview=False):
        driver = self.driver
        isEnd = False
        isNext = False
        self.isPoupExist()
        self.isSoundPopup()
        print("팝업 체크")

        print("select answser 진입")

        # 답안 체크 
        while(True):
            try:
                # check anwser
                self.isPoupExist()
                selector = self.getSelectAnswer()
                driver.find_element(By.XPATH, selector).click()
                print("답안 체크")
                sleep(1.2)            

                if self.isShown(self.blackButton):
                    break
                else:
                    selector = self.getSelectAnswer()
                    driver.find_element(By.XPATH, selector).click()
            except NoSuchElementException:
                print('not found')
                break
        # 정답 확인하기 
        while(True):
            # check anwser 
            isNext = False
            try:
                self.isPoupExist()
                self.isSoundPopup()
                btnText = driver.find_element(By.XPATH, self.blackButton).get_attribute('text')
                print(f'found > {btnText}')
            except NoSuchElementException:
                selector = self.getSelectAnswer()
                driver.find_element(By.XPATH, selector).click()

            if btnText.find('정답 확인하기') >= 0:
                sleep(1.2)
                driver.find_element(By.XPATH, self.blackButton).click()
                # if hilight pop up
                self.isPoupExist()
                self.isSoundPopup()
                isNext = True
            
            if isNext:
                sleep(1.2)
                btnBlackBar = driver.find_element(By.XPATH, self.blackButton)
                btnText = btnBlackBar.get_attribute('text')
                print(f'found > {btnText}')
                self.isSoundPopup()
                if btnText.find('다음 문제') >= 0:
                    driver.find_element(By.XPATH, self.blackButton).click()
                    sleep(0.8)
                elif btnText.find('학습 종료하기') >= 0:
                    # 쪽지 시험이라면 
                    if isReview:
                        sleep(1)
                        driver.find_element(By.XPATH, self.blackButton).click()
                        print('학습 종료하기 버튼 클릭')
                        sleep(1)

                        for i in range(0,1):
                            sleep(2)
                            # n Cycle 결과보기 -> n Cycle 시작하기
                            btnElement = driver.find_element(By.XPATH, self.gotoHomeButton)
                            btnElement.click()
                            print(f'{btnElement.text} 버튼 클릭')
                    else:
                        self.TestPrep_End(isEnd)
                else:
                    if self.isShown(self.blackButton):
                        driver.find_element(By.XPATH, self.blackButton).click()
                        print("re click")
                    #return True
                    

    def VocaTest(self):
        driver = self.driver
        isHomework = False
        while(True):
            # 어휘 학습 
            # 아는 단어네요 or 정확히 똑같아요! 
            knowTextTop = '//android.view.View[4]/android.view.View/android.view.View/android.view.View[2]/android.widget.Button'
            knowTextBottom = '//android.view.View[4]/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'
            QuestionType = '//android.view.View[1]/android.view.View/android.widget.TextView'
            if driver.find_element(By.XPATH, QuestionType).is_displayed():
                self.selectAnswer()
            else:
                knowBtn = driver.find_element(By.XPATH, knowTextTop)
                knowBtn.click()

                # 복습이 있다면?
                if driver.find_element(By.XPATH, "//android.view.View[1]/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]").is_displayed():
                    while(True):
                        # 복습하기 버튼 클릭
                        driver.find_element(By.XPATH, '//android.view.View[4]/android.view.View/android.view.View/android.view.View[1]/android.widget.Button').click()
                        # 단어 먼저보기 클릭
                        driver.find_element(By.XPATH, '//android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.widget.Button').click()
                        sleep(3.5)
                        driver.find_element(By.XPATH, knowTextBottom).click()
                        sleep(0.8)
                        driver.find_element(By.XPATH, knowTextTop).click()
                        
                        # 완료 했는지 체크
                        isEndText = driver.find_element(By.XPATH, "//android.view.View[1]/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]").get_attribute('text')
                        if isEndText.find("완료") >= 0:
                            break
                driver.find_element(By.XPATH, knowTextBottom).click()
                break
        
            





    def email_login(self):
        driver = self.driver
        driver.implicitly_wait(10)

        email_id = 'sunbae@yopmail.com'
        email_pw = '1qaz2wsx'

        # already has account 
        #driver.find_element(By.ID, "co.riiid.vida:id/btn_has_account").click()
        driver.find_element(By.XPATH, '//android.view.ViewGroup/android.widget.LinearLayout[2]').click()
        sleep(2)
        
        # i doesn't find a login type
        # co.riiid.vida:id/content_email
        driver.find_element(By.XPATH, '//android.view.ViewGroup/android.widget.LinearLayout[2]').click()
        sleep(1)

        # go email login 
        # co.riiid.vida:id/btn_email
        driver.find_element(By.XPATH, "//android.view.ViewGroup/android.widget.LinearLayout[3]/android.widget.LinearLayout[2]").click()
        sleep(1)

        # email field
        emailBtn =  driver.find_element(By.XPATH, "//android.view.ViewGroup[1]/android.widget.EditText")
        emailBtn.send_keys(email_id)
        sleep(1)                                                                 

        # pw field
        pwBtn =  driver.find_element(By.XPATH, "//android.view.ViewGroup[2]/android.widget.EditText")
        pwBtn.send_keys(email_pw)
        sleep(1)

        # enter the login button
        loginBtn = driver.find_element(By.ID, 'co.riiid.vida:id/btn_sign_in')
        loginBtn.click()

        sleep(5)        

    def getSelectAnswer(self):
        driver = self.driver 
        # 일반 답안 1개인 경우 
        testGroup = driver.find_elements(By.XPATH, '//android.view.View[5]/android.view.View')
        testCnt = len(testGroup)
        num = random.randrange(0, testCnt)
        num += 3
        print(f'random num : {num}')
        anwserTest = f'//android.view.View[5]/android.view.View/android.view.View[{num}]' 
        return anwserTest

    # 마지막 문제일 경우 처리
    def TestPrep_End(self, isEnd):
        driver = self.driver
        sleep(1.2)
        try:
            btnElement = driver.find_element(By.XPATH, self.blackButton)
            btnElement.click()
            print('학습 종료하기 버튼 클릭')
            sleep(1.2)
            # 홈으로 가기
            btnElement = driver.find_element(By.XPATH, self.gotoHomeButton)
            btnElement.click()
            print('홈으로 가기 버튼 클릭')
            print('학습 셀 완료!')
        except NoSuchElementException:
            pass


    def isShown(self, xP):
        # 어떠한 Element 들이 다 보여진 상태를 체크하는 함수
        if self.driver.find_element(By.XPATH, xP).is_displayed():
            return True
        else:
            return False


    def isSoundPopup(self):
        driver = self.driver

        try:
            if self.isShown(self.startSoundCheck):
                print("사운드체크 시작하기 존재 및 클릭")
                startSoundCheck = driver.find_element(By.XPATH, self.startSoundCheck)
                startSoundCheck.click()
                sleep(0.8)
                startTestPrep = driver.find_element(By.XPATH, self.startTestPrep)
                startTestPrep.click()
                print("내 목소리가 들리나요 존재 및 클릭")
                sleep(0.7)

            sleep(1)
            if self.isShown(self.soundPlayWhenLCblack):
                print("소리 재생하기 검정 버튼 존재")
                soundPlay = driver.find_element(By.XPATH, self.soundPlayWhenLCblack)
                soundPlay.click()
                sleep(0.7)
        except Exception as e:
            print(f'exception : {e}')

    def isPoupExist(self):
        driver = self.driver

        try: 
            if self.isShown(self.testPrepPopup):                    
                popupBtn = driver.find_element(By.XPATH, self.testPrepPopup)
                popupBtn.click()
                print("팝업 닫음")
        except Exception as e:
            print("팝업 없음")
    

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TableSearchTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

