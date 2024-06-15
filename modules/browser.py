from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Browser:
    def __init__(self):
        self.driver = None

    def setupWebDriver(self):
        options=Options()
        options.add_argument("--incognito")
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def waitTilVisible(self, by: str, string: str):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, string)))
        return element

    def waitTilClickable(self, by: str, string: str):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, string)))
        return element

    def waitTilPresence(self, by: str, string: str):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, string)))
        return element

    def close(self):
        self.driver.close()