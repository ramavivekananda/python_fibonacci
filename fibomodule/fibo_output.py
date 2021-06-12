import sys
from fibonacci import  Fibonacci 
result = []

try:
    print("Enter the number to get fibonacci > ")
    inputValue = int(input())
    outputObj = Fibonacci(inputValue)
    outputObj.create_fibonacci()
    result = outputObj.get_output()
    if len(result) > 0 :
        print("Fibonacci Result is -> " , result)

except:
    print("Some error ", sys.exc_info()[0], "occurred.")