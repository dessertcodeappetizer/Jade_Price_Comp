from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class Test1:
    def __init__(self, source, destination, date, monyr, date_pas, result_queue):
        self.source = source
        self.destination = destination
        self.date = date
        self.monyr = monyr
        self.date_pas = date_pas
        self.result_queue = result_queue
        
    def gb(self):
        driver = webdriver.Chrome()
        driver.get("https://www.goibibo.com/")
        time.sleep(2)
        # driver.minimize_window()
        # Avoiding offers
        # actions = ActionChains(driver)
        # actions.move_by_offset(10, 5)
        # actions.click()
        # actions.perform()
        
        loct1 = driver.find_element(By.XPATH, "//span[@class='logSprite icClose']")
        loct1.click()
        time.sleep(2)
        
        #avoiding app offers
        add_loctr = driver.find_element(By.XPATH, "//div[@id='root']/div[2]/p[1]")
        add_loctr.click()
        
        #source
        from_loctr = driver.find_element(By.XPATH, "/html//div[@id='root']/div[3]/div/div/div[1]/div[1]/div/div/span[.='From']")
        from_loctr.click()
        time.sleep(2)
        inputf_loctr = driver.find_element(By.XPATH, "/html//div[@id='root']/div[3]/div/div/div[1]/div[1]/div/div[2]//input")
        inputf_loctr.send_keys(self.source)
        time.sleep(2)
        src_loctr1 = driver.find_element(By.XPATH, "//ul[@id='autoSuggest-list']/li[1]/div/div[1]/div")
        src_loctr1.click()
        
        #destination
        # to_loctr = driver.find_element(By.XPATH, "/html//div[@id='root']/div[3]/div/div/div[1]/div[2]/div/div/span[.='To']")
        # to_loctr.click()
        time.sleep(2)
        inputt_loctr = driver.find_element(By.XPATH, "/html//div[@id='root']/div[3]/div/div/div[1]/div[2]/div/div[2]//input")
        inputt_loctr.send_keys(self.destination)
        time.sleep(2)
        src_loctr2 = driver.find_element(By.XPATH, "//ul[@id='autoSuggest-list']/li[1]/div/div[1]/div")
        src_loctr2.click()
        
        #calender
        proper_date = self.date_pas + " " + self.monyr[:3] + " " + self.date + " " + self.monyr[-4:]
        for _ in range(12):
            monyr_cal = driver.find_element(By.XPATH, "//*[@id='root']/div[3]/div/div/div[1]/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]").text
            time.sleep(1)
            if monyr_cal == self.monyr:
                date_loctr = driver.find_element(By.XPATH, f"//div[@aria-label='{proper_date}']")
                date_loctr.click()
                time.sleep(1)
                done_loctr = driver.find_element(By.XPATH, "//span[@class='fswTrvl__done']")
                done_loctr.click()
                time.sleep(1)
                break
            else:
                nxt_btn_loctr = driver.find_element(By.XPATH, "//span[@aria-label='Next Month']")
                nxt_btn_loctr.click()
        
        #search  
        src_loctr3 = driver.find_element(By.XPATH, "//span[@class='sc-12foipm-85 fUaVPB']")
        src_loctr3.click()
        time.sleep(20)
        
        currn_url = driver.current_url
        price_loctr = driver.find_element(By.XPATH, "/html//div[@id='root']/div[2]/div/div[1]/div[3]/div[2]//div[@class='alignItemsEnd flexCol padB5']/div").text
        result = price_loctr, currn_url
        self.result_queue.put(result)
        # return price_loctr, currn_url