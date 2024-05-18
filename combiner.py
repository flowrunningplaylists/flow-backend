from statistics import fmean


class Combiner:
    def __init__(self, arrs: list[list[float]]):
        self.arrs = sorted(arrs, key=len, reverse=True)
    
    def combine(self) -> list[float]:
        new_list = [ [] for _ in range(len(self.arrs[0])) ]
        for arr in self.arrs:
            for i in range(len(arr)):
                new_list[i].append(arr[i])
                
        new_list = list(map(fmean, new_list))
        return new_list
