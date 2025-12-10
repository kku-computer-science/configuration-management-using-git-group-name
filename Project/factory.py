from AllSort.BubbleSort import Bubble
from AllSort.Quicksort import Quicksort

class factory:
    @staticmethod
    def getSort(name):
        if name.strip().lower() == "bubble":return Bubble()
        if name.strip().lower() == "quick":return Quicksort()
        else:
            print(f"Unknown sorting : {name}")
            exit(1)
