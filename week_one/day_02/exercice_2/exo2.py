from collections import Counter

sentece = "data science python"

result = Counter(sentece.replace(" ", ""))

print(result)
