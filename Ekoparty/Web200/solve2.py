#!/usr/bin/python2
import requests

#https://code.activestate.com/recipes/172845-python-luhn-checksum-for-credit-card-validation/
def cardLuhnChecksumIsValid(card_number):  
    """ checks to make sure that the card passes a luhn mod-10 checksum """

    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )

data = requests.post("http://86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000/api.php", headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "X-Requested-With": "XMLHttpRequest", "Referer": "http://86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000/", "Content-Length": "18", "Cookie": "ekocard3r=sVkT-ozU9pYbHcTR8I1CP9GVOu8", "Connection": "close", "X-dotNet-Beautifier": "11; DO-NOT-REMOVE"}, data="{\"action\":\"start\"}")

jdata = data.json()

def get_missing_number_visa(prefix, suffix):  
    for i in range(10):
        for j in range(10):
            for q in range(10):
                for w in range(10):
                    for v in range(10):
                        our_num = str(i) + str(j) + str(q) + str(w) + str(v)
                        if cardLuhnChecksumIsValid(prefix + our_num + suffix):
                            print "FOUND", prefix + our_num + suffix
                            return our_num
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break

def get_missing_number_amex(prefix, suffix):  
    for i in range(10):
        for j in range(10):
            for q in range(10):
                for w in range(10):
                    for v in range(10):
                        for y in range(10):
                            for o in range(10):
                                our_num = str(i) + str(j) + str(q) + str(w) + str(v) + str(y) + str(o)
                                if cardLuhnChecksumIsValid(prefix + our_num + suffix):
                                    print "FOUND", prefix + our_num + suffix
                                    return our_num
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break

def get_missing_number_mcard(prefix, suffix):  
    for i in range(10):
        for j in range(10):
            for q in range(10):
                for w in range(10):
                    for v in range(10):
                        for y in range(10):
                            for o in range(10):
                                for u in range(10):
                                    our_num = str(i) + str(j) + str(q) + str(w) + str(v) + str(y) + str(o) + str(u)
                                    if cardLuhnChecksumIsValid(prefix + our_num + suffix):
                                        print "FOUND", prefix + our_num + suffix
                                        return our_num
                                else:
                                    continue
                                break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break


def solve_amex(prefix, suffix):  
    num = get_missing_number_amex(prefix, suffix)
    print num
    return num

def solve_visa(prefix, suffix):  
    num = get_missing_number_visa(prefix, suffix)
    print num
    return num

def solve_mcard(prefix, suffix):  
    num =  get_missing_number_mcard(prefix, suffix)
    print num
    return num

amex = solve_amex(jdata['pamex'], jdata['samex'])  
visa = solve_visa(jdata['pvisa'], jdata['svisa'])  
mcard = solve_mcard(jdata['pmcard'], jdata['smcard'])

resp = requests.post("http://86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000/api.php", headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://86dc35f7013f13cdb5a4e845a3d74937f2700c7b.ctf.site:20000/", "Cookie": "ekocard3r=sVkT-ozU9pYbHcTR8I1CP9GVOu8", "Connection": "close", "Upgrade-Insecure-Requests": "1", "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "37", "X-dotNet-Beautifier": "12; DO-NOT-REMOVE"}, data = "{\"nvisa\":\""+str(visa)+"\",\"nmcard\":\""+str(mcard)+"\",\"namex\":\""+str(amex)+"\",\"action\":\"validate\"}")  
print resp.json() 