import requests
import os


def crawl(pageNumber, limit=50, fromDate='2022-01-01', toDate='2022-12-15'):
    URL = 'https://h.smtso.com/crossURL'
    # print("loginName", os.getenv('loginName'))
    # data to be sent to api
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    ua += '  (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

    data = {'page': 1,
            'limit': 50,
            'crossmethod': 'queryHuoYun',
            'keyword': '',
            'source': '',
            'ttt': 'b',
            '_SeeSearchCustomsData': False,
            'loginName': os.getenv('loginName'),
            'loginPassword': os.getenv('loginPassword'),
            'cpms': '',
            'hgbm': '',
            'cgs': '',
            'gys': '',
            'cgsdz': '',
            'gysdz': '',
            '_firstClick': 1,
            'StartDate': fromDate,
            'EndDate': toDate,
            'Origin_Country': '',
            'Local_Port': '',
            'Transport': '',
            'Foreign_Port': ''
            }

    headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'JSESSIONID=; accountCode=; loginName=;loginPassword=',
            'Origin': 'https://h.smtso.com',
            'Referer': 'https://h.smtso.com/huoyun',
            'User-Agent': ua,
            'X-Requested-With': 'XMLHttpRequest',
            }

    r = requests.post(URL, timeout=30, headers=headers, data=data)

    result = r.json()

    if r.status_code == 200 and result['code'] == 0:
        return result['rows']
    else:
        print(result)
        return []
    # print("Status Code", r.status_code)
    # print("JSON Response ", r.json())
