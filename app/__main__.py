from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import concurrent.futures
import threading
from config.appdriver import drive_in, get_wallet_details



# ask for Browser to be used

browser=str()

print('''
              *************************************************************************
     ***********************************      BIT_SHARK     *******************************************
**********************                     author : HucksApp            *********************************************
     ************************                  version :v-1          *****************************
             ''')

pages_to_check = int(input('PLS ENTER NO OF PAGES YOU WOULD LIKE TO CHECK: '))
starting_page = int(input('PLS ENTER THE PAGE YOU WOULD LIKE TO START FROM : '))


try:

    ch = input('DO YOU WANT TO USE CHROME : ENTER : y or n: ')

    if ch == 'n':
        fr = input('Bit_SHARK will use FIREFOX: ENTER : y: ')
        if fr == 'y':
            browser = 'firefox'
        else:
            print(f'ENTRY IS INVALID: {fr}')
    elif ch == 'y':
        browser = 'chrome'
    else:
        print(f'ENTRY IS INVALID: {ch}')


    driver = webdriver.Chrome('/Users/Ahrabprince/PycharmProjects/bit_shark_v1/web_drivers/chromedriver')
    for i in range(starting_page, pages_to_check):
        add_list=list()
        priv_k_l=list()
        count=0
        url = f'https://lbc.cryptoguru.org/dio//{i}'

        drive_in(driver=driver, url=url, add_list=add_list,  priv_k_l=priv_k_l)
        for link in add_list:
            count+=1

            t=threading.Thread(target=get_wallet_details, args=(driver,link,i,count,priv_k_l,))
            t.start()
            t.join()

        print('main ended')

except Exception as e:

    print(f'this is the error{e}')