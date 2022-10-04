if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    arr2=[]
    for el in arr:
        if not el in arr2:
            arr2.append(el)
    first_max_number=max(arr2)
    arr2.remove(first_max_number)
    second_max_number=max(arr2)
    print(second_max_number)