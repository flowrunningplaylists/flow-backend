from statistics import fmean

test_list = [
    [1, 1, 4, 50, 300],
    [10, 1, 4, 50, 1, 1, 1 , 1, 300],
    [2, 3, 4, 300],
    [10, 1, 4, 50, 40, 44, 300],
    [9, 1, 2, 50, 31],
    [10, 1, 4, 50, 32],
    [2, 3, 4, 50, 33],
]

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

cb = Combiner(arrs=test_list)
print(cb.combine())
