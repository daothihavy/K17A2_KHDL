# bài 1
print("bài toán về số nhỏ nhất và số lớn nhất")
import math
a=eval(input("nhập số a: "))
b=eval(input("nhập số b: "))
c=eval(input("nhập số c: "))
d=eval(input("nhập số c: "))
g=max(a,b,c,d)
h=min(a,b,c,d)
print("max=",g)
print("min=",h)

# bài 2
import math
x=int(input("nhập số x: "))
g=abs(x)
print("|x|=",g)

# bài 3
x=int(input("nhập số x: "))
n=int(input("nhập số n: "))
import math
S=(math.pow(x,2)+1)*n
print("S=",S)

# bài 4
x=int(input("nhập số x: "))
n=int(input("nhập số n: "))
import math
S=math.pow(pow(x,2)+x+1,n)+math.pow(pow(x,2)-x+1,n)
print("S=",S)


# bài 5
diem_quan_trong_can_kiem_tra = input("Nhập điểm quan trọng cần kiểm tra: ")
ma_buu_chinh_can_kiem_tra = input("Nhập mã bưu chính cần kiểm tra: ")

diem_quan_trong_va_ma_buu_chinh = [
    ("Thành phố Hồ Chí Minh", "700000"),
    ("Quận 1, TP.Hồ Chí Minh", "700001"),
    ("Quận 3, TP.Hồ Chí Minh", "700002"),
    ("Hà Nội", "100000"),
    ("Quận Hoàn Kiếm, Hà Nội", "100001"),
    ("Quận Ba Đình, Hà Nội", "100002"),
    ("Đà Nẵng", "550000"),
    ("Quận Hải Châu, Đà Nẵng", "551000"),
    ("Quận Thanh Khê, Đà Nẵng", "552000"),
    ("Hải Phòng", "180000"),
    ("Quận Hồng Bàng, Hải Phòng", "181000"),
    ("Quận Ngô Quyền, Hải Phòng", "182000"),
    ("Cần Thơ", "900000"),
    ("Ninh Kiều, Cần Thơ", "901000"),
    ("Cái Răng, Cần Thơ", "902000"),
    # V.v
]
def la_ma_buu_chinh_hop_li(diem_quan_trong, ma_buu_chinh):
    for diem_quan_trong, ma_buu_chinh in diem_quan_trong_va_ma_buu_chinh:
        if diem_quan_trong and ma_buu_chinh:
            return True
    return False
# Sử dụng hàm để kiểm tra mã bưu chính cho điểm quan trọng cụ thể
ket_qua = la_ma_buu_chinh_hop_li(diem_quan_trong_can_kiem_tra, ma_buu_chinh_can_kiem_tra)

print(ket_qua)


# bài 7
import string
a=str(input('nhập chuỗi:'))
s_sub=str(input('nhập chuỗi con s_sub:'))
s_find=str(input('nhập chuỗi tìm s_find:'))
s_replace=str(input('nhập chuỗi thay thế s_replace:'))
print('chuỗi sau khi loại bỏ khoảng trắng ở đầu và cuối:',a.strip())
print('số lần s_sub xuất hiện trong chuỗi',a.count(s_sub))
print('chuỗi s sau khi tìm kiếm và thay thế:',a.replace(s_find,s_replace))


# bài 8
import datetime
nam=int(input('nhập năm: '))
thang=int(input("nhập tháng: "))
ngay=int(input("nhập ngày: "))
print("ngày tháng năm vừa nhập:",ngay,thang,nam)
import calendar
# giả sử true là năm nhuận, false không là năm nhuận
print(calendar.isleap(nam))
# giả sử giá trị số 0:thứ 2; 1:thứ 3; 2:thứ 4;......
print(calendar.weekday(nam,thang,ngay))
# giả sử phần tử thứ nhất là ngày đầu tiên trong tháng, phần tử thứ hai là số ngày trong tháng
print(calendar.monthrange(nam,thang))

