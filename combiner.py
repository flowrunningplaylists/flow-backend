from statistics import fmean
from matplotlib import pyplot as plt
import numpy as np
import io


class Combiner:
    def __init__(self, arrs: list[list[float]]):
        self.arrs = arrs
    
    def combine(self) -> list[float]:
        sorted_arrs = sorted(self.arrs, key=len, reverse=True)
        new_list = [ [] for _ in range(len(sorted_arrs[0])) ]
        for arr in sorted_arrs:
            for i in range(len(arr)):
                new_list[i].append(arr[i])
                
        new_list = list(map(fmean, new_list))
        return new_list

    def getAvgs(self) -> list[float]:
        return list(map(fmean, self.arrs))
    
    def getPlot(self, bpm, cadence, time):
        fig, ax = plt.subplots(figsize=(10, 5))
    
        ax.plot(time, bpm, linestyle=':', marker='o', color='blue', label='BPM')
        ax.plot(time, cadence, linestyle=':', marker='o', color='green', label='Cadence')
        ax.set_title('BPM and Cadence over Time')
        ax.set_xlabel('Time')
        ax.set_ylabel('Value')
        ax.legend()
        
        img = io.BytesIO()
        fig.savefig(img, format='png')
        img.seek(0)
        
        plt.close(fig)
        return img
    
    def showPlot(self, bpm, cadence, time):
        fig, ax = plt.subplots(figsize=(10, 5))
    
        ax.plot(time, bpm, linestyle=':', marker='o', color='blue', label='BPM')
        ax.plot(time, cadence, linestyle=':', marker='o', color='green', label='Cadence')
        ax.set_title('BPM and Cadence over Time')
        ax.set_xlabel('Time')
        ax.set_ylabel('Value')
        ax.legend()
        
        fig.show()
        input("Input anything to stop showing...")
        plt.close(fig)

if __name__ == '__main__':
    bpm = [100, 125, 111, 123, 150, 256, 203, 100]
    cadence = [67, 89, 97, 101, 124, 167, 199, 86]
    time = [1, 2, 3, 4, 5, 6, 7, 8]
    
    cb = Combiner([[]])
    fig = cb.showPlot(bpm, cadence, time)
    img = cb.getPlot(bpm, cadence, time)
