from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from modules import Extra


class Login:
    def __init__(self, account, browser):
        self.account = account
        self.browser = browser
        self.driver = browser.driver
        self.captcha = False
        self.login()

    def login(self):
        self.driver.get("https://www.wizard101.com/game")
        self.browser.waitTilVisible(By.NAME, "loginUserName").send_keys(self.account["user"])
        self.browser.waitTilVisible(By.NAME, "loginPassword").send_keys(self.account["pass"])
        self.browser.waitTilClickable(By.CLASS_NAME, "wizardButtonInput").click()

        # Checks for Recaptcha
        try:
            self.browser.waitTilVisible(By.ID, "jPopFrame_content")
            self.captcha = True
        except TimeoutException:
            pass

    def loginCheck(self):
        try:
            username = self.browser.waitTilVisible(By.ID, "userNameOverflow")
            if username.text == self.account["user"]:
                Extra.printGreen(f'[LOGIN] Successfully logged into {self.account["user"]}')
            elif username.text == "Login":
                Extra.printRed("[LOGIN] Error trying to login. Check if username and password are correct.")
                exit()
            else:
                Extra.printRed("[LOGIN] Error trying to login.")
                exit()
        except TimeoutException:
            Extra.printRed("[LOGIN] Error trying to login. Exception")
            exit()
