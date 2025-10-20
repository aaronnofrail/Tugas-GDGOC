tinggi_badan = [170, 180, 175.4, 159, 150, 185, 174]
total_tb = sum(tinggi_badan)
jumlah_mahasiswa = 7
rata_rata = total_tb/jumlah_mahasiswa

if rata_rata > 180:
    print("Tinggi badan mahasiswa kelas ini tinggi")
elif rata_rata > 170:
    print("Tinggi badan mahasiswa kelas ini rata rata")
elif rata_rata > 160:
    print("Tinggi badan mahasiswa kelas ini pendek")
