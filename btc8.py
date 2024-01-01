# bài 1
a, b, c, d = map(int, input("Nhap 4 so a, b, c, d: ").split())
max = a
if max < b:
    max = b
if max < c:
    max = c
if max < d:
    max = d
print(f"Gia tri lon nhat la: {max}")

min = a
if min > b:
    min = b
if min > c:
    min = c
if min > d:
    min = d
print(f"Gia tri nho nhat la: {min}")

# bài 2
x = float(input("Nhap gia tri x:"))
if x > 0:
    print(f"|x| = {x}")
else:
    print(f"|x| = {-x}")

# bài 3
a = float(input("Nhap he so a:"))
b = float(input("Nhap he so b:"))
if a != 0:
    print(f"Nghiem cua phuong tring la x = {(-b)/a}")
else:
    if b == 0:
        print("Phuong trinh co vo so nghiem")
    else:
        print("Phuong trinh co vo nghiem")

# bài 4
import math
a, b, c = map(float, input("Nhap 3 canh cua tam giac: ").split())
if a <= 0 or b <= 0 or c <=0 or a + b <= c or b + c <= a or a + c <= b:
    print("3 canh vua nhap khong phai la 3 canh cua 1 tam giac")
else:
    p = (a + b + c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"Dien tich tam giac la: {s}")

# bài 5
year = int(input("Nhap nam can kiem tra: "))
if year < 1:
    print("Nam khong xac dinh")
else:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} la nam nhuan")
    else:
        print(f"{year} khong phai la nam nhuan")

# bài 6
loai_xe = int(input("Nhap loai xe 4 cho hoac 7 cho (4,7): "))
if loai_xe != 4 and loai_xe != 7:
    print("Yeu cau nhap 4 hoac 7")
else:
    quang_duong = float(input("Nhap quang duong (km): "))
    if quang_duong <=0:
        print("Quang duong khong xac dinh")
    else:
        thoi_gian_cho = int(input("Nhap thoi gian cho (phut): "))
        if thoi_gian_cho < 0:
            print("Thoi gian cho khong xac dinh")
        else:
            tong_tien = 0.0
            tien_cho = 0.0
            if thoi_gian_cho > 5:
                tien_cho = (thoi_gian_cho - 5) * 800
            if loai_xe == 4:
                if quang_duong >= 21:
                    tong_tien = 11000 + (20 - 0.8)*12100 + (quang_duong - 20) * 10000 + tien_cho
                elif quang_duong > 0.8:
                    tong_tien = 11000 + (quang_duong - 0.8)*12100 + tien_cho
                else:
                    tong_tien = 11000 + tien_cho
            if loai_xe == 7:
                if quang_duong >= 21:
                    tong_tien = 13000 + (20 - 0.8)*14100 + (quang_duong - 20) * 12000 + tien_cho
                elif quang_duong > 0.8:
                    tong_tien = 13000 + (quang_duong - 0.8)*14100 + tien_cho
                else:
                    tong_tien = 13000 + tien_cho
            print(f"Loai xe: {loai_xe} cho")
            print(f"Quang duong: {quang_duong} km")
            print(f"Thoi gian cho: {thoi_gian_cho} phut")
            print(f"Tong tien: {tong_tien} VND")

# bài 7
kwh_dien = float(input("Nhap so kWh dien (kWh): "))
if kwh_dien < 0: 
    print("So kWh khong xac dinh")
else:
    tong_tien = 0.0
    if kwh_dien >= 401:
        tong_tien = 50*1.675 + 50*1734 + 100*2014 + 100*2536 + 100*2834 + (kwh_dien - 400)*2927
    elif kwh_dien >= 301: 
        tong_tien = 50*1.675 + 50*1734 + 100*2014 + 100*2536 + (kwh_dien - 300)*2834
    elif kwh_dien >= 201: 
        tong_tien = 50*1.675 + 50*1734 + 100*2014 + (kwh_dien - 200)*2536
    elif kwh_dien >= 101: 
        tong_tien = 50*1.675 + 50*1734 + (kwh_dien - 100)*2014
    elif kwh_dien >= 51:
        tong_tien = 50*1.675 + (kwh_dien - 50)*1734
    else: 
        tong_tien = kwh_dien*1.675
    print(f"Tong tiẻn dien la: {tong_tien}")

# bài 8
m_1 = "Standard - 1,260,000" 
m_2 = "Superior Garden View - 1,550,000" 
m_3 = "Superior Ocean View - 1,830,000" 
m_4 = "Garden View Bungalow - 1,830,000" 
m_5 = "Pool View Bungalow - 2,120,000" 
m_6 = "Family Room - 2,120,000" 
m_7 = "Beach Front Bungalow - 2,540,000" 
m_8 = "VIP sea View - 4,800,000" 
m = int(input("Nhap ma phong (1 - 8):"))
if m > 8 and m < 1:
    print("Ma phong khong hop le")
else:
    so_dem = int(input("Nhap so dem o lai: "))
    if so_dem < 1:
        print("So dem khong hop le")
    else:
        tong_tien = 0.0
        giam_gia = 0.0
        if so_dem > 1 and so_dem < 4:
            giam_gia = 0.25
        elif so_dem >= 4:
            giam_gia = 0.3
        else:
            giam_gia = 0.0
        if m == 1:  
            tong_tien = 1260000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_1} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")
        if m == 2:
            tong_tien = 1550000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_2} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")
        if m == 3:
            tong_tien = 1830000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_3} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")
        if m == 4:
            tong_tien = 1830000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_4} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")
        if m == 5:
            tong_tien = 2120000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_5} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")
        if m == 6:
            tong_tien = 2120000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_6} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")
        if m == 7:
            tong_tien = 2540000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_7} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")
        if m == 8:
            tong_tien = 4800000*so_dem*(1-giam_gia)
            print(f"Ma {m} - {m_8} - {so_dem} dem - giam {giam_gia*100}%: {tong_tien}")

# bài 9
n = 10
while n > -1:
    print(n)
    n = n - 1
else:
    print("Start!!")

# bài 10
n = int(input("Nhap so nguyen n: "))
x = float(input("Nhap so thuc x: "))
s = (x**2 + 1)**n
print(f"S = ({x}^2 + 1)^{n} = {s}")

# # # bài 11
n = int(input("Nhap so nguyen n: "))
x = float(input("Nhap so thuc x: "))
a = (x**2 + x + 1)**n + (x**2 - x + 1)**n
print(f"A = ({x}^2 + {x} + 1)^{n} + ({x}^2- {x} + 1)^{n} = {a}")


# # # bài 12
x = int(input("Nhap vao so nguyen duong x: "))
if x < 2:
    print(f"{x} khong phai so nguyen to")
else:
    for i in range(2,x):
        if x%i == 0:
            print(f"{x} khong phai so nguyen to")
            break
    else:
        print(f"{x} la so nguyen to")


# # # bài 13
#A = tổng các số lẻ nhỏ hơn hay bằng n
n = int(input("Nhap vao so nguyen duong n: "))
tong = 0
for i in range(0, n+1):
    if i%2!=0:
        tong = tong + i
print(f"A = {tong}")

#B = tổng các số chẵn nhỏ hơn hay bằng n
n = int(input("Nhap vao so nguyen duong n: "))
tong = 0
for i in range(0, n+1):
    if i%2==0:
        tong = tong + i
print(f"B = {tong}")

#C = tích các số từ 1 đến n
n = int(input("Nhap vao so nguyen duong n: "))
tich = 1
for i in range(1, n+1):
    tich = tich*i
print(f"C = {tich}")

#D = tích các số chia hết cho 3 nhỏ hơn hay bằng n
n = int(input("Nhap vao so nguyen duong n: "))
tich = 1
for i in range(1, n+1):
    if i%3==0:
        tich = tich*i
print(f"D = {tich}")

#E = tổng các số nguyên tố nhỏ hơn hay bằng n
n = int(input("Nhap vao so nguyen duong n: "))
tong = 0
for i in range(2, n+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        tong = tong + i
print(f"E = {tong}")

#F = tổng chuỗi đan dấu
n = int(input("Nhap vao so nguyen duong n: "))
tong = 0.0
flag = True
for i in range(1, n+1):
    if flag == True:
        tong = tong + 1.0/i
        flag = False
    else:
        tong = tong - 1.0/i
        flag = True
print(f"F = {tong}")



# # # bài 14
n = int(input("Nhap so cac so nguyen can tinh: "))
if n < 0:
    print("n khong hop le")
else:
    tong = 0
    for i in range(1,n+1):
        k = int(input(f"Nhap so nguyen thu {i}: "))
        tong = tong + k
    print(f"Tong cac so vua nhap: {tong}")


# # # bài 15
tong = 0
while True:
    n = int(input("Nhap so nguyen: "))
    print(n)
    tong = tong + n
    if n == 0:
        break
print(f"Tong cac so vua nhap: {tong}")


# # # bài 16
a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))
if a < 0 or b < 0:
    print("a, b phai lon hon 0")
min = a
if min > b:
    min = b
for i in range(min, 0, -1):
    if a%i == 0 and b%i == 0:
        print(f"UCLN({a},{b}) = {i}")
        break


# # # bài 17
a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))
if a < 0 or b < 0:
    print("a, b phai lon hon 0")
max = a
if max < b:
    max = b
while True:
    if max % a == 0 and max % b == 0:
        print(f"BCNN({a},{b}) = {max}")
        break
    max = max + 1


# # # bài 18
x = int(input("Nhap vao so nguyen duong x: "))
if x < 0:
    print("x phai la so nguyen duong")
else:
    if x == 0:
        print("0 khong phai la so hoan hao")
    tong = 0
    for i in range(1, x):
        if x%i==0:
            tong = tong + i
    if tong == x:
        print(f"{x} la so hoan hao")
    else:
        print(f"{x} khong phai so hoan hao")


# # # bài 19
day_so = input("Nhap vao mot day so bat ky, moi so cach nhau boi dau cach: ")
#Nhap vao day so "1 3 4 5 6 7 9 10 11 27 13 14 99 16 17 18 21 20"
if day_so[0] != "1":
    print("Day so phai bat dau tu so 1")
else:
    day_so_nguoc = day_so[::-1]
    pos = 0
    count = 0
    day_so_moi = ""
    for i in day_so_nguoc:
        if i == " ":
            k = day_so_nguoc[pos - count : pos]
            k = k[::-1]
            if int(k) % 2 != 0:
                day_so_moi = day_so_moi + k + " "
            count = 0
        else:
            count = count + 1
        pos = pos + 1
    day_so_moi = day_so_moi + "1"
    print(day_so_moi)


# # # bài 20
n = int(input("Nhap so nguyen duong n: "))
x = int(input("Nhap so nguyen x: "))
if n < 0:
    print("n khong hop le")
else:
    tong = 0
    for i in range(1,n+1):
        giai_thua = 1
        for j in range(1,i+1):
            giai_thua = giai_thua*i
        tong = tong + (x**i)/giai_thua
    print(f"e^{x} = {tong}")