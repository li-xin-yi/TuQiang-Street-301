import gmpy2
from gmpy2 import mpz

N=mpz('720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929')


#A=3p+2q here! (note that (3p+2q)/2 is odd!)

a,b=gmpy2.isqrt_rem(6*N)
A=gmpy2.add(gmpy2.mul(2,a),1) #when |(3p+2q)/2-sqrt(6*N)|<=0.5 hold, there is also |A-2*sqrt(6*N)|<=1, A=ceil(2sqrt(6*N))
A2=pow(A,2)
x,d=gmpy2.isqrt_rem(A2-24*N) #so let 6p=A+x and 4q=A-x, then X=sqrt(A^2-24*N)
if d==0:
    p,r1=gmpy2.f_divmod(gmpy2.sub(A,x),6)
    q,r2=gmpy2.f_divmod(gmpy2.add(A,x),4)
    if r1==0 and r2==0:
        print p
