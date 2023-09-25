# havaDurumu="güneşli"
# if havaDurumu=="güneşli": #if içerisindeki değer sağlanıyor ise koşulun içine gir!
#     print("güneş kremini sür")

#region örnek1 

#kulanıcıdan bir sayı al ve negatif veya pozitif olup olmadığına karar ver 
sayi=int(input("Bir sayı griniz\t:"))
if sayi<0:
    print("Girdiğiniz sayı negatiftir.")
elif sayi>0:
    print("Girdiğiniz sayı pozitiftir")

else:
    print("Girdiğiniz sayı 0 dır.")

#endregion 

#region ornek 2
kullaniciAdi=input("Lütfen kullanıcı adınızı giriniz\t:")
if kullaniciAdi!="user" :
    print("Admin paneline giriş yetkiniz bulunmamaktadır")

#endregion

#if bloğu kesinlikle boş geçilemez ! pass kullanabilirsin (geçici olarak hata vermesini engellemek adına )
#break point kullanımı hatanın nerden kaynaklığını öğrenmek adına önemli!

#region en büyük sayıyı bulma örneği 
sayi1=int(input("bir sayı giriniz\t:"))
sayi2=int(input("bir sayı giriniz\t:"))
sayi3=int(input("bir sayı giriniz\t:"))
eb=sayi1
if sayi2>eb:
    eb=sayi2
if sayi3>eb:
    eb=sayi3
print(f"En büyük sayı {eb}'dir")

#endregion

#else yapısı if clause un false olduğu durumlarda çalışır 

#region tek-çift algoritması
sayi=int(input("Lütfen bir sayı giriniz\t:"))
if sayi%2 == 0:
    print("Sayı çiftdir")
else:
    print("sayı çift değildir,tektir")
    #endregion 
