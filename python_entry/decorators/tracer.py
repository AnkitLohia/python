#from tracer import hello
#hello('a'); hello('b'); hello.count
#first trace decorator is applied followed by escape_unicode

def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return x.encode('unicode-escape')
    return wrap

def check_if_string(index):
    def validator(f):
        def wrap(*arg, **kwargs):
            if isinstance(arg[index], basestring) == False:
                raise ValueError("Argument {0} must be non-negative".format(arg[index]))
            return f(*arg, **kwargs)
        return wrap
    return validator

class Trace:
    def __init__(self):
        self.count = 0

    def __call__(self, f):
        def wrap(*args, **kwargs):
            return f(*args, **kwargs)
        self.count += 1
        return wrap

tracer = Trace()
@tracer
@escape_unicode
@check_if_string(0)
def hello(name="ankitcs"):
    print "hello {0}".format(name)
