from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

def main():
    cart = Cart()
    dvd1 = DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95)
    dvd2 = DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 124, 24.95)
    dvd3 = DigitalVideoDisc("Aladdin", "Animation", "Ron Clements", 90, 18.99)

    cart.add_dvd(dvd1)
    cart.add_dvd(dvd2)
    cart.add_dvd(dvd3)

    print(f"Total cost: {cart.total_cost():.2f} $")

if __name__ == "__main__":
    main()
