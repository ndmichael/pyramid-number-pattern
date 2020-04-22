"""Version 3 of Pyramid Number Pattern with Reflection
forming a DIAMOND
landscape view for best display
for numbers > one length i.e 10 above
just tilt your phone
Design/Code by: BlackRose Micheal
"""


class AdvPattern:
    def __init__(self):
        self.result = None

    def patternUtil(self, n):
        l = [[n]]
        ll = [[]]
        result = None
        for i in range(n - 1, 0, -1):
            l.append(l[-1] + [i])

        for i in range(1, len(l)):
            ll += [l[i][::-1][1:]]

        self.result = zip(l, ll)
        self.zipMerge(self.result)

    def zipMerge(self, result):
        self.zm = []
        for m in result:
            # print(m[0],  end=" ")
            self.zm.append(m[0] + m[1])

        return self.zm

    def pattern_print(self):
        n = len(self.zm)
        K = n
        D = int(7 / 2) - 1
        for m in self.zm:
            for k in range(K):
                print(end="  ")
            K -= 1
            for j in m:
                print(j, end=" ")
            print()

        # self.zm = self.zm.reverse()

        for m in self.zm[::-1][1:]:
            for k in range(D):
                print(end="  ")
            D += 1
            for j in m:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    print("Pyramid Number Pattern in Diamond Reflection", end=" \n\n")
    obj = AdvPattern()
    for i in range(9, -1, -1):
        obj.patternUtil(i)
        obj.pattern_print()

    print("\n\n '©' Micheal")
