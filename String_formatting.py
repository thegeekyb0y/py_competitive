def print_formatted(number):
    for i in range(1,number+1):
        length_binary=len(bin(number)[2:])
        
        print(f"{str(i).rjust(length_binary,' ')} {str(oct(i)[2:]).rjust(length_binary,' ')} {str(hex(i)[2:]).upper().rjust(length_binary,' ')} {str(bin(i)[2:]).rjust(length_binary,' ')} ")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)