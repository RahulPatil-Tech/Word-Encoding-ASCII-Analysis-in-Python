from collections import Counter
import numpy as np
def word_to_qubits(word):
    sentence = []
    for ch in word:
        binary = format(ord(ch), '08b')
        sentence.append(
            f"The letter '{ch}' is encoded into qubits as a superposition of states {binary}.\n")
    return " ".join(sentence)
a = str(input("Enter Word:"))
result = word_to_qubits(a)
print(result)
s = list(a)
print(f"List from String: {s}")
s = np.array([ord(c) for c in a])
means = np.mean(s)
print(f"Mean for the word is as per ASCII: {means}")
print("Significance of ASCII Mean Calculation:")
print("1. The string is converted into numeric ASCII values so mathematical operations can be applied.")
print("2. The mean represents the average ASCII value of all characters in the word.")
print("3. This value has no linguistic or semantic meaning in natural language.")
print("4. ASCII values are encoding-specific and do not represent importance or sentiment.")
print("5. This approach is mainly useful for learning, basic encoding experiments, or low-level text analysis.")

b = Counter(a)
print(f"Count of Letters entired into String: {dict(b)}")
c = set(list(a))
g = Counter(c)
print(f"Count of Letters entired into String (After Filtering): {sorted(dict(g))}")
result = " ".join(f"{k}: {v}" for k, v in g.items())
print(f"Count of letters entered into string (After Filtering): {result}")
