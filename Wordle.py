import csv
import random
import sys
import termcolor


def validation(t):
    with open('words.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['NAME'] == t:
                return True
    return False
# cauta incercarea in baza de date


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
    # word = "ASIEA"

    t = ""
    i = j = 0
    ok = [0, 0, 0, 0, 0]  # in ok retinem 0, 1 sau 2 pentru fiecare litera din word
    freq = [0] * 26

    frequency(word, freq)
    # print(freq)

    while i < 6:  # aici am pus doar 6 incercari, modificam pentru numar nelimitat
        t = input()
        sys.stdout.write('\x1b[1A')
        if validation(t) is True:
            # Incercare valida
            j = 0
            freq = [0] * 26  # listele fiind mutabile nu permit copi, asa ca refac vectorul de frecventa la fiecare pas
            frequency(word, freq)
            for x in range(5):
                if t[x] == word[x]:
                    ok[x] = 2;
                    freq[ord(t[x]) - 65] -= 1
            for x in t:  # verificam litera cu litera incercarea
                var = word.find(x)  # pozitia literei in word(cuvantul cheie), daca exista
                if var > -1:
                    if ok[j] < 2 and freq[ord(x) - 65] > 0:
                        ok[j] = 1  # valoarea 1 semnifica doar indetitate de litera, output galben
                        freq[ord(x) - 65] -= 1
                j += 1
            i += 1  # iteratorul creste numai pentru incercari valide
            for j in range(5):
                if ok[j] == 2:
                    print(termcolor.colored(t[j], 'green'), end="")
                elif ok[j] == 1:
                    print(termcolor.colored(t[j], 'yellow'), end="")
                else:
                    print(t[j], end="")
            ok = [0, 0, 0, 0, 0]
            print('\n')
            if t == word:
                print(termcolor.colored("JOC FINALIZAT!", 'green'))
                break
        else:
            # Cuvant invalid
            print(termcolor.colored(t, 'red'))
    else:
        print(termcolor.colored(f"AI PIERDUT! CUVANTUL ERA: {word}", 'red'))


main()
