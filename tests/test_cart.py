import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.dvd1 = DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95)
        self.dvd2 = DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 124, 24.95)
        self.dvd3 = DigitalVideoDisc("Aladdin", "Animation", "Ron Clements", 90, 18.99)

    def test_total_cost(self):
        self.cart.add_dvd(self.dvd1)
        self.cart.add_dvd(self.dvd2)
        self.cart.add_dvd(self.dvd3)
        self.assertAlmostEqual(self.cart.total_cost(), 63.89, places=2)

    def test_cart_limit(self):
        for _ in range(20):
            self.assertTrue(self.cart.add_dvd(self.dvd1))
        self.assertFalse(self.cart.add_dvd(self.dvd1))

    def test_search_by_title(self):
        self.cart.add_dvd(self.dvd1)
        self.cart.add_dvd(self.dvd2)
        results = self.cart.search_by_title("Lion")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Lion King")

    def test_print_cart(self):
        self.cart.add_dvd(self.dvd1)
        output = self.cart.print_cart()
        self.assertIn("The Lion King", output)
        self.assertIn("Total cost", output)

if __name__ == "__main__":
    unittest.main()
