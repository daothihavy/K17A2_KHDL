# bai 4
a = (5 - 3) // 2
print(f"(5 - 3) // 2 = {a}")
b = 8 - 3 * 2 - (1 + 1)
print(f"8 - 3 * 2 - (1 + 1) = {b}")


#bai 5
so_luong = int(input("Nhap so luong: "))
don_gia = int(input("Nhap don gia: "))
thanh_tien = so_luong * don_gia
print(f"Thanh tien = {so_luong} * {don_gia} = {thanh_tien}")


#bai 6
alice_candies = 121
bob_candies = 77
carol_candies = 109
to_smash = (alice_candies + bob_candies + carol_candies)%3
print(to_smash)


#bai 7
do_c = float(input("Nhap do C: "))
do_f = (9/5)*do_c + 32
print(f"{do_c} do C = {do_f} do F")


#bai 8
s1 = input("Nhap chuoi s1: ")
s2 = input("Nhap chuoi s2: ")
s3 = input("Nhap chuoi s3: ")
index = int(input("Nhap index: "))
print(f"Chieu dai chuoi s1: {len(s1)}")
print(f"Chieu dai chuoi s2: {len(s2)}")
print(f"Chieu dai chuoi s3: {len(s3)}")
print(f"Chuoi s4: {s1[index : ]}")
print(f"Chuoi s2 lap lai 2 lan: {s2*2}")


#bai 9
lai_suat_mot_nam = float(input("Lai suat 1 nam (%):"))
so_tien_gui = float(input("So tien gui: "))
so_thang_gui = int(input("So thang gui: "))
tien_lai = (so_tien_gui * so_thang_gui) * (lai_suat_mot_nam/ 100 / 12)
tong_so_tien = so_tien_gui + tien_lai
print(f"Tien lai = ({so_tien_gui} * {so_thang_gui}) * ({lai_suat_mot_nam}/100/12) = {tien_lai} VND")
print(f"Tong so tien = {so_tien_gui} + {tien_lai} = {tong_so_tien} VND")
