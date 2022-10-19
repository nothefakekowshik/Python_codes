'''Input : ((()
Output : 2
Explanation : ()

Input: )()())
Output : 4
Explanation: ()() 

Input:  ()(()))))
Output: 6
Explanation:  ()(())'''

str=")()())"
st=[]
max_len=0
for i in range(len(str)):
    if(str[i]=='('):
        st.append(i)
    else:
        if(len(st)!=0):
            st.pop()
        if(len(st)!=0):
            max_len=max(max_len,i-st[len(st)-1])
        else:
            st.append(i)
    

print(max_len)
