print("\t\tKÖK ALICI")

def kok(sayi, kuvvet):
    return pow(sayi, 1/kuvvet)


while True:
    s = input("Kökünü almak istediğiniz sayıyı giriniz:\nÇıkmak için q'ya basınız.")
    if s != "q":
        try:
            s = float(s)
            k = input(f"{s} sayısının kaçıncı kuvvetini alacaksınız: ")
            k = float(k)
            sonuc = kok(s, k)
            print(sonuc)
        except ValueError:
            print("Lütfen bir sayı değer giriniz.")
    else:
        break