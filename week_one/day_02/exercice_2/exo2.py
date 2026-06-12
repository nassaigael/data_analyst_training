from collections import Counter

sentence = "data science python"

result = Counter(sentence.replace(" ", ""))

print(result)
