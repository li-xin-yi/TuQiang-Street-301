import gmpy2
from gmpy2 import mpz


N=mpz('648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877')

(a,b)=gmpy2.isqrt_rem(N)
A=gmpy2.add(a,1)
while True:
    A2=pow(A,2)
    (x,d)=gmpy2.isqrt_rem(gmpy2.sub(A2,N))
    if d==0:
        p=gmpy2.sub(A,x)
        q=gmpy2.add(A,x)
        if gmpy2.is_prime(p):
            print p
            break
    A=gmpy2.add(A,1)
