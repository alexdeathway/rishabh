def fizz_buzz(x):
    if x%3==0 and x%5==0:
        return "Fizz_Buzz"
    if x%3==0:
       return "Fizz"
    if x%5==0:
        return "Buzz"
    return (x)
print(fizz_buzz(5384))