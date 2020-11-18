from urllib import request, parse
import http.cookiejar

KeyWord = "python"
url = "https://www.lagou.com/jobs/list_" + KeyWord + "?&cl=false&fromSearch=true&labelWords=&suginput="
url_GetJob = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36",
    "Referer": url
}
data = {
    "first": "true",
    "pn": "1",
    "kd": KeyWord
}

cookie_jar = http.cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie_jar)
opener = request.build_opener(handler)

req = request.Request(url, headers=headers)
opener.open(req) # 目的是获取Cookie
req2=request.Request(url_GetJob,headers=headers, data=parse.urlencode(data).encode('utf-8'))
res = opener.open(req2)
print(res.read().decode('utf-8'))