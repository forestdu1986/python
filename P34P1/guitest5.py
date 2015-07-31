import shelve

s=shelve.open("test.dat")
#s[u"杜林"]=u"浙AF117D"
for i in s:
    print(i, s[i])
s.close()
