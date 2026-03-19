class stringReverse:
    def __init__(self, str):
        self.str = str

    def reverse(self):
        words = self.str.split()
        reversed_words = words[::-1]
        print(" ".join(reversed_words))


s2 = stringReverse("I like coding very much .")
s2.reverse()