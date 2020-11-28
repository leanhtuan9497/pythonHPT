import sys

def main():
    pass

if __name__ == "__main__":
    list = []
    while True :
        list.append(int(input()))
        print("Nhap tiep(y/n)")
        chon = input()
        if chon == "n":
            break
    print(list)
    print("Nhap so ")
    so = int(input())

    for i in range(len(list)):
        if list[i] == so:
            print(i)

 
