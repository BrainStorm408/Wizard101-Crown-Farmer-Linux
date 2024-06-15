from modules import tuples, Recaptcha, Extra
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class Trivia:
    def __init__(self, browser):
        self.browser = browser
        self.driver = browser.driver
        self.triviaCounter = 0
        self.questionCounter = None
        self.change = None
        self.skip = None

    def triviaStart(self):
        for currentTrivia in tuples.trivias:
            self.skip = False
            self.questionCounter = 0
            self.change = "4"
            self.driver.get(tuples.links[self.triviaCounter])
            retry = self.quickCheck()
            if retry:
                self.driver.get(tuples.links[self.triviaCounter])
                self.quickCheck()
            if self.skip:
                print(f"[TRIVIA] Skipping {currentTrivia}")
            else:
                print(f"[TRIVIA] Starting {currentTrivia}")
                while self.questionCounter < 12:
                    self.triviaSolve()
                    self.questionCounter+=1
                    self.change = "2"
                    print(f"[TRIVIA] {self.questionCounter}/12")
                blocked = True
                while blocked:
                    blocked = Recaptcha(self.browser).recapTwo()
                Extra.printGreen(f"[TRIVIA] Finished {currentTrivia}")
            self.triviaCounter += 1

    def quickCheck(self):
        try:
            self.browser.waitTilVisible(By.XPATH, self.getXPATH(False, "1"))
            return False
        except TimeoutException:
            try:
                alreadyDone = self.browser.waitTilVisible(By.XPATH, "/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[2]/div/h2")
                if alreadyDone.text == "Come Back Tomorrow!":
                    self.skip = True
                return False
            except TimeoutException:
                try:
                    Extra().rejectCookies(self.browser)
                    return False
                except TimeoutException:
                    try:
                        upstreamError = self.browser.waitTilVisible(By.XPATH, "/html/body/div/div/h1")
                        print(upstreamError.text)
                        if upstreamError.text == "Upstream origin server was unreachable.":
                            self.browser.refresh()
                        return True
                    except:
                        Extra.printRed("[TRIVIA] Unknown issue occured")
                        exit()
    def triviaSolve(self):
        if not 'num' in locals():
            num = 0
        next = False

        try:
            answer1 = self.browser.waitTilVisible(By.XPATH, self.getXPATH(False, "1"))
        except TimeoutException:
            self.quickCheck()
            answer1 = self.browser.waitTilVisible(By.XPATH, self.getXPATH(False, "1"))
        answer1Box = self.browser.waitTilClickable(By.XPATH, self.getXPATH(True, "1"))
        answer2 = self.browser.waitTilVisible(By.XPATH, self.getXPATH(False, "2"))
        answer2Box = self.browser.waitTilClickable(By.XPATH, self.getXPATH(True, "2"))
        answer3 = self.browser.waitTilVisible(By.XPATH, self.getXPATH(False, "3"))
        answer3Box = self.browser.waitTilClickable(By.XPATH, self.getXPATH(True, "3"))
        answer4 = self.browser.waitTilVisible(By.XPATH, self.getXPATH(False, "4"))
        answer4Box = self.browser.waitTilClickable(By.XPATH, self.getXPATH(True, "4"))

        while not next:
            answers = tuples.answers[self.triviaCounter][num]
            if answer1.text == answers:
                answer1Box.click()
                num = 0
                next = True
            elif answer2.text == answers:
                answer2Box.click()
                num = 0
                next = True
            elif answer3.text == answers:
                answer3Box.click()
                num = 0
                next = True
            elif answer4.text == answers:
                answer4Box.click()
                num = 0
                next = True
            else:
                num += 1
            if next == True:
                self.browser.waitTilClickable(By.XPATH, f"/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[{self.change}]/table[2]/tbody/tr[2]/td[2]/div[3]/button/div").click()

    def getXPATH(self, answerBox: bool, number: str):
        if answerBox:
            endOfPath = "span[1]/a"
        else:
            endOfPath = "span[2]"
        XPATH = f'/html/body/div[5]/div[3]/div[2]/div[3]/div[3]/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div/div/div/div[{self.change}]/table[2]/tbody/tr[2]/td[2]/div[2]/div[{number}]/{endOfPath}'
        return XPATH
