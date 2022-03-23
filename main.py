# A+B
# 类型1：多组输入，组数未知

# 方法1：
# import sys
# for line in sys.stdin:
#     # strip()不带参数，默认是清除两边的空白符
#     # split()通过指定分隔符对字符串进行切片，默认以空格为分隔符
#     a = line.strip().split()
#     print(a)
#     a = [int(x) for x in a]
#     print(a)
#     print(sum(a))

# 方法二
# while True:
#     try:
#         a,b = map(int,input().strip().split())
#         print(a + b)
#     except EOFError:
#         break

# while True:
#     try:
#         l = list(map(int,input().strip().split()))
#         print(sum(l))
#     except EOFError:
#         break


# 类型2:多组输入，组数t已知

# 方法1:忽视组数t的输入，其余组照常遍历
# import sys
# for line in sys.stdin:
#     data = list(map(int,line.strip().split()))
#     if len(data) == 1:
#         continue
#     else:
#         print(data[0]+data[1])

# 方法2:使用内置函数
# t = int(input())
# for i in range(t):
#     a,b = map(int,input().strip().split())
#     print(a+b)
#
# t = int(input())
# for i in range(t):
#     l = list(map(int,input().strip().split()))
#     print(sum(l))


# 类型3:多数输入，有终止条件
# 方法1:
# import sys
# for line in sys.stdin:
#     a,b = map(int,line.strip().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)
#
# import sys
# for line in sys.stdin:
#     a = list(map(int,line.strip().split()))
#     if a == [0,0]:
#         break
#     print(sum(a))


# 方法2:
# while True:
#     n,m = map(int,input().strip().split())
#     if n == 0 and m == 0:
#         break
#     print(n+m)


# 类型4:多组输入，有终止条件，每行个数已知
# 方法1:
# import sys
# while True:
#     line = sys.stdin.readline().strip()
#     if line == '0':
#         break
#     else:
#         l = list(map(int,line.strip().split()))
#         print(sum(l[1:]))

# 方法2:
# while True:
#     l = list(map(int,input().split()))
#     if len(l) == 1 and l[0] == 0:
#         break
#     else:
#         print(sum(l[1:]))

# while True:
#     l = list(map(int,input().strip().split()))
#     if l == [0]:
#         break
#     else:
#         print(sum(l[1:]))

# 类型5:多组输入，有组数t,求一系列和
# 方法1:
# n = int(input())
# for i in range(n):
#     l = list(map(int,input().strip().split()))
#     print(sum(l[1:]))

# 类型六：多组输入，每行个数已知，一系列和
# import sys
# for line in sys.stdin
#     list = list(map(int,line.strip().split()))
#     print(sum(l[1:]))
#
# while True:
#     try:
#         l = list(map(int,input().strip().split()))
#         print(sum(l[1:]))
#     except EOFError:
#         break


# 字符串排序
# import sys
# fi_line = sys.stdin.readline()
# se_line = sys.stdin.readline()
# string = se_line.strip().split()
# string.sort()
# st = ' '.join(string)
# print(st)
#
#
# while True:
#     try:
#         n = int(input())
#         mystr = list(map(str,input().strip().split()))
#         mystr.sort()
#         print(' '.join(mystr))
#     except EOFError:
#         break
#
#
# import sys
# for line in sys.stdin:
#     lists = line.strip().split(',')
#     lists.sort()
#     print(','.join(lists))

while True:
    try:
        mystr = input().strip().split(',')
        mystr.sort()
        print(','.join(mystr))
    except EOFError:
        break
