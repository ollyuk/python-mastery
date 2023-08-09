class TraceMem:
    def __init__(self, value):
        current, peak = value
        self.mb_val = 1048576
        self.current = current / self.mb_val
        self.peak = peak / self.mb_val

    def __str__(self):
        return f'current={self.current:,.2f}, peak={self.peak:,.2f}'
