from statistics import fmean


class Combiner:
    def __init__(self, arrs: list[list[float]]):
        self.arrs = arrs
    
    def combine(self) -> list[float]:
        sorted_arrs = sorted(sorted_arrs, key=len, reverse=True)
        new_list = [ [] for _ in range(len(sorted_arrs)) ]
        for arr in sorted_arrs:
            for i in range(len(arr)):
                new_list[i].append(arr[i])
                
        new_list = list(map(fmean, new_list))
        return new_list

    def getAvgs(self) -> list[float]:
        return list(map(fmean, self.arrs))
    
    