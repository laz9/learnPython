from sqlExecu import selectSql

select_top_sql = 'select * from cnpptop where type = %s'

input_type = input()
datas = selectSql(select_top_sql,input_type)
if not datas:
    print("没有查到相应的数据哦，请检查输入是否正确~")
for data in datas:
    print(data)
    print("为你推荐以下品牌哦~\n1.",data[2],'\n2.',data[3],'\n3.',data[4],'\n4.',data[5],'\n5.',data[6],'\n6.',data[7],'\n7.',data[8],'\n8.',data[9],'\n9.',data[10],'\n10.',data[11])