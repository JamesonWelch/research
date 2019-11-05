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

class A:
    @staticmethod
    def f(x=[]):
        x.append(len(x))
        return x

print(f'A.f() = {A.f()}')
print(f'A.f() = {A.f()}')
print(f'A.f() = {A.f()}')

class A:
    def f(self, x=[]):
        x.append(len(x))
        return x

print(f'A().f() = {A().f()}')
print(f'A().f() = {A().f()}')
print(f'A().f() = {A().f()}')

print(f'locals = {locals().keys()}')
print(f'globals = {globals().keys()}')
print(f'locals is globals = {locals() is globals()}')
