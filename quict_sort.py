# a[p...r] p是第一个元素，r是最后一个元素(第9个)
#即p = 0, r = 8
a = [3,8,4,1,9,2,6,5,7]
def quick_sort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q - 1)
        quick_sort(a, q + 1, r)
    #print(a)
    return a

def partition(a, p, r):
    i = p - 1#i 在数组之外(指向第-1个元素，表示small zone为空)
    key = a[r]#以第r个元素作为key
    for j in range(p, r):#遍历整个数组（除最后一个元素，即最后一次循环为j = r-1）
        if a[j] < key:
            i = i + 1#i向右移动一个单元(表示small zone的长度增长1)
            a[i], a[j] = a[j], a[i]#i,j两个元素交换位置，将a[j]放如small zone里
        #否则，i指针位置不变，j增加(表示big zone的长度增长1)。表示本轮循环指向的元素a[j]放入big zone里
    a[i+1], a[r] = a[r], a[i+1]#最后，将key跟i+1指向的位置交换（将中轴放在small zone和big zone之间）
    #print(a)
    return i + 1#返回中轴的索引（即返回q）

