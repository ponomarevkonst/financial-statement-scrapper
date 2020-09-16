import time
from typing import List
from lxml import etree
from io import StringIO
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_org_n_from_nalog_ru(inns: List[str]):
    '''
    Selenium balance sheet scrapper from bo.nalog.ru.
    :param inns: inn of organisations
    :param results: id of input organisations on this site
    :return:
    '''
    options = FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    ac = ActionChains(driver)
    parser = etree.HTMLParser()
    # driver.implicitly_wait(10)
    results = []
    for inn in inns:
        url = f'https://bo.nalog.ru/search?query={inn}&page=1'
        driver.get(url)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search")))
        ac.click().perform()
        tree = etree.parse(StringIO(driver.page_source), parser)
        orgs = tree.xpath('//*[@id="root"]/main/div/div/div[2]/div[2]/a')
        if len(orgs) > 0:
            id_link = orgs[0].attrib['href']
            id = "".join(list(filter(str.isdigit, id_link)))
            org_name = tree.xpath('//*[@id="root"]/main/div/div/div[2]/div[2]/a/div[1]/div[1]/span')[0].text
            results.append({'name': org_name, 'inn': inn, 'id': id})
    return results
