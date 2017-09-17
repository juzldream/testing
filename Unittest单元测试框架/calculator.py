#!/bin/python


class Count:
	
	def __init__(self,a,b):
		self.a = int(a)
		self.b = int(b)

	def add(self):
		'''
		计算加法。
		'''
		return self.a + self.b

	def sub(self):
		'''
		计算加法。
		'''
		return self.a - self.b

	def is_prime(self,n):
		'''
		判定一个数是否是质数。
		'''
		if n <= 1:
			return False
		for i in range(2,n):
			if n % i == 0:
				return False
		return True
