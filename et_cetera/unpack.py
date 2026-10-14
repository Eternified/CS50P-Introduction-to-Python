def f(*args, **kwargs):
    print(f"Named: {kwargs}")

f(galleons=100, sickles=50, knuts=25)