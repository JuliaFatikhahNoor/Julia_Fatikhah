#Tampilanawal
print("""
---------------------------------------------------
        SELAMAT DATANG DI TOKO SEMBAKO SRC               
---------------------------------------------------
""")
#Pilihan Login di toko sembako
print("""
---------------------------------------------------
              LOGIN TOKO SEMBAKO SRC                           
---------------------------------------------------           
""")
print ("1. Login Sebagai Admin Toko")
print ("2. Login Sebagai Pembeli ")
print ("3. Keluar")
pilihan = input ("Pilih menu (1/2/3) :")
print ("---------------------------------------------------  ")

#list barang sembako
from prettytable import PrettyTable

table =  PrettyTable()
table.field_names = ["No", "Nama Barang", "Harga/pcs", "Stok Barang"]

table.add_row(["001", "Minyak Bimoli", "24000", "24"])
table.add_row(["002", "Gula", "17000", "12"])
table.add_row(["003", "Tepung Kompas", "15000", "12"])
table.add_row(["004", " Teh Sariwwangi", "7000", "12"])
table.add_row(["005", "Indomie", "3500", "40"])
table.add_row(["006", "Sunlight", "10000", "24"])
table.add_row(["007", "Kopi Kapal Api", "7000", "12"])
table.add_row(["008", "Sabun Daia", "20000", "10"])
table.add_row(["009", "Akua", "4000", "24"])
table.add_row(["010", "1 sak Beras 5 kg", "78000", "10"])
print(table)



def admin_login():
    username = input("Masukkan username admin: ")
    password = input("Masukkan password admin: ")
    
    if username == 'TokoSembakoSRC' and password == 'tokosembakot2':
        print("Login admin berhasil!")
        while True:
            print("\n=== Menu Admin ===")
            print("1. Tambah Produk")
            print("2. Tampilkan Produk")
            print("3. Update Produk")
            print("4. Hapus Produk")
            print("5. Keluar")
            admin_pilihan = input("Pilih menu (1/2/3/4/5): ")
            if admin_pilihan == '1':
                create ()
            elif admin_pilihan == '2':
                read ()
            elif admin_pilihan == '3':
                update ()
            elif admin_pilihan == '4':
                delete ()
            elif admin_pilihan == '5':
                print("Terima kasih! Sampai jumpa lagi.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")     


#Fungsi Craete
def create ():
    No = (input("Masukkan Id barang baru :"))
    Nama_Barang = (input("Masukkan nama barang:"))
    Harga = int(input("Masukkan Harga produk:"))
    Stok_Barang = int(input("Masukkan stok produk:"))
    table.add_row([No, Nama_Barang, Harga, Stok_Barang])
    print(table)

#Fungsi read
def read ():
    print(table)   

#Fungsi Update
def update():
    No = input("Masukkan Nomor: ")
    Nama_Barang = input("Masukkan Nama Barang: ")
    Harga = input("Masukkan Harga Terbaru: Rp. ")
    for i, row in enumerate(table._rows):
        if int(row[0]) == No:
            table._rows[i] = [row[0], input("Masukkan Harga Terbaru: ")]
    print("Data berhasil diupdate")

#Fungsi delete                                        
def delete():
    No = (input("Pilih nomor yang akan dihapus: "))
    for i, row in enumerate(table._rows):
        if int(row[0]) == No:
            table.del_row(i)
    print("Data berhasil dihapus") 


if pilihan == "1":
   admin_login()
elif pilihan == "2":
   print ("Selamat Datang")
   pembelian = input ("Silahkan memilih barang yang ingin anda beli :")
   jumlah = int(input("Masukkan jumlah yang ingin Anda beli :"))
