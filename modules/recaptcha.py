import os
import urllib
import pydub
import time
import speech_recognition as sr
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from modules import Extra


class Recaptcha:
    def __init__(self, browser):
        self.browser = browser
        self.driver = browser.driver
        self.blocked = False


    def recapOne(self):
        print("[RECAPTCHA] Starting solving process...")
        # Switches to Recaptcha iframe
        self.switchFrame(1)
        # Switches to Checkbox iframe
        self.switchFrame(2)
        # Clicks the checkbox
        try:
            self.browser.waitTilClickable(By.CLASS_NAME, "recaptcha-checkbox-border").click()
        except ElementClickInterceptedException:
            # When clicking is blocked. Goes back to default frame and checks for popup and goes back to captcha frame.
            self.switchFrame(0)
            Extra().rejectCookies(self.browser)
            self.switchFrame(1)
            self.switchFrame(2)
            self.browser.waitTilClickable(By.CLASS_NAME, "recaptcha-checkbox-border").click()
        # Goes back to original frame, then back to Recaptcha frame
        self.switchFrame(0)
        self.switchFrame(1)
        # Goes into Recaptcha challenge frame and clicks audio challenge
        self.switchFrame(3)
        self.browser.waitTilClickable(By.XPATH, "/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/button").click()
        # Tries to get audio source. If fails, most likely IP blocked
        try:
            self.browser.waitTilPresence(By.ID, "audio-source").get_attribute("src")
        except TimeoutException:
            self.blocked = self.checkIfBlocked()
        if self.blocked:
            pass
        else:
            self.audioRecognition()
            self.switchFrame(0)
            self.switchFrame(1)
            self.browser.waitTilClickable(By.CLASS_NAME, "buttonsubmit").click()
            self.switchFrame(0)
            Extra.printGreen("[RECAPTCHA] Finished Recaptcha")

    def recapTwo(self):
        self.browser.waitTilClickable(By.CLASS_NAME, "kiaccountsbuttongreen").click()
        self.switchFrame(1)
        self.browser.waitTilClickable(By.CLASS_NAME, "buttonsubmit").click()
        skip = False
        try:
            self.switchFrame(4)
        except TimeoutException:
            skip = True
            self.switchFrame(0)
        if not skip:
            self.browser.waitTilClickable(By.XPATH, "/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/button").click()
            try:
                self.browser.waitTilPresence(By.ID, "audio-source").get_attribute("src")
            except TimeoutException:
                self.blocked = self.checkIfBlocked()
            if self.blocked:
                return True
            else:
                self.audioRecognition()
                self.switchFrame(0)
                self.switchFrame(1)
                self.switchFrame(0)
                Extra.printGreen("[RECAPTCHA] Finished Recaptcha")
                time.sleep(5)
                return False
        else:
            return False

    def switchFrame(self, frame: float):
        if frame == 0:
            self.driver.switch_to.default_content()
        elif frame == 1:
            jpopFrame = self.browser.waitTilVisible(By.ID, "jPopFrame_content")
            self.driver.switch_to.frame(jpopFrame)
        elif frame == 2:
            recapFrame = self.browser.waitTilVisible(By.CSS_SELECTOR, "#recaptcha > div > div > iframe")
            self.driver.switch_to.frame(recapFrame)
        elif frame == 3:
            audioFrame = self.browser.waitTilVisible(By.XPATH, "/html/body/div[3]/div[4]/iframe")
            self.driver.switch_to.frame(audioFrame)
        elif frame == 4:
            recap = self.browser.waitTilVisible(By.XPATH, "/html/body/div[3]/div[2]/iframe")
            self.driver.switch_to.frame(recap)

    def audioRecognition(self):
        src = self.browser.waitTilPresence(By.ID, "audio-source").get_attribute("src")
        urllib.request.urlretrieve(src, os.getcwd() + "\\sample.mp3")
        sound = pydub.AudioSegment.from_mp3(os.getcwd() + "\\sample.mp3")
        sound.export(os.getcwd() + "\\sample.wav", format="wav")
        sample_audio = sr.AudioFile(os.getcwd() + "\\sample.wav")
        r = sr.Recognizer()
        with sample_audio as source:
            audio = r.record(source)
        key = r.recognize_google(audio)
        self.browser.waitTilVisible(By.ID, "audio-response").send_keys(key.lower())
        self.browser.waitTilVisible(By.ID, "audio-response").send_keys(Keys.ENTER)
        self.driver.switch_to.default_content()

    def checkIfBlocked(self):
        try:
            audioError = self.browser.waitTilVisible(By.XPATH, "/html/body/div/div/div[1]/div[2]/div")
            if audioError.text == "Your computer or network may be sending automated queries. To protect our users, we can't process your request right now. For more details visit our help page.":
                Extra.printRed("[RECAPTCHA] IP Currently Blocked. Changing IP...")
                Extra().startVPN()
                time.sleep(10)
                self.switchFrame(0)
                self.driver.refresh()
                return True
        except TimeoutException:
            return False

