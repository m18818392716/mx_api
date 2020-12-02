# coding:utf-8
'''
（1）这是随便找的，贴吧不用headers就可以访问：【美图】杂图_美图吧_百度贴吧
（2）原本也打算抓点妹子图，但我乎这么纯净的界面，还是别污了。

（3）源码重点掌握：Requests请求，Re正则提取标签，Beautifulsoup提取标签；获取图片大小；判断文件夹是否存在；图片保存等。

（4）预留作业：利用Pillow将抓取的图片拼接，形成照片墙，难度★★★☆☆；别以为没用哈，用好了这货词云，图云都可以自撸；后面验证码，图片相似处理都要靠它完成初级处理。这么说吧，数据清洗靠Pandas，文本处理靠Gensim，图片处理靠Pillow，视频处理我不会。

（5）凡是在该源码基础上改编的爬虫，可以将源码投稿到本专栏；奖励若干中、英文Python资料，源码，视频。
'''
import re,requests
from bs4 import BeautifulSoup

headers = {
    # 'Host': 'i.meizitu.net',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding':'gzip, deflate',
    'Upgrade-Insecure-Requests':'1'
}  # 请求头，蛇无头不行，带上吧，后面会讲到用Cookie实现单账号免密登录

s = requests.session()  # 保留会话

def re_test(text):
    '''
    :param text: 网页源文件
    :return: 返回图片的链接
    '''
    # https://imgsa.baidu.com/forum/w%3D580/sign=20bec30aa0ec8a13141a57e8c7029157/2508562c11dfa9ecfd81b1f26bd0f703938fc180.jpg
    img_url = re.findall('https://imgsa.baidu.com/forum/.*?jpg',text)
    return  img_url


def bs_test(text):
    '''
    :param text: 网页源文件
    :return: 返回图片的链接
    '''
    # <img class="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/sign=44312fe1a5af2eddd4f149e1bd110102/1c3477094b36acaf1ce5c71b75d98d1000e99c2f.jpg" size="201260" width="479" height="852">
    soup = BeautifulSoup(text, "lxml")
    img_urls = soup.find_all('img',{'class':'BDE_Image'})
    img_url = [i.get('src') for i in img_urls]
    return  img_url

def img_size(content):
    # 熟悉下面这个图片处理库，对于验证码处理和AI有很大帮助哦。
    from PIL import Image
    from io import BytesIO
    img = Image.open(BytesIO(content))
    # width,height = img.size  # 获取图片大小，更改图片大小，拼接照片墙自己先试试
    return img.size

def save_img(url):
    '''
    :param url: 图片地址
    :return: 木有返回值
    '''
    img_name = url.strip().split('/')[-1]
    print(img_name)
    url_re = s.get(url.strip(),headers=headers)
    if url_re.status_code == 200:  # 200是http响应状态
        # print('准备保存')
        import os
        if not os.path.exists('baidu_img'):  # 没有文件夹，则创建文件夹
            os.mkdir('baidu_img')
        if img_size(url_re.content)[0] > 400 and img_size(url_re.content)[1] > 600:  # 图片宽*高大于400*600像素才保存
            print('尺寸不错，留下了')
            open('baidu_img/' + img_name, 'wb').write(url_re.content)

if __name__ == '__main__':
    for i in range(2) : # 用2页测试一下
        url = 'https://tieba.baidu.com/p/5033202671?pn='+str(i+1)  # 构造和Page相关的链接
        req_text = s.get(url).text
        # print(re_test(req_text)) # 正则
        # urls = re_test(req_text)
        # print(bs_test(req_text)) # BS
        urls = bs_test(req_text)
        for img_url in re_test(req_text):  # 采用正则获取图片链接
            save_img(img_url)