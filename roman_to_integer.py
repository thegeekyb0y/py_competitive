# Problem : https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        sum = 0

        for i in range(len(s)):
            c = s[i]

            if i != 0 and (c == "V" or c == "X") and s[i - 1] == "I":
                continue
            if i != 0 and (c == "L" or c == "C") and s[i - 1] == "X":
                continue
            if i != 0 and (c == "D" or c == "M") and s[i - 1] == "C":
                continue

            if c == "C":
                if i == len(s) - 1:
                    sum += dict[c]
                    continue
                if s[i + 1] == "D":
                    sum += 400
                    continue
                elif s[i + 1] == "M":
                    sum += 900
                    continue

            if c == "X":
                if i == len(s) - 1:
                    sum += dict[c]
                    continue
                if s[i + 1] == "L":
                    sum += 40
                    continue
                elif s[i + 1] == "C":
                    sum += 90
                    continue

            if c == "I":
                if i == len(s) - 1:
                    sum += dict[c]
                    continue
                if s[i + 1] == "V":
                    sum += 4
                    continue
                elif s[i + 1] == "X":
                    sum += 9
                    continue

            sum += dict[c]

        return sum
