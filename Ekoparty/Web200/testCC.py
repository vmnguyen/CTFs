#!/usr/bin/python3
# -*- coding: utf-8 -*-
# by ..:: crazyjunkie ::.. 2014
# If you need a Good Wordlist ====> http://uploaded.net/folder/j7gmyz

"""
gencc: A simple program to generate credit card numbers that pass the
MOD 10 check (Luhn formula).
Usefull for testing e-commerce sites during development.
by ..:: crazyjunkie ::.. 2014
"""

from random import Random
import copy
import requests
import json
global nMaster 
nMaster= ""
global nAmexi 
nAmexi= ""
global nVisaa 
nVisaa=  ""
headers = {'Host': '86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/json','X-Requested-With': 'XMLHttpRequest','Cache-Control': 'max-age=0','Referer': 'http://86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000/','Content-Length': '40','Cookie': 'ekocard3r=lx9JmuKXLRMUP,30EgJrKpENlg0','Connection': 'keep-alive'}
cookies = dict(ekocard3r='eqc6Swbst7RiPbz,c4TFsbHpnZb')
payload = {'action': 'start'}
r = requests.post('http://86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000/api.php',json=payload,headers =headers) 
result = r.text
print (result)
pmcard = (r.json().get('pmcard'))
smcard = (r.json().get('smcard'))
pvisa= (r.json().get('pvisa'))
svisa = (r.json().get('svisa'))
pamex =(r.json().get('pamex'))
samex = (r.json().get('samex'))

visaPrefixList = [
        list(pvisa)
       ]

mastercardPrefixList = [
        list(pmcard)]

amexPrefixList = [list(pamex)]



def completed_number(prefix, length,postFix):
    """
    'prefix' is the start of the CC number as a string, any number of digits.
    'length' is the length of the CC number to generate. Typically 13 or 16
    """

    
    
    # generate digits
    flag = True
    tmp = 0
    tmp1 = prefix
    ccnumber = prefix
    while flag:

        checked = int(postFix[3])

        while len(ccnumber) < (length - 4):
            digit = str(generator.choice(range(0, 10)))
            ccnumber.append(digit)

        for i in list(postFix[:3:]):
            ccnumber.append(i)
        #ccnumber.append(list(postFix[:3:]))
        '''
        ccnumber.append(list(postFix[:3:])
        '''
        # Calculate sum

        sum = 0
        pos = 0

        reversedCCnumber = []
        reversedCCnumber.extend(ccnumber)
        reversedCCnumber.reverse()

        while pos < length - 1:

            odd = int(reversedCCnumber[pos]) * 2
            if odd > 9:
                odd -= 9

            sum += odd

            if pos != (length - 2):

                sum += int(reversedCCnumber[pos + 1])

            pos += 2

        # Calculate check digit
        checkdigit = (int(sum / 10 + 1) * 10 - sum) % 10
        
        if tmp >= 1:
            flag = False
        else:
            if checkdigit == checked:
                flag = False
                ccnumber.append(str(checkdigit))
                if len(ccnumber) == length:

                    return ''.join(ccnumber)
            tmp = tmp + 1
            ccnumber = tmp1
            print 


    return "Wrong"


def credit_card_number(rnd, prefixList, length, howMany, postFix):

    result = []

    while len(result) < howMany:

        ccnumber = copy.copy(rnd.choice(prefixList))
        tmpK = completed_number(ccnumber, length,postFix)
        if tmpK != "Wrong":
            result.append(tmpK)

    return result


def output(title, numbers):

    result = []
    result.append(title)
    result.append('-' * len(title))
    result.append('\n'.join(numbers))
    result.append('')

    return '\n'.join(result)

#
# Main
#

generator = Random()
generator.seed()        # Seed from current time

print("credit card generator by ..:: crazyjunkie ::..\n")

mastercard = credit_card_number(generator, mastercardPrefixList, 16, 1, smcard) #16

visa13 = credit_card_number(generator, visaPrefixList, 13, 1,svisa) #13


amex = credit_card_number(generator, amexPrefixList, 15, 1, samex) # 15
print (mastercard[0])
print (visa13[0])
print (amex[0])

nMaster = int(mastercard[0][4:12:])
nVisaa = int(visa13[0][4:9:])
nAmexi =  int(amex[0][4:11:])
print (nMaster)
print (nVisaa)
print (nAmexi)

headers2 = {'Host': '86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0','Accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Referer': 'http://86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000/','Content-Length': '40','Cookie': 'ekocard3r=lx9JmuKXLRMUP,30EgJrKpENlg0','Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1','Content-Type': 'application/x-www-form-urlencoded' ,'Content-Length': '37'}
payload2 = {'nvisa': nVisaa,'nmcard': nMaster, 'namex': nAmexi}
json = {'action': 'validate'}
#payload2 = {'nvisa': visa,'nmcard':mastere, 'namex':amex,'action': 'validate'}
r = requests.post('http://86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000/api.php',json = json,data=payload2,headers =headers) 
print (r.text)