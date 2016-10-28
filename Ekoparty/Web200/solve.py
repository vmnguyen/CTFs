import requests
import json
headers = {'Host': '86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/json','X-Requested-With': 'XMLHttpRequest','Cache-Control': 'max-age=0','Referer': 'http://86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000/','Content-Length': '40','Cookie': 'ekocard3r=RX-t-fOfnW1VV8YlZ,S6eSh,a64','Connection': 'keep-alive'}
cookies = dict(ekocard3r='eqc6Swbst7RiPbz,c4TFsbHpnZb')
payload = {'action': 'start'}
r = requests.post('http://86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000/api.php',json=payload,headers =headers) 
result = r.text
print result
pmcard = int(r.json().get('pmcard'))
smcard = int(r.json().get('smcard'))
pvisa = int(r.json().get('pvisa'))
svisa = int(r.json().get('svisa'))
pamex = int(r.json().get('pamex'))
samex = int(r.json().get('samex'))

master = -smcard  +pmcard
visa = -svisa  +pvisa
amex = -samex +  pamex

master = abs(master)
visa = abs(visa)
amex = abs(amex)
print visa
print master
print amex
headers2 = {'Host': '86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0','Accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Referer': 'http://86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000/','Content-Length': '40','Cookie': 'ekocard3r=RX-t-fOfnW1VV8YlZ,S6eSh,a64','Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1','Content-Type': 'application/json' ,'Content-Length': '89'}
payload2 = {'nvisa': visa,'nmcard': master, 'namex': amex,'action': 'validate'}
#json = {'nvisa': visa,'nmcard':master, 'namex':amex,}
#payload2 = {'nvisa': visa,'nmcard':mastere, 'namex':amex,'action': 'validate'}
r = requests.post('http://86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000/api.php',data=payload2,headers =headers) 
print r.text
# ekocard3r=eqc6Swbst7RiPbz%2Cc4TFsbHpnZb
#print result.split('\n')[2]
