from lxml import etree
import requests

# url = "https://www.cnpp.cn/china/list_8753.html"

for i in range(130,150):
    url = "https://www.cnpp.cn/china/list_" + str(i) + ".html"
    print(url)
    resp = requests.get(url)
    wb_data = resp.text
    html = etree.HTML(wb_data)
    divs = html.xpath('/html/body/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div')
    if not divs:
        print("为空")
    else:
        for div in divs:
            kind = div.xpath('//*[@id="position"]/a[4]/text()')
            name = div.xpath('//*[@id="pos_bangdan"]/div[2]/div[1]/div/div[2]/div//div[1]/div[1]/a/em/text()')
            print(kind, name)

resp.close()
