print("Vucut Kitle Endeksi")
boy = float(input("Boy (m):"))
kilo = float(input("Kilo (kg):"))

endeks = kilo/(boy*boy)


if endeks <=18:
    print("\n Zayıfsınız VKİ:{}".format(endeks))
elif endeks > 18 and endeks<=25 :
    print("\n Normal VKİ:{}".format(endeks))
elif endeks > 25 and endeks <=30:
    print("\n Fazla Kilolu VKİ:{}".format(endeks))
elif endeks > 30 :
    print("\n Şişman VKİ:{}".format(endeks))
