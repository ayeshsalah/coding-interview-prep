# Leetcode
# 30. Substring with Concatenation of All Words
# https://www.youtube.com/watch?v=06Ym9c7SuOU


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0:
            return []
        words_count = {}
        word_len = len(words[0])
        result = []
        substr_len = len(words) * word_len

        # count of all the words 
        for word in words:
            words_count[word] = words_count.get(word, 0) + 1

        # sliding window
        for left in range(len(s)-substr_len+1): # subtracting substr_len+1 as concatenated substr cannot be found in length less than substr_len
            visited_words = {}
            for right in range(len(words)):
                # print(right)
                # create window of word length
                starting_index = left+right*word_len
                # find the temp word
                temp_word = s[starting_index:starting_index+word_len]
                # print(temp_word)
                # if temp word not in original words list then break
                if temp_word not in words_count:
                    break
                # add word to visited_words dict
                visited_words[temp_word] = visited_words.get(temp_word, 0) + 1
                # print(visited_words)
                # if the count of temp_word is more than original word count then break
                if visited_words[temp_word] > words_count[temp_word]:
                    break
            if visited_words == words_count:
                result.append(left)
        return result
        