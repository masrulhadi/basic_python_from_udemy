userName = input("Enter your name: ")
print("Hello", userName)

a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")

# penjumlahan
print("addition of", a, "and", b, "is", int(a) + int(b))

# penggabungan string
print("addition of", a, "and", b, "is", str(a+b))

# penjumlahan dengan tipe data string
print("addition of", a, "and", b, "is", str(int(a) + int(b)))

# --------------------------------------------------------------------
print("-------------------------------------------------------------")
# --------------------------------------------------------------------

# penjumlahan dengan tipe data integer
satu = int(input("Enter 1st number: "))
dua = int(input("Enter 2nd number: "))
print("penjumlahan integer:", satu + dua)

# penggabungan string
satu1 = str(input("Enter 1st number: "))
dua1 = str(input("Enter 2nd number: "))
print("addition of", satu1, "and", dua1, "is", satu1 + dua1)

result = satu + dua
print("hasil dari result adalah", result)

result = satu1 + dua1
print("hasil dari result adalah", result)

# --------------------------------------------------------------------
print("-------------------------------------------------------------")
# --------------------------------------------------------------------

nama = input("Enter your name : ")
usia = input("Enter your age  : ")

print("Hello", nama, "you are", usia, "years old")
print("Hello", nama, "you are", int(usia), "years old")
print("Hello" + " " + nama + " " + "you are" + " " + str(usia) + " " + "years old")
print(f"Hello {nama} you are {usia} years old")