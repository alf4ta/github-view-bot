from selenium import webdriver
import os
from pystyle import Colorate, Colors, Center
from selenium.webdriver.chrome.options import Options
import time

driver_path = 'chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument('--headless') 

driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

driver.get('ur github link')

os.system('cls')

num_refreshes = 1000

counter = 0

banner = (Colorate.Horizontal(Colors.blue_to_purple, """
           $$\  $$$$$$\  $$\   $$\   $$\               
          $$ |$$  __$$\ $$ |  $$ |  $$ |              
 $$$$$$\  $$ |$$ /  \__|$$ |  $$ |$$$$$$\    $$$$$$\  
 \____$$\ $$ |$$$$\     $$$$$$$$ |\_$$  _|   \____$$\ 
 $$$$$$$ |$$ |$$  _|    \_____$$ |  $$ |     $$$$$$$ | 
$$  __$$ |$$ |$$ |            $$ |  $$ |$$\ $$  __$$ |
\$$$$$$$ |$$ |$$ |            $$ |  \$$$$  |\$$$$$$$ |
 \_______|\__|\__|            \__|   \____/  \_______|                                 
    """, 1))
os.system(f'title https://github.com/alf4ta')
while counter < num_refreshes:
    driver.refresh()
    counter += 1
    os.system('cls')
    print(banner)
    print(f"Views: {counter}")
    os.system(f'title Views - {counter}')

driver.quit()
