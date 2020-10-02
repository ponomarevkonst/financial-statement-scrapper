# Russian Accounting Standards Financial Statement scrapper
Selenium based web scrapper for retrieving financial statements indexes from bo.nalog.ru.

  1. Run FastAPI server
  2. Send request with id (INN, OKPO) of organisation 
  3. Receive some financial indexes like
      * Profit margin
      * EBIT margin
      * Sales margin
      * Gross margin
      * ROE
      * more soon...
  
### Tech
RASFS scrapper uses a number of open source projects to work properly:

* FastAPI + uvicorn - for realy fast api creating
* Selenium - awesome web-scraping tool
* Firefox + geckodriver - its a selenium driver
* lxml - web page parsing tool
* pandas - excel files parsing tool
* Ansible - for quick deployment on your server

### Installation 


### Deployment
