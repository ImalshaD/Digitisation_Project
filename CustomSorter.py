class CustomSorter:
    @staticmethod
    def sortByYandX(list1 : list) -> list:
        sorted_list = sorted(list1, key=lambda cell: (cell.getC1Cordinates()[0], cell.getC1Cordinates()[1]))
        return sorted_list