"""
Code Language:

The two detective agents who are working on a secret mission wants to communicate in code language with each other.
They decided below some rules for encoding a message.
** The first word should be changed as all vowels should be replaced by %
** The second word should be changed like all consonants should be replaced by #
** The third word should be changed like all char should be converted to upper case
** All 3 letters concatenate together

Input:
Where are you? Meet me near the clock tower.
Output:
Wh%r%a#rYOU? M%%t#eNEAR th%##o#TOWER.

(Explanation: Given string contains 9 words, hence will consider 3 pairs, each containing 3 consecutive words from the
start of the string. we will apply the given rules for each pair to covert the message into code language.)
"""


def string(st):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X',
                  'Y', 'Z']

    words = st.split()
    # print(words)

    final_list = []
    updated_words = []

    while len(words) > 0:
        for n in words:
            updated_words.append(n)

            updated_words = updated_words

            a = []
            for word in updated_words[:1]:
                for ch in word:
                    if ch in vowels:
                        l = word.replace(ch, '%')
                        word = l
                a.append(l)

            for word in updated_words[1:2]:
                for ch in word:
                    if ch in consonants:
                        l = word.replace(ch, '#')
                        word = l
                a.append(l)

            for word in updated_words[2:3]:
                a.append(word.upper())

        final_list.append(a)

        del updated_words[:3]
        del words[:3]
        updated_words.append(words[:3])

    # print(final_list)

    final_str = ''
    for i in final_list:
        result = ''.join(i)
        final_str += result + ' '
    print(final_str)


string('Where are you? Meet me near the clock tower.')
string('We need Associates.')
string('Key: Tokyo!')
