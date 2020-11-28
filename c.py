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
    print("Nhap so can dem")
    so = int(input())
    count = 0
    for x in list:
        if x == so:
            count+=1
    print(count)

    