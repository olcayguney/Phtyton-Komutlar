import random

listem = [1, 2, 3, 4, 5]
print(listem, "Başlangıç listesi")

# listName.append(value)    APPEND
# Listenin **sonuna** komut içerisindeki değeri ekler!
listem.append(77)
print(listem, "append")

# listName.insert(index, value)  INSERT
# Listenin girilen indexine girilen değeri ekler!
listem.insert(1, 88)
print(listem, "insert")

# listName.remove(value)  REMOVE
# Komutun içerisindeki değeri listeden siler  
# !( Birden fazla varsa sadece ilk bulduğunu siler)
listem.append(88)
print(listem, "append 88")
listem.remove(88)
print(listem, "remove 88")

# listName.pop()  POP
# Listenin **sonundaki** elemanı siler ve döndürür!
son = listem.pop()
print(listem, "pop", "çıkan:", son)

# listName.pop(index)  POP (index ile)
# Girilen indexteki elemanı siler ve döndürür!
ikinci = listem.pop(1)
print(listem, "pop(1)", "çıkan:", ikinci)

# listName.clear()  CLEAR
# Listenin tüm elemanlarını siler!
listem.clear()
print(listem, "clear")

# listName.extend([a, b, c])  EXTEND
# Listeye birden fazla eleman ekler!
listem.extend([10, 20, 30])
print(listem, "extend")

# listName.count(value)  COUNT
# Listede verilen değerden kaç tane olduğunu döndürür!
print("20 sayısı:", listem.count(20), "adet var")

# listName.index(value)  INDEX
# Verilen değerin listedeki ilk indexini döndürür!
print("30'un indexi:", listem.index(30))

# listName.sort()  SORT
# Listeyi küçükten büyüğe sıralar!
listem.sort()
print(listem, "sort")

# listName.reverse()  REVERSE
# Listeyi ters çevirir!
listem.reverse()
print(listem, "reverse")

# listName.copy()  COPY
# Listenin bir kopyasını oluşturur!
yeni_liste = listem.copy()
print(yeni_liste, "copy")




