class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}

        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        occurrences = counts.values()

        return len(occurrences) == len(set(occurrences))  



        