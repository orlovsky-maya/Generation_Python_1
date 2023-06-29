s = [int(i) for i in input().split()]
summa = sum(s)
st = [str(j) for j in s]
print('+'.join(st), '=', summa, sep='')