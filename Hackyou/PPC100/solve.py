#!/usr/bin/python2
import requests
import base64
answer = ""
cookies = dict(PHPSESSID='s29olq64qtq4mkip1uahh88rn4')
while True:
	r = requests.post('http://hackyou-captcha.ctf.su/',  data = {'answer':answer},cookies=cookies )
	result = r.text
	print result
	result =  result.split('<code>', 1 )[1]
	result =  result.split('</code>', 1 )[0]
	result = base64.b64decode(result)
	answer = result
	print result