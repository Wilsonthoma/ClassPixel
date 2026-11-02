#for loop
for i in range(1,11):
    print(f"Welcome to my shop {i}")
    
    my_customer=("Erick","Wilson", "Brian", "Frank", "Angela")
    for name in my_customer:
        print(f"wilcome to our Course {name}")
        
        
        my_shopping=[230,569,890,98]
        total=0
        
        for sum in my_shopping:
            total=total + sum
        print(f"the total for my shopping is:{total}")

#while

num=0
while num <=8:
    print(f"loop : {num}")         
    num+=2
    
    
#imagne you start with a 0 and save 100 every day untill you save 500
money=0
while  money<500:
    money=money+100
    print(f" Your total savings are:{money}") 
print("congratulations! you have reached the target")      
        