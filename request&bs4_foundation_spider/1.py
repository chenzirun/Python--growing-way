import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status
		r.encoding = r.apparent_encoding
		return r.text

	except:
		return ""

# 提取html中得有用部分， 添加到list中
def fillUnivList(ulist, html):
	soup = BeautifulSoup(html, 'html.parser')
	for tr in soup.find('tbody').children:
		if isinstance(tr, bs4.element.Tag):
			tds = tr('td')
			ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])



def printUnivList(ulist, num):
	#print("{:^10}\t{:^12}\t{:^10}\t{:^10}".format('排名','学校','地区', '分数'))
	# 这个{4} 的作用是表示在打印学校名称时，使用format函数的第四个变量也就是chr（12288）来进行填充，就是用中文字幅宽度来填充，chr（12288）中文字符空格填充
	tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"
	print(tplt.format('排名','学校','地区', '分数',chr(12288)))
	for i in range(num):
		u = ulist[i]
		print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))

def main():
	uinfo = []
	url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
	html = getHTMLText(url)
	fillUnivList(uinfo, html)
	printUnivList(uinfo, 20)

main()



