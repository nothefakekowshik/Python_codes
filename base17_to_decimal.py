s="23GF"
#o/p:10980
s=s[::-1]
print(s)
ans=0
dict={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16}
for i in range(len(s)):
    if(s[i] not in dict):
        ans+=(int(s[i])*pow(17,i))
        print(ans)
    else:
        temp_val=dict[s[i]]
        ans+=(int(temp_val)*pow(17,i))
        print(ans)
print()
print(ans)

