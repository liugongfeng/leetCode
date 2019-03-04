class Solution:

    def merge(self, nums1, m, nums2, n):
        """
        :param nums1: List[int]
        :param m:     int
        :param nums2: List[int]
        :param n:     int
        :return:      void
        """
        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[m-1+n] = nums2[n-1]
                n -= 1
            else:
                nums1[m-1+n] , nums1[m-1] = nums1[m-1], nums1[m-1+n]
                m -= 1
        if m == 0 and n > 0:
            nums1[:n] = nums2[:n]

            
