import requests as rq
import re
import os
import time
import json

from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
from IPython.core.display import clear_output
from random import randint
from requests import get
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from time import time
start_time = time()

from warnings import warn

def headers_edit(cookies):
    headers = {
        # must
        "Host": "app.joinhandshake.com"
        ,'X-Requested-With': 'XMLHttpRequest'
        ,"Cookie": cookie
        ,"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
        ,'Accept': 'application/json, text/javascript, */*; q=0.01'
        #
        ,'Accept-Encoding': 'gzip, deflate, br'
        ,'Accept-Language': 'zh-CN,zh;q=0.9'
        ,'Connection': 'keep-alive'
        ,'Sec-Fetch-Dest': 'empty'
        ,'Sec-Fetch-Mode': 'cors'
        ,'Sec-Fetch-Site': 'same-origin'
        ,'cache-control': 'no-cache, no-store'
    }
    return headers


def data_edit(query, page=1):
    data = {
        'category': 'Posting',
        "ajax": "true",
        "including_all_facets_in_searches": "true",
        "page": page,
        "per_page": "25",
        "sort_direction": "desc",
        "sort_column": "default",
        "query": query
    }
    return data


def get_query_search(headers, data, search_type=1):
    url = 'https://app.joinhandshake.com/postings?'
    my_data = rq.get(url, headers=headers, data=data).text

    if search_type == 1:
        my_json = json.loads(my_data)
        return int(my_json['total_pages'])
    else:
        re_data = re.findall('.000Z","job_id":(.*?),',str(my_data))
        return re_data


if __name__ == '__main__':
    cookie = 'production_auth_token=d2NSTEEwN1UvRWl1TjhXOEFZRXlqRUdWaGtIb0NRYWhwVzdvRXdSQ2s3NWNVbVBWSHIwdmhKek9mREJ2d2pteUZUVFM0VjN0NWUyaXdnb1g5R1V3N202dTFUdXFlYW9nK1A2OTlTWm1oNTZNVFRrN0s1VEVGNHlyeTN0TEhocnhuc2tudXV2eG1TSzdQOFJ4bS9wSWQ4N3ZlaEUyeW55YWYvV3Q1d2hDVWRQZmNtWGFhWU84N0JKQWYzTUoyOVY5Tm0zNHE0MUFkLzJJRGVrSUhOR0xYZUxlclM1a2p6TTdmRWpPNCsxL0Z0a1IwVVZtL3FGQ0dCdkh0RENNMzZvK0xKY0gyTndYbDJwcVVRT2lLQUxuelNhdkU1Y1JVdlcxWXU0c2ZwZUEydmp1L29UZWdQczZKMitRSHBOTGU2RW1Pa2lUV0hCZ0dnZkdlYkdKdktkaldlaXRFNmdQK3ZhL2JCUmpoV3hqU2lkTFFZUEpqeGJMa0YyLzNZdWZYMktDQkRQaDZuVEpJZk5lV2tKUDl3MDVhZDg0dGlScGxhSEFPdnNVa3NtYXpDbWI2S1RFUDg1b2JWUGdhZ2Z0c2hUMS0tVUpYcnJlTlFCM1c5c1RuN25PUjJoUT09--7f6f6806635335c33bae774d9c31a0689c47b51f'
    # default
    headers = headers_edit(cookie)
    query = "computer science"
    # first to get page
    data = data_edit(query=query)
    query_page = get_query_search(headers, data, search_type=1)
    print(query, query_page)

    # progress = 1
    # with open(f'./results/{query}_job_id_{progress}.txt', 'w',
    #           encoding='utf-8') as f:
    #     # start to do a for
    #     for simple_page in range(progress, query_page+1):
    #         data = data_edit(query=query, page=simple_page)
    #         ids = get_query_search(headers, data, search_type=2)
    #         for each_id in ids:
    #             f.write(each_id)
    #             f.write('\n')
    #         print(progress)
    #         progress += 1
    #         time.sleep(0.5)

    progress = 1450
    with open(f'./results/{query}_output_{progress}.txt', 'w',
              encoding='utf-8') as g:
        with open(f'./results/{query}_job_id_1.txt', 'r',
                  encoding='utf-8') as f:
            for _ in range(progress):
                next(f)
            for num, line in enumerate(f):

                job_id = line.strip()
                url = f"https://app.joinhandshake.com/jobs/{job_id}" \
                              "/search_preview?is_automatically_selected=false&_=1602699600622"

                response = rq.get(url, headers=headers)
                time.sleep(0.3)
                job_json = json.loads(response.text)
                idx = job_json['job']['id']
                role_name = job_json['job']['title']
                try:
                    location = job_json['job']['locations'][0]['name']
                except IndexError:
                    location = 'United States'
                desc = job_json['job']['description']
                job_type = job_json['job']['employment_type']['name']
                salary = job_json['job']['pay_rate']
                try:
                    employee = job_json['job']['employer']['institution_size']['name']
                except KeyError:
                    employee = 'Not Specified'

                print(idx, role_name, location, job_type, salary, employee)
                json_parse = {
                    'idx': idx,
                    'role_name': role_name,
                    'location': location,
                    'description': desc,
                    'job_type': job_type,
                    'pay_rate': salary,
                    'size': employee
                }
                s = json.dumps(json_parse)
                g.write(s)
                g.write('\n')
