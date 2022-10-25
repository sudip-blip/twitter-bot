from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PROMISED_DOWN=30 # change this with your ISP prmised Download speed
PROMISED_UP=30  #change this with your ISP prmised Download speed
CHROME_DRIVER_PATH="D:\chromedriver.exe"  #path to chromedriver on your pc
TWITTER_NUM="" #your twitter username/num/gmail inside qutation
TWITTER_PASSWORD="" #twitter pass inside quotatiob
ISP_PROVIDER_TWITTER=""

s=Service(CHROME_DRIVER_PATH)
driver=webdriver.Chrome(service=s)


class InternetSpeedBot:
    def __init__(self,driver,down,up):
        self.driver=driver
        self.down=down
        self.up=up

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        # time.sleep(10)
        text=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        text.click()
        time.sleep(50)
        self.down=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        
        if float(self.down)<PROMISED_DOWN or float(slef.up)<PROMISED_UP:
            return True
        else:
            return False
    


    def post_at_provider(self):
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys("sudipkc00") #username
        self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click() #next button
        time.sleep(3)

        self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys("00sudip@kc") # password

        self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div').click() #Login button
        time.sleep(3)
        tweet=f'Your company promised this download/upload speed:{PROMISED_DOWN}/{PROMISED_UP} but I am getting this speed download/upload{self.down}/{self.up} {ISP_PROVIDER_TWITTER}'
        self.driver.find_element(By.CSS_SELECTOR,'.DraftEditor-editorContainer div').send_keys('tweet') #tweet compose

        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div').click() #Tweet button
        self.driver.quit()


bot=InternetSpeedBot(driver,PROMISED_DOWN ,PROMISED_UP)
if bot.get_internet_speed():
    bot.post_at_provider()
