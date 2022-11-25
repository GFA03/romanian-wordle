import csv
import random
import sys
import termcolor
import bot

f = open("cuvinte_wordle.txt", "r")
lst = []
lst = f.read().split()
f.close()

def frequency(word, freq):
    for x in word:
        freq[ord(x) - 65] += 1
# face frecventa literelor din cuvant


def main():
    a = random.randint(1, 11454)
    # obtine un numar random din intervalul [1,11454] ce reprezinta indexul unui cuvant

    word = ""

    with open('words.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ID'] == str(a):
                word = row['NAME']
                # cauta cuvantul cu indexul a din baza de date si-l retine in var word
                break

    # print(word)
    # word = "VINEI"

    guess = ""
    i = True
    j = 0
    ok = [0, 0, 0, 0, 0]  # in ok retinem 0, 1 sau 2 pentru fiecare litera din word
    freq = [0] * 26
    avb_words = lst
    frequency(word, freq)
    # print(freq)

    while i is True:
        if guess == "":
            guess = "TAREI"
        else:
            guess = bot.best_word(ok, avb_words)
        sys.stdout.write('\x1b[1A')
        # Incercare valida
        j = 0
        freq = [0] * 26  # listele fiind mutabile nu permit copi, asa ca refac vectorul de frecventa la fiecare pas
        frequency(word, freq)
        for x in range(5):
            if guess[x] == word[x]:
                ok[x] = 2
                freq[ord(guess[x]) - 65] -= 1
        for x in guess:  # verificam litera cu litera incercarea
            var = word.find(x)  # pozitia literei in word(cuvantul cheie), daca exista
            if var > -1:
                if ok[j] < 2 and freq[ord(x) - 65] > 0:
                    ok[j] = 1  # valoarea 1 semnifica doar indetitate de litera, output galben
                    freq[ord(x) - 65] -= 1
            j += 1
        #i += 1  iteratorul creste numai pentru incercari valide
        for j in range(5):
            if ok[j] == 2:
                print(termcolor.colored(guess[j], 'green'), end="")
            elif ok[j] == 1:
                print(termcolor.colored(guess[j], 'yellow'), end="")
            else:
                print(guess[j], end="")
        avb_words = bot.shrink(guess, ok, avb_words)
        ok = [0, 0, 0, 0, 0]
        print('\n')
        if guess == word:
            print(termcolor.colored("JOC FINALIZAT!", 'green'))
            i = False
            break

if __name__ == '__main__':
    main()
