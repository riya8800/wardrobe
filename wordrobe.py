class ClothingItem:
    def __init__(self, name, color, category):
        self.name = name
        self.color = color
        self.category = category

    def describe(self):
        return f"{self.color} {self.name} ({self.category})"


def find_by_color(items, color):
    return [item for item in items if item.color == color]


if __name__ == "__main__":
    items = [
        ClothingItem("tank top", "blue", "tops"),
        ClothingItem("skirt", "red", "skirts"),
        ClothingItem("shorts", "blue", "shorts"),
    ]
    for item in find_by_color(items, "blue"):
        print(item.describe())