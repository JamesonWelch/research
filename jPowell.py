# jPowell.py


# mutable default arguments
def f(x=[]):
    x.append(len(x))
    return x

print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')

def f(x=None):
    if x is None:
        x = []
    x.appenx(len(x))
    return x

print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')

def f(*args, **kwargs):
    def f(x=[]):
        x.append(len(x))
        return x
    return f(*args, **kwargs)

print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')

def d(f):
    def _(*args, **kwargs):
        return f(*args, **kwargs)
    return _

@d
def f(x=[]):
    x.append(len(x))
    return x

print(f'f() = {f()}')
print(f'f() = {f()}')
print(f'f() = {f()}')
