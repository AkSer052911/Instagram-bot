from datetime import time
from selenium import webdriver
from personal_data import username,password
from selenium.webdriver.common.keys import Keys
import time
import instaloader


class Insta_Bot:

    def __init__(self, browser,username,password):
        self.browser = browser
        browser.get("https://www.instagram.com/")
        self.ig = instaloader.Instaloader()
        self.username = username
        self.password = password



    def login(self):
        try:
            time.sleep(5)

            username_input = self.browser.find_element("xpath", "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
            username_input.clear()
            username_input.send_keys(self.username)

            time.sleep(4)

            password_input = self.browser.find_element("name", "password")
            password_input.clear()
            password_input.send_keys(self.password)
            password_input.send_keys(Keys.ENTER)

        except:
            print("some problems in login...")
            self.quit_of_brw()

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

    def donwload_all_info(self, url):
        self.browser.get(url)
        dirname = url.split('/')[-2]
        self.ig.download_profile(dirname, url)

    def download_some_user_info(self,url,dir_name):
        self.browser.get(url)
        post = instaloader.Post.from_shortcode(self.ig.context, shortcode = url.split("/")[-2])
        self.ig.download_post(post, target=dir_name)

    def send_message(self,account_name,message):
        self.browser.get("https://www.instagram.com/direct/inbox/")
        time.sleep(2)

        self.browser.find_element("xpath", "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input").clear()
        self.browser.find_element("xpath", "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input").send_keys(self.username)
        time.sleep(1.5)

        self.browser.find_element("xpath",  "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input").clear()
        self.browser.find_element("xpath", "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input").send_keys(self.password)
        self.browser.find_element("xpath", "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input").send_keys(Keys.ENTER)
        time.sleep(4)

        #if self.browser.find_element("xpath", "/html/body/div[1]/section/main/div/div/div/div/button"):
        self.browser.find_element("xpath", "/html/body/div[1]/section/main/div/div/div/div/button").click()
        time.sleep(3)

        #if self.browser.find_element("xpath", "/html/body/div[4]/div/div/div/div[3]/button[2]"):
        self.browser.find_element("xpath", "/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        time.sleep(4)

        self.browser.find_element("xpath", "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button").click()
        time.sleep(3)

        self.browser.find_element("xpath", "/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input").send_keys(account_name)
        time.sleep(3)

        self.browser.find_element("xpath", "/html/body/div[6]/div/div/div[2]/div[2]/div/div").click()
        time.sleep(3)

        self.browser.find_element("xpath", "/html/body/div[6]/div/div/div[1]/div/div[2]/div/button").click()
        time.sleep(3)

        self.browser.find_element("xpath","/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(message)
        self.browser.find_element("xpath","/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(Keys.ENTER)








browser = webdriver.Chrome()
inst = Insta_Bot(browser,username, password)
inst.login()








