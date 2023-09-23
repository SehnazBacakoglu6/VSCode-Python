#Tüm satırlar sola kayılı olması lazım !!ındentation error
#cls (clear screen) terminald yazıyoruz
#Terminali kapatmak için crtl+""
# shift+ alt+f (formatters)
# py --version
# pip --version
# py -m pip install --upgrade pip
#Dosyalarını sürekli kaydet!!
print("Hello world!")
print("şehnaz","bacakoğlu") #çıktı-->> şehnaz bacakoğlu 
print() #print de argüman yazılmak zorunda değil hata vermez sadece bir boşluk verir !
print("şehnaz\nbacakoğlu\n")
print("şehnaz\tbacakoğlu")
print("şehnaz\t\tbacakoğlu") #2 tab kadar boşluk
print("İstanbul\nKadıköy\t\tİş\t\t\tMerkezi")
print("\\")
print("Selam \"Şehnaz\"") #kaçış karakteri kullanımı ( \ )
#print de mutalaka çift tırnak olmak zorunda değil örn: sayı ise
print(r"c\n") #raw kullanımı 
print('merhaba şehnaz\'ın dünyasına hoşgeldiniz')

print("Dünyanın","En","Güzel","Şehri",sep="♥",end="→")
print("İstanbul",end=".") # çıktı>>> Dünyanın♥En♥Güzel♥Şehri→İstanbul.