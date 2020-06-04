def shw_img(a=1,b=2,c=3,visualize=True,e=int):
    d = a+b
    print(e)
    return d



def sum_(a,b=2,c=3):
    print(a+b+c)

def average3(num1, num2, num3=9):
  result = (num1 + num2 + num3)/3
  return result

print(shw_img(3,e=1))




a=1
c=2
d =  a if not (a,int) else c

print("d :  ", d)
print("a : " ,a)


print("**"*100)
import argparse as ar

# parser = ar.ArgumentParser(description='Process some integers.')
#
# #parser.add_argument('--sum', dest='accumulate', action='store_const',const=sum, default=max,help='sum the integers (default: find the max)')
#
# parser.add_argument("temp",metavar='test입니다',type=str)
# parser.add_argument('integers', metavar='N', type=int)
# args = parser.parse_args()
# print(args)
#
# print("RESULT  : " ,args.temp)
#
# a ="hi"
# s = ['a','b','c']
# d = ['a','b','c']
# c = s/"{}.333".format(d)
# print(c)
# def vis_data(x,y = None, c = 'r'):
#     print(y)
#     print(c)
#
#
# vis_data(1)
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(e=90)
if 'g' in x:
    print("HI")
y= dict()
y['a']={1:2}
y['a'].update({2:3})
print(y)

