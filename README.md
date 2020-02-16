# search
fofa、shodan - api python

res = arr

for i in res:
  print i
  
fp=open(filename,'a')

fp.write('%s\n'%str(i))

fofa：
对单个关键词进行搜索并导出，填入相应的key即可

shodan：
对单个关键词进行搜索并导出，填入相应的key即可

patch：
可以批量对指定的IP段进行获取并且解析，获取的数据base64并且存入json中，后续解析。


