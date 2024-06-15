import os
from selenium.webdriver.common.by import By

class Extra:
    def printGreen(self: str):
        print(f"\033[92m{self}\033[00m")

    def printYellow(self: str):
        print(f"\033[93m{self}\033[00m")

    def printRed(self: str):
        print(f"\033[91m{self}\033[00m")

    def startVPN(self):
        os.system("protonvpn-cli c -r")

    def stopVPN(self):
        os.system("protonvpn-cli d")

    def rejectCookies(self, browser):
        browser.waitTilClickable(By.ID, "onetrust-reject-all-handler").click()
