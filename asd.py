def atm():
    kullaniciadi = "Burak"
    sifrem = "1234"
    bakiye = 5000
    borc = 3000
    hak = 3
    kredi = 2000
    ev = 500
    araba = 300

    while True:
        hesap = input("kullanici adinizi giriniz =")
        sifre = input("Şifrenizi girin =")
        hak -= 1
        if hesap == kullaniciadi and sifre == sifrem:
            while True:
                print(f"""

Hoşgeldin {kullaniciadi}

Bakiyeniz = {bakiye}
Borcunuz = {borc}

İşlemler:
0 - Çıkış
1 - Para Çekme
2 - Para Yatırma
3 - Para Gönderme
4 - Bakiye Sorgula
5 - Borç Yatırma
6 - Şifre Değişme
7 - Kredi Çekme
8 - Güncel Borç
9 - Kredi Limiti
10 - Ev al
""")
                islem = int(input("Yapmak istediğiniz işlem ="))
                if islem == 1:
                    while True:
                        cek = int(input("Çekmek istediğiniz miktarı girin ="))
                        if cek > bakiye:
                            print("Bakiyeniz yetersiz.")
                        else:
                                bakiye -= cek
                                print(f"{cek} TL çekildi. Kalan Bakiyeniz {bakiye}")
                                break
                elif islem == 2:
                    while True:
                        yatir = int(input("Yatırmak istediğiniz miktarı giriniz ="))
                        if yatir > 0:
                            bakiye += yatir
                            print (f"{yatir} TL yatırıldı. Güncel bakiyeniz {bakiye}")
                            break
                        else:
                            print("Geçersiz miktar")
                elif islem == 3:
                    while True:
                        gonder = int(input("Göndermek istediğiniz miktarı giriniz ="))
                        hesapNo = input("Göndermek istediğiniz hesabı giriniz =")
                        if gonder < bakiye:
                            print(f"{hesapNo} hesabına {gonder} TL miktarında para gönderilecek. Onaylıyor musunuz ?")
                            while True:
                                onay = input("E/H = ")
                                if onay == "E":
                                    bakiye -= gonder
                                    print(f"İşlem onaylandı. Güncel bakiyeniz {bakiye}")
                                    break
                                elif onay == "H":
                                    print("İşlem iptal ediliyor..")
                                    break
                                else:
                                    print("Geçersiz işlem")
                            break
                        else:
                            print("Yetersiz bakiye.")
                elif islem == 4:
                    print(f"Güncel bakiyeniz = Güncel bakiyeniz {bakiye}")
                elif islem == 5:
                    if borc > 0:
                        print(f"Mevcut borcunuz = {borc} TL.")
                        while True:
                            borcum = int(input("Yatırmak istediğiniz miktarı giriniz. ="))
                            if borcum < bakiye:
                                if borcum <= borc:
                                    bakiye -= borcum
                                    borc -= borcum
                                    print(f"{borcum} TL borç ödendi. Kalan borcunuz {borc}. Güncel Bakiye {bakiye}")
                                    break
                                else:
                                    print("Fazla yatırdınız.")
                            else:
                                print("Bakiye yetersiz..")
                    else:
                        print("Borcunuz bulunmuyor")
                elif islem == 6:
                    hakkim = 3
                    while True:
                        eskisifre: input("Mevcut şifrenizi giriniz = ")
                        hakkim
                        if eskisifre == sifrem:
                            yenisifre: input("Yeni şifrenizi giriniz = ")
                            if sifrem in yenisifre:
                                print("Yeni şifreniz eskisine çok benzer")
                            else:
                                sifrem = yenisifre
                                print("Şifreniz güncellendi.")
                                break
                        elif hakkim == 0:
                            print("Hakkınız bitti. Daha sonra tekrar deneyiniz.")
                            break
                        else:
                            print("Hatalı şifre")
                            
                elif islem == 7:
                    if kredi > 0:
                        while True:
                            kredicek = int(input("Çeknek istediğiniz miktar ="))
                            if kredicek <= kredi:
                                borc += kredicek
                                bakiye += kredicek
                                kredi -= kredicek
                                print(f"Çekilen kredi {kredicek} TL. Güncel borcunuz {borc}. Kalan kredi limiti {kredi}")
                                break
                            else:
                                print("Kredi limitini aştınız.")
                    else:
                        print("Krediniz kalmadı.")
                elif islem == 8:
                    print(f"Güncel borcunuz = {borc} TL")

                elif islem == 9:
                    print(f"Kredi limitiniz = {kredi} TL")   
                elif islem == 10:
                    if ev < bakiye:
                        print(f"Hesabınızdan {ev} TL çekilecek onaylıyor musunuz ?")
                        while True:
                            onay1 = input("Y/N = ")
                            if onay1 == "Y":
                                bakiye -= ev
                                print(f"İşlem onaylandı. Güncel bakiyeniz {bakiye}")
                                break

                            elif onay1 == "N":
                                print("İşlem iptal ediliyor..")
                                break
                            

                    else:
                        print("Yetersiz bakiye")

                        






                elif islem == 0:
                    print("Çıkış yapılıyor")
                    break
            break
        elif hak == 0:
            print("Hakkınız bitti. Çıkış yapılıyor..")
            break
        elif hesap != kullaniciadi:
            print(f"Kullanıcı adı hatalı. Kalan hakkınız {hak}")
        elif sifre != sifrem:
            print(f"Hatalı şifre. Kalan hakkınız {hak}")
                
atm()    