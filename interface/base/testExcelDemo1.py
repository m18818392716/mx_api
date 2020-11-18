import requests
from bs4 import BeautifulSoup
import re

#获取网页源码，生成soup对象
def getSoup(url,headers):
    res = requests.get(url,headers=headers)
    return BeautifulSoup(res.text,'lxml')

#解析数据
def getData(soup):
    data=[]
    ol=soup.find('ol',attrs={'class':'grid_view'})
    for li in ol.find_all('li'):
        tep=[]
        titles=[]
        for span in li.find_all('span'):
            if span.has_attr('class'):
                if span.attrs['class'][0]=='title':
                    titles.append(span.string.strip())  #获取电影名
                elif span.attrs['class'][0]=='rating_num':
                    tep.append(span.string.strip())     #获取评分
                elif span.attrs['class'][0]=='inq':
                    tep.append(span.string.strip())     #获取评论
        tep.insert(0,titles)
        data.append(tep)
        print(tep)
        print("-------------")
        print(data)
        print("=============")
    return data

#获取下一页链接
def nextUrl(soup):
    a=soup.find('a',text=re.compile('^后页'))
    if a:
        return a.attrs['href']
    else:
        return None

if __name__ == '__main__':
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
    url="https://movie.douban.com/top250"
    soup=getSoup(url,headers)
    data=getData(soup)
    print(data)
    nt=nextUrl(soup)
    while nt:
        soup=getSoup(url+nt,headers)
        print(getData(soup))
        nt=nextUrl(soup)