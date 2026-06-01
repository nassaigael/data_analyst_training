words = ["python", "java", "javascript", "c", "rust", "go", "swift", "ruby"]

result = sorted(words, key=lambda x: (-len(x), x))

print(result)