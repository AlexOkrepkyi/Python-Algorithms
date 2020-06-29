class Solution:

    def longest_common_prefix(self, strs: List[str]) -> str:

        common_prefix = []

        for letter in zip(*strs):
            if len(set(letter)) == 1:
                common_prefix.append(letter[0])
            else:
                break

        return "".join(common_prefix)


"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
