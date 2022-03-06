def starts_with_A(word):
    if (word[0])== "A":
        return True
    else:
        return False


# Main Routine
word_to_check = input("Enter word: ").title()
print(starts_with_A(word_to_check))

