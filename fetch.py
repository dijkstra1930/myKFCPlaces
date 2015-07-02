#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib.parse
import urllib.request
import json
from collections import Counter

# Constants
BASE_URL = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'

# vars
cities = []
result = Counter()

def fetch_kfc(cityname):
	values = {'cname' : cityname, 'pageIndex' : '1', 'pageSize' : '1' }
	data = urllib.parse.urlencode(values)
	data = data.encode('utf-8') # data should be bytes
	req = urllib.request.Request(BASE_URL, data)
	req.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
	with urllib.request.urlopen(req) as response:
	   myres = json.loads(response.read().decode("utf-8"))
	   return myres['Table'][0]['rowcount']

def fetch_all_cities():
	with open(INPUT_FILE, 'r') as f:
		cities = f.read().split(',')

	with open(OUTPUT_FILE, 'w', encoding='utf8') as outfile:
		for single_city in cities:
			if(single_city):
				city_count = fetch_kfc(single_city)
				result[single_city] = city_count
				outfile.write(single_city + ',')
				outfile.write(str(city_count) + '\n')
				outfile.flush()
				print(result)

fetch_all_cities()
