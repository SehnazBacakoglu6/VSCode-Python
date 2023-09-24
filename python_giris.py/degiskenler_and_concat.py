#değişkenler RAM de saklanır
#region değişken tanımlama
# 1-camel casing
# adSoyad="şehnaz bacakoğlu"
# sinavNotu=90
# 2-underscore casing --- alt tire rotasyonu 
# ad_soyad="şehnaz bacakoğlu"
# sinav_notu=90

#endregion
#region concat
ver="3.10.0"
os="10"
print(" windos versiyonu "+ os," python versiyonu "+ ver)

#çıktıları daha iyi hale getirir.
name="şehnaz"
print(" hoşgeldin "+ name)
#endregion
#swap için değişen ata bir değişkeni temp e ata .Sıralama algoritmalarında çoğunlukla kullanılır!!
# a=10
# b=20
# temp=a
# a=b
# b=temp

#ram de steak ve heap bölümleri vardır.steak de sayısal veri tipleri(value types) saklanır.Heap de ise object veri tipleri(list,obj,str),referans tipleri saklanır.(adres ile çalışır)
#value typeslar adres ile çalışmaz!!!!!
#pars etmek=bölmek 
#region basamaklarına ayırma sorusu
sayi=562
birler=sayi%10
onlar=(sayi%100)//10
yüzler=sayi//100
print(yüzler,onlar,birler)

#endregion
