import requests
# url = "https://www.cnpp.cn/"
# url1 = "https://www.cnpp.cn/china/list_375.html"
#
# resp = requests.get(url)
# resp1 = requests.get(url1)
#
# print(resp)
# # print(resp.text)
# print(resp1.text)

url = "https://fanyi.baidu.com/sug"

word = input("请输入你要翻译的英文单词")
dat = {
    "kw": word
}

resp = requests.post(url,data=dat)
print(resp.json())
resp.close()