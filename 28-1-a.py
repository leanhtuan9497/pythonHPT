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
    z = ""
    listSC = []
    listSL = []
    for x in list:
        if x%2 == 0:
            z = str(x)
            print(z)
            listSC.append(x)
        else:
            listSL.append(x)
    print("List So Chan: ") 
    print(listSC)
    print("List So Le: ") 
    print(listSL)