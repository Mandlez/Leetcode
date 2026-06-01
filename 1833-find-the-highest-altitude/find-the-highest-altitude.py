class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        hightest = 0

        for g in gain:
            altitude += g
            hightest = max(hightest, altitude)

        return hightest   