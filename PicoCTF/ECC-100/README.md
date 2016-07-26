#ECC-100
Before i solve this challenge, i don't know about Elliptic curves. I used google to find out what is Elliptic curves and Elliptic curves cryptography. 

When i found it, i use Sega to solve this problem. 

First, from the position of C, I can find out ax + b( a = 0, so easy to find b :))) ) 

I see y^2 = x^3 + ax + b mod n. When i saw it in the first time, i thought it just modular on the right side, but actualy, they modular both of it, left and right.


Use Sage, i definied F = Zmod(928669833265826932708591)

X = 236857987845294655469221

Y = 12418605208975891779391

Then i can get b by that way: b = F(Y^2 - X^3)

b = 268892790095131465246420

After that, i define Elliptic curves with a = 0, b = 268892790095131465246420, and modular F

Folow that link 'http://doc.sagemath.org/html/en/reference/plane_curves/sage/schemes/elliptic_curves/constructor.html', i find that i just need 3 argument to define this EllipticCurve, because a1 = a2 = a3 = 0

E = EllipticCurve(F, [ 0, 268892790095131465246420 ]) 

Create new point of E

C = E.point((X,Y))

I can get M by this command: "M = 87441340171043308346177 * C"

M = (6976767380847367326785 : 828669833265826932708578 : 1)

=> Mx = 6976767380847367326785

   My = 828669833265826932708578
   
Decode 2 numbers, we can get the flag

Flag is: 'E L L I P T I C   C U R V E S   A R E   F U N'

