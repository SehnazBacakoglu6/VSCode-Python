#sürekli tekrarlayan işlemler var ise loop(döngü) kullanılır.
#Döngü içerisindeki işlem yapıldıktan sonra sayaçı arttırmaya dikkat.Aksi akdirde sonsuz döngüye sebep olur [başlangıç-bitiş-artış miktarı]!!
#infinite loop belleği yorar.

# i=0
# while i<5:
#     print(i)
#     i+=1
    
#başka bir değişken atayıp,döngüyü o değiken ile kontrol edebiliriz.
#region örnek önemli
cif=0
tek=0
cift=0
tekt=0
sayi=int(input("Lütfen sayı giriniz,çıkmak için 0 \t:"))
while sayi!=0:
    if sayi%2==0:
        cift+=sayi
        cif+=1
        sayi=int(input("Lütfen sayı giriniz,çıkmak için 0 \t:"))

    else:
        tekt+=sayi
        tek+=1
        sayi=int(input("Lütfen sayı giriniz,çıkmak için 0 \t:"))

    if sayi==0 :
        break
print(f"Girdiğiniz tek sayıların toplamı {tekt} {tek} adet tek  sayı girdiniz, girdiğiniz çift sayıların toplamı {cift} {cif} adet çift sayı dır")
#endregion