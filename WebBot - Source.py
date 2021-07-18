from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import undetected_chromedriver.v2 as uc
import time
from csv import reader
import os

#clear
clear = lambda: os.system('cls')

print("Welcome to WebBot V1.0 to access websites using free proxies.")
time.sleep(3)
print("You can use it to vote for xtremetop100 or at least visit some blocked websites.")
time.sleep(3)
print("This project made by Ahmed Ism3lawy using Python 3, Selenium and Undetected Chrome Driver.")
time.sleep(7)
clear()
Choice = input("1. Load Proxies\n2. Test Proxies\n3. Go to website\nYour choice: ")

def TestProxy(ReadyProxy):
    print("Testing Proxy using: " + ReadyProxy)
    opts = uc.ChromeOptions()
    proxy = "--proxy-server=" + ReadyProxy
    opts.add_argument("--incognito")
    opts.add_argument(proxy)
    browser = uc.Chrome(options=opts,enable_cdp_events=True)
    try:
        browser.get("http://www.whatismyproxy.com/")
        browser.implicitly_wait(1)
        browser.quit()
    except:
        print("There is a prblem. Free proxies, so may face some problems.")
        browser.quit()

if Choice == "1":
    clear()
    print("Loading some proxies.")
    time.sleep(5)
    driver = uc.Chrome()
    driver.get("https://sslproxies.org/")
    driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//th[contains(., 'IP Address')]"))))
    ips = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 1]")))]
    ports = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered dataTable']//tbody//tr[@role='row']/td[position() = 2]")))]
    driver.close()
    proxies = []
    for i in range(0, len(ips)):
        proxies.append(ips[i]+','+ports[i])
    for i in range(0, len(proxies)):
        try:
            with open("proxy.txt", "a") as file_object:
                file_object.write(proxies[i] + "\n")
            print("Add: {}".format(proxies[i]))
        except Exception:
            driver.quit()
    time.sleep(1) # Wait 1 Second
    driver.quit()
    quit()

if Choice == "2":
    clear()
    # Load Proxies from txt file
    with open('proxy.txt', 'r') as ReadProx:
        ReadProxiesFile = reader(ReadProx)
        ProxiesRows = list(ReadProxiesFile)
    ProxiesList = ProxiesRows

    for i in range(len(ProxiesList)):
        ProxyIP = ProxiesList[i][0]
        Port = ProxiesList[i][1]
        ReadyProxy = ProxyIP + ":" + Port
        TestProxy(ReadyProxy)

    time.sleep(1) # Wait 1 Second
    driver.quit()
    quit()

if Choice == "3":
    clear()
    print("Please provide your link that you want to visit and how many times? and for how long in seconds!")
    Link = input("Website you want to visit: ")
    Times = input("How many times you want to visit: ")
    Long = input("How long you want to set the delay in seconds: ")
    with open('proxy.txt', 'r') as ReadProx:
        ReadProxiesFile = reader(ReadProx)
        ProxiesRows = list(ReadProxiesFile)
    ProxiesList = ProxiesRows
    
    for i in range(int(Times)):
        ProxyIP = ProxiesList[i][0]
        Port = ProxiesList[i][1]
        ReadyProxy = ProxyIP + ":" + Port
        clear()
        print(i+1,". Site: "+ Link +", Times: "+ Times +", Delay: "+ Long +", Proxy: "+ ReadyProxy)
        opts = uc.ChromeOptions()
        proxy = "--proxy-server=" + ReadyProxy
        #opts.add_argument("--incognito")
        opts.add_argument(proxy)
        browser = uc.Chrome(options=opts,enable_cdp_events=True)
        try:
            browser.get(Link)
            browser.implicitly_wait(1)
            time.sleep(int(Long))
            browser.quit()
        except:
            print("There is a prblem. Free proxies, so may face some problems.")
            browser.quit()
        time.sleep(int(Long))
    time.sleep(1) # Wait 1 Second
    browser.quit()
    quit()