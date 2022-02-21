from pairspossible import obj_2_list


class EqualSumPairs():
    list4 = []

    def __init__(self, data):
        self.data_list = data

    def sumofpairs(self):
        sum_digit = 0
        for i in range(len(self.data_list)):
            for j in self.data_list[i]:
                if j.isdigit():
                    z = int(j)
                    sum_digit = sum_digit + z
            self.list4.append(sum_digit)
            sum_digit = 0
        return self.list4

    def diffrentpairsumcount(self):
        count = 0;
        set1 = set(self.list4)
        print(set1)
        count = len(set1)
        return count


obj_4 = EqualSumPairs(obj_2_list)
print(obj_4.sumofpairs())
print(obj_4.diffrentpairsumcount())