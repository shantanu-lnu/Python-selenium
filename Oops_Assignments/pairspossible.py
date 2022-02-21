from stringclass import StringClass


class PairsPossible(StringClass):
    list3 = []

    def __init__(self, string_1):

        self.obj_1 = StringClass(string_1)
        self.obj_1.firstlist = self.obj_1.convert(string_1)

    def pairs(self):
        for i in range(self.obj_1.strlen()):
            for j in range(self.obj_1.strlen()):
                self.list3.append(self.obj_1.firstlist[i] + " " + self.obj_1.firstlist[j])
        return self.list3


obj_2 = PairsPossible("923456")
obj_2_list = (obj_2.pairs())
print(obj_2_list)