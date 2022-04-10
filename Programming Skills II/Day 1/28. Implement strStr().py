class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle!="":
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i:i+len(needle)]==needle:
                    return i
        else:
            return 0
        return -1
        