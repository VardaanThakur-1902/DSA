class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for interval in intervals:

            # Current interval before newInterval
            if interval[1] < newInterval[0]:
                ans.append(interval)

            # Current interval after newInterval
            elif interval[0] > newInterval[1]:
                ans.append(newInterval)
                newInterval = interval

            # Overlapping intervals
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        ans.append(newInterval)
        return ans