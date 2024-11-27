import string
from collections import Counter
file = open("what_is_python.txt", "r")

wordlist=[]
line = file.read()
print("-----Input file:python.txt ------\n",line)
line_no_punc=line.translate(str.maketrans("", "", string.punctuation))
wordlist = line_no_punc.split()


print(max(wordlist))

count_dict = Counter(wordlist)

print(count_dict.most_common(10))













