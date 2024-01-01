#bai 1
n = float(input("Nhập 1 số n: "))
if n > 0:
    result = n**2
    print("Giá trị bình phương của ", n, " là ", result)


#bai 2
n = int(input("Nhập số tự nhiên n: "))
if n > 0:
    print("Các số nguyên trong phạm vi từ 1 đến N")
    for i in range(1, n+1):
        print(i)
else:
    print("n phải là số tự nhiên")


#bai 3
print("Nhập vào 2 số tự nhiên m, n (m < n)")
n = int(input("Nhập số tự nhiên n: "))
m = int(input("Nhập số tự nhiên m: "))
if m > 0 and n > 0:
    if m < n:
        print("Các số chia hết cho m trong khoảng từ 1 đến n:")
        for i in range(1, n+1):
            if i%m == 0:
                print(i)
    else:    
        print("Yêu cầu m < n")
else:
    print("m, n phải là 2 số tự nhiên")


#bai 4 
print("Nhập vào 3 số a, b, c")
a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))
max = a
if max <= b:
    max = b
if max <= c:
    max = c
print("Giá trị lớn nhất: ", max)


#bai 5
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
if a > 0 and b > 0:
    max = a
    if max <= b:
        max = b
    while True:
        if max % a == 0 and max % b == 0:
            break
        else:
            max += 1
    print("BCNN của hai số ", a, " và ", b," là: ", max)
else:
    print("Yêu cầu nhập 2 số nguyên dương")


#bai 6
print("Nhập các hệ số của hệ phương trình bậc nhất 2 ẩn")
a1 = float(input("Nhập vào hệ số a1: "))
b1 = float(input("Nhập vào hệ số b1: "))
c1 = float(input("Nhập vào hệ số c1: "))
a2 = float(input("Nhập vào hệ số a2: "))
b2 = float(input("Nhập vào hệ số b2: "))
c2 = float(input("Nhập vào hệ số c2: "))

d = a1*b2 - a2*b1
dx = c1*b2 - c2*b1
dy = a1*c2 - a2*c1

if d != 0:
    x = dx/d
    y = dy/d
    print("Nghiệm của hệ phương trình là: (x, y) = (", x, ", ", y,")")
else:
    if dx != 0 or dy != 0:
        print("Hệ phương trình vô nghiệm")
    else:
        print("Hệ phương trình vô số nghiệm")

print("Nhập tháng và năm cần tính")
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))
if m > 0 and y > 0 and m < 13:
    if m == 1:
        d = 31
    elif m == 2:
        if y % 4 == 0 and y % 100 != 0:
            d = 29
        else:
            d = 28
    elif m == 3:
        d = 31
    elif m == 4:
        d = 30
    elif m == 5:
        d = 31
    elif m == 6:
        d = 30
    elif m == 7:
        d = 31
    elif m == 8:
        d = 31
    elif m == 9:
        d = 30
    elif m == 10:
        d = 31
    elif m == 11:
        d = 30
    else:
        d = 31
    print("Số ngày trong tháng là: ", d)
else:
    print("Không chính xác tháng hoặc năm")

a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
if a > 0 and b > 0:
    min = a
    if min >= b:
        min = b
    while True:
        if a % min == 0 and b % min == 0:
            break
        else:
            min -= 1
    print("UCNN của hai số ", a, " và ", b," là: ", min)
else:
    print("Yêu cầu nhập 2 số nguyên dương")


#bai 7
n = int(input("Nhập số nguyên n bất kì: "))
if n < 0:
    n = -n
tong = 0
thuong = n
while True:
    so_du = thuong % 10
    thuong = thuong // 10
    tong = tong + so_du
    if thuong == 0:
        break
print("Tổng các chữ số là: ", tong)

