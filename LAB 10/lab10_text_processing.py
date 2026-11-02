
print("====================================================")
print("                TEXT PROCESSING TOOL")
print("====================================================")

sentence = input("Enter a sentence: ")

print("\n--- Processing Results ---")

index_pos = int(input("Enter position for indexing: "))
print(f"Character at position {index_pos}     : '{sentence[index_pos]}'")

start_idx = int(input("Enter start index for slicing : "))
end_idx = int(input("Enter end index for slicing   : "))
print(f"Sliced string [{start_idx}:{end_idx}]         : '{sentence[start_idx:end_idx]}'")

upper_str = sentence.upper()
print(f"Uppercase                   : {upper_str}")

lower_str = sentence.lower()
print(f"Lowercase                   : {lower_str}")

old_word = input("Enter word to replace       : ")
new_word = input("Enter replacement word      : ")
replaced_str = sentence.replace(old_word, new_word)
print(f"After replace               : {replaced_str}")

length_val = len(sentence)
print(f"Length of sentence          : {length_val}")

print("\n====================================================")
print("Analysis Complete!")
print("====================================================")