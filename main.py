from selenium import webdriver
import os
from pystyle import Colorate, Colors, Center
from selenium.webdriver.chrome.options import Options
import time
import colorama
import msvcrt

github = "ur github url"
green = "\033[38;5;83m"
red = "\033[38;5;203m"
white = "\033[38;5;231m"

driver_path = 'chromedriver.exe'

chrome_options = Options()
headless_mode = True

def toggle_headless_mode():
    global headless_mode
    headless_mode = not headless_mode

toggle_key = b'p'  # You can change the toggle keybind here

driver = None

if not headless_mode:
    driver = webdriver.Chrome(executable_path=driver_path)
else:
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

driver.get(github)

os.system('cls')

num_refreshes = 9999999999999999

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
    print("Repo: https://github.com/alf4ta/github-view-bot")
    print(f"Views: \033[38;5;133m{counter}{white} - Headless: {f'{green}ENABLED{white}' if headless_mode else f'{red}DISABLED{white}'} - headless keybind: \033[38;5;133mP{white}")
    os.system(f'title Alf4ta ViewBot - Views - {counter}')
    
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == toggle_key:
            toggle_headless_mode()
            driver.quit()  # Quit the current driver instance
            if not headless_mode:
                driver = webdriver.Chrome(executable_path=driver_path)
            else:
                chrome_options.add_argument('--headless')
                driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
            driver.get(github)

driver.quit()
