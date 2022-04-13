# Utility module that contains utilities to be used throughout.

def verbose_wrapper(func, *args, **kwargs):
    def inner(*args, **kwargs):
        print(f"Function {func.__name__} called.")
        out = func(*args, **kwargs)
        print(f"Function {func.__name__} completed successfully.")
        return out
    return inner