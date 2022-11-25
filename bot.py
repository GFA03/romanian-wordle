from scipy.stats import entropy

#   0 = GRI
#   1 = GALBEN
#   2 = VERDE

f = open("cuvinte_wordle.txt", "r")
lst = []
lst = f.read().split()
f.close()

def frequency(ok, guess, freq):
    for i in range(5):
        if ok[i] > 0:
            freq[ord(guess[i]) - 65] += 1
    for i in range(5):
        if ok[i] == 0 and freq[ord(guess[i]) - 65] == 0:
            freq[ord(guess[i]) - 65] = -1


def shrink(guess, ok, lst):
    avb_words = []  # lista de cuvinte posibile avand in vedere inputul
    aux = 0
    freq = [0] * 26
    frequency(ok, guess, freq)
    # aux==0, lista de available words este goala, deci ia cuvinte din lista initiala(cu toate cuvintele)
    # aux==1, lista de available words NU este goala, deci aplica filtrul pt lista de available words

    for i in range(5):

        if ok[i] == 2:
            if aux == 0:
                avb_words=[element_lst for element_lst in lst if guess[i] == element_lst[i] and element_lst.count(guess[i]) >= freq[ord(guess[i]) - 65]]
                if len(avb_words) == 0:
                    return []
                aux = 1

            else:
                avb_words=[element_lst for element_lst in avb_words if guess[i] == element_lst[i] and element_lst.count(guess[i]) >= freq[ord(guess[i]) - 65]]
                if len(avb_words) == 0:
                    return []

    for i in range(5):

        if ok[i] == 1:
            if aux == 0:
                avb_words=[element_lst for element_lst in lst if guess[i] in element_lst and guess[i]!= element_lst[i] and element_lst.count(guess[i]) >= freq[ord(guess[i]) - 65]]
                if len(avb_words) == 0:
                    return []
                aux = 1
            else:
                avb_words=[element_lst for element_lst in avb_words if guess[i] in element_lst and guess[i] != element_lst[i] and element_lst.count(guess[i]) >= freq[ord(guess[i]) - 65]]
                if len(avb_words) == 0:
                    return []

    for i in range(5):

        if ok[i] == 0:
            if aux == 0:
                avb_words=[element_lst for element_lst in lst if (guess[i] in element_lst and freq[ord(guess[i]) - 65] != -1 and guess[i] != element_lst[i]) or guess[i] not in element_lst]
                if len(avb_words) == 0:
                    return []
                aux = 1

            else:
                avb_words=[element_lst for element_lst in avb_words if guess[i] not in element_lst or (freq[ord(guess[i]) - 65] != -1 and element_lst.count(guess[i]) <= freq[ord(guess[i]) - 65] and guess[i] != element_lst[i])]
                if len(avb_words) == 0:
                    return []

    return avb_words

def calculare_entropie(word, lst):
    ok = [(0, 0, 0, 0, 0), (0, 0, 0, 0, 1), (0, 0, 0, 0, 2), (0, 0, 0, 1, 0), (0, 0, 0, 1, 1), (0, 0, 0, 1, 2), (0, 0, 0, 2, 0), (0, 0, 0, 2, 1), (0, 0, 0, 2, 2), (0, 0, 1, 0, 0), (0, 0, 1, 0, 1), (0, 0, 1, 0, 2), 
(0, 0, 1, 1, 0), (0, 0, 1, 1, 1), (0, 0, 1, 1, 2), (0, 0, 1, 2, 0), (0, 0, 1, 2, 1), (0, 0, 1, 2, 2), (0, 0, 2, 0, 0), (0, 0, 2, 0, 1), (0, 0, 2, 0, 2), (0, 0, 2, 1, 0), (0, 0, 2, 1, 1), (0, 0, 2, 1, 2), (0, 0, 2, 2, 0), (0, 0, 2, 2, 1), (0, 0, 2, 2, 2), (0, 1, 0, 0, 0), (0, 1, 0, 0, 1), (0, 1, 0, 0, 2), (0, 1, 0, 1, 0), (0, 1, 0, 1, 1), (0, 1, 0, 1, 2), (0, 1, 0, 2, 0), (0, 1, 0, 2, 1), (0, 1, 0, 2, 2), (0, 1, 1, 0, 0), (0, 1, 1, 0, 1), (0, 1, 1, 0, 2), (0, 1, 1, 1, 0), (0, 1, 1, 1, 1), (0, 1, 1, 1, 2), (0, 1, 1, 2, 0), (0, 1, 1, 2, 1), (0, 1, 1, 2, 2), (0, 1, 2, 0, 0), (0, 1, 2, 0, 1), (0, 1, 2, 0, 2), (0, 1, 2, 1, 0), (0, 1, 2, 1, 1), (0, 1, 2, 1, 2), (0, 1, 2, 2, 0), (0, 1, 2, 2, 1), (0, 1, 2, 2, 2), (0, 2, 0, 0, 0), (0, 2, 0, 0, 1), (0, 2, 0, 0, 2), (0, 2, 0, 1, 0), (0, 2, 0, 1, 1), (0, 2, 0, 1, 2), (0, 
2, 0, 2, 0), (0, 2, 0, 2, 1), (0, 2, 0, 2, 2), (0, 2, 1, 0, 0), (0, 2, 1, 0, 1), (0, 2, 1, 0, 2), (0, 2, 1, 1, 0), (0, 2, 1, 1, 1), (0, 2, 1, 1, 2), (0, 2, 1, 2, 0), (0, 2, 1, 2, 1), (0, 2, 1, 2, 2), (0, 2, 2, 0, 0), (0, 2, 2, 0, 1), (0, 2, 2, 0, 2), (0, 2, 2, 1, 0), (0, 2, 2, 1, 1), (0, 2, 2, 1, 2), (0, 2, 2, 2, 0), (0, 2, 2, 2, 1), (0, 2, 2, 2, 2), (1, 0, 0, 0, 0), (1, 0, 0, 0, 1), (1, 0, 0, 0, 2), (1, 0, 0, 1, 0), (1, 0, 0, 1, 1), (1, 0, 0, 1, 2), (1, 0, 0, 2, 0), (1, 0, 0, 2, 1), (1, 0, 0, 2, 2), (1, 0, 1, 0, 0), (1, 0, 1, 0, 1), (1, 0, 1, 0, 2), (1, 0, 1, 1, 0), (1, 0, 1, 1, 1), (1, 0, 1, 1, 2), (1, 0, 
1, 2, 0), (1, 0, 1, 2, 1), (1, 0, 1, 2, 2), (1, 0, 2, 0, 0), (1, 0, 2, 0, 1), (1, 0, 2, 0, 2), (1, 0, 2, 1, 0), (1, 0, 2, 1, 1), (1, 0, 2, 1, 2), (1, 0, 2, 2, 0), (1, 0, 2, 2, 1), (1, 0, 2, 2, 2), (1, 1, 0, 0, 0), (1, 1, 0, 0, 1), (1, 1, 0, 0, 2), (1, 1, 0, 1, 0), (1, 1, 0, 1, 1), (1, 1, 0, 1, 2), (1, 1, 0, 2, 0), (1, 1, 0, 2, 1), (1, 1, 0, 2, 2), (1, 1, 1, 0, 0), (1, 1, 1, 0, 1), (1, 1, 1, 0, 2), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1), (1, 1, 1, 1, 2), (1, 1, 1, 2, 0), (1, 1, 1, 2, 1), (1, 1, 1, 2, 2), (1, 1, 2, 0, 0), (1, 1, 2, 0, 1), (1, 1, 2, 0, 2), (1, 1, 2, 1, 0), (1, 1, 2, 1, 1), (1, 1, 2, 1, 2), (1, 1, 2, 
2, 0), (1, 1, 2, 2, 1), (1, 1, 2, 2, 2), (1, 2, 0, 0, 0), (1, 2, 0, 0, 1), (1, 2, 0, 0, 2), (1, 2, 0, 1, 0), (1, 2, 0, 1, 1), (1, 2, 0, 1, 2), (1, 2, 0, 2, 0), (1, 2, 0, 2, 1), (1, 2, 0, 2, 2), (1, 2, 1, 0, 0), (1, 2, 1, 0, 1), (1, 2, 1, 0, 2), (1, 2, 1, 1, 0), (1, 2, 1, 1, 1), (1, 2, 1, 1, 2), (1, 2, 1, 2, 0), (1, 2, 1, 2, 1), (1, 2, 1, 2, 2), (1, 2, 2, 0, 0), (1, 2, 2, 0, 1), (1, 2, 2, 0, 2), (1, 2, 2, 1, 0), (1, 2, 2, 1, 1), (1, 2, 2, 1, 2), (1, 2, 2, 2, 0), (1, 2, 2, 2, 1), (2, 0, 0, 0, 0), (2, 0, 0, 0, 1), (2, 0, 0, 0, 2), (2, 0, 0, 1, 0), (2, 0, 0, 1, 1), (2, 0, 0, 1, 2), (2, 0, 0, 2, 
0), (2, 0, 0, 2, 1), (2, 0, 0, 2, 2), (2, 0, 1, 0, 0), (2, 0, 1, 0, 1), (2, 0, 1, 0, 2), (2, 0, 1, 1, 0), (2, 0, 1, 1, 1), (2, 0, 1, 1, 2), (2, 0, 1, 2, 0), (2, 0, 1, 2, 1), (2, 0, 1, 2, 2), (2, 0, 2, 0, 0), (2, 0, 2, 0, 1), (2, 0, 2, 0, 2), (2, 0, 2, 1, 0), (2, 0, 2, 1, 1), (2, 0, 2, 1, 2), (2, 0, 2, 2, 0), (2, 0, 2, 2, 1), (2, 0, 2, 2, 2), (2, 1, 0, 0, 0), (2, 1, 0, 0, 1), (2, 1, 0, 0, 2), (2, 1, 0, 1, 0), (2, 1, 0, 1, 1), (2, 1, 0, 1, 2), (2, 1, 0, 2, 0), (2, 1, 0, 2, 1), (2, 1, 0, 2, 2), (2, 1, 1, 0, 0), (2, 1, 1, 0, 1), (2, 1, 1, 0, 2), (2, 1, 1, 1, 0), (2, 1, 1, 1, 1), (2, 1, 1, 1, 2), (2, 1, 1, 2, 0), (2, 1, 1, 2, 1), (2, 1, 1, 2, 2), (2, 1, 2, 0, 0), (2, 1, 2, 0, 1), (2, 1, 2, 0, 2), (2, 1, 2, 1, 0), (2, 1, 2, 1, 1), (2, 1, 2, 1, 2), (2, 1, 2, 2, 0), (2, 1, 2, 2, 1), (2, 2, 0, 0, 0), 
(2, 2, 0, 0, 1), (2, 2, 0, 0, 2), (2, 2, 0, 1, 0), (2, 2, 0, 1, 1), (2, 2, 0, 1, 2), (2, 2, 0, 2, 0), (2, 2, 0, 2, 1), (2, 2, 0, 2, 2), (2, 2, 1, 0, 0), (2, 2, 1, 0, 1), (2, 2, 1, 0, 2), (2, 2, 1, 1, 0), (2, 2, 1, 1, 1), (2, 2, 1, 1, 2), (2, 2, 1, 2, 0), (2, 2, 1, 2, 1), (2, 2, 2, 0, 0), (2, 2, 2, 0, 1), (2, 2, 2, 0, 2), (2, 2, 2, 1, 0), (2, 2, 2, 1, 1), (2, 2, 2, 2, 0), (2, 2, 2, 2, 2)]
    S = list()
    for out in ok:
        avb_words = shrink(word, out, lst)
        S.append(len(avb_words)/len(lst))
    return entropy(S, base = 2)

# returneaza cuvantul cu cea mai mare entropie
def best_word(ok, avb_words):
    max_entr=-10000
    for cuv in avb_words:
        entropie=calculare_entropie(cuv,avb_words)
        if entropie>max_entr:
            max_entr=entropie
            cuv_entr=cuv
    return cuv_entr

def frequency2(word, freq):
    for x in word:
        freq[ord(x) - 65] += 1

def main():
    f = open("output.txt", "a")
    H = list()
    # Calculeaza entropia intregii liste si o adauga in lista H
    '''
    for word in lst:
        entropie = calculare_entropie(word, lst)
        H.append([word, entropie])
    '''   
    H.sort(key = lambda x: x[1], reverse = True)
    for i in range(len(H)):
        f.write(str(H[i]) + "\n")

if __name__ == "__main__":
    main()