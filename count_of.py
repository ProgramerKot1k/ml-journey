s = input('Enter your text')
c = 'qeyuioaj'
a = [i for i in s.lower() if i in c]
print(*a)

