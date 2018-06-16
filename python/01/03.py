#!/usr/local/bin/python3
num1,num2=-1,7
print('猜数字游戏！')
while num1!=num2:
    num1=int(input('请输入一个数字'))
    if num1<num2:
        print('猜的数字小了。。。')
    elif num1>num2:
        print('猜的数字大了。。。')
    elif num1==num2:
        print('恭喜您！猜对了。')

