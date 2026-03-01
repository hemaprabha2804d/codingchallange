class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge both arrays
        merged = nums1 + nums2
        merged.sort()
        
        n = len(merged)
        
        # If odd length, return middle element
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            # If even length, return average of two middle elements
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0