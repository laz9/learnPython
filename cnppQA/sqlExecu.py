import pymysql

# 创建连接
con = pymysql.connect(host='localhost',user='root',password='qwe123',database='cnpp_db',port=3306)
# 创建游标对象
cur = con.cursor()

insert_top_sql = 'insert into cnpptop(idpptop,type,rank01,rank02,rank03,rank04,rank05,rank06,rank07,rank08,rank09,rank10) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
insert_info_sql = 'insert into cnppinfo(idppinfo,type,kind,sort) values(%s,%s,%s,%s)'

select_top_sql = 'select * from cnpptop where type=%s'
select_info_sql = 'select * from cnppinfo where type=%s'

delete_top_sql = 'delete from cnpptop'
delete_info_sql = 'delete from cnppinfo'

top_tup = (138,'手机','aa','bb','cc','dd','ee','ff','gg','hh','ii','jj')
info_tup = (138,'手机','数码','通讯')

def insertSql(sql, tup):
    # 创建连接
    con = pymysql.connect(host='localhost', user='root', password='qwe123', database='cnpp_db', port=3306)
    # 创建游标对象
    cur = con.cursor()
    try:
        # 执行sql
        cur.execute(sql,tup)
        # 提交事务
        con.commit()
        print('插入一条数据成功')
    except Exception as e:
        print(e)
        con.rollback()
        print('\033[0;35;46m 插入一条数据失败 \033[0m')
    finally:
        con.close()


# insertTopSql(insert_top_sql,top_tup)
# insertTopSql(insert_info_sql,info_tup)

def selectSql(sql,type):
    # 创建连接
    con = pymysql.connect(host='localhost', user='root', password='qwe123', database='cnpp_db', port=3306)
    # 创建游标对象
    cur = con.cursor()
    try:
        # 执行sql
        cur.execute(sql,(type))
        datas = cur.fetchall()
        print('查询数据成功')
        return datas
    except Exception as e:
        print(e)
        print("查询数据失败")
    finally:
        # 关闭连接
        con.close()



# selectSql(select_top_sql,"手机")
# selectSql(select_info_sql,"手机")

def deleteSql(sql):
    # 创建连接
    con = pymysql.connect(host='localhost', user='root', password='qwe123', database='cnpp_db', port=3306)
    # 创建游标对象
    cur = con.cursor()
    try:
        # 执行sql
        cur.execute(sql)
        con.commit()
        print('删除表数据成功')
    except Exception as e:
        print(e)
        con.rollback()
        print("删除表数据失败")
    finally:
        # 关闭连接
        con.close()

# deleteSql(delete_top_sql)
# deleteSql(delete_info_sql)

# selectSql(select_top_sql,"手机")
# selectSql(select_info_sql,"手机")


if __name__ == '__main__':
    deleteSql(delete_info_sql)
    # selectSql(select_top_sql,"冰柜")


