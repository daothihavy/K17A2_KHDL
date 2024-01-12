# bài 1
def sign(x):
    if x<0:
        a=-1
    elif x>0:
        a=1
    else:
        a=0
    return a
x=float(input("nhap so:"))
print(sign(x))


# bài 3
def BMI(can_nang, chieu_cao):
    BMI=can_nang/(chieu_cao*chieu_cao)
    print('chỉ số BMI:%.2f'%BMI)
    if BMI<18.5:
        print('đánh giá theo chỉ số: gầy')
    elif BMI>=18.5 and BMI<24.99:
        print('đánh giá theo chỉ số: bình thường')
    else:
        print('đánh giá theo chỉ số: thừa cân')
    return
a=float(input("nhập cân nặng(kg):"))
b=float(input("nhập chiều cao(m):"))
BMI(a,b) 
        

# bài 4
def tinh_S(n,x):
    S=(x**2+1)**n
    print('S=',S)
    return
n=float(input("nhập số n: "))
x=float(input("nhập số x: "))
tinh_S(n,x)

# bài 5
def tinh_A(n,x):
    A=(x**2+x+1)**n+(x**2-x+1)**n
    print('A=',A)
    return
n=float(input("nhập số n: "))
x=float(input("nhập số x: "))
tinh_A(n,x)


# bài 6
def kiem_tra_so_nguyen_to(x):
    if x<=1:
        print(x,"không phải là số nguyên tố")
    else:
        for i in range(1, x):
            if x % i ==0:
                print(x,"không phải là số nguyên tố")
            else:
                print(x,"là số nguyên tố")
    return

x = int(input("nhap so x:"))


# bài 7
def ham_tra_ve_phan_nguyen(a,b):
    if a%b==0: 
        print("a chia hết cho b")
    else:
        print("a không chia hết cho b")
    return
a=float(input("nhập số a: "))
b=float(input("nhập số b: "))
ham_tra_ve_phan_nguyen(a,b)

# bài 8
n = int(input("Nhập vào số N lớn hơn 0:"))
S = 0
for i in range(1, n):
    if (n % i == 0):
        S += i
if (S == n):
    print(n, " là số hoàn hảo")
else:
    print(n, " không phải là số hoàn hảo")



# bài 9
r=float(input('nhập bán kính:'))
a=float(input('nhập chiều dài:'))
b=float(input('nhập chiều rộng:'))
s=lambda r:3.14*(r**2)
p=lambda r:3.14*2*r
S=lambda a,b:a*b
P=lambda a,b:(a+b)*2
print('diện tích hình tròn:',s(r))
print('chu vi hình tròn:',p(r))
print('diện tích hình chữ nhật:',S(a,b))
print('chu vi hình chữ nhật:',P(a,b))
