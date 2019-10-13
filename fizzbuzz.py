import sys
def fizz_buzz(x):
    if x%3==0 and x%5==0:
        return "Fizz_Buzz"
    if x%3==0:
       return "Fizz"
    if x%5==0:
        return "Buzz"
    return (x)
user_input=int(input("Enter Your Number:"))
if type(user_input)==int:
    print(fizz_buzz(user_input))
else:
    print("Enter Value of type integer")
    sys.exit()      
    
