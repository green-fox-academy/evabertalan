class MySuperString:
    def __init__(self, mystr):
        self.mystr = mystr

    def reverse(self):
        n = len(self.mystr)
        reversed=''
        for i in range(n):
            reversed = self.mystr[i] + reversed
            print(reversed)
        return reversed

    def characters(self, character):
        count = 0
        for i in self.mystr:
            if i == character:
                count += 1
        return count

        print(count)

    def no_space(self):
        copy=''
        for i in self.mystr:
            if i==' ':
                copy = copy + '_'
            else:
                copy = copy + i
        return copy


class MySuperAverage:
    def __init__(self, mylist):
        self.mylist = mylist

    def average(self):
        summ = 0
        n = len(self.mylist)
        for i in self.mylist:
            summ=summ+i
        avrg=summ/n
        print(avrg)
