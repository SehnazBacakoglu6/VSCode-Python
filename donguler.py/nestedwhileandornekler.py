# nested while iç içe while döngüsüdür
#region ornek1 
# i = 0
# j = 0
# while i < 3:
#     while j < 3:
#         print(f"{i} {j} ,end=" " ")
#         j += 1
#     j = 0 #çok önemli!
#     i += 1
#     print() #satır yapısı oluşturmak için 
#endregion
#region ornek2
"""
. . . . . . . . . .  
. . . . . . . . . .  
. . . . . . . . . .  
. . . . . . . . . .  
. . . . . . . . . .  
. . . . . . . . . .  
. . . . . . . . . .  
. . . . . . . . . .  
. . . . . . . . . .  
. . . . . . . . . .  

"""
i=0
j=0
while i<10:
    while j<10:
        print(".",end=" ")
        j+=1
    j=0
    i+=1
    print()#alt satıra alabilmesi için 
#endregion
#sonsuz döngüyü terminal de kırmak için ctrl+c 
# region ornek 3
# i=0
# while i<5:
#     print("*",end="\n")
#     i+=1
# endregion
# region ornek 4
# i = 0
# while i < 100:
#     if i % 2 != 0:
#         print(i,end=" ")
#     i += 1
# endregion
# region faktöriyelin değerini karşısına yazdırma
# i=1
# sonuc=1
# while i<6:
#     sonuc*=i
#     print(i,end="\t")
#     print(sonuc)
#     i+=1
# endregion
# region 1 den 100 e kadar 7 ye tam bölünenlerin sayısını bulan algoritma
# sayi=0
# toplam=0
# i=1
# while i<101:
#     if i%7==0:
#         toplam+=i
#         sayi+=1
#     i+=1
# print(f"Yediye tam bölünenlerin sayısı {sayi} toplamı {toplam}dır")
# endregion
#region haneleri toplamı hane sayısına eşit olan 100-999 arası tam sayıları ekrana bastıran algoritma
# i=100
# while i<1000:
#     hToplam=(i//100)+ (i%10)+(i%10)
#     if hToplam == 3:
#         print(i,end=" ")
#     i+=1

#endregion
