class Pen:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __str__(self):
        return f"Computer({self.color}, {self.size})"