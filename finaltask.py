import open(Book1.txt)
import open(Book2.txt)
import open(book3.txt)

f1 = open(Book1.txt,W)
f2 = open(Book2.txt,W)
f3 = open(Book3.txt,W)

def longest_word(word_list)
    longest_word = ''
    largestLen=0

    for word in word_list:
        if word[-1].isalpha() == False:
                word = word[:-1]
        if len(word) > len(longest_word)
            longest_word = word
    print ("The longest word(s) in the list is %s." % largestWord)
        if len(longest) > len(longest_word[0]):
            real_longest = [longest]
        elif len(longest) == len(longest_word[0]):
            longest_word.append(longest)
        linenum += 1
        print(longest)
for word in longest_word:
    print('This word is one of the largest:', word)
