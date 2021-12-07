# Project 6! Strings2
# This program helps Obiwan use C3P0 to translate into Droid latin a.k.a pig latin.

sentence = input('Hello its me, C3P0. Most droids speak Droid Latin\nPlease allow me translate for you: ').lower()
words = sentence.split()

for i, word in enumerate(words):
    # Check for vowel in first letter
    if word[0] in 'aeiou':
        words[i] = words[i] + "yay"
    else:
        # set vowel checker value
        has_vowel = False

        for j, letter in enumerate(word):
            if letter in 'aeiou':
                words[i] = word[j:] + word[:j] + "yay"
                has_vowel = True
                break

            # if word begins with a consonant add "ay"
            if has_vowel == False:
                words[i] = words[i] + "ay"

droid_latin = ' '.join(words)
print("Droid Latin: ", droid_latin)


# Run file


def main():
    if __name__ == '__main__':
        main()
