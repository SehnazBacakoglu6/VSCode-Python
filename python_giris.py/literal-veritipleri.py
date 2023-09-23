#region literal 
# # literal = sabit (değişmez değer)
# string =metinsel değişmez değer
# integer = tam sayı değişmez değer
# float = kayan noktalı sayı değişmez değer
# bolean = true,false türler değişmez değer
# koleksiyon,list,tuple,dictionary
#endregion
#region veri tipleri 
print(500) #integer 
print(3.14) #float
print(1.75) #float
print("şehnaz") #string
#Bolean ifade büyük harf ile başlar !


#endregion
# region type belirleme
print(type("şehnaz"))
print(type(2002))
print(type(True))
print(type(3.14)) 
# <class 'str'>  
# <class 'int'>  
# <class 'bool'> 
# <class 'float'>
#endregion
#region operatörler
# +,-,*,/ ,mod alma,** (üst alma) ,tam bölme(//)

# işlemlerde yer alan veri tiplerinden herhangi biri float ise sonucu float verir!!
#tam bölme her zaman bir küçük tamsayıya yuvarlar
#mod alma bölümde kalan kısımdır.
#endregion 
#region operatör öncelikleri

# 1-üst alma
# 2-çarpma,bölme,mod alma
# 3-toplama çıkarma
#Önceliklerden sonra soldan sağa doğru işlem yapılır.


#endregion
#region örnekler
print(2*4-(4/(3+3)+2/5))
print((3**3/(2/5))**0.5)
print((1+14/2)-15/(1+8/2))

#endregion