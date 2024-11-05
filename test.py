import unittest
from app import cartItem,shoppingCart

class testApp(unittest.TestCase):

    def test_menambahkanBarang_success(self):

        #input objek shoppingCart
        cart = shoppingCart()

        item = cartItem("ayam",5000)

        #memanggil method menambahkan barang
        result = cart.menambahkanBarang(item)

        #output yang diinginkan                              
        expectation = ("Barang ayam berhasil ditambahkan", 5000)

        #untuk testing hasil dan ekspetasi pada program
        self.assertEqual(result, expectation)

    def test_hapusBarang_success(self):

        cart = shoppingCart()

        nama = "ayam"
        harga = 5000
        item = cartItem(nama,harga)
        cart.menambahkanBarang(item)

        result = cart.hapusBarang ("ayam")
        expectation = "Barang ayam berhasil dihapus"

        self.assertEqual(result, expectation)

    def testTotalHarga(self):
        cart = shoppingCart()

        nama = "ayam"
        harga = 5000
        item = cartItem(nama,harga)
        cart.menambahkanBarang (item)
    

        result = cart.totalHarga (5000)

        expectation = "Total belanja adalah 5000"

        self.assertEqual(result, expectation)

if __name__ == "__main__":
    unittest.main()