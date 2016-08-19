import gmpy2
from gmpy2 import mpz

ciphertext=mpz('22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540')
N=mpz('179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581')
e=mpz('65537')

(a,b)=gmpy2.isqrt_rem(N)
A=gmpy2.add(a,1)
A2=pow(A,2)
(x,d)=gmpy2.isqrt_rem(gmpy2.sub(A2,N))
if d==0:
    p=gmpy2.sub(A,x)
    q=gmpy2.add(A,x)
phiN=gmpy2.mul(gmpy2.sub(p,1),gmpy2.sub(q,1))
d=gmpy2.invert(e,phiN)
plaintext=gmpy2.powmod(ciphertext,d,N)
encoded=gmpy2.digits(plaintext,16)
comb=encoded.split('00')
m_encoded=comb[1]
m=m_encoded.decode('hex')
print m
