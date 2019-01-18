# 第三题 求最大子序列之和

def maxSeqSum(list_nums):
    maxsum = 0
    # 遍历到节点之前的序列最大和
    max_ = 0
    length_ = len(list_nums)
    for i in range(length_):
        if max_ <= 0:
            max_ = list_nums[i]
        else:
            max_ += list_nums[i]

        if max_ > maxsum:
            maxsum = max_

    return maxsum

list_ = [2, -3, 3, 50]
maxsum = maxSeqSum(list_)
print("max sub sequence sum is: ",maxsum)

