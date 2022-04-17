# Utility module that contains utilities to be used throughout.

COLORS = (
    "#000000",   # Black
    "#ffffff",   # White
    "#ff0000",   # Red
    "#00ff00",   # Green
    "#0000ff",   # Blue
    "#ffdd00"    # Yellow (slightly more "banana"-y for better visibility)
)
COLORNAMES = (
    "Black",
    "White",
    "Red",
    "Green",
    "Blue",
    "Yellow"
)
DEFAULTCOLOR = "#444444"

def verbose_wrapper(func, *args, **kwargs):
    def inner(*args, **kwargs):
        print(f"Function {func.__name__} called.")
        out = func(*args, **kwargs)
        print(f"Function {func.__name__} completed successfully.")
        return out
    return inner

def target_to_words(target):
    out = []
    for c in range(4):
        out += [COLORNAMES[target[c]]]
    return out