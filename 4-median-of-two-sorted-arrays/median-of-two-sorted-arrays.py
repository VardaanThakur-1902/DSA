class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Make nums1 the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m

        while low <= high:
            # Partition nums1
            i = (low + high) // 2

            # Partition nums2
            j = (m + n + 1) // 2 - i

            # Left and right values of nums1
            left1 = float('-inf') if i == 0 else nums1[i - 1]
            right1 = float('inf') if i == m else nums1[i]

            # Left and right values of nums2
            left2 = float('-inf') if j == 0 else nums2[j - 1]
            right2 = float('inf') if j == n else nums2[j]

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                # Odd number of elements
                if (m + n) % 2 == 1:
                    return max(left1, left2)

                # Even number of elements
                else:
                    left_max = max(left1, left2)
                    right_min = min(right1, right2)

                    return (left_max + right_min) / 2.0

            # nums1 partition is too far right
            elif left1 > right2:
                high = i - 1

            # nums1 partition is too far left
            else:
                low = i + 1