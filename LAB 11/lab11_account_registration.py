

def analyze_document():
    sentence = input("Enter a sentence: ")

    words_count = len(sentence.split())
    vowels_count = 0
    consonants_count = 0
    digits_count = 0
    spaces_count = 0
    special_chars_count = 0

    vowels = set("aeiouAEIOU")

    for char in sentence:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
        elif char.isdigit():
            digits_count += 1
        elif char.isspace():
            spaces_count += 1
        else:
            special_chars_count += 1

    total_characters = len(sentence)
    total_letters = vowels_count + consonants_count
    vowel_percentage = (
        (vowels_count / total_letters * 100) if total_letters > 0 else 0.0
    )

    print("=" * 48)
    print("DOCUMENT ANALYSIS REPORT")
    print("=" * 48)
    print(f"Sentence: {sentence}")
    print(f"Total characters: {total_characters}\n")

    print("--- Character Breakdown ---")
    print(f"Words:              {words_count}")
    print(f"Vowels:             {vowels_count}")
    print(f"Consonants:         {consonants_count}")
    print(f"Digits:             {digits_count}")
    print(f"Spaces:             {spaces_count}")
    print(f"Special characters: {special_chars_count}\n")

    print("--- Summary ---")
    print(f"Total letters: {total_letters}")
    print(f"Vowel percentage: {vowel_percentage:.1f}%\n")

    print("=" * 48)
    print("Analysis Complete!")
    print("=" * 48)


if __name__ == "__main__":
    analyze_document()



