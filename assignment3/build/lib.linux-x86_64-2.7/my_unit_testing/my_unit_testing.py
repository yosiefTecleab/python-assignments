import sys
class UnitTest(object):
    def __init__(self, func, args, kwargs, res):    # make test
        
        self.testfunc=func
        self.testargs=args
        self.testkwargs=kwargs
        self.testresult=res          

    def __call__(self):                             # run test
        try:
            if self.testfunc(*self.testargs,**self.testkwargs)==self.testresult:
                return True
            else:
                print "Test Failed!! at ", self.testfunc
                print "Arguments:", self.testargs,",", self.testkwargs
                print "Error: Did not produce the expected result", self.testresult
                return False
        except:
            print "Test Failed!! at ", self.testfunc
            print "Arguments:", self.testargs,",", self.testkwargs
            print "Error:" , sys.exc_info()[0]
            return False
        

