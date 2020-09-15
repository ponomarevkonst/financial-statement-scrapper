import concurrent.futures

from nalog_scrapper.data_processing import FinStatements
from nalog_scrapper.formulas import *
from nalog_scrapper.downloaders import download_excel_from_nalog
from nalog_scrapper.scrappers import get_org_n_from_nalog_ru


def process_file(org_info):
    fin = FinStatements(download_excel_from_nalog(org_info['id']))
    years = [2019, 2018]
    for year in years:
        org_info.update({year: {'profit_margin': profit_margin(fin, year), 'ebit_margin': ebit_margin(fin, year),
                                'sales_margin': sales_margin(fin, year), 'gross_margin': gross_margin(fin, year),
                                'roe': roe(fin, year)}})
    return org_info


def main(inn_list):  # ['6704000505', '5321029508']
    org_n_list = get_org_n_from_nalog_ru(inn_list)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(process_file, org_n_list)
    return list(results)


if __name__ == '__main__':
    print(main(['6704000505', '7706107510', '5321029508']))
