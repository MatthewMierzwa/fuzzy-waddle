class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lst=[]
        for i in nums1:
            lst.append(i)
        for j in nums2:
            lst.append(j)
        h=sorted(lst)
        if (len(h)&1)==1:
            return h[(len(h)/2)]
        else:
            t1=h[int((len(h)/2))]
            t2=h[int((len(h)/2)-1)]
            return ((t1+t2)/2.0)
