class written:
    def __init__(self, wmks):
        self.wm = wmks


class sports:
    def __init__(self, smks):
        self.sm = smks


class results(written, sports):
    def __init__(self, w, s):
        written.__init__(self, w)
        sports.__init__(self, s)

    def display(self):
        print("the total marks =", (self.wm + self.sm))


r1 = results(90,60)
r1.display()