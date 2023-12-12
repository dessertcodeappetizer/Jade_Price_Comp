from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
import time
class Test:
    def __init__(self, source, destination, date, monyr, date_pas, result_queue):
        self.source = source
        self.destination = destination
        self.date = date
        self.monyr = monyr
        self.date_pas = date_pas
        self.result_queue = result_queue
        
    def mmt(self):
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome()
        driver.get("https://www.makemytrip.com/")
        time.sleep(2)
        # driver.minimize_window()
        # Avoiding offers
        actions = ActionChains(driver)
        actions.move_by_offset(10, 5)
        actions.click()
        actions.perform()
        actions.click()
        actions.perform()
        # actions.click()
        # actions.perform()
        
        #Closing commercial adds
        # time.sleep(3)
        # loct1 = driver.find_element(By.XPATH, "//span[@class='commonModal__close']")
        # loct1.click()
        
        #finding from and filling it with value
        time.sleep(2)
        loct2a = driver.find_element(By.XPATH, "//label[@for='fromCity']")
        loct2a.click()
        time.sleep(2)
        loct2 = driver.find_element(By.XPATH, "//input[@placeholder='From']")
        loct2.send_keys(self.source)
        time.sleep(2)
        loct2b = driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-0-item-0']")
        time.sleep(2)
        loct2b.click()
        time.sleep(2)
        
        #finding to and filling it with value
        loct3a = driver.find_element(By.XPATH, "//label[@for='toCity']")
        loct3a.click()
        time.sleep(2)
        loct3 = driver.find_element(By.XPATH, "//input[@placeholder='To']")
        loct3.send_keys(self.destination)
        time.sleep(2)
        loct3b = driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-0-item-0']")
        time.sleep(2)
        loct3b.click()
        time.sleep(5)
        
        
        # loct4 = driver.find_element(By.XPATH, "//label[@for='departure']")
        # loct4.click()
        proper_date = self.date_pas + " " + self.monyr[:3] + " " + self.date + " " + self.monyr[-4:]
        print(proper_date)
        for _ in range(12):
            # monyr_cal = driver.find_element(By.XPATH, "/html//div[@id='root']/div[@class='bgGradient webpSupport']/div[@class='minContainer']/div/div/div//div[@class='RangeExample']/div[2]/div[@class='DayPicker-wrapper']/div[@class='DayPicker-Months']/div[1]/div[@role='heading']/div").text
            monyr_cal = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div").text
            print(monyr_cal)
            time.sleep(1)
            if self.monyr == monyr_cal:
                date_loctr = driver.find_element(By.XPATH, f"//div[@aria-label='{proper_date}']")
                date_loctr.click()
                time.sleep(2)
                break
            else:
                nxt_btn_loctr = driver.find_element(By.XPATH, "//span[@aria-label='Next Month']")
                nxt_btn_loctr.click()
        
        search_btn_loctr = driver.find_element(By.XPATH, "//a[@class='primaryBtn font24 latoBold widgetSearchBtn ']")
        search_btn_loctr.click()
        time.sleep(15)
        
        actions.move_by_offset(10, 5)
        actions.click()
        actions.perform()
        time.sleep(2)
        curren_url = driver.current_url
        # price_btn_loctr = driver.find_element(By.XPATH, "/html//div[@id='listing-id']/div[@class='splitVw']/div[1]/div[@class='listingCardWrap']/div/div[2]/label/div/div[2]/div[2]/div/p").text
        price_btn_loctr = driver.find_element(By.XPATH, "//*[@id='listing-id']/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/div/div").text
        result = price_btn_loctr, curren_url
        self.result_queue.put(result)
        # return price_btn_loctr, curren_url