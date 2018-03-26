#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
from django.http import HttpResponse
response=requests.get('http://kaijiang.500.com/static/info/kaijiang/xml/kl8/20180326.xml?_A=OCVBTSZE1522035057105');
response.encoding='gb18030'
#print(response.text)
soup=BeautifulSoup(response.text,'lxml');
#nums=soup.find_all(id="ssl_expect_detail",limit=6);
#nums=soup.find_all(class_='td_kjhm01',limit=6);
#nums=soup.select('tbody tr td',limit=6);
nums=soup.select('row',limit=6);
#print(nums);
file = open("title.txt","w")
file.write(str(nums))
file.close()
arr={}
i=0
for num in nums:
	arr[i]={'expect':num['expect'],'opencode':num['opencode'],'opentime':num['opentime']};
	#print(key)
	i=i+1
#print(json.dumps(arr));
def hello(request):
    return HttpResponse(json.dumps(arr))