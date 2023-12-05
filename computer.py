class Computer:
    def __init__(self, cost, cpu, gpu):
        self.cost = cost
        self.cpu = cpu
        self.gpu = gpu

    def __str__(self):
        return f"Computer({self.cost}, {self.cpu}, {self.gpu})"