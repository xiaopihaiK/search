import requests
import time
import re

key = ""

keywords = raw_input('please input keywords :')

count_com = 'https://api.shodan.io/shodan/host/count?key='+str(key)+'&query='+str(keywords)

content_url = 'https://api.shodan.io/shodan/host/search?key='+str(key)+'&query='+str(keywords)

def get_count():
	try:
		r=requests.get(url = count_com)
		count = int(r.content.split('"total":')[1].split('}')[0])
		page_count = count/100
		print page_count
		get_content(page=page_count)
	except Exception as e:
		print e

def get_content(page):
	for i in range(1,page+1):
		try:
			r=requests.get(url = content_url+'&page='+str(i))
			time.sleep(1)
			ip = re.findall('"ip_str": "(.*?)"',r.content)
			port = re.findall('"port": (.*?),',r.content)
			city = re.findall('"city": (.*?),',r.content)
			for ii in range(0,100):
				# res = str(ip[ii])
				res = str(ip[ii])+str(':')+str(port[ii])+str('----')+str(city[ii])
				print res
			print '-'*30 + 'Page : '+str(i)+'-'*30
		except Exception as e:
			print e

get_count()
