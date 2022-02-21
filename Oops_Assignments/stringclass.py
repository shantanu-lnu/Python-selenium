class StringClass:

    firstlist = []
    Mainstring = ""

    def __init__(self, string):
        self.inputstr = string
        self.Mainstring = string
        # print(str)

    def getdata(self):
        string = self.inputstr
        return string

    def strlen(self):
        strsize = len(self.inputstr)
        return strsize

    def convert(self, string):
        strlist = list(string)
        # strlist[:0] = str
        return strlist


obj = StringClass("123456")
obj.Mainstring = obj.getdata()
obj.firstlist = obj.convert(obj.Mainstring)
print("Size of the given string: ", obj.strlen())

print("List converted from string " + obj.Mainstring + " is: ", obj.firstlist)