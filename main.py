import os
from time import sleep
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()


class InternetComplainer:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def twitter_login(self):
        self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span"
        ).click()
        sleep(2)
        self.driver.find_element(
            by=By.CSS_SELECTOR,
            value="label div div input"
        ).send_keys(os.environ["email"])
        sleep(2)
        self.driver.find_element(
            by=By.XPATH,
            value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div"
        ).click()
        sleep(2)
        self.driver.find_element(
            by=By.CSS_SELECTOR,
            value="div div div input"
        ).send_keys(os.environ["twitter_username"])
        self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div"
        ).click()
        sleep(1)

        self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
        ).send_keys(os.environ["pass"])
        self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div"
        ).click()

    def twitter_post(self):
        self.driver.find_element(
            by=By.CSS_SELECTOR,
            value="div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr"
        ).send_keys(f"Autmatically complaining about my internet speed. I got down:{self.down} and up:{self.up}")

        self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span"
        ).click()

    def complain(self):
        self.driver.get("https://twitter.com/")
        sleep(5)
        self.twitter_login()
        sleep(2)
        self.twitter_post()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(5)
        self.driver.find_element(value="onetrust-accept-btn-handler").click()
        self.driver.find_element(by=By.CSS_SELECTOR, value="div a span.start-text").click()
        sleep(5)
        self.down = self.get_down_speed()
        self.up = self.get_up_speed()

    def get_down_speed(self):
        css_selector_string = "span.result-data-large.number.result-data-value.download-speed"
        download_speed_element = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value=css_selector_string
        )
        while download_speed_element.text == "—":
            sleep(2)
            download_speed_element = self.driver.find_element(
                by=By.CSS_SELECTOR,
                value=css_selector_string
            )
        return download_speed_element.text

    def get_up_speed(self):
        css_selector_string = "span.result-data-large.number.result-data-value.upload-speed"
        upload_speed_element = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value=css_selector_string
        )
        while upload_speed_element.text == "—":
            sleep(2)
            upload_speed_element = self.driver.find_element(
                by=By.CSS_SELECTOR,
                value=css_selector_string
            )
        return upload_speed_element.text


ic = InternetComplainer()
ic.get_internet_speed()
sleep(5)
ic.complain()

sleep(20)
