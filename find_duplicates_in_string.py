#Find duplicate characters in a string

s = input("Enter a string: ")


#space complexity: O(1) because the frequency array has a fixed size of 256
freq = [0] * 256

for ch in s:
    freq[ord(ch)] += 1

    if freq[ord(ch)] == 2:
        print(f"Duplicate: {ch}")
