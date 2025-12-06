from AllSort.BubbleSort import Bubble

class factory:
    @staticmethod
    def getSort(name):
        if name.strip().lower() == "bubble":return Bubble()
        else:
            print(f"Unknown sorting : {name}")
            exit(1)