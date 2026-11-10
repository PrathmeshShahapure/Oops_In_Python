class Fraction:
    def __init__(self,a,b):
        self.num=a
        self.den=b

    def __str__(self):
        return (f'{self.num}/{self.den}')

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __eq__(self, other):            
        return self.num * other.den == other.num * self.den


a=Fraction(1,2)
b=Fraction(1,2)
print(a)
print(a==b)
print(a+b)