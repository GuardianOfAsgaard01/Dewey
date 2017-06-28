import json

with open('KitapListesi.json', 'r') as k:
    old_data = json.load(k)
i = len(old_data)


class dewey():

    def __init__(self, i, kategori, adi, yazari, yayin_yili, old_data):
        self.i = i
        self.kategori = kategori
        self.adi = adi
        self.yazari = yazari
        self.yayin_yili = yayin_yili
        self.old_data = old_data
        dewey.siniflama_numarasi(self)

    def siniflama_numarasi(self):
        t = "{}.{}".format(self.kategori, self.i+1)
        dewey.siniflandirma_kodu(self, t)

    def siniflandirma_kodu(self, t):
        if self.yazari == "":
            sinif_kodu = self.adi[0] + self.adi[1] + self.adi[2]
        else:
            x = self.yazari.split(" ")[-1]
            sinif_kodu = x[0] + x[1] + x[2]
        dewey.outline(self, sinif_kodu, t)

    def outline(self, sinif_kodu, t):
        if self.kategori[0] == "0":
            renk = "\x1b[0;30;44m" + "|  RENK  |" + "\x1b[0m"
        elif self.kategori[0] == "1":
            renk = "\x1b[7;35;47m" + "|  RENK  |" + "\x1b[0m"
        elif self.kategori[0] == "2":
            renk = "\x1b[7;34;47m" + "|  RENK  |" + "\x1b[0m"
        elif self.kategori[0] == "3":
            renk = "\x1b[6;30;46m" + "|  RENK  |" + "\x1b[0m"
        elif self.kategori[0] == "4":
            renk = "\x1b[0;30;46m" + "|  RENK  |" + "\x1b[0m"
        elif self.kategori[0] == "5":
            renk = "\x1b[6;30;42m" + "|  RENK  |" + "\x1b[0m"
        elif self.kategori[0] == "6":
            renk = "\x1b[7;36;40m" + "|  RENK  |" + "\x1b[0m"
        elif self.kategori[0] == "7":
            renk = "\x1b[0;32;41m" + "|  RENK  |" + "\x1b[0m"
        elif self.kategori[0] == "8":
            renk = "\x1b[0;30;45m" + "|  RENK  |" + "\x1b[0m"
        else:
            renk = "\x1b[7;32;40m" + "|  RENK  |" + "\x1b[0m"

        print("__________")
        print(renk)
        print("----------")
        print("|  {} |".format(t))
        print("|   {}  |".format(sinif_kodu.upper()))
        print("|  {}  |".format(self.yayin_yili))
        print("----------")
        print(renk)
        print("----------")

        new_data = {
            t : {
            'kitabin_adi' : self.adi,
            'kitabin_yazari' : self.yazari,
            'basim_yili' : self.yayin_yili
            }
        }

        self.old_data.update(new_data)

        with open('KitapListesi.json', 'w') as k:
            json.dump(old_data, k)

while True:
    print("                 ")
    print("Yeni kitap eklemek için 1'e,")
    print("Kitapları listelemek için 2'ye,")
    print("Sistemden çıkmak için Enter'a basınız.")
    print("                 ")

    e = input("Hangi işlemi yapmak istiyorsunuz? ")
    print("                 ")

    if e == "1":
        kategori = input("Dewey'e göre kategori numarasını giriniz: ")
        adi = input("Kitabın adını giriniz: ")
        yazari = input("Yazarın adını giriniz[Belli değilse boş bırakın]: ")
        yayin_yili = input("Kitabın basım yılını giriniz: ")
        dewey(i, kategori, adi, yazari, yayin_yili, old_data)

    elif e == "2":
        print(json.dumps(old_data, indent=4))

    elif e == "":
        break

    else:
        print("xxxxxxxxxxxxx")
        print("Hatalı giriş!")
        print("             ")

