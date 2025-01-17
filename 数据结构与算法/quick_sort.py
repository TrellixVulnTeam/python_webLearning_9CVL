#coding:utf-8

def quick_sort(alist,start,end):
	"""快速排序"""

	# 递归的推出条件
	if start > end:
		return


	# 设定起始元素为要寻找位置的基准元素
	mid = alist[start]

	# low为序列左边的由左向右移动的标志
	low = start

	# high为序列右边的由右边向左移动的标志
	high = end

	while low < high:
		# 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
		while low < high and alist[high] >= mid:
			high -= 1
		# 将high指向的元素放到low的位置上
		alist[low] = alist[high]


		# 将low与high未重合，low指向的元素比基准元素小，则low向右移动
		while low < high and alist[low] < mid:
			low += 1
		# 将low指向的元素放到high的位置上
		alist[high] = alist[low]

	# 推出循环后， low与high重合，此时所指位置为基准元素的正确位置
	# 将基准元素放到该位置
	alist[low] = mid

	# 对基准元素左边的子序列进行快速排序
	quick_sort(alist,start,low-1)

	# 对基准元素右边的子序列进行快速排序
	quick_sort(alist,low+1,end)


alist = [45,93,17,77,31,55,20]
quick_sort(alist,0,len(alist)-1)
print(alist)