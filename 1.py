class Solution:
  # @return a tuple, (index1, index2)
  def twoSum(self, num, target):
    index = {}
    for i in range(len(num)):
      if num[i] not in index:
        index[num[i]] = [i]
      else:
        index[num[i]].append(i)

    for i in range(len(num)):
      if target - num[i] in index:
        indices = index[target - num[i]]
        if i != indices[0]:
          return i + 1, indices[0] + 1
        if len(indices) > 1 and i != indices[1]:
          return i + 1, indices[1] + 1
    return None


assert Solution().twoSum([2, 7, 11, 15], 9) == (1, 2)
assert Solution().twoSum([3, 2, 4], 6) == (2, 3)
assert Solution().twoSum([0, 4, 3, 0], 0) == (1, 4)

