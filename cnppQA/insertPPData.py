from lxml import etree
import requests
from sqlExecu import insertSql


# 爬取品牌数据并插入到数据库中
for i in range(638,9999):
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
            id = [i]
            rank = div.xpath('//*[@id="pos_bangdan"]/div[2]/div[1]/div/div[2]/div//div[1]/div[1]/a/em/text()')
            types = div.xpath('//*[@id="position"]/a/text()')
            # 处理type不一致的情况
            if len(types) != 4:
                print('\033[1;45m                   %s                        \033[0m'%len(types))

            if len(types) == 5:
                type = [types[-1]]
                kind = [types[-2]]
                sort = [types[1]]
            elif len(types) == 2:
                type = [types[-1]]
                kind = [types[-2]]
                sort = [types[-2]]
            elif len(types) == 1:
                type = [types[-1]]
                kind = [types[-1]]
                sort = [types[-1]]
            else:
                type = [types[-1]]
                kind = [types[-2]]
                sort = [types[-3]]

            # 处理排名品牌不足十个的情况
            if len(rank) < 10:
                while(len(rank) < 10):
                    rank.append("NAN")
            elif len(rank) > 10:
                rank = rank[0:10]


            # 将多个list列表合并，再转为tuple元组
            list_top = id + type + rank
            tup_top = tuple(list_top)
            list_info = id + type + kind + sort
            tup_info = tuple(list_info)
            print(tup_top,tup_info)

            insert_top_sql = 'insert into cnpptop(idpptop,type,rank01,rank02,rank03,rank04,rank05,rank06,rank07,rank08,rank09,rank10) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            insert_info_sql = 'insert into cnppinfo(idppinfo,type,kind,sort) values(%s,%s,%s,%s)'
            insertSql(insert_top_sql,tup_top)
            insertSql(insert_info_sql, tup_info)
resp.close()
