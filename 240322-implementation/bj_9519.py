import sys
input = sys.stdin.readline

X = int(input())
origin_word = input().strip()
word = origin_word
n = len(origin_word)
word_list = [origin_word]

def shuffle():
  global word, word_list
  new_word = ''
  mid = n // 2
  for idx in range(mid):
    new_word += word[idx] + word[n-idx-1]
  if n % 2 != 0:
    new_word += word[n//2]
  word = new_word

while True:
  shuffle()
  if origin_word == ''.join(word):
    break
  word_list.append(word)
print(word_list[-X%len(word_list)])
