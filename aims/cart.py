from typing import List
from aims.dvd import DigitalVideoDisc

class Cart:
    MAX_NUMBERS_ORDERED = 20

    def __init__(self):
        self.items: List[DigitalVideoDisc] = []

    def add_dvd(self, dvd: DigitalVideoDisc) -> bool:
        # [Fix A]: Chặn nghiêm ngặt khi giỏ đạt đủ 20 đĩa
        if len(self.items) >= self.MAX_NUMBERS_ORDERED:
            print("Cart is full! Cannot add more items.")
            return False
        self.items.append(dvd)
        return True

    def remove_dvd(self, dvd: DigitalVideoDisc) -> bool:
        if dvd in self.items:
            self.items.remove(dvd)
            return True
        return False

    def total_cost(self) -> float:
        return round(sum(item.cost for item in self.items), 2)

    def print_cart(self) -> str:
        lines = ["***********************CART***********************", "Ordered Items:"]
        for idx, item in enumerate(self.items, 1):
            lines.append(f"{idx}. {item}")
        lines.append(f"Total cost: {self.total_cost():.2f} $")
        lines.append("***************************************************")
        output = "\n".join(lines)
        print(output)
        return output

    def search_by_title(self, keyword: str) -> List[DigitalVideoDisc]:
        return [item for item in self.items if item.is_match(keyword)]
