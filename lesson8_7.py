"""7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата."""


class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        # (a+bi) + (c+di) = (a+c)+(b+d)i
        # a=>c b=>d
        return f"({(self.a + other.a)}+{(self.b + other.b)}i)"

    def __mul__(self, other):
        # (a+bi)·(a′+b′i)=(a·a′−b·b′)+(a·b′+b·a′)i
        return f"({(self.a*other.a - self.b*other.b)}+{(self.a*other.b+self.b*other.a)}i)"

    def info(self):
        print(f"({self.a}+{self.b}i)")


num_1 = ComplexNumber(1,2)
num_1.info()
num_2 = ComplexNumber(3,4)
num_2.info()

z = num_1+num_2
print(z)
z = num_1*num_2
print(z)

# python library
x = complex(1, 2)
print(x)
y = complex(3, 4)
print(y)
z = x + y
print(z)
z = x * y
print(z)

exit()


