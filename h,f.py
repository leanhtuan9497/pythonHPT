
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
    print("List chua sap xep")
    print(list)
    print("List sap xep tang dan")
    list.sort()
    print(list)
    print("List sap xep giam dan")
    list.sort(reverse = True)
    print(list)

    
