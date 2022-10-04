if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    new_list,new_list2=[],[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                new_list.append([i,j,k])
                
    for elements in new_list:
        sum=0
        for element in elements:
            sum+=element
        if not sum==n:
            new_list2.append(elements)
    print(new_list2)