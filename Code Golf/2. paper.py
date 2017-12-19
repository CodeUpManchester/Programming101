a,b,c,r,m,n,s=26,31,28,1.4142,[209,840,124,249,161,916,499],[115,177,354],{'A':26,'B':31,'C':28}
def ht(w):
 return [w,int(round(r*w))]
x=raw_input()
w,h=ht(s[x[0]])
for i in range(10-int(x[1:])):
 w,h=ht(h)
 h=h+1 if h in m else h-1 if h in n else h
print [w,h]
