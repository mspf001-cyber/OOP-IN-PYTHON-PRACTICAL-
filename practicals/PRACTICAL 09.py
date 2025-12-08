"""Practical 09: File operations"""

# Create sample file
with open('sample.txt', 'w') as f:
    f.write("Hello World\nPython Programming\nFile Handling\nData Processing\n")

# Read file
with open('sample.txt', 'r') as f:
    content = f.read()
    lines = content.split('\n')
    words = content.split()

# a) Count characters, words, lines
print(f"Characters: {len(content)}")
print(f"Words: {len(words)}")
print(f"Lines: {len([l for l in lines if l])}")

# b) Character frequency
char_freq = {}
for char in content:
    if char != '\n':
        char_freq[char] = char_freq.get(char, 0) + 1
print(f"\nChar frequency: {dict(sorted(char_freq.items(), key=lambda x: x[1], reverse=True)[:10])}")

# c) Words in reverse
print(f"\nWords reversed: {words[::-1]}")

# d) Copy even/odd lines
with open('sample.txt', 'r') as f:
    lines = f.readlines()

with open('File1.txt', 'w') as f1, open('File2.txt', 'w') as f2:
    for i, line in enumerate(lines, 1):
        (f1 if i % 2 == 0 else f2).write(line)

print("\nEven lines -> File1.txt, Odd lines -> File2.txt")