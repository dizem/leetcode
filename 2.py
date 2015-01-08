# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  # @return a ListNode
  def addTwoNumbers(self, l1, l2):
    head = None
    tail = None
    carry = 0
    while l1 is not None or l2 is not None:
      val = carry
      if l1 is not None:
        val += l1.val
        l1 = l1.next
      if l2 is not None:
        val += l2.val
        l2 = l2.next
      carry = val // 10
      node = ListNode(val % 10)
      if head is None:
        head = tail = node
      else:
        tail.next = node
        tail = tail.next
    if carry > 0:
      tail.next = ListNode(carry)
    return head


def buildList(nums):
  head = None
  tail = None
  for val in nums:
    if head is None:
      head = tail = ListNode(val)
    else:
      tail.next = ListNode(val)
      tail = tail.next
  return head


def printList(l):
  while l:
    print(l.val)
    l = l.next
  print()


l1 = buildList([2, 4, 3])
printList(l1)
l2 = buildList([5, 6, 4])
printList(l2)
s = Solution().addTwoNumbers(l1, l2)
printList(s)