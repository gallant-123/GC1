'''
=================================================
Graded Challenge 1

Nama  : Emmanuel Gallant Sadenna Tibian
Batch : HCK-023

Program ini dibuat untuk membantu proses belanja menjadi lebih efisien
=================================================
'''



class cartItem:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class shoppingCart:
    def __init__(self):
        self.items = [] #untuk menyimpan item yang dibuat

        #function menambahkan barang
    def menambahkanBarang(self,item):
            # nama = input("Masukkan nama barang: ")
            # harga = int(input("Masukkan harga barang: "))
            # #untuk menambahkan item yang ingin ditambahkan
            # item = cartItem (nama,harga)
            self.items.append(item)
            print(f"Barang {item.nama} berhasil ditambahkan")

        #function hapus barang
    def hapusBarang(self):
            nama = input("Masukkan barang yang ingin dihapus: ")
            for item in self.items:
               #untuk menghapus barang yang sudah tidak diinginkan
               if item.nama == nama:
                   self.items.remove(item)  
                   print("Barang berhasil dihapus")
        
        #function total harga
    def totalHarga(self):
        total = sum(item.harga for item in self.items)
        return f"Total belanja adalah {total}"
        
        #funtion tampilkan barang        
    def showBarang(self):
            if not self.items:
                print("Data belum tersedia")
            else:
            #menampilkan barang yang sudah diinput
                print("Barang di keranjang:")
                i = 1
                for item in self.items:
                     print(f"{i}. {item.nama} - Rp {item.harga}")
                     i += 1

    def runningProgram(self):
        pilihanMenu = ""
        while pilihanMenu != 5:
            #menu utama pada prgoram
            print("\nMenu: ")
            print("1. Menambah barang")
            print("2. Hapus barang")
            print("3. Tampilkan barang di keranjang")
            print("4. Lihat total belanja")
            print("5. Exit")

            pilihanMenu = input("Pilih menu: ")

            if pilihanMenu == "1":
                nama = input("Masukkan nama barang: ")
                harga = int(input("Masukkan harga barang: "))
                #untuk menambahkan item yang ingin ditambahkan
                item = cartItem (nama,harga)
                self.menambahkanBarang(item)
            elif pilihanMenu == "2":
                self.hapusBarang()
            elif pilihanMenu == "3":
                self.showBarang()
            elif pilihanMenu == "4":
                hasil = self.totalHarga()
                print(hasil)
            elif pilihanMenu == "5":
                print("Sampai Jumpa! Terima kasih sudah belanja di Toko Makmur.")
                break
            else:
                print("Pilihan tidak sesuai")
            

if __name__ == "__main__":

    tempObject = shoppingCart()
    tempObject.runningProgram()