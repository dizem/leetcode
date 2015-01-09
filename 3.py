class Solution:
  def lengthOfLongestSubstring(self, s):
    index = {}
    length = 0
    max_length = 0
    start = 0
    for i in range(0, len(s)):
      if s[i] not in index or start > index[s[i]]:
        length += 1
      else:
        length = i - index[s[i]]
        start = index[s[i]] + 1
      index[s[i]] = i
      max_length = max(length, max_length)
    return max_length


print(Solution().lengthOfLongestSubstring("kkyhiddqscdxrjmowf"))
print(Solution().lengthOfLongestSubstring(
  "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"))