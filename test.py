import unittest
from app import shoppingCart,cartItem

class testApp(unittest.TestCase):

    def test_menambahkanBarang_success(self):

        #input objek shoppingCart
        cart = shoppingCart()

        #memanggil method menambahkan barang
        result = cart.menambahkanBarang("ayam", 5000)

        #output yang diinginkan                              
        expectation = ("Barang ayam berhasil ditambahkan", 5000)

        #untuk testing hasil dan ekspetasi pada program
        self.assertEqual(result, expectation)

    def test_hapusBarang_success(self):

        cart = shoppingCart()

        result = cart.hapusBarang ("ikan",5000)
        expectation = ("Barang ayam berhasil dihapus", 5000)

        self.assertEqual(result, expectation)

    def testTotalHarga(self):
        cart = shoppingCart()

        cart.menambahkanBarang("ikan", 5000)
        cart.menambahkanBarang("ayam", 6000)

        result = cart.totalHarga

        expectation = "Total harga adalah 11000"

        self.assertEqual(result, expectation)

if __name__ == "__main__":
    unittest.main()