x = 1
print(x)
print(type(x))

x = 10000000000000000000000000000000000000000000000000000000000000001
print(x)
print(type(x))

home = 10
away = 15
print(home+ away)
print(type(home + away))

print(10 * 4)
print(type(10*4))

goals_for = 10
goals_against = 7
print(goals_for - goals_against)
print(type(goals_for - goals_against))

print(100 / 20)
print(type(100 / 20))

res1 = 3/2
print(res1)
print(type(res1))

print('-' * 10)
res1 = 3//2
print(res1)
print(type(res1))

a = 5
b = 3
print(a ** b)

print('True division 3/2:', 3/ 2)
print('True division 3//2:', -3 /2)
print('Integer division 3//2:', 3 //2)
print('Integer division 3//2:', -3 // 2)

print('*' * 10)

age = int(input('Please enter your age:'))
print(type(age))
print(age)

print('*' * 10)

exchange_rate = float(input("Please enter the exchange rate to use: "))
print(exchange_rate)
print(type(exchange_rate))

print(2.3 + 1.5)
print(1.5 / 2.3)
print(1.5 * 2.3)
print(2.3 - 1.5)
print(1.5 - 2.3)

i = 3 * 0.1
print(i)

print('+' * 10)

f = 3.2e4 + 0.00002e-6
formatString = "%16.20g"
print(formatString % f)
print(type(f))

c1 = 1j
c2 = 2j
c3 = c1 * c2
print(c3)
print(type(c3))
print(c3.real)
print(c3.imag)

print('=' * 10)
all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))

print(int(True))
print(int(False))
print(bool(1))
print(bool(0))

status = bool(input('OK to proceed: '))
print(status)
print(type(status))

x = 0
x += 1
print('x =', x)
