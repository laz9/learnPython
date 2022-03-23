import pymysql

# 创建连接
# con = pymysql.connect(host='localhost',user='root',password='qwe123',database='pythondb',port=3306)
# 创建游标对象
# cur = con.cursor()

# table_sql = """
#     create table t_student(
#         son int primary key auto_increment,
#         sname varchar(30) not null,
#         age int(2),
#         score float(3.1)
#     )
# """

insert_sql = 'insert into t_student(sname,age,score) values(%s,%s,%s)'

def create_table(sql):
    # 创建连接
    con = pymysql.connect(host='localhost', user='root', password='qwe123', database='pythondb', port=3306)
    # 创建游标对象
    cur = con.cursor()
    try:
        # 执行sql
        cur.execute(sql)
        print('创建表成功')
    except Exception as e:
        print(e)
        print("创建表失败")
    finally:
        con.close()


def insertOne(sql):
    # 创建连接
    con = pymysql.connect(host='localhost', user='root', password='qwe123', database='pythondb', port=3306)
    # 创建游标对象
    cur = con.cursor()
    try:
        # 执行sql
        cur.execute(sql,("小大",18,90))
        # 提交事务
        con.commit()
        print('插入一条数据成功')
    except Exception as e:
        print(e)
        con.rollback()
        print("插入一条数据失败")
    finally:
        con.close()

def insertMany(sql):
    # 创建连接
    con = pymysql.connect(host='localhost', user='root', password='qwe123', database='pythondb', port=3306)
    # 创建游标对象
    cur = con.cursor()
    try:
        # 执行sql
        cur.executemany(sql,[("薯片",18,60),("苹果",18,88),("西兰花",18,99)])
        # 提交事务
        con.commit()
        print('插入多条数据成功')
    except Exception as e:
        print(e)
        con.rollback()
        print("插入多条数据失败")
    finally:
        con.close()

search_sql = 'select * from t_student'

def search(sql):
    # 创建连接
    con = pymysql.connect(host='localhost', user='root', password='qwe123', database='pythondb', port=3306)
    # 创建游标对象
    cur = con.cursor()
    try:
        # 执行sql
        cur.execute(sql)
        students = cur.fetchall()
        for student in students:
            son = student[0]
            sname = student[1]
            age = student[2]
            score = student[3]
            print('son:',son,'sname:',sname,'age:',age,'score:',score)
        print('查询数据成功')
    except Exception as e:
        print(e)
        print("查询数据失败")
    finally:
        # 关闭连接
        con.close()


update_sql='update t_student set sname=%s where sname=%s'

def update(sql):
    # 创建连接
    con = pymysql.connect(host='localhost', user='root', password='qwe123', database='pythondb', port=3306)
    # 创建游标对象
    cur = con.cursor()
    try:
        # 执行sql
        cur.execute(sql,('三三','西兰花'))
        con.commit()
        print('修改成功')
    except Exception as e:
        print(e)
        con.rollback()
        print("修改失败")
    finally:
        # 关闭连接
        con.close()

delete_sql = 'delete from t_student where sname=%s'
def delete(sql):
    # 创建连接
    con = pymysql.connect(host='localhost', user='root', password='qwe123', database='pythondb', port=3306)
    # 创建游标对象
    cur = con.cursor()
    try:
        # 执行sql
        cur.execute(sql, ('三三'))
        con.commit()
        print('删除成功')
    except Exception as e:
        print(e)
        con.rollback()
        print("删除失败")
    finally:
        # 关闭连接
        con.close()


update(update_sql)
search(search_sql)
delete(delete_sql)
search(search_sql)
