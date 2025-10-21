# Adding two floating numbers
a = 4.5
b = 2.3
sum = a + b
print("Sum:", sum)
print("Type of sum:", type(sum))

# Subtract two integers
x = 8
y = 3
difference = x - y
print("Difference:", difference)
print("Type of difference:", type(difference))

# Multiply a float and an integer
m = 1.5
n = 4
product = m * n
print("Product:", product)
print("Type of product:", type(product))
def f(x):
    return x**3 + 8

def main():
    answer = f(9)
    print("Answer:", answer)

    if answer > 27:
        print("YAY!")