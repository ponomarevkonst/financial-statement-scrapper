import io
import zipfile
import requests

def download_excel_from_nalog(org_n):
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