class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        common_prefix = ""

        if len(strs) == 0:                                           # return empty string, if empty list was given
            return common_prefix

        for letter in range(len(min(strs))):                         # for every letter in the shortest word
            common_letter = strs[0][letter]
            if all(word[letter] == common_letter for word in strs):  # if all corresponding letters are similar
                common_prefix += common_letter                       # add this letter to the "common_letter" string
            else:
                break                                                # else break

        return common_prefix


"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
