import sys
from encription import *

## { @autor Isac Canedo}

p=lookForProbablyPrime(200)
q=lookForProbablyPrime(200)
rsa=RSA(p,q)
var=sys.argv[1]
file=open(var,"w+")
file.write(str(rsa.n)+'\n'+str(rsa.d))
file.close()
var=sys.argv[2]
file=open(var,"w+")
file.write(str(rsa.n)+'\n'+str(rsa.e))
file.close()
