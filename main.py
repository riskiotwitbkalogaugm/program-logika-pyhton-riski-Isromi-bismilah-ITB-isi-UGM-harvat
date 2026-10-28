print("PROGRAM PENENTU KELULUSAN SISWA")
print("===============================")

nama = input("Masukkan nama siswa: ")
nilai = float(input("Masukkan nilai siswa: "))

print("===============================")
print("Nama Siswa :", nama)
print("Nilai      :", nilai)

if nilai >= 80 and nilai <= 100:
    print("Keterangan : LULUS")
elif nilai >= 0 and nilai < 80:
    print("Keterangan : TIDAK LULUS")
else:
    print("Keterangan : NILAI TIDAK VALID")

print("===============================")