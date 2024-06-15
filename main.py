import os
import json
import setup
import time
from selenium.webdriver.common.by import By
from modules import Extra, Browser, Login, Recaptcha, Trivia

def checkjson():
    global jsonPath
    jsonPath = f"{os.getcwd()}/accounts.json"
    if not os.path.exists(jsonPath):
        Extra.printRed("[EXTRA] Couldn't find accounts.json: Starting setup.py")
        setup.setup()


def setupAccounts():
    with open(jsonPath) as accounts:
        return json.load(accounts)


def main():
    checkjson()
    Extra.printYellow("{0:{1}^40}".format(' Wizard101 Crown Farmer ', "="))
    time.sleep(5)
    accounts = setupAccounts()
    repeat = True

    for account in accounts:
        print(f"[MAIN] Starting process for {account['user']}")
        browser = Browser()
        browser.setupWebDriver()
        recaptcha = Recaptcha(browser)
        login = Login(account, browser)
        if login.captcha:
            while repeat:
                recaptcha.recapOne()
                if recaptcha.blocked:
                    repeat = True
                    browser.waitTilClickable(By.CLASS_NAME, "wizardButtonInput").click()
                else:
                    repeat = False
        login.loginCheck()
        Trivia(browser).triviaStart()
        browser.close()


if __name__ == "__main__":
    main()
