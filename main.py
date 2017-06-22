i = 0
kategori = "RENK"

class dewey():
    def __init__(self, i, kategori):
        self.i = i
        self.kategori = input("Dewey Onlu Sistemi'ne göre kategori numarasını giriniz: ")
        dewey.siniflama_numarasi(self)
    def siniflama_numarasi(self):
        t = "{}.{}".format(self.kategori,self.i)
        self.i += 1
        dewey.kitap_hakkinda_bilgi(t)
    def kitap_hakkinda_bilgi(t):
        adi = input("Kitabın adın giriniz: ")
        yazar = input("Yazarın adını, soyadını giriniz[Yazarı belli değilse direk ENTER'a basınız]: ")
        yayin_yili = input("Kitabın basım yılını giriniz: ")
        dewey.siniflandirma_kodu(adi, yazar, t, yayin_yili)
    def siniflandirma_kodu(adi, yazar, t, yayin_yili):
        if yazar == "":
            sinif_kodu = adi[0] + adi[1] + adi[2]
        else:
            x = yazar.split(" ")[-1]
            sinif_kodu = x[0] + x[1] + x[2]
        dewey.outline(t, sinif_kodu, yayin_yili)
    def outline(t, sinif_kodu, yayin_yili):
        if kategori[0] == "0":
            renk = "\x1b[0;30;44m" + "|  RENK  |" + "\x1b[0m"
        elif kategori[0] == "1":
            renk = "\x1b[7;35;47m" + "|  RENK  |" + "\x1b[0m"
        elif kategori[0] == "2":
            renk = "\x1b[7;34;47m" + "|  RENK  |" + "\x1b[0m"
        elif kategori[0] == "3":
            renk = "\x1b[6;30;46m" + "|  RENK  |" + "\x1b[0m"
        elif kategori[0] == "4":
            renk = "\x1b[0;30;46m" + "|  RENK  |" + "\x1b[0m"
        elif kategori[0] == "5":
            renk = "\x1b[6;30;42m" + "|  RENK  |" + "\x1b[0m"
        elif kategori[0] == "6":
            renk = "\x1b[7;36;40m" + "|  RENK  |" + "\x1b[0m"
        elif kategori[0] == "7":
            renk = "\x1b[0;32;41m" + "|  RENK  |" + "\x1b[0m"
        elif kategori[0] == "8":
            renk = "\x1b[0;30;45m" + "|  RENK  |" + "\x1b[0m"
        else:
            renk = "\x1b[7;32;40m" + "|  RENK  |" + "\x1b[0m"
        print("__________")
        print(renk)
        print("----------")
        print("|  {} |".format(t))
        print("|   {}  |".format(sinif_kodu.upper()))
        print("|  {}  |".format(yayin_yili))
        print("----------")
        print(renk)
        print("----------")
dewey(i,kategori)
