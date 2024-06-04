import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyautogui
import sys

'''
@Actor TaeKyung Lim 
@Desc 동행복권 사이트 자동로그인 해서 로또 번호 선택하는 화면까지 자동화 하였습니다.
      동행복권 측에서 리뉴얼이 들어가서 ui가 바뀌면 다시 만들어야 할수도 있습니다.
@Date 2024-06-04
'''
form_uiclass= uic.loadUiType('./basic/dlottositeauto.ui')[0]

#화면을 띄우는데 사용되는 class
class WindowClass(QMainWindow, form_uiclass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def auto_dlottosite(self):
        lid=self.txtid.text()
        lpw=self.txtpw.text()

        #id와 비밀번호를 입력했는지 체크
        if not lid or not lpw:
            pyautogui.alert('아이디 혹은 비밀번호를 입력해주세요.')
        else :
            chrome_options = Options()
            chrome_options.add_experimental_option('detach', True)

            driver = webdriver.Chrome(options=chrome_options)

            driver.get("https://dhlottery.co.kr/common.do?method=main")

            ele=driver.find_element(By.LINK_TEXT, "로그인")
            driver.execute_script("arguments[0].click();", ele)

            time.sleep(1)

            loginid = driver.find_element(By.ID, "userId")
            loginid.send_keys(lid)
            time.sleep(1)
            loginpw = driver.find_element(By.NAME, "password")
            loginpw.send_keys(lpw)
            time.sleep(1)
            btnlogin=driver.find_element(By.LINK_TEXT, "로그인")
            driver.execute_script("check_if_Valid3();")

            driver.maximize_window()
            time.sleep(1)
            driver.execute_script("goLottoBuy(2);")

            self.txtid.setText('')
            self.txtpw.setText('')

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()

    myWindow.show()

    sys.exit(app.exec_())