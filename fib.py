fn=0
sn=1
res=0
for n in range(10):
    print(res)
    fn=sn
    sn=res
    res=fn+sn
