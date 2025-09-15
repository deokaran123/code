# building a calculator using the inbuilt function of python
n = input("Enter the expression: ")
try: 
    print(eval(n))
except SyntaxError :
    print("Please write in correct syntax")
except ZeroDivisionError:
    print("Dividing any number by zero is infinity")
except NameError:
    print("Only Integer values are allowed")
# This calculator is build by Raj "github.com/RudraVitap"

