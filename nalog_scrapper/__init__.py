import io
import zipfile
import requests
import pandas as pd
import concurrent.futures
from typing import List
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_org_n(inns: List[str]):
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
    driver.get("https://bo.nalog.ru/search?allFieldsMatch=false&period=2019&page=1")
    driver.implicitly_wait(10)
    ac.click().perform()
    search = driver.find_element(By.CSS_SELECTOR, "#search")
    results = []
    for inn in inns:
        search.send_keys(inn, Keys.ENTER)
        search.clear()
        org = driver.find_elements(By.CSS_SELECTOR,
                                   '#root > main > div > div > div.results-search-table > div.results-search-tbody > a')
        if len(org) > 0:
            id_link = org[0].get_attribute('href')
            id = "".join(list(filter(str.isdigit, id_link)))
            org_name = driver.find_element(By.CSS_SELECTOR,
                                       '#root > main > div > div > div.results-search-table > '
                                       'div.results-search-tbody > a > div:nth-child(1) > '
                                       'div.results-search-table-item.results-search-table-name > span').text
            results.append({'name': org_name, 'inn': inn, 'id': id})
    return results


def download_excel(org_n):
    """
    Downloader of zipped excel from bo.nalog.ru by site_id of organization.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
    link = f'https://bo.nalog.ru/download/bfo/{org_n}?auditReport=false&balance=true&capitalChange=true&clarification=false&targetedFundsUsing=false&correctionNumber=0&financialResult=true&fundsMovement=true&type=XLS&period=2019'
    downloaded_zip = requests.get(link, headers=headers).content
    zf = zipfile.ZipFile(io.BytesIO(downloaded_zip), 'r')
    with zf.open(zf.namelist()[0], 'r') as file:
        excelfile = file.read()
    return excelfile


def find_in(df, string_code, year, codes=0, years={}):
    """
    Searcher of the value of the needed balance sheet element by year.
    """
    if string_code // 1000 == 1:
        years = {2019: 16, 2018: 22, 2017: 28}
        codes = 13
    elif string_code // 1000 == 2:
        years = {2019: 20, 2018: 27}
        codes = 15
    n = df.iloc[:, codes]
    year_column = years[year]
    index = n.index[list(n).index(str(string_code))]
    value = df.iloc[index, year_column]
    negative = -1 if value[0] == '(' else 1
    try:
        value = int("".join([x for x in value if x.isdigit()]))
    except:
        value = 0
    return negative * value


def process_file(org_info):
    excelfile = download_excel(org_info['id'])
    excel = pd.ExcelFile(excelfile)
    balance = pd.read_excel(excel, 'Balance')
    pnl = pd.read_excel(excel, 'Financial Result')
    represent = lambda number: str(round(100 * number, 2)) + '%'
    profit_margin = lambda year: represent(find_in(pnl, 2400, year) / find_in(pnl, 2110, year))
    ebit_margin = lambda year: represent(find_in(pnl, 2300, year) / find_in(pnl, 2110, year))
    sales_margin = lambda year: represent(find_in(pnl, 2200, year) / find_in(pnl, 2110, year))
    gross_margin = lambda year: represent(find_in(pnl, 2100, year) / find_in(pnl, 2110, year))
    roe = lambda year: represent(
        find_in(pnl, 2400, year) / (find_in(balance, 1300, year) + find_in(balance, 1300, year - 1)))
    years = [2019, 2018]
    for year in years:
        org_info.update({year: {'profit_margin': profit_margin(year), 'ebit_margin': ebit_margin(year), 'sales_margin': sales_margin(year), 'gross_margin': gross_margin(year), 'roe': roe(year)}})
    return org_info

def main(inn_list): #['6704000505', '5321029508']
    org_n_list = get_org_n(inn_list)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(process_file, org_n_list)
    return list(results)

if __name__ == '__main__':
    print(main(['6704000505', '5321029508']))
