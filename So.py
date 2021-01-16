import math

def check_so_nguyen_to(n):
    if n < 2:
        return False
    for x in range(2, int(math.sqrt(n)+1)):
        if n%x == 0:
            return False
    return True


if __name__ == '__main__':
    for x in range(1,50):
        if(check_so_nguyen_to(x)):
            print(x)


