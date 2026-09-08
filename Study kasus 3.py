batas_nilai = (65, 100)
nilai_masuk = []
lulus = []
remedi = []

while True:
    angka = input("Masukkan nilai (atau (selesai)): ")

    if angka == "selesai":
        break

    nilai = int(angka)

    nilai_masuk.append(nilai)

    if nilai >= batas_nilai[0]:
        lulus.append(nilai)
    else:
        remedi.append(nilai)

hapus = input("Masukkan nilai yang ingin dihapus:")

if hapus != "":
    angka_hapus = int(hapus)
    if angka_hapus in nilai_masuk:
        nilai_masuk.remove(angka_hapus)
    if angka_hapus in lulus:
        lulus.remove(angka_hapus)
    if angka_hapus in remedi:
        remedi.remove(angka_hapus)

print("List nilai masuk:", nilai_masuk)
print("List lulus:", lulus)
print("List remedi:", remedi)
