
# read in list of words
f = open("p042_words.txt")
words = f.read().split(',')

# get the word values
print(ord('Z')-64)
count = []
word_count = len(words)
for x in range(word_count):
    count.append(0)
    for letter in words[x]:
        # subtract 64 from the ordinal position of the letter, which gives A=1, B=2...
        count[x] = count[x] + ord(letter)-64

# get the list of potential triangle numbers
n = 0
tn = 0
triangle_nums = []
count_max = max(count)
while tn < count_max:
    n = n + 1
    tn = n*(n+1)/2
    triangle_nums.append(tn)

# compare triangle numbers to word counts
triangle_word_count = 0
for x in count:
    if x in triangle_nums:
        triangle_word_count = triangle_word_count + 1

print(triangle_word_count)
