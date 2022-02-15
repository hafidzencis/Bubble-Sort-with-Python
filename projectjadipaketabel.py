from prettytable import PrettyTable #digunakan untuk ketika file tercompile maka data tersebut muncul dengan bentuk tabel 
import pandas as pan #digunakan untuk mengimpor data excel ke python

data_excel = pan.read_excel(r'./pertandingan-pialadunia2018.xlsx') #membaca file excel
data_list = data_excel.values.tolist() #mengubah data_excel ke bentuk list


while True: #perulangan digunakan untuk membuat program
    print("=====Program melakukan sorting dari tempat pertandingan dan jadwal pertandingan=====")

    print("Masukkan angka 1 untuk melakukan program sorting tempat pertandingan secara ascending")
    print("Masukkan angka 2 untuk melakukan program sorting tempat pertandingan secara descending")
    print("Masukkan angka 3 untuk melakukan program sorting jadwal pertandingan secara descending")
    print("Masukkan angka 4 untuk melakukan program sorting jadwal pertandingan secara ascending")
    print("Masukkan angka 5 memberhentikan program\n")
    masuk = int(input("Masukkan angka : ")) # digunakan untuk inputan user

    class pialadunia: #kelas piala dunia ini digunakan untuk memecah data 
        def __init__(self,ambil):
            self.negara = ambil[0] #pertandingan dimasukkan ke indeks 0
            self.tempat = ambil[1] #tempat pertandingan dimasukkan ke indeks 1
            self.jadwal = ambil[2] #jadwal pertandingan dimasukkan ke indeks 2

                
    tabelPD = PrettyTable(["Pertandingan","Tempat","Jadwal"]) #tabel dengan baris pertama digunakan untuk judul
    
    daftarpd =[] 
    for i in range(len(data_list)): #data_list lalu dimasukka  ke pialadunia lalu dipecah lalu dimasukkan ke list berbentuk daftarpd
        daftarpd.append(pialadunia(data_list[i]))

        
    if masuk == 1:
        def urut_tempat(daftar):#melakukan sorting bubble pada tempat secara ascending
            n = len(daftar)
            for i in range (n):
                for j in range(0,n-i-1):
                    if daftar[j].tempat > daftar[j+1].tempat :
                        daftar[j], daftar[j+1] = daftar[j+1], daftar[j]

        print("FeatureA mencoba featuerA merge no FF")
        urut_tempat(daftarpd)
        for i in daftarpd:
            tabelPD.add_row([i.negara,i.tempat,i.jadwal])
        print(tabelPD)
        print("\n")
    
    if masuk == 2:
        def urut_tempatbel(daftar):#melakukan sorting bubble pada tempat descending
            n = len(daftar)
            for i in range (n):
                for j in range(0,n-i-1):
                    if daftar[j].tempat < daftar[j+1].tempat :
                        daftar[j], daftar[j+1] = daftar[j+1], daftar[j]

        print("Pale pale")
        urut_tempatbel(daftarpd)
        for i in daftarpd:
            tabelPD.add_row([i.negara,i.tempat,i.jadwal])
        print(tabelPD)
        print("\n")

   
    print("Feature A")
    if masuk == 3 :
        def urut_belakang(daftar): #melakukan sorting bubble pada jadwal secara descending
            n = len(daftar)
            for i in range (n):
                for j in range(0,n-i-1):
                    if daftar[j].jadwal < daftar[j+1].jadwal :
                        daftar[j], daftar[j+1] = daftar[j+1], daftar[j]

    
        urut_belakang(daftarpd)
        for i in daftarpd:
            tabelPD.add_row([i.negara,i.tempat,i.jadwal])

        print(tabelPD)
        print("\n")

    if masuk == 4:
        def urut_depan(daftar): #melakukan sorting bubble pada jadwal secara ascending
            n = len(daftar)
            for i in range (n):
                for j in range(0,n-i-1):
                    if daftar[j].jadwal > daftar[j+1].jadwal :
                        daftar[j], daftar[j+1] = daftar[j+1], daftar[j]

        urut_depan(daftarpd)

        for i in daftarpd:
            tabelPD.add_row([i.negara,i.tempat,i.jadwal])
        print(tabelPD)
        print("\n")

    if masuk == 5 : #memberhentikan program
        break
