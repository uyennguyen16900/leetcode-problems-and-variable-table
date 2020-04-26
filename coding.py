# Given a sorted linked list, delete all duplicates such that each element appear only once.

# head = 1->1->2 = 1->2
# curr = 2


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None:
        return head

    curr = head
    while curr.next is not None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

# m 0
# n 1
# l 0

def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        l = len(nums1) - 1
        while n > 0 and m > 0:
            if nums1[m-1] <= nums2[n-1]:
                nums1[l], nums2[n-1] = nums2[n-1], nums1[l]
                l -= 1
                n -= 1

            else:
                nums1[l], nums1[m-1] = nums1[m-1], nums1[l]
                l -= 1
                m -= 1

        if n > 0:
            while n > 0:
                nums1[n-1] = nums2[n-1]
                n -= 1
