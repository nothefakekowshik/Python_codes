def find_distance(x1,x2,y1,y2):
    return (((x2-x1)**2) - ((y2-y1)**2))
def check(input1,input2):
    x_start=1
    y_start=1
    while(x_start < input1 or y_start < input2):
        if(x_start+y_start > input1 or x_start+y_start > input2):
            break
        print(x_start,y_start)

        if( find_distance(x_start,input1,x_start+y_start,input2) > find_distance(x_start+y_start,input1,y_start,input2 ) ):
            y_start+=x_start
        else:
            x_start+=y_start
            
        
        
            
        

input1=int(input())
input2=int(input())
print(check(input1,input2))

