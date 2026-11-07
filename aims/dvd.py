class DigitalVideoDisc:
    def __init__(self, title: str, category: str = "", director: str = "", length: int = 0, cost: float = 0.0):
        self.title = title
        self.category = category
        self.director = director
        self.length = length
        self.cost = float(cost)

    def is_match(self, keyword: str) -> bool:
        # Sửa lỗi: không phân biệt hoa thường
        return keyword.lower() in self.title.lower()

    def __str__(self) -> str:
        return f"DVD - {self.title} - {self.category} - {self.director} - {self.length} mins: {self.cost:.2f} $"
