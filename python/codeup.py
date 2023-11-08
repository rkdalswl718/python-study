def f(a,b):
    if (a%b%c == 0):
        return b;
    return f(b, a%b%c)

a,b,c = map(int, input().split())

print(f(f(a,bA),c))