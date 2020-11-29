import math
def main():
    pass

def check(x):
    if x < 2:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0: 
            return False
    return True
if __name__ == "__main__":
    list = []
    while True :
        list.append(int(input()))
        print("Nhap tiep(y/n)")
        chon = input()
        if chon == "n":
            break
    listSNT = []
    for x in list:
        if check(x):
            print(x)
            listSNT.append(x)
    print(listSNT)