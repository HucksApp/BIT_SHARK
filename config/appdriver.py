
#firefox_driver = webdriver.Firefox('/Users/Ahrabprince/PycharmProjects/bit_shark_v1/web_drivers/geckodriverr')


def get_wallet_details(driver , address_link):
    driver.get(address_link)
    final_balance_all = driver.find_elements_by_css_selector('div.sc-8sty72-0.cyLejs span.bFGdFC.sc-16b9dsl-1.iIOvXh')[10].text
    if final_balance_all.index('0')!=0:
        print(final_balance_all)
    print(f'one thread just finished')
    #driver.back()


def drive_in(url,driver,add_list):
    # Values
    driver.get(url)
    assert 'l' in driver.title

    private_keys = driver.find_elements_by_css_selector('span[id]')
    for private_key_elem in private_keys:
        private_key = private_key_elem.get_attribute('id')

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









