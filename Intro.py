print("Selamat datang di restoran kami!")

while True:
    kode = input("Reservasi atas nama siapa?: ")

    if kode == "Arundaffa Nahara":
        print("Selamat datang! Anda adalah tamu khusus, silahkan lihat menu restoran!\n")
        break
    else:
        print(
            "Maaf, mungkin anda tidak terdaftar, atau ada kesalahan penulisan pada nama.\n")

print("Menu restoran:")
print("1. Mont-Blanc  - Rp60.000")
print("2. Confit de Canard  - Rp120.000")
print("3. Foie Gras - Rp80.000")
print("4. Keluar")

total = 0

while True:
    pilihan = input("\nPilih menu: ")

    if pilihan == "1":
        print("Anda memilih Mont-Blanc.")
        total += 60000
    elif pilihan == "2":
        print("Anda memilih Confit de Canard.")
        total += 120000
    elif pilihan == "3":
        print("Anda memilih Foie Gras.")
        total += 80000
    elif pilihan == "4":
        print("\nTerima kasih sudah berkunjung!")
        break
    else:
        print("Pilihan tidak valid, silakan pilih 1-4.")

print(f"\nTotal yang harus dibayar: Rp{total}")
print("Sampai jumpa!")
