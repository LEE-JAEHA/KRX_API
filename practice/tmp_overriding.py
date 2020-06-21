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
# # vis_data(1)
# # tmp = "회사명	close	diff	open	high	low	volume	MMS_MA20P	MMS_MA60P	MMS_MA120P	MMS_ATR	MMS_slowk	MMS_slowd	MMS_MOM	MMS_RSI	MMS_ADX	MMS_macd	MMS_macdsignal	MMS_macdhist	MMS_aroondown	MMS_aroonup	MMS_VAR	MMS_WILLR	search	combine"
# # tmp2 = tmp.split("\t")
# # print(tmp2)
# #
# # from tqdm import  tqdm
# # from tqdm import trange
# # import time
# # for i in trange(10):
# #     time.sleep(0.5)
# #     print(i)
# #
# import os
# path = "D:\MVP\code\yolo\yolo2\data\plate\labels"
# file_list = os.listdir(path)
# data_=list()
# for i in file_list:
#     tmp = i.split(".")[0]
#     print(tmp)
#     data_.append(tmp)
#     #print("D:/MVP/code/yolo/yolo2/data/plate/images/"+i)
#     #print(i)
#
# path = "D:\MVP\code\yolo\yolo2\data\plate\images"
# file_list = os.listdir(path)
# for i in file_list :
#     tmp = i.split(".")[0]
#     if tmp in data_:
#         print("D:/MVP/code/yolo/yolo2/data/plate/images/"+i)

#print ("file_list: {}".format(file_list))
#
#
# tmp = input(": ")
# print(tmp.split('\t'))


stride = 2
tmp = [stride] + [1] *(2-1)
print(tmp)