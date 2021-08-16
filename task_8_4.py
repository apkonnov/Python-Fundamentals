from functools import wraps


def val_checker(val_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            try:
                if val_func(*args):
                    result = func(*args)
                    return result
                else:
                    raise ValueError(f'ValueError: wrong val: {args[0]}')
            except ValueError as e:
                print(f'Еrr: {e}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)

a = calc_cube(-5)
print(a)
