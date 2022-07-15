import pandas as pd
df=pd.read_csv("data.csv")
ti=df.sum(axis="columns")# column sum
ti2=ti**2#squaring them to get tisquare
ti2=list(ti2)#to get sum of ti2 we are makinh into list
ti2.append(sum(ti2))
ti=list(ti)
sumti=sum(ti)
ti.append(sumti)
bj=df.sum(axis="rows")
df=df.append(bj,ignore_index=True)
bj2=bj**2
temp=list(bj2)
sumbj2=sum(temp)
temp.append(sumbj2)
temp.append(0)
df['ti']=ti
df['ti**2']=ti2
bj2=pd.DataFrame(temp)
df.loc[4]=temp
print(df)
#calculations
raw=pd.read_csv("data.csv")
raw=raw**2
rss=raw.values.sum()
print(rss)

cf=ti[len(ti)-1]**2/raw.size
print(cf)

sst=rss-cf
print(sst)

sstr=((1/len(raw.columns))*ti2[len(ti2)-1])-cf
print(sstr)

ssb=((1/len(raw))*temp[len(temp)-2])-cf
print(ssb)

sse=sst-sstr-ssb
print(sse)

#ANOVA 2 WAY CLASSIFICATION
s2tr=sstr/(len(raw)-1)
s2b=ssb/(len(raw.columns)-1)
s2e=sse/((len(raw)-1)*(len(raw.columns)-1))

print(s2tr)
print(s2b)
print(s2e)

ftr=s2tr/s2e
fb=s2b/s2e

print(ftr)
print(fb)



   b1   b2   b3  b4    ti  ti**2
0   13    7    9   3    32   1024
1    6    6    3   1    16    256
2   11    5   15   5    36   1296
3   30   18   27   9    84   2576
4  900  324  729  81  2034      0
786
588.0
198.0
56.0
90.0
52.0
28.0
30.0
8.666666666666666
3.230769230769231
3.4615384615384617
