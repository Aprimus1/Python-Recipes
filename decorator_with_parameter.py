def upper_lower(arg):
    def func_wrapper(f):
        def wrap(*args, **kwargs):
            if arg == 'upper':
                return f(*args, **kwargs).upper()
            else:
                raise TypeError
        return wrap
    return func_wrapper

@upper_lower('upper')
def hello(name):
    return 'Hello ' + name
