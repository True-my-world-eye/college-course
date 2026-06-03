class Calculator:
    def __init__(self):
        self.hist=[]
    def add(self, a: float, b: float) -> float:
        res=a+b
        self.hist.append(("add",a,b,res))
        return res
    
    def subtract(self, a: float, b: float) -> float:
        res=a-b
        self.hist.append(("subtract",a,b,res))
        return res
    def multiply(self, a: float, b: float) -> float:
        res=a*b
        self.hist.append(("multiply", a, b, res))
        return res

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("除零错误")
        res = a / b
        self.hist.append(("divide", a, b, res))
        return res
    
    def power(self, a: float, b: float) -> float:
        res = a ** b
        self.hist.append(("power", a, b, res))
        return res
    
    def history(self)->list:
        return self.hist

if __name__ == "__main__":
    c=Calculator()
    c.add(1,2)
    c.subtract(2,3)
    c.multiply(3,4)
    c.divide(4,5)
    c.power(2,3)
    print(c.history())
    