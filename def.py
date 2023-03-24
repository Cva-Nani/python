def var_args(*x):
    t=0
    for num in x:
        t=t+num
    print("total=",t)
var_args()
var_args(11)
var_args(11,22)
var_args(11,22,33)
var_args(11,22,33,44)