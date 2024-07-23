# lab7q3 Vic 24283699
import functools

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def map(x):
    for i in range(0, len(x)):
        if(x[i] % 2 == 0):
            x[i] = (x[i] / 2)
        else:
            x[i] = (x[i] * 3)
    return x

def my_filter(x):
    temp = []
    for i in range(0, len(x) ):
        if( x[i] >= 5 and x[i] <= 20):
            temp.append(x[i])
        
    return temp
    
def summult(x, y):
    if(x > y):
        return x + y
    else:
        return x*y
        
    
print("Result after map: ", map(data))    
print("Result after filter: ", my_filter(data))
filtered_data = my_filter(data)
print("Result after reduce: ", functools.reduce(summult, filtered_data)) 


