#!/usr/bin/python2
import requests
lines = [line.rstrip('\n') for line in open('data.txt')]

i = 0
for k in lines:	
	r = requests.get('http://hackyou-web100.ctf.su/' + k, auth = ('reader', 'p4$$wordTHNOQ0n2D1'))
	if 'flag' in r.text:
		print r.text
		break