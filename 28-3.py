
class SinhVien:
    def __init__(sv,hoten,tuoi,lop):
        sv.hoten = hoten
        sv.tuoi = tuoi
        sv.lop = lop

listSV = []
while True :
    print("Nhap ten")
    temp = str(input())    
    hoten = ""
    for x in temp.split(' '):
        nameLower = name
        name = nameLower[0].upper()
        name += nameLower[1:]
        hoten = hoten + name + " "
    print("Nhap tuoi")
    tuoi = int(input())
    print("Nhap lop")
    lop = str(input())
    sv = SinhVien(hoten,tuoi,lop)
    listSV.append(sv)
    print("Nhap tiep(y/n)")
    chon = input()
    if chon == "n":
        break

print("===============Sap xep theo  tuoi===============")
listSV.sort(key =lambda x: x.tuoi)
for i in range(len(listSV)):
    print("Thong tin sv thu " + str(i+1) + ":")
    print("Ho Ten SV : " + listSV[i].hoten)
    print("Ngay sinh SV : " + str(listSV[i].tuoi))
    print("Lop Sv: " + listSV[i].lop)

print("===============Sap xep theo  ho ten===============")
listSV.sort(key = lambda x:x.hoten)
for i in range(len(listSV)):
    print("Thong tin sv thu " + str(i+1) + ":")
    print("Ho Ten SV : " + listSV[i].hoten)
    print("Ngay sinh SV : " + str(listSV[i].tuoi))
    print("Lop Sv: " + listSV[i].lop)

print("===============Sap xep theo ten===============")
listSV.sort(key = lambda x:x.hoten.split(' ')[-1])
for i in range(len(listSV)):
    print("Thong tin sv thu " + str(i+1) + ":")
    print("Ho Ten SV : " + listSV[i].hoten)
    print("Ngay sinh SV : " + str(listSV[i].tuoi))
    print("Lop Sv: " + listSV[i].lop)