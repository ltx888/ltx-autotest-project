#
# arr = [3,5,15,45,67,23,44,98,1,23]
'''# length = len(arr)
# for i in range(length-1):
#         for j in range(length - i - 1):
#             if arr[j] > arr[j+1]:
#                arr[j], arr[j+1] = arr[j+1], arr[j]
#                print(arr)
# '''
# length = len(arr)
# for i in range(length - 1):
#     least = i
#     for j in range(i + 1,length):
#         if arr[j] < arr[least]:
#             least = j
#         arr[i], arr[least] = arr[least],arr[i]
# python 四种简单的排序方法 冒泡排序 选择排序 插入排序 快速排序
#题目是：有一组“+”和“-”符号，要求将“+”排到左边，“-”排到右边，写出具体的实现方法。
# def StringSort(data):
#     startIndex=0
#     endIndex=0
#     count=len(data)
#     while startIndex+endIndex<count:
#         if data[startIndex]=='-':
#             data[startIndex],data[count-endIndex-1]=data[count-endIndex-1],data[startIndex]
#             endIndex+=1
#         else:
#             startIndex+=1
#     return data
# data=['-','-','+','-','+','+','-','+','+','-','-','+','-']
# print(StringSort(data))

