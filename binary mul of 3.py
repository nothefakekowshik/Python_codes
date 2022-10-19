# def binaryToDecimal(binary):
#     binary1 = binary
#     decimal, i, n = 0, 0, 0
#     while (binary != 0):
#         dec = binary % 10
#         decimal = decimal + dec * pow(2, i)
#         binary = binary // 10
#         i += 1
#     print(decimal)
#     if(decimal%3==0):
#         print('1')
#     else:
#         print('0')
# if __name__ == '__main__':
#     binaryToDecimal(100)
#     binaryToDecimal(101)
#     binaryToDecimal(1001)


a="0"
even_pos=0
odd_pos=0
for i in range(0,len(a),2):
    if(a[i]=="1"):
        even_pos+=1
for i in range(1,len(a),2):
    if(a[i]=="1"):
        odd_pos+=1
    
print(even_pos-odd_pos)

