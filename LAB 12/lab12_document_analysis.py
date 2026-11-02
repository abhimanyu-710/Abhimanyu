
print("======================================================")
print("              DOCUMENT ANALYSIS SYSTEM")
print("======================================================")

sentence = input("Enter a sentence: ")

total_characters = len(sentence)
words = len(sentence.split())

vowels = 0
consonants = 0
digits = 0
spaces = 0
special_chars = 0

vowel_set = "aeiouAEIOU"

for char in sentence:
    if char.isalpha():
        if char in vowel_set:
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special_chars += 1

total_letters = vowels + consonants
vowel_percentage = (vowels / total_letters * 100) if total_letters > 0 else 0.0

print("\n" + "=" * 54)
print("              DOCUMENT ANALYSIS REPORT")
print("======================================================")
print(f"Sentence          : {sentence}")
print(f"Total characters  : {total_characters}")
print()
print("--- Character Breakdown ---")
print(f"Words             : {words}")
print(f"Vowels            : {vowels}")
print(f"Consonants        : {consonants}")
print(f"Digits            : {digits}")
print(f"Spaces            : {spaces}")
print(f"Special characters: {special_chars}")
print()
print("--- Summary ---")
print(f"Total letters     : {total_letters}")
print(f"Vowel percentage  : {vowel_percentage:.1f}%")
print("======================================================")
print("Analysis Complete!")
print("======================================================")