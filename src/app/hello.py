"""BADLY FORMATTED
def  add_numbers( a,b ):

sum= a+  b
print ("Sum is:",sum )

return sum

class calculator:
def __init__(self,number ):
    self.number= number

def square( self ):return self.number  *self.number
def cube(self):return self.number*self.number*self.number

def  display(self ):print(   "Number:",self.number, "Square:", self.square(), "Cube:",self.cube() )

calc= calculator( 5 )
calc.display( )

"""


def gen_set() -> set[int]:
    return {1, 2, 3}


def main():
    print("Hello from hello.py")


def add_numbers(a, b):
    sum = a + b
    print("Sum is:", sum)

    return sum


class calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number * self.number

    def cube(self):
        return self.number * self.number * self.number

    def display(self):
        print("Number:", self.number, "Square:", self.square(), "Cube:", self.cube())


calc = calculator(5)
calc.display()


if __name__ == "__main__":
    main()
