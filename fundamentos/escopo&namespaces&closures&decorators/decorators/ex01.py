import functools

def log_passos(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{wrapper.__name__}')
        f = func(*args, **kwargs)
        print(f'{func.__name__}')
        return f
    return wrapper

@log_passos
def my_func():
    print('minha função')

my_func()

