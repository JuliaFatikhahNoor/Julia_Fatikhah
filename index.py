# Tampilan Menu
print ("============================")
print ("MENGONVERSI MATA UANG RUPIAH")
print ("============================")

# Membuat Akun
print ("Registrasi Akun")
ussarname = input ("Masukkan Nama : ")
Nim = input ("Masukkan Nim  : ")

print ("============================")
print ("   AKUN ANDA TELAH DIBUAT   ")
print ("============================")

print ("")

# Menampilkan Pilihan 

print (" Pilih Operasi ")
print ("1. Konversi Rupiah ke Yen")
print ("2. Konversi Rupiah ke Ringgit")
print ("3. Konversi Rupiah ke USD")
print ("4. Selesai")

print ("")

# Meminta input dari pengguna
print ("============================")
pilihan = input ("Masukkan Pilihan (1/2/3/4): ")
print ("============================")

# Memasukkan nominal Rupiah
print ("")
Rupiah = float(input("Masukkan Rp: "))

# Memasukkan kurs Mata Uang
Yen = 103
Ringgit = 3287
USD = 15402

# Proses operasi berdasarkan pilihan  
print ("")
if pilihan == "1":
    konversi = (Rupiah)/Yen 
    print ("Hasil Konversi adalah ¥",konversi,)
    print ("")

elif pilihan == "2":
    konversi = (Rupiah)/Ringgit
    print ("Hasil konversi adalah RM", konversi,)
    print ("")
    
elif pilihan == "3":
    konversi = (Rupiah)/USD
    print ("Hasil konversi adalah $", konversi,)
    print ("")

else: 
    print ("Pilihan Tidak Valid")
    print ("")

# Penutup
print ("============================")
print ("      Program Selesai       ")
print ("============================")
