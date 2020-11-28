
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
    print("Nhap so can xoa")
    so = int(input())

    while so in list:
        list.remove(so)
    print(list)

    