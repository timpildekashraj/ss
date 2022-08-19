ls = ['a','s','d','d']
# print(type(ls))
def loop(s):
    print(s*3)

def map(loop,ls):
    for l in ls:
        loop(l)

map(loop,ls)

#function as argument

# function programming