import requests
import time
import re
import base64

requests.adapters.DEFAULT_RETRIES = 5

fread = open('result.txt','r')

fwrite = open('xx.json','a')

all_search = []

for i in fread.readlines():
	x = 'net:"'+i.strip('\n')+'"'
	all_search.append(x)

key = ""

# keywords = raw_input('please input keywords :')

# count_com = 'https://api.shodan.io/shodan/host/count?key='+str(key)+'&query='+str(keywords)

# content_url = 'https://api.shodan.io/shodan/host/search?key='+str(key)+'&query='+str(keywords)

def get_count():
	for keywords in all_search:
		count_com = 'https://api.shodan.io/shodan/host/count?key='+str(key)+'&query='+str(keywords)
		content_url = 'https://api.shodan.io/shodan/host/search?key='+str(key)+'&query='+str(keywords)
		try:
			r=requests.get(url = count_com)
			time.sleep(2)
			count = int(r.content.split('"total":')[1].split('}')[0])
			page_count = count/100
			print page_count
			get_content(page=page_count,content_url = content_url)
		except Exception as e:
			print e

def get_content(page,content_url):
	for i in range(1,page+1):
		try:
			r=requests.get(url = content_url+'&page='+str(i))
			time.sleep(2)
			encode = base64.b64encode(r.content)
			fwrite.write('%s\n'%str(encode))
			# ip = re.findall('"ip_str": "(.*?)"',r.content) # front re result and next to parse this data
			# port = re.findall('"port": (.*?),',r.content)
			# city = re.findall('"city": (.*?),',r.content)
			# for ii in range(0,100):
			# 	res = str(ip[ii])+str(':')+str(port[ii])+str('----')+str(city[ii]) # per page total 100 result and from 0 to 100 to show this data
			print '-'*30 + 'Page : '+str(i)+'-'*30
		except Exception as e:
			print e

get_count()
