
d1 = {
    'name':'john',
    'age':31,
    'car':'ford',
    'year' :1991,
}
for key,value in d1.items():
    print(f'{key=}and {value=}')
d2 = {'a':3,'c':2,'b':1,'d':4}
print(d2.items())
x=dict(sorted(d2.items()))
print(x)
d3={'a':3,'b':4,'c':3,'d':5}
def f1(d):
    for key ,val in d.items():
        print(key,val)
f1(d1)