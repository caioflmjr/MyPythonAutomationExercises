def collatz(n):
    if n % 2 == 0:
        return n // 2
    else: 
        return 3 * n + 1
    
print('escolha um numero: ')
int = int(input())

i = 0
while int != 1:
    print(int, end=' ')
    int = collatz(int)
print(int, end=' ')
