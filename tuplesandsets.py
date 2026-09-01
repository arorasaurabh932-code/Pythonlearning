keys = ['a','b','c','d']
values = [1,2,3]
x=list(zip(keys,values))
y=dict(zip(keys,values))
print(x)
print(y)
#converting string into dictionary using ast
import ast
st= "{'name':'john','age':30}"
d2= ast.literal_eval(st)
print(d29)
d1 = {
    'name':'john',
    'age':31,
    'car':'ford',
    'year' :1991,
}
d1['year']=2022
print(d1)
d1.update({'year':2030})
print(d1)