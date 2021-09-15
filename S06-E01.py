def Tavan(N1, N2):
    hasel_tavan = N1
    for i in range (N2-1):
        Hasel=0
        for j in range(N1):
            Hasel += hasel_tavan
        hasel_tavan = Hasel

    return hasel_tavan

print(Tavan(3,2))
