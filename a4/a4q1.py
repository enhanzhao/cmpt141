#Enhan Zhao 11097118

paragraph = "  I am a Canadian, a free Canadian, free to speak without fear, free to worship in my own way, free to stand for what I think right, free to oppose what I believe wrong, or free to choose those who shall govern my country. This heritage of freedom I pledge to uphold for myself and all mankind!!....  "


paragraph = paragraph.replace(",", "")
paragraph = paragraph.replace("!", "")
paragraph = paragraph.replace(".", "")
paragraph = paragraph.lstrip()
paragraph = paragraph.rstrip()
lst = paragraph.split()


def count_words(word, word_list):
    """
    counts how many times a word appears in a list
    word is a single word
    word_list is a list that contains single words
    returns the number of occurrences of word in word_list
    """
    count = 0
    for w in word_list:
        if w == word:
            count = count + 1
    return count


def unique_words(word_list):
    """
    returns unique words in a list
    word_list is a list that contains single words
    returns a list of unique words in word_list
    """
    unique_list = []
    for i in word_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
    
unique_lst = unique_words(lst)

for w in unique_lst:
    print("The word", w, "appears", count_words(w, lst), "times in the paragraph.")
