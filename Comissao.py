N = input()
V = float(input())
if (V <= 250):
    print(N,"%.2f" %V)
elif (V>250):
    R = V * 1.50
    print(N , "%.2f" %R)
elif (V>500):
    R2 = V * 2
    print(N, "%.2f" %R2)