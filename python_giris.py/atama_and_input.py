#atama operatörü>>>>> eşittir(=) sağdaki değer soldaki değişkene ataması yapılır.
#region vki hesaplama
# kilo=80
# boy=1.68
# vki=kilo/(boy**2)
# print(vki)
# round(vki,2)
# print(f"Boyu{boy}, kilosu {kilo} olan kişinin vksi {vki}dir")
#endregion
#region değer arttırma/azaltma shortcut operatörü ile 
i=1
i+=i
i*=5
print(i)
#endregion
# region input
#input kullanıcıdan değer almaktır.
adSoyad=input("Adınıı yazınız\t:")
print("Adınız:",adSoyad)
#input da veri girşi yaptığımızda string olarak algılar.Bu yüzden tip dönüşümü yapmamız (casting) gerekiyor 
#endregion
#region casting (tip dönüşümü)
import datetime
x=datetime.datetime.today().year
dTarihi=int(input("doğum tarihinizi giriniz\t:"))
yas=x-dTarihi
print(yas)

#endregion
#concanation için aynı iki veri tipi concat yapılır>>> tip değişimi yapabilirsin!

