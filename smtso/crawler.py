import requests


def crawl(pageNumber, limit=50):
    URL = 'https://h.smtso.com/crossURL'

    # data to be sent to api
    data = {'page': 1,
            'limit': 50,
            'crossmethod': 'queryHuoYun',
            'keyword': '',
            'source': '',
            'ttt': 'b',
            '_SeeSearchCustomsData': False,
            'loginName': '55BEE3DA07BF346A55AED1DA04913865',
            'loginPassword': '55BEFFD80791346A5690D19F',
            'cpms': '',
            'hgbm': '',
            'cgs': '',
            'gys': '',
            'cgsdz': '',
            'gysdz': '',
            '_firstClick': 1,
            'StartDate': '2022-01-01',
            'EndDate': '2022-12-15',
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
            'Cookie': 'JSESSIONID=94DD2DED079D0C98F908718D8ACF57A3; accountCode=57ADFFDA13822F3442BED1D60491282F41B9869210E7373554BED1D807B8282C4287E39710B8382157BEEF9110B82468; loginName=55BEE3DA07BF346A55AED1DA04913865; loginPassword=55BEFFD80791346A5690D19F',
            'Origin': 'https://h.smtso.com',
            'Pragma': 'no-cache',
            'Referer': 'https://h.smtso.com/huoyun',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'macOS'
            }

    r = requests.post(URL, timeout=30, headers=headers, data=data)

    result = r.json()
    if r.status_code == 200 and 'rows' in result:
        return result['rows']
    else:
        return []
    # print("Status Code", r.status_code)
    # print("JSON Response ", r.json())
