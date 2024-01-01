# bai 1
x = int(input("Nhap vao so nguyen x: "))
S = 1 + x + (x**3)/3 + (x**5)/5
print(S)


#bai 2
result = 1 + 2
print("result = ", result)
original_result = result
result = result - 1
print("result = ", result)
result = result * 2
original_result = result
print("result = ", result)
result = result ** 3
original_result = result
print("result = ", result)
result = result + 8
origianal_result = result
print("result = ", result)
result = result % 7
original_result = result
print("result = ", result)
result = result // 2
origianal_result = result
print("result = ", result)


#bai 3
result = 5
print("result = ", result)
result -= 1
print("result = ", result)
result += 3
print("result = ", result)
result = - result 
print ("result = ", result)
result = True
print("result = ", not result)


# bai 4
x = 10
y = 4
print("x= %d, y =%d"%(x,y))
equivelence = x == y
print("x == y is", equivelence)
equivelence =x != y
print("x != y is", equivelence)
equivelence =  x > y
print("x > y is", equivelence)
x = 8
y = 9
print("x = %d, y = %d"%(x,y))
equivelence = x >= y
print("x >= y is", equivelence)
equivelence = x < y
print(" x < y is", equivelence)
equivelence = x <= y
print("x <= y is", equivelence)


#bai 5
x = 15
y = 12
print('Binary of x =', bin(x), ', Binary of y =', bin(y))
print('x & y =', bin(x & y))
print('x | y =', bin(x | y))
print('x ^ y =', bin(x ^ y))
print("~x =", bin(~x))
print("x << 2 =", bin(x << 2))
print("y >> 2 =", bin(y >> 2))


#bai 6
x = True
y = False
print("x and y :", x and y)
print("x or y :", x or y)
print("not x :", not x)
print("x is y :", x is y)
print("x is not y :", x is not y)


#bai 7
tien_muon_doi = int(input("Nhap so tien muon doi: "))
print(f"So tien muon doi: {tien_muon_doi}")
so_to_1 = tien_muon_doi//500000
tien_con_lai = tien_muon_doi%500000
print(f"So to 500000: {so_to_1}")
so_to_2 = tien_muon_doi//200000
tien_con_lai = tien_muon_doi%200000
print(f"So to 200000: {so_to_2}")
so_to_3 = tien_muon_doi//100000
tien_con_lai = tien_muon_doi%100000
print(f"So to 100000: {so_to_3}")
so_to_4 = tien_muon_doi//50000
tien_con_lai = tien_muon_doi%50000
print(f"So to 50000: {so_to_4}")
print(f"So tien con lai: {tien_con_lai}")
