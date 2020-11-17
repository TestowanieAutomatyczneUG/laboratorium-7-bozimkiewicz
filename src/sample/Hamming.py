class Hamming:
    def distance(self, first, second):
        if len(first) != len(second):
            raise ValueError('Value cannot be of different length')
        counter = 0
        for i in range(0, len(first)):
            if first[i] != second[i]:
                counter += 1
        return counter
