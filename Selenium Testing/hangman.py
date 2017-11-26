#!/usr/bin/python3
#-*- coding:utf-8 -*-
# author:racher
# date:2017-11-26


import random


print('\033[1;31;40m')
print("*" * 55)
print("*      Welcome to my JuzlDream guessing game.         *")
print("*      Author\t:racher                               *")
print("*      Blog\t:http://www.github.com/juzldream      *")
print("*      Date\t:2017-11-26                           *")
print("*" * 55)
print('\033[0m')

crads = random.randint(1,99)

print(crads)

num = int(input("\033[1;34;40m请输入你要猜的数字：\n\033[0m"))
while num != crads:
	if num > crads:
		num = int(input("\033[1;33;40m猜大了，再猜一次吧！\n\033[0m"))
	else:
		num = int(input("\033[1;34;40m猜小了，再猜一次吧！\n\033[0m"))  

print("\033[1;32;40m恭喜你中了%d万元大奖！土豪我们做朋友吧！\n\033[0m"%(crads))