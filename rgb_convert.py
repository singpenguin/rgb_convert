#!/use/bin/env python
#-*- coding:utf-8 -*-

import sys,re

base = [str(x) for x in range(10)] + [chr(x) for x in range(ord("A"),ord("A")+6)]

def convert(c):
	if re.match("^#([0-9a-fA-f]{3}|[0-9a-fA-f]{6})$",c):
		c = c[1:]
		if len(c) == 6:
			print(str(int(c[:2].upper(),16))+","+str(int(c[2:4].upper(),16))+","+str(int(c[4:].upper(),16)))
			return
		elif len(c) == 3:
			print(str(int(c[0].upper(),16))+","+str(int(c[1].upper(),16))+","+str(int(c[2].upper(),16)))
			return
		else:
			print("error color %s" % c)
			return
	else:
		tmp = c.split(",")
		if len(tmp) != 3:
			print("error color %s" % c)
			return
		s = "#"
		for x in tmp:
			num,yu = divmod(int(x),16)
			s += base[num]+base[yu]
		print(s)
		return

if __name__ == "__main__":
	print("example: '#a1b2c3' or 10,11,12")
	if len(sys.argv) < 2:
		print("invalid parameters")
	else:
		convert(sys.argv[1])
