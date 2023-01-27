#!usr/bin/python3
def safe_print_division(a, b):
    r = 0
    try:
        if b == 0:
            r = None
        r = a / b
    except:
        pass
    finally:
        print("{} {}".format("Inside result:", r))
    return(r)
