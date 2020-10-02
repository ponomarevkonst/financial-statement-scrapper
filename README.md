# Financial Statement scrapper
Selenium based web scrapper for retrieving financial statements indexes.

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
FS scrapper uses a number of open source projects to work properly:

* FastAPI + uvicorn - for realy fast api creating
* Selenium - awesome web-scraping tool
* Firefox + geckodriver - its a selenium driver
* lxml - web page parsing tool
* pandas - excel files parsing tool
* Ansible - for quick deployment on your server

### Installation 
FS scrapper requires python3 to run. You can install dependences by yourself or run setup.py.

```sh
$ python3 setup.py
```

### Deployment
This project has [Ansible Playbook](https://github.com/ponomarevkonst/financial-statement-scrapper/blob/master/deployment/playbook.yml) for quick deployment on your server.
```sh
$ ansible-playbook deploymet/playbook.yml
```
