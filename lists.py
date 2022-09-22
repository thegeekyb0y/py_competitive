# Problem : https://www.hackerrank.com/challenges/python-lists/problem

N = int(input())
l = []

for i in range(N):
    command, *number = input().split() 
    
    if command == 'insert':
        l.insert(int(number[0]),int(number[1]))
                        
    elif command == 'print':                       
        print(l)
                        
    elif command == 'remove':
        l.remove(int(number[0]))
                        
    elif command == 'append':
        l.append(int(number[0]))
                        
    elif command == 'sort':
        l.sort()
                        
    elif command == 'pop':
        l.pop()
        
    elif command == 'reverse':
        l.reverse()
