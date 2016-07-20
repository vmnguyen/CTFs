import gmpy2
import math
from decimal import Decimal
import decimal
from gmpy2 import mpz
n1 = 35063150508457777331352115011073055588296956439372831059986364725129481378681107485698749078151688303177960753991173964281787468144958739264272994893082498147897935032463389080743253458533138852265358835661409739659201284776532915316926900713668799446290660488487029111650273206912453218949876875284080458051038334002999686736524265284694748497546859676963824134071406969
n2= 15059397384460919116100377862571156756944824538417086202304833921441315352540046801970145861734056877101504659505381546755837815101591771626306527657970358160959117210354354781393049545888494609622149272962585700967963058516423228763177232170656777211652327897450240701089704850828937562245233405715040283658631874802344687977119401088983582827907614471403921861250226567
n3 = 25421427570134964001410885528157148491730957791615978254612776161959717607185959344377640456719897494645280647039941544750603657171803194383741961629042507917994029486611721332965904051895200703070171254831075364560308498233097992460447756581694005842472151116446376171206682939469906334710242931783881925847598757932339012847663691637002961473135487429018749299162912311
c1 = 20803199418134966193125000577816487509741212749561201823168635617595656926231297584917425024427142311605862344929053565607225030802798995655195566457362125451456023523966781216718773827242955544208943620217719429881111568136264470646050462609856169752642598258016144382059546322004324796912762397972638262906666837254586177691808415810518363397409013692925365524993556854
c2 = 43064740712761063617840230956158894748384947538837089370580386439680527464911727518977922461032659028138420575474274591012650701699868039519465201273263026482354364229025737682196151799608430437357539761456135640227823186569581905611196846183650557524143233639907227838468464441047974728496363837078884853803711846935129309186516651316458337504198667098346096168747993105
c3 = 24576717603547727410754890507253662573538018214641948134089815736006020881615258206943424281706233245662019857213453172351366336772854594528570929754485018881803167187477933769487367318101761284150233610612720620858592661454122817650588608009717367577228439765393708695027920498847770979739948321504702656150537601996832709214701207384469467478668870348298263008928606024

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
t1 =  c1* (n2*n3)*modinv(n2*n3,n1)

t2 =  c2*(n1*n3)*modinv(n1*n3,n2)
t3 =  c3*(n2*n1)*modinv(n2*n1,n3)
c = (t1+t2+t3)%(n1*n2*n3)
c =decimal.Decimal(c)
temp =  int(pow(mpz(c), 0.5))
print temp
message = hex(temp).lstrip('0x')
print 'message = ', message
