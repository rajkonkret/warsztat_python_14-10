def all_args(*args, **kwargs):
    print("args", args)
    print("kwargs", kwargs)


all_args()
all_args(1, 2, 3, 4)
all_args(a=1, b=9, name="Radek")
# args ()
# kwargs {}
# args (1, 2, 3, 4)
# kwargs {}
# args ()
# kwargs {'a': 1, 'b': 9, 'name': 'Radek'}
# all_args(a=8, 9)  # SyntaxError: positional argument follows keyword argument
all_args(6, b=0)
# args (6,)
# kwargs {'b': 0}
