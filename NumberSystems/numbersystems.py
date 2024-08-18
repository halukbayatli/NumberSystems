"""
Ad: Haluk
Soyad: Bayatlı
Numara: 23100011030
"""

s = "TABAN DEĞİŞTİRME PROGRAMI"
s = s.center(150, "-")
print(s)
print("     1) Onluk tabandan ikilik tabana çevirme ----> 1",
      "     2) İkilik tabandan onluk tabana çevirme ----> 2",
      "     3) Çıkmak için                          ----> 3", sep="\n")
while True:
    action = int(input("İşlem seçiniz: "))
    match action:
        case 1:
            while True:
                reverse_binary = ""
                binary = ""
                number = int(input("Sayı giriniz: "))
                if number <= 0:
                    continue
                number0 = number
                while number0 > 0:
                    remainder = number0 % 2
                    reverse_binary += str(remainder)
                    number0 //= 2
                for i in range(len(reverse_binary)):
                    binary += reverse_binary[-(i+1)]
                print("    Onluk tabanda sayı:{} ---> İkilik tabanda sayı:{}".format(number, binary))
                break
        case 2:
            while True:
                binary = input("Sayı giriniz: ")
                control = 1
                for i in binary:
                    if i not in "01":
                        control = 0
                if control == 1:
                    number = 0
                    for n in range(len(binary)):
                        number += (int(binary[-(n+1)])*2**n)
                    print("    İkilik tabanda sayı:{}  ---> Onluk tabanda sayı:{}".format(binary, number))
                    break
                else:
                    continue
        case 3:
            break
        case _:
            continue
