import plusOperation
import minusOperation

a = int(input("enter a:"))
b = int(input("enter b:"))
op = input("enter an operation:")

if (op == "+"):
    answer = plusOperation.plus(a,b)
    

if (op == "-"):
    answer = minusOperation.minus(a,b)
    
print(f"answer is {answer}")