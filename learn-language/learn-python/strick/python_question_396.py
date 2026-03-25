# Python Question: Implement a Text Justification Algorithm
'''
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:

A word cannot be split into two lines.
Each word is guaranteed not to exceed maxWidth in length.
The input array words contains at least one word.

Example:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand   well",
  "enough to explain to",
  "a computer.  Art is",
  "everything  else we",
  "do                  "
]
'''

# Solution
def fullJustify(words, maxWidth):
    """
    Justifies the given words to fit within the specified maximum width.

    Args:
        words: A list of words.
        maxWidth: The maximum width of each line.

    Returns:
        A list of justified lines.
    """
    result = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(current_line) + len(word) > maxWidth:
            # Line is full, justify and add to result
            if len(current_line) == 1:
                # Single word in line, left justify
                result.append(current_line[0] + " " * (maxWidth - current_length))
            else:
                # Multiple words, distribute spaces
                spaces_needed = maxWidth - current_length
                spaces_between = spaces_needed // (len(current_line) - 1)
                extra_spaces = spaces_needed % (len(current_line) - 1)

                justified_line = ""
                for i in range(len(current_line) - 1):
                    justified_line += current_line[i]
                    justified_line += " " * spaces_between
                    if extra_spaces > 0:
                        justified_line += " "
                        extra_spaces -= 1
                justified_line += current_line[-1]
                result.append(justified_line)

            # Start a new line
            current_line = [word]
            current_length = len(word)
        else:
            # Add word to current line
            current_line.append(word)
            current_length += len(word)

    # Last line, left justify
    last_line = " ".join(current_line)
    last_line += " " * (maxWidth - len(last_line))
    result.append(last_line)

    return result

# Test cases
def test_solution():
    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth1 = 16
    expected1 = ["This    is    an", "example  of text", "justification.  "]
    assert fullJustify(words1, maxWidth1) == expected1

    words2 = ["What","must","be","acknowledgment","shall","be"]
    maxWidth2 = 16
    expected2 = ["What   must   be", "acknowledgment  ", "shall be        "]
    assert fullJustify(words2, maxWidth2) == expected2

    words3 = ["Science","is","what","we","understand","well","enough","to","explain",
             "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth3 = 20
    expected3 = ["Science  is  what we", "understand   well", "enough to explain to", "a computer.  Art is", "everything  else we", "do                  "]
    assert fullJustify(words3, maxWidth3) == ["Science  is  what we", "understand   well", "enough to explain to", "a computer.  Art is", "everything  else we", "do                  "]

    words4 = ["Listen","to","many,","speak","to","a","few."]
    maxWidth4 = 6
    expected4 = ['Listen', 'to    ', 'many, ', 'speak ', 'to   a', 'few.  ']
    assert fullJustify(words4, maxWidth4) == ['Listen', 'to    ', 'many, ', 'speak ', 'to   a', 'few.  ']

    words5 = ["a"]
    maxWidth5 = 1
    expected5 = ['a']
    assert fullJustify(words5, maxWidth5) == expected5

    words6 = ["a"]
    maxWidth6 = 2
    expected6 = ['a ']
    assert fullJustify(words6, maxWidth6) == ['a ']

    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()