from datetime import time
from random import random
from selenium import webdriver
from personal_data import username,password
from selenium.webdriver.common.keys import Keys
import time
import instaloader


class Insta_Bot:

    def __init__(self, browser):
        self.browser = browser
        browser.get("https://www.instagram.com/")
        self.ig = instaloader.Instaloader()



    def login(self, username, password):
        try:
            time.sleep(5)

            username_input = self.browser.find_element("xpath", "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
            username_input.clear()
            username_input.send_keys(username)

            time.sleep(4)

            password_input = self.browser.find_element("name", "password")
            password_input.clear()
            password_input.send_keys(password)
            password_input.send_keys(Keys.ENTER)

        except:
            print("some problems in login...")
            self.quit_of_brw(browser)

    def quit_of_brw(self):
        self.browser.quit()
        self.browser.close()

    def user_info(self,user_url):
        try:
            self.browser.get(user_url)

            user_name = self.browser.find_element("xpath", "/html/body/div[1]/section/main/div/header/section/div[1]/h2")

            num_of_subscribers = self.browser.find_element("xpath", "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span")

            num_of_subscriptions = self.browser.find_element("xpath", "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span")

            num_of_publications = self.browser.find_element("xpath", "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span")

            full_name = self.browser.find_element("xpath", "/html/body/div[1]/section/main/div/header/section/div[2]/h1")

            inf_dict = {"user_name" : user_name.text, "num_of_subscribers" : num_of_subscribers.text, "num_of_subscriptions" : num_of_subscriptions.text,
            "num_of_publications" : num_of_publications.text, "full_name" : full_name.text}

            return inf_dict

        except:
            print("some problems in user_info")
            self.quit_of_brw(browser)

    def donwload_info(self, url):
        self.browser.get(url)
        dirname = url.split('/')[-2]
        self.ig.download_profile(dirname, url)




browser = webdriver.Chrome()
inst = Insta_Bot(browser)
inst.login(username, password)
time.sleep(4)
print(inst.user_info("https://www.instagram.com/djyliakimova/"))





