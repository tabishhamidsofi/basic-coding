class Calculator:
    
    def __init__(self,result):
        self.result = result
        
    def add_values(self,a,b):
        addition = a + b
        self.result = addition
        return self.result 
    
    def add(self, value):
        self.result = self.result + value
        return self.result
    
    def multiply_values(self,a,b):
        product = a * b
        self.result = product
        return self.result
    
    def multiply(self, value):
        self.result = self.result * value
        return self.result
    
    def subtract_values(self,a,b):
        difference = a - b
        self.result = difference
        return self.result
    
    def subtract(self, value):
        self.result = self.result - value
        return self.result
     
    def divide_values(self,a,b):
        if b == 0:
            return f'Anything divided by 0 is not defined'
        division = a / b
        self.result = division
        return self.result
    
    def divide(self, value):
        if value == 0:
            return f'Anything divided by 0 is not defined'
        self.result = self.result / value
        return self.result
    
    def underroot(self,a):
        under_root = a ** 0.5
        self.result = under_root
        return self.result


if __name__ == "__main__":
    calc = Calculator(0)

    # Adding the 2 numbers 
    result = calc.add_values(10, 20)
    print(f'Addition = {result}')

    # Subtracting 2 values
    result = calc.subtract_values(20, 5)
    print(f'Subtraction = {result}')

