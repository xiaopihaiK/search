import requests
import json
import re
import base64

keywords = base64.b64encode(raw_input('please input keywords:'))

count = raw_input('please input result count:')

url = 'https://fofa.so/api/v1/search/all?email=&key=&qbase64='+str(keywords)+'&size='+str(count)

filename = base64.b64decode(keywords)

f=open(filename+'.txt','a')

try:
	r=requests.get(url = url)
	size = re.findall(',"size":(.*?),',r.content)[0]
	r=r.text
	r=json.loads(r)['results']
	for i in range(len(r)):
		res = r[i-1][1]+':'+r[i-1][2]
		print res
		f.write('%s\n'%str(res))
	print '-'*50
	print 'All result total : %s'%str(size)
	print '-'*50
except Exception as e:
	print e
