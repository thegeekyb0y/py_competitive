n = int(input())

if n % 2 == 0:
    if n in range(2, 5):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    elif n > 20:
        print("Not Weird")
else:
    print("Weird")
