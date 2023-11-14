# # # # A basic prototype service for detecting the words typed by a user by swapping the fingers from key to key on the keyboard,
# # # #  more popularly knows as glide typing is to be implemented. A user usually intends to type a sequence of the character they
# # # # swiped over.

# # # # Given an input string s and an array of n strings, dictionary, find the lexicographically smallest word in the dictionary
# # # that is a subsequence of the given string s. If there is no such string return the string “-1” as the answer.
# # # # Note: string x is considered lexicographically smaller
# #  than another string y if the string x will occur be for u in the dictionary order.

# # # # Example:
# # # # Suppose s=“hgferyjkllkop” and dictionary =[“coffe”,”coding”,”happy”,”hello”,”hop”]
# # # # The only possible valid words that are a subsequence of
#  the given string are “ hello” and “hop”. Since “hello” is
# lexicographically smaller, report “hello” is answer

# # # # In javascript

def findSubsequence(s, dictionary):
    result = "-1"
    for word in dictionary:
        if isSubsequence(word, s) and (result == "-1" or word < result):
            result = word
    return result


def isSubsequence(word, s):
    i = 0
    j = 0
    while i < len(word) and j < len(s):
        if word[i] == s[j]:
            i += 1
        j += 1
    return i == len(word)


# Example usage
s = "hgferyjkllkop"
dictionary = ["coffe", "coding", "happy", "hello", "hop"]
result = findSubsequence(s, dictionary)
print(result)  # Output: "hello"
