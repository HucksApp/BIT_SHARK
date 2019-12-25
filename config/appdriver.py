
#firefox_driver = webdriver.Firefox('/Users/Ahrabprince/PycharmProjects/bit_shark_v1/web_drivers/geckodriverr')


def get_wallet_details(driver , address_link, i,count,priv_k_l):
    driver.get(address_link)
    balance_all = driver.find_elements_by_css_selector('div.sc-8sty72-0.cyLejs span.bFGdFC.sc-16b9dsl-1.iIOvXh')
    final_balance_all=balance_all[10].text
    addRs =balance_all[1].text
    fbList=float(final_balance_all.split(' ')[0])
    link_obj ={'fbList':fbList, 'wal_count':count}
    print(f'this is final balance list {fbList}')
    print(f'this is final balance count {count}')
    print(f'this is private address list {link_obj}')
    

    #if fbList>=0.001:
    for x in priv_k_l:
        if x['private_key_count'] ==link_obj['wal_count']:
            priv_access_key = x['private_key']
    print(f'this wallet {final_balance_all} was found in  page {i} and the address is {addRs}..the private key {priv_access_key}')
    with open('/Users/Ahrabprince/PycharmProjects/bit_shark_v1/result/result.txt','a') as result:
       result.write(f'this wallet balance: {final_balance_all}. was found in  page {i} and the wallet address is {addRs}..the private key {priv_access_key}'+ "\n")

    print(f'EMPTY WALLET')
    #driver.back()


def drive_in(url,driver,add_list,priv_k_l):
    # Values
    count = 0
    driver.get(url)
    assert 'l' in driver.title

    private_keys = driver.find_elements_by_css_selector('span[id]')
    for private_key_elem in private_keys:
        private_key = private_key_elem.get_attribute('id')
        count += 1
        key_obj = {'private_key':private_key, 'private_key_count':count}
        priv_k_l.append(key_obj)


    compress_addresses = driver.find_elements_by_css_selector('span a:last-of-type')
    for comp_address_elem in compress_addresses:
        comp_address = comp_address_elem.text

    wallet_addresses = driver.find_elements_by_css_selector('span a:nth-of-type(2)')
    for address_elem in wallet_addresses:
        wallet_address = address_elem.text
        address_link = address_elem.get_attribute('href')
        add_list.append(address_link)
    







    # with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor
        #  executor.submit(get_wallet_details, driver, address_link)









