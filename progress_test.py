import sys
import time

class ProgressBar:
    def __init__(self, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end="\r"):
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.print_end = print_end
        self.iteration = 0

    def print_progress(self, iteration):
        self.iteration = iteration
        percent = ("{0:." + str(self.decimals) + "f}").format(100 * (self.iteration / float(self.total)))
        filled_length = int(self.length * self.iteration // self.total)
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        print(f'\r{self.prefix} |{bar}| {percent}% {self.suffix}', end=self.print_end)
        if self.iteration == self.total:
            print()

# Example code to test the progress bar
if __name__ == "__main__":
    total_files = 100
    progress = ProgressBar(total_files, prefix='Progress:', suffix='Complete', length=50)
    
    for i in range(1, total_files + 1):
        time.sleep(0.1)  # Simulating work
        progress.print_progress(i)