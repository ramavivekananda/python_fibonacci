import sys

class Fibonacci :
    def __init__(self, inputnumber) :
        self.number = inputnumber
        self.__output_array = []

    def create_fibonacci(self) :
        try:            
            if self.number <= 0:
                raise Exception("Sorry, numbers should be greater than zero")
            if not type(self.number) is int:
                raise TypeError("Only integers are allowed")
            # implementation starts    
            startingValue, currentValue, nextValue ,count = 0,1,0,0            
            while count < self.number :               
                self.__output_array.append(startingValue)
                count +=1
                nextValue = startingValue + currentValue
                startingValue = currentValue
                currentValue = nextValue
                
        except TypeError:
            print("Only integers are allowed")
        except Exception:
            print("Sorry, numbers should be greater than zero")
        except:
            print("Some error ", sys.exc_info()[0], "occurred.")

    def get_output(self) :
        return self.__output_array