import random
import math

s = "KELİME TAHMİN OYUNU"
s = s.center(150, "-")
print(s)

word_list =[
    "system","data","algorithm","such","base","node","model","case",
    "program","informaiton","set","code","funciton","process","application",
    "software","class","point","type","network","tree","object","element",
    "input","operation","level","memory","table","order","file","variable",
    "language","write","list","structure","compute","sequence","computer",
    "bit","probability","machine","array","page","error","step","search",
    "most","path","graph","web","length","several","security","proof",
    "access","obtain","matrix","task","image","form","interface",
    "resource","address","implementation","loop","first","read","location",
    "hardware","behavior","programming","field","parameter","distribution",
    "definition","instance","interaction","internet","representation","edge","stack",
    "return","procedure","link","output","block","domain","store","call","device",
    "server","static","dataset","detection","execute","least","key"
]

gamenumber = 1 # Oyun sırası
userPoint = 0 # Puan
indexlist = [] # Sorulan kelimelerin tekrardan aynısı olmaması ve kontrol etmek için indeks listesi
while True:
    print("     Oyuna başlamak veya devam etmek için ----> 1",
          "     Oyundan çıkmak için                  ----> 2", sep="\n")
    action = int(input("İşlem seçiniz: "))
    if action == 1:
        print(("| " + str(gamenumber) + ". Oyun |").center(150, " "))
        randomIndex = random.randint(0,len(word_list)-1)
        for i in range(len(indexlist)):
            if randomIndex == indexlist[i]:
                randomIndex = random.randint(0, len(word_list)-1)
        word = word_list[randomIndex]
        length = len(word)
        secretWord = "_" * length # Gizli kelimenin gizlenmesi
        clueLetterNumber = length // 3 # İpucu harfler için harf sayısı
        clueLetterIndex = [] # Sorulan kelimenin doğru puanlama yapılması için indeks eleman listesi
        for index in range(clueLetterNumber):
            nIndex = random.randint(0, length - 1)
            secretWord = secretWord[:nIndex] + word[nIndex] + secretWord[nIndex+1:]
            clueLetterIndex.append(nIndex)
        userInputLetter = "" # Kullanıcının girdiği harflerin tutan string dizisi
        userGuessRight = math.ceil(length**0.5) # Tahmin hakkı
        GuessRight = userGuessRight
        while True:
            print(secretWord.center(150, " "))
            print("     Puan: {}\n     Tahmin Hakkı: {}\n     Girilen Harfler: {}".format(userPoint, userGuessRight,userInputLetter))
            print("     Kelime tahminizi harf olarak yapmak için ----> 1",
                  "     Kelime tahminizi direk yapmak için       ----> 2", sep="\n")
            choose = int(input("Seçim: "))
            if choose == 1:
                while True:
                    guessLetter = input("Bir harf girin: ").lower() # Kullanıcının girdiği harf girişi
                    if guessLetter in "ıöüğşç":
                        print("Lütfen türkçe karakter girmeye denemeyiniz...")
                        continue
                    else:
                        break
                if guessLetter in userInputLetter:
                    print("Girilen harfleri girmeye denemeyiniz...")
                    userGuessRight -= 1
                elif guessLetter in word:
                    nLoudLetter = 0 # Sesli harflerin sayısını tutan sayac
                    nQuiteLetter = 0 # Sessiz harflerin sayısını tutan sayac
                    for i in range(len(word)):
                        if i in clueLetterIndex:
                            continue
                        else:
                            if guessLetter == word[i]:
                                secretWord = secretWord[:i] + guessLetter + secretWord[i+1:]
                                if guessLetter in "aeiou":
                                    nLoudLetter += 1
                                elif guessLetter in "bcdfghjklmnpqrstvwxyz":
                                    nQuiteLetter += 1
                                if guessLetter not in userInputLetter:
                                    userInputLetter += guessLetter + ","
                                clueLetterIndex.append(i)
                    userPoint += (4*nLoudLetter) + (3*nQuiteLetter)
                elif guessLetter not in word:
                    print("Girdiğiniz harf kelimenin içinde yok lütfen başka bir harf deneyiniz...")
                    userGuessRight -= 1
                    userPoint -= 5
                if userGuessRight == 0:
                    print(word.center(150, " "))
                    print(("Kelimeyi maalesef bilemediniz. Üzgünüm :(").center(150, " "))
                    exit()
                elif secretWord == word:
                    if userGuessRight == GuessRight:
                        userPoint += 5
                    print(secretWord.center(150, " "))
                    print(("Kelime tahminizi bildiniz. Tebrikler!!! :)").center(150, " "))
                    print("     Puan: {}\n     Tahmin Hakkı: {}\n     Girilen Harfler: {}".format(userPoint,userGuessRight,userInputLetter))
                    gamenumber += 1
                    indexlist.append(randomIndex)
                    break
            elif choose == 2:
                userInputWord = input("Kelime giriniz: ")
                if userInputWord == word:
                    nLoudLetter = 0
                    nQuiteLetter = 0
                    for i in range(len(word)):
                        if i not in clueLetterIndex:
                            if userInputWord[i] in "aeiou":
                                nLoudLetter += 1
                            elif userInputWord[i] in "bcdfghjklmnpqrstvwxyz":
                                nQuiteLetter += 1
                    userPoint += (4*nLoudLetter) + (3*nQuiteLetter)
                    if userGuessRight == GuessRight:
                        userPoint += 5
                    print(word.center(150, " "))
                    print(("Kelime tahminizi bildiniz. Tebrikler!!!").center(150, " "))
                    print("     Puan: {}\n     Tahmin Hakkı: {}\n     Girilen Harfler: {}".format(userPoint,userGuessRight,userInputLetter))
                    gamenumber += 1
                    indexlist.append(randomIndex)
                    break
                else:
                    print("Girdiğiniz kelime eşleşmiyor lütfen başka bir kelime giriniz.")
                    userPoint -= 5
                    userGuessRight -= 1
    elif action == 2:
        exit()
    else:
        continue