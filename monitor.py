class Monitor:
    def __init__(self, resolution, size):
        self.resolution = resolution
        self.size = size

    def __str__(self):
        return f"Computer({self.resolution}, {self.size})"