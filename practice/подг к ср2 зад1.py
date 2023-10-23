a = input()
count = 0
while 'дров' in a or 'полен' in a:
    count += 1
    a = input()
print(count)
