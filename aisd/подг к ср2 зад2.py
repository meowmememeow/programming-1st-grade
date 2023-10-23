mood = input()
a = input()
b = input()
if mood == 'ХОРОШЕЕ':
    step = 5
else:
    step = 3
for i in range(a, b + 1, step):
    print(i, end=' ')
