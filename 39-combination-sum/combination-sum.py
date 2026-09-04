class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, remaining, path):
            # Found a valid combination
            if remaining == 0:
                result.append(path[:])
                return

            # Try candidates from start onward
            for i in range(start, len(candidates)):
                num = candidates[i]

                # Since candidates are sorted,
                # no later number can work either
                if num > remaining:
                    break

                # Choose the current number
                path.append(num)

                # i instead of i + 1 because
                # the same number can be reused
                backtrack(i, remaining - num, path)

                # Undo the choice
                path.pop()

        candidates.sort()
        backtrack(0, target, [])

        return result