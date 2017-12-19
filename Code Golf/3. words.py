i=raw_input().split(' ')
i.sort()
if len(i)>3: 
 n,o,s,t,v,z=len(i),[],[],0,[],[0,1,2]
 r=((n-1)/3)+1
 for c in z:
  v+=[i[t:t+r-1+int(c<(n%3 if n%3>0 else 3))]]
  k=v[c]
  t+=len(k)
  s+=[max([len(w) for w in k])]
  if len(k)<r:k+=[' '*s[c]]
 for l in range(r):o+=[v[i][l]+' '*(s[i]+1-len(v[i][l])) for i in z]+['\n']
 print ''.join(o)
else:
 print ' '.join(i)

