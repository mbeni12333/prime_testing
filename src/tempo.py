
def gen_carmichael(N=1e5, n_facteur_max=5):
    """
    int->int
    """
    premiers = np.array([i for i in range(3, int(N), 2) if first_test(i)])
    

    nb_facteur = 3
    
    #indexes = np.arange(len(premiers))

    indexes = np.array(0)

    test = 3
    while True:
        test -= 1
        #np.random.shuffle(indexes)

        acci = []
        acc = []

        maxValue = N

        for i in range(nb_facteur):

            if i == 0:
                randomInt = np.random.randint(len(premiers))

            else:
                randomInt = np.random.choice(indexes, 1)[0]

            selectedPremier = premiers[randomInt]

            maxValue /= selectedPremier
            maxIndex = np.searchsorted(premiers, maxValue)


            acc.append(selectedPremier)
            acci.append(randomInt)


            if maxIndex == 0:
                break

            indexes = np.arange(maxIndex)
            indexes = np.setdiff1d(indexes, acc)


        if len(acc) != nb_facteur:
            continue

        print(acc)

        n = np.prod(acc)

        if isCarmichael_facteurs(n, acc):
            return n
