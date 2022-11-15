import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options=Options()
options=webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver=webdriver.Chrome()

options.add_experimental_option('excludeSwitches',['enable-logging'])

driver.implicitly_wait(3)
driver.get('https://lms.jbnu.ac.kr/')
login_x_path='//*[@id="loginform"]/table/tbody/tr[1]/td[2]/input'
driver.find_element(By.XPATH,r'//*[@id="id"]').send_keys('202211147')
driver.find_element(By.XPATH,r'//*[@id="passwd"]').send_keys('wlals0923!')
driver.find_element(By.XPATH,r'//*[@id="loginform"]/table/tbody/tr[1]/td[2]/input').click()
driver.find_element(By.XPATH,r'//*[@id="nav"]/li[5]/a').click()

f = open("과제.txt", 'w')
f.write('')
f.close()

for n in range(6):
    try:
        driver.find_element(By.XPATH,r'//*[@id="treebox"]/div/table/tbody/tr[%d]/td[2]/table/tbody/tr/td[4]/span' %(n+2)).click()

        _cookies=driver.get_cookies()
        cookies_dict={}
        for cookie in _cookies:
            cookies_dict[cookie['name']]=cookie['value']

        session=requests.session()
        headers={'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

        session.headers.update(headers)
        session.cookies.update(cookies_dict)

        time.sleep(1)

        page=driver.page_source
        soup=BeautifulSoup(page,'html.parser')

        link=soup.select('#borderB > tbody > tr.btr > td:nth-child(2)')#.getText().replace(' ','').replace('\n','').replace('\t','')
        link2=soup.select('#borderB > tbody > tr.btr > td:nth-child(3)')#.getText().replace(' ','').replace('\n','').replace('\t','')

        task=[]
        for i in link:
            tmp=i.get_text().replace(' ','').replace('\n','').replace('\t','')
            task.append(tmp)
            task.append("\n")

        for k in link2:
            tmp2=k.get_text().replace(' ','').replace('\n','').replace('\t','')
            task.append(tmp2)
            task.append("\n")

        f=open("과제.txt",'a',encoding='UTF-8')

        for i in task:
            f.write(i)
        
        f.close()
        driver.back()
    except:
        driver.back()

