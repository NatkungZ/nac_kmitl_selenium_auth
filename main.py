import os
import sys
import time
import urllib.request

from selenium import webdriver
from selenium.webdriver.support.ui import Select


# Write Log to /tmp/firefox_console/webdriver.log
p = webdriver.FirefoxProfile()
p.set_preference("webdriver.log.file", "/tmp/firefox_console")

driver = webdriver.Firefox(p)
clear = lambda: os.system('clear')
write_log = lambda: os.system('echo \"Loging in    : $(date)\" >> net_log')
write_error_log = lambda: os.system('echo \"NAC not load : $(date)\" >> net_log')


def connect():
    driver.get('https://nac.kmitl.ac.th/dana-na/auth/url_default/welcome.cgi')
    try:
        select = Select(driver.find_element_by_id('realm_17'))
        select.select_by_value('ระบบแอคเคาท์เก่า (Generation1)')
        driver.execute_script(open("./auto_auth.js").read())
        write_log()
    except:
        print ('Can\'t load page element not found')
        write_error_log()


def internet_on():
    try:
        response=urllib.request.urlopen('http://www.google.co.th',timeout=20)
        return True
    except urllib.error.URLError as err: pass
    return False


while(True):
    if internet_on():
        print ('Connection working find.')
    else:
        print('Connection Lost Reloadscript.')
        connect()
    for each in range(0,5):
        sys.stdout.write(" .")
        sys.stdout.flush()
        time.sleep(1)
    clear()
