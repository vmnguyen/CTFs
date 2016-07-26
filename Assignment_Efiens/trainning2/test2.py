
import gmpy2

n = 175564501286736789057775865657776940085217569623184268057093988563063442511327664329120759084240597208110083094265310834575064432545013887480404476008775753831651335146021224992757262351029271514782552450025849748627578330991434171599998210643107358643024202865417624557379469790863463884107347254855965878987
i =  (int)(gmpy2.isqrt(n))
for m in range(1,10000000):
	p = i + m
	q = (int)(n/(i+m))	
	result = n - p*q
	if result == 0:
		print p
		print q