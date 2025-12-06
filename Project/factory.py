from AllSort.BubbleSort import Bubble

class factory:
    def getSort(self, name):
        if name.strip().lower() == "bubble":return Bubble()
        else:
            print(f"Unknown sorting : {name}")
            exit(1)