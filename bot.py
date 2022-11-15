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

_cookies=driver.get_cookies()
cookies_dict={}
for cookie in _cookies:
    cookies_dict[cookie['name']]=cookie['value']

session=requests.session()
headers={'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

session.headers.update(headers)
session.cookies.update(cookies_dict)

res=session.get('https://lms.jbnu.ac.kr/paper/paperSelectGroup.jsp')
page=driver.page_source
soup=BeautifulSoup(page,'html.parser')

subjects=[]
link=soup.select_one('div.containerTableStyle')
link2=link.select('table>tbody>tr>td>table>tbody>tr')
for i in link2:
    tmp=i.get_text()
    subjects.append(tmp)

s = []
search="2학기"

for k in list(subjects):
    if search in k:
        print(k)
        s.append(k)

name=pd.DataFrame(s)
name.to_csv('과목명.txt',index=False,header=False)
driver.close()

while(True):
    pass
