# bài 1
# cho 4 danh sách sau:
a=[1,2,3]
b=[1,[2,3]]
c=[]
d=[1,2,3][1:]
print(len(a),len(b),len(c),len(d))

# bài 2
team=[['Steven', 'Neena', 'Lex', 'Alexander', 'Bruce'],['David', 'Jack', 'Bill', 'Tom', 'Mike', 'Daniel'],['Alexander', 'Adam', 'Payam', 'Kevin', 'Sigal', 'Mike']]
list1=team[2]
list2=list1[1]
print('đội trưởng đội yếu nhất:',list2)

# bài 3
animals = ["ant", "bear", "cat", "dog", "elephant", "fish", "goat", "hippo"]
animal=input('tôi muốn tìm con:')
print('số lượng động vật:',len(animals))
for i in animals:
    if animal==i:
        print('có',animal,'trong danh sách động vật')
        break
else:
    print('không có')
    
# bài 4
a=[]
while True:
    b=int(input('nhập giá trị:'))
    a.append(b)
    c=int(input('tiếp tục nhập giá trị?\n  1:có   0:không\n   '))
    if c==1:
        continue
    if c==0:
        break
x=int(input('nhập gía trị cần tìm x:'))
print("list:",a)
print('tổng các giá trị trong list',sum(a))
print(x,'xuất hiện',a.count(x),'lần trong list')
d=[]
for i in a:
    if i>x:
       d.append(i)
print('các số lớn hơn',x,'trong list:',d)

# bài 5
a=[]
while True:
    b=int(input('nhập giá trị:'))
    a.append(b)
    c=int(input('tiếp tục nhập giá trị?\n  1:có   0:không\n   '))
    if c==1:
        continue
    if c==0:
        break
print('list:',a)
def kiem_tra_so_nguyen_to(x):
 if x<2:
    return False
 else:
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
         return False
    return True
d=[]
e=[]
f=[]
for i in a:
    if kiem_tra_so_nguyen_to(i):
        d.append(i)
    if i<0:
        e.append(i)
    if i>0:
        f.append(i)
if len(d)!=0:
    print('các số nguyên tố trong list:',d)
else:
    print('không có số nguyên tố trong list')
if len(e)!=0:
    print('các phần tử âm trong list:',e)
    print('trung bình cộng các số âm:',sum(e)/len(e))
else:
    print('không có phần tử âm trong list')
if len(f)!=0:
    print('các phần tử dương trong list:',f)
    print('trung bình cộng các số dương:',sum(f)/len(f))
else:
    print('không có phần tử dương trong list')
print('giá trị max trong list:',max(a))
print('giá trị min trong list:',min(a))
a.sort()
print('list sắp tăng dần:',a)

# bài 6
a=[74,74,72,72,73,69,69,71,76,71]
b=[]
for i in a:
    s=i/0.0254
    b.append(s)
print(b[0:4])
print(b[-3:])
print('chiều cao trung bình:',sum(b)/len(b))
print('chiều cao lớn nhất:',max(b))
print('chiều cao nhỏ nhất:',min(b))
b.sort()
print('giá trị tăng dần:',b)
b.reverse()
print('giá trị giảm dần:',b)

# bài 7
L=[2,5,6,3,2,4,6,3,2,1]
thresh=int(input('nhập số:'))
a=[]
def elementwice_greater_than(L,thresh):
    for i in L:
        if i <= thresh:
            b=False
            a.append(b)
        if i > thresh:    
            b=True
            a.append(b)
    return a
print(elementwice_greater_than(L,thresh))

# bài 8
nums=[1,2,3,4,7,5,6,8,9]
def has_lucky_numbers(nums):
    for i in nums:
        if i%7==0:
            print(True)
            break 
    else:
        print(False)
    return
has_lucky_numbers(nums)

# bài 9
arrival=['adele','fleda','owen','may','mona','gillbert','ford']
def party_late(arrival,name):
    if (arrival.index(name)+1)==(len(arrival)):
        return False 
    if (arrival.index(name)+1)>(len(arrival)/2):
        return True
    else:
        return False

print(party_late(arrival,name='gillbert'))
print(party_late(arrival,name='ford'))
print(party_late(arrival,name='mona'))


# bài 10
meals_1=['Redneck Ribs', 'Prawn Star', 'San Quentin Squid', 'Fist Full of Pizza', 'Honky Tonk Chicken']
meals_2 =['Redneck Ribs', 'Prawn Star', 'Running Bear Salmon', 'Running Bear Salmon', 'Honky Tonk Chicken']
def menu_is_boring(meals):
    for i in meals:
        if meals.index(i)+1==len(meals):
            return False
        if i==meals[meals.index(i)+1]:
            return True 
  
print(menu_is_boring(meals_1))
print(menu_is_boring(meals_2))

# bài 11
tuple="red", "green", 'yellow', 'blue', 'black', "white", "pink", "orange", "red", "blue"
a=int(input('nhập số từ 0 đến 9:'))
b=int(input('nhập số từ -1 đến -9:'))
s_find=input('nhập chuỗi cần tìm:')
print(tuple)
print('tuple[',a,']=',tuple[a])
print('tuple[',b,']=',tuple[b])
print(s_find,'xuất hiện trong tuple',tuple.count(s_find))

# bài 12
tuple_a=3,1,2,4
tuple_b=5,7,6,8
tuple_c=tuple_a+tuple_b
print('tuple_c:',tuple_c)
a=list(tuple_c)
a.sort()
tuple_d=tuple(a) 
print('tuple_d:',tuple_d)
print('tuple[3]=',tuple_d[3])
print('3 phần tử cuối cùng của tuple d',tuple_d[-3:])

