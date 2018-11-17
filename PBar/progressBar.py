import sys
class ProgressBar:
    def __init__(self, count = 0, total = 0, width = 50):
        self.count = count
        self.total = total
        self.width = width
    def move(self):
        self.count += 1
    def log(self):
        sys.stdout.write(' ' * (self.width + 9) + '\r')
        sys.stdout.flush()
        progress = 0
        progress = self.width * self.count / self.total
        if self.total > 50:#too big to display
            hex_unit = self.total/50#every unit size
            progress = int(self.count/hex_unit) if int(self.count/hex_unit)>0 else 1
        sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
        sys.stdout.write('#' * progress + '-' * (self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()
