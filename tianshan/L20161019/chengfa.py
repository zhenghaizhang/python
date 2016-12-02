for i in range(1,10):
    for j in range(1,i+1):
        print('%d * %d = %d' % (i,j,i*j), end=" ")
    print()

for i in range(1,10):
    print('  ' * 2*(10-i), end="")
    for j in range(1,i+1):
        print('%d * %d = %d' % (i,j,i*j), end="")
    print()

for i in range(9,0,-1):
    for j in range(i,0,-1):
        print('%d * %d = %d' % (i,j,i*j), end=" ")
    print()
