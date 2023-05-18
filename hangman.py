lives = 5
word = "Apple"
collected_chars = set([])

def is_resolved(chars, collected_chars):
        for char in chars:
                if char not in collected_chars:
                        return False

        return True

def resolve_word(collected_chars, word, chosen_letter):
        chars = list(word.lower())
        collected_chars.add(chosen_letter)

        if is_resolved(chars = chars, collected_chars = collected_chars):
                return 'word_resolved'
        if chosen_letter.lower() in chars:
                return 'letter_accepted'

        return 'letter_rejected'

def partial_word(collected_chars, word):
        chars = list(word)
        resolved_chars = []

        for char in chars:
                if char.lower() in collected_chars:
                        resolved_chars.append(char)
                else:
                        resolved_chars.append("_")

        return ' '.join(resolved_chars)




while lives > 0:
        print("You have {} lifes.".format(lives))
        print("The word is ", partial_word(collected_chars = collected_chars, word = word))
        letter = input("Choose a letter: ").lower()
        result = resolve_word(collected_chars = collected_chars, word = word, chosen_letter = letter)
        if result == 'word_resolved':
                print("You guessed the word: " + word)
                break
        if result == 'letter_rejected':
                lives -= 1
                print("The letter you chose is not in the word.")
                continue
else:
        print("You died. The word was " + word)
