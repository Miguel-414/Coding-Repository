num1 = 0
num2 = 1
fibonacci = list()
for i in range(20):
    num3 = num1 + num2
    print(num3)
    fibonacci.append(num3)
    num1 = num2
    num2 = num3

print(f" lista de fibonacci {fibonacci}")    