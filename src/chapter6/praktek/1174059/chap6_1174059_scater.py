# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:35:19 2019

@author: Ah elah
"""

def scatter(npm):
	import matplotlib.pyplot as plt
	import random as r
	i = (int(npm)%3)+2
	rowcol = ""
	if i%2==0:
		row=i/2
		rowcol=str(int(row))+"2"
	if i%3==0:
		row=i/3
		rowcol=str(int(row))+"3"
	a=1
	while a<=i:
		plt.subplot(int(rowcol+str(a)))
		y = [r.randint(1,10),r.randint(1,10),r.randint(1,10),r.randint(1,10),r.randint(1,10),r.randint(1,10),r.randint(1,10)]
		plt.plot([1,2,3,4,5,6,7], y,'ro')
		a+=1	
	plt.show()
	return i
scatter("1174059")