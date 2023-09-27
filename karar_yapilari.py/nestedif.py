#nested if iç içe if demektir
# havaYagisliMi=True
# HavaSogukMi=True
# if havaYagisliMi==True:
#     if HavaSogukMi==True:
#         print("ceketini giy ve şemsiyeni al ")
#     else:
#         print("şemsiyeni al ceketini giymene gerek yok")
# else:
#     print("hava güzel ceket veya şemsiye almana gerek yok ")
#if-elif-else çoklu şartlarda bu yapı kullanılır aynı zamanda gerekli durumlarda nested if de kullanılır.

#region ornek 1
"""
    - Yakıt tüketimini hesaplayan uygulama yazalım
        - Yakıt tipi kullanıcıdan alınacak benzin/dizel
        - Aracınızın 100 km.'deki ortalama yakıt tütekimi kullanıcıdan alınacak
        - Anlık yakıt kuru internetten bakılabilir
"""
# yakitTipi=input("Aracını hangi tür yakıtı kullanıyor dizel/benzin\t:")
# yakitTuk=int(input("Aracınız 100 km de ortalama ne kadar yakıt tüketiyor (litre)\t:?"))
# yakitUcretD=40.80
# yakitUcretB=39.26
# if yakitTipi=="benzin":
#     print(f"Aracınız 100 km de ortalama {round((yakitUcretB*yakitTuk),2)} tl yakıt tüketmektedir")
# else:
#     print(f"Aracınız 100 km de ortalama {round((yakitUcretD*yakitTuk),2)} tl yakıt tüketmektedir")
#endregion

#region ornek 2
# fiyatBilgisi=int(input("Alacağınız ürünün ücreti nedir?\t:"))
# kargoBedeli=7.5 
# if fiyatBilgisi<=250:
#     fiyatBilgisi+=kargoBedeli
# print(f"Ödeyeceğiniz toplam tutar{fiyatBilgisi} TL dir")

#endregion

#tek bir algoritma yok .Önemli olan en kısa ve temiz kodu yazabilmek.

#region ornek 3
# kullaniciAdi=input("Lütfen kullanıcı adınızı giriniz\t:")
# parola=int(input("Lütfen kullanıcı parolanızı giriniz\t:"))
# if kullaniciAdi=="user":
#     if parola==1234:
#         print("kullanıcı adı ve parola hatalı.tekrar deneyiniz ")
#     print("kullanıcı adı hatalı, tekrar deneyiniz")
# elif kullaniciAdi=="admin":
#     if parola==1234:
#         print("parola hatalı,tekrar deneyiniz.")
#     else:
#         print("login başarılı,sisteme girişiniz yapıldı")
#endregion
#input alırkende f string kullanabiliriz.
