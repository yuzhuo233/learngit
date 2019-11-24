'''
import multiprocessing as mp
import os

	
from multiprocessing.dummy import Pool as ThreadPool # 线程池
import threading
 
def job(q):
	av_number=Queue.get(timeout = 1)
    comm = 'you-get '+ 'https://www.bilibili.com/video/av'+str(av_number)+' -o D:/dogvedio'
	os.system(comm)
	
if __name__ == '__main__':
	q = Queue(maxsize)
	numbers = [74801042,71424947,73449123]
	for url in lista:
	comm = 'you-get '+ 'https://www.bilibili.com/video/av'+av_number+' -o D:/dogvedio'
	os.system(comm)
	
    pool = ThreadPool(4) # 创建一个包含4个线程的线程池
    pool.map(job, range(12))
    pool.close() # 关闭线程池的写入
    pool.join() # 阻塞，保证子线程运行完毕后再继续主进程 
	'''
import requests
import json
import re
headers={
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': "buvid3=A044DA74-C01B-42BC-B372-1EACFEE1A3B1110261infoc; LIVE_BUVID=AUTO2915597160962481; UM_distinctid=16b265372d8272-00341ea93c651c-37c153e-1fa400-16b265372d9752; stardustvideo=1; CURRENT_FNVAL=16; rpdid=|(u)~m~Rm)~l0J'ullm~uYuJ); fts=1563001956; _uuid=D0E5C074-5557-704F-CD29-F83ABC9F212667702infoc; _ga=GA1.2.1119830336.1570779240; sid=5wh5x38u; im_notify_type_31796618=0; CURRENT_QUALITY=16; INTVER=1",
'Host': 'api.bilibili.com',
'Referer': 'https://www.bilibili.com/v/life/animal/?spm_id_from=333.5.b_7072696d6172795f6d656e75.66',
'Sec-Fetch-Mode': 'no-cors',
'Sec-Fetch-Site': 'same-site',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

for i in range(1,2):
#url='https://api.bilibili.com/x/tag/ranking/archives?callback=jqueryCallback_bili_878756404671655&tag_id=17181&rid=75&type=300&pn='+str(i)+'&ps=20&jsonp=jsonp&_=1574525557867'''	
	url='https://api.bilibili.com/x/tag/ranking/archives?callback=jqueryCallback_bili_7203244338086447&tag_id=17181&rid=75&type=300&pn=313&ps=20&jsonp=jsonp&_=1574526048317'
	res=requests.get(url=url,headers=headers)
	text=res.text
	data = re.findall('{.*}',text)[0]       
	data= json.loads(data)
	ids=[]
	for archive in data['data']['archives']:
		ids.append(archive['aid'])
	print(ids)