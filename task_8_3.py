from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({", ".join(map(lambda el: str(el) + ": " + str(type(el)), args))})')
        # print(f'{func.__name__}({", ".join(map(lambda el: str(el) + ": " + str(type(el)), kwargs.values()))})')
        return result
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
