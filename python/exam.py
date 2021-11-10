class test:
    def testing(self):
        print("one")
        lst={"zero":000,"one":111,"three":333}
        try:
            print("linux")
            print(lst["once"])
            print("windows")
        except NameError:
            print("except-1")
        except KeyError:
            print("except-2")
        except:
            print("except-3")
        try:
            x=45/lst["zero"]
        except ZeroDivisionError:
            print("except-4")
        finally:
            print("fianlly")
        print("two")

te = test()
te.testing()