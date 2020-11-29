import datetime

class SinhVien:
    def __init__(sv,hoten,ngaysinh,lop):
        sv.hoten = hoten
        sv.ngaysinh = ngaysinh
        sv.lop = lop

listSV = []
while True :
    print("Nhap ten")
    hoten  = str(input())
    print("Nhap ngay sinh")
    ngaysinh = str(input())
    print("Nhap lop")
    lop = str(input())
    sv = SinhVien(hoten,ngaysinh,lop)
    listSV.append(sv)
    print("Nhap tiep(y/n)")
    chon = input()
    if chon == "n":
        break
    
print("===============In ho ten va ngay sinh===============")
for i in range(len(listSV)):
    print("Thong tin sv thu " + str(i+1) + ":")
    print("Ho Ten SV : " + listSV[i].hoten)
    print("Ngay sinh SV : " + listSV[i].ngaysinh)

print("===============In ho ten va lop===============")
for i in range(len(listSV)):
    print("Thong tin sv thu " + str(i+1) + ":")
    print("Ho Ten SV : " + listSV[i].hoten)
    print("lop SV : " + listSV[i].lop)

print("===============In ho ten va tuoi===============")
for i in range(len(listSV)):
    print("Thong tin sv thu " + str(i+1) + ":")
    print("Ho Ten SV : " + listSV[i].hoten)
    namsinh = int(listSV[i].ngaysinh.split("/")[-1])
    namhientai = datetime.datetime.now().year
    tuoi = namhientai - namsinh
    print("Tuoi SV: " +str(tuoi))