import pandas as pd # untuk pembuatan dataframe
import sys # untuk melakukan exit program

list_pesanan = [] # untuk input data pesanan
list_jumlah = [] # untuk input jumlah pesanan
list_harga = [] # untuk input harga pesanan
list_pembayaran = [] # untuk hasil jumlah * harga pesanan

class Transaction(object):
    
    
    def __init__(self):
        """Function tidak digunakan dan hanya dilewatkan."""
        pass
        
        
    def Calculasi(self):
        """Function ini memberikan user memilih untuk memasukan pesanan, 
        menghapus pesanan, menambahkan pesanan, pengecekan pesanan atau 
        membatalkan pesanan sesuai kode yang disediakan dan jumlah proses 
        yang diinginkan, jika kode yang dimasukan salah maka user diminta 
        validasi kode hingga benar dan jika ingin membatalkan proses user 
        dapat pilih "cancel" lalu proses berhenti. data tersebut dimasukan ke dalam list yang 
        sudah disediakan sebelumnya, kemudian list tersebut dibuat ke 
        dalam dictionary dan mengubahnya ke dalam bentuk dataframe."""
        
        jumlah_pesanan = int(input("Anda mau pesan berapa item ? : "))
        for i in range(jumlah_pesanan):
            self.nama_item = str(input("Masukan pesanan: "))
            self.jumlah_item = int(input("Total per/pcs: "))
            self.harga_item = int(input("Masukan harga item: "))
            self.hitung = self.jumlah_item * self.harga_item            
            list_pesanan.append(self.nama_item)
            list_jumlah.append(self.jumlah_item)
            list_harga.append(self.harga_item)
            list_pembayaran.append(self.hitung)
        dict_transaksi = {'Pesanan' : list_pesanan,
                          'Jumlah pesanan':list_jumlah,
                          'Harga pesanan':list_harga, 
                          'Total Pembayaran' : list_pembayaran}          
        tabel_transaksi = pd.DataFrame(dict_transaksi)    
        print(tabel_transaksi)
        
        print("=========Cek Pesanan========")
        print("Keterangan : yes adalah mengganti pesanan")
        print("Keterangan : no adalah tidak ada yang diubah")
        print("Keterangan : Newlist adalah membuat kolom baru")
        print("Keterangan : cancel adalah pembatalan proses")
        
        while True:
            try :
                kode_pengecekan = str(input("Pengecekan Pesanan ?  "))         
                if kode_pengecekan == "yes":
                    jumlah_index = int(input("Masukan jumlah index yang akan diganti : "))
                    for i in range(jumlah_index):
                        print("Masukan index untuk menghapus pesanan")
                        self.pesanan = int(input())
                        list_pesanan.pop(self.pesanan)
                        print("Masukan pesanan baru")
                        self.pesanan = str(input())
                        list_pesanan.append(self.pesanan)

                        print("Masukan index untuk menghapus jumlah pesanan ")
                        self.jumlah = int(input())
                        list_jumlah.pop(self.jumlah)
                        print("Masukan jumlah baru")
                        self.jumlah = int(input())
                        list_jumlah.append(self.jumlah)

                        print("Masukan index untuk menghapus harga pesanan")
                        self.harga = int(input())
                        list_harga.pop(self.harga)
                        print("Masukan harga baru")
                        self.harga = str(input())
                        list_harga.append(self.harga)


                        print("Masukan index untuk menghapus Total Pembayaran")
                        self.hitung = int(input())
                        list_pembayaran.pop(self.hitung)
                        print("Masukan jumlah pesanan sesuai inputan sebelumnya untuk hasil total pembayaran")
                        self.jumlah = int(input())
                        print("Masukan harga pesanan sesuai inputan sebelumnya untuk hasil total pembayaran")
                        self.hitung = int(input())
                        self.total = self.hitung * self.jumlah
                        list_pembayaran.append(self.total)

                        tabel_transaksi = pd.DataFrame(dict_transaksi)
                        print(tabel_transaksi)  
                    break;
                    
                elif kode_pengecekan == "Newlist": 
                        jumlah_list = int(input("Masukan jumlah list baru yang akan dibuat : "))
                        for i in range(jumlah_list):
                            print("Masukan list baru untuk pesanan !")
                            pesanan_baru=str(input())
                            print("Masukan list baru untuk jumlah pesanan !")
                            jumlah_baru=int(input())
                            print("Masukan list baru untuk harga pesanan !")
                            harga_baru=int(input())
                            list_pesanan.append(pesanan_baru)
                            list_jumlah.append(jumlah_baru)
                            list_harga.append(harga_baru)
                            print("Masukan jumlah pesanan sesuai inputan sebelumnya untuk hasil total pembayaran")
                            self.jumlah = int(input())
                            print("Masukan harga pesanan sesuai inputan sebelumnya untuk hasil total pembayaran")
                            self.hitung = int(input())
                            self.total = self.hitung * self.jumlah
                            list_pembayaran.append(self.total)
                        tabel_transaksi = pd.DataFrame(dict_transaksi)    
                        print(tabel_transaksi)
                        break;
                        
                elif kode_pengecekan == "no" :
                    print("Ke Proses Selanjutnya!")
                    tabel_transaksi = pd.DataFrame(dict_transaksi)    
                    print(tabel_transaksi)
                    break;
                    
                elif kode_pengecekan == "cancel":
                    sys.exit("Pembatalan Proses...")
                    
                else :
                    print("Inputan Kode Salah, Lihat kode di Cek Pesanan !")
                    
            except ValueError:
                continue
             
            
    def Delete_rows(self):
        """Function ini kelanjutan dari function sebelumnya yang
         bertujuan untuk melakukan penghapusan user dengan cara memilih 
         row sesuai jumlah yang diinginkan dan bisa juga tidak dihapus. 
         Jika user ingin membatalkan pesanan dapat memilih "cancel" lalu 
         proses berhenti."""
        
        while True:
            try :        
                kode_delete = str(input("Apakah ada rows yang ingin di hapus ?(yes/no/cancel) : "))
                if kode_delete == "yes":
                    jumlah_rows = int(input("Berapa rows yang ingin di hapus ? : "))
                    for i in range(jumlah_rows):
                        nomor_index = int(input("Masukan index!"))
                        list_pesanan.pop(nomor_index)
                        list_jumlah.pop(nomor_index)
                        list_harga.pop(nomor_index)
                        list_pembayaran.pop(nomor_index)
                    break;
                    
                elif kode_delete == "no":
                    print("Ke Proses Selanjutnya!")
                    break;
                    
                elif kode_delete == "cancel":
                    sys.exit("Pembatalan Proses...")
                    
                else :
                    print("Inputan Kode Salah, Lihat kode di Cek Pesanan !")
                    
            except ValueError:
                continue  
            
            
    def reset(self):
        """Function ini kelanjutan dari function sebelumnya yang
         bertujuan untuk reset semua pesanan dan automatis proses berhenti."""
        
        dict_transaksi = {'Pesanan' : list_pesanan,
                          'Jumlah pesanan':list_jumlah,
                          'Harga pesanan':list_harga, 
                          'Total Pembayaran' : list_pembayaran}
        tabel_transaksi = pd.DataFrame(dict_transaksi)
        
        while True:
            try : 
                kode_clear = str(input("Apakah Anda ingin membatalkan atau menghapus semua pesanan ? (yes/no"))
                if kode_clear == "yes":
                    dict_transaksi.clear()                      
                    sys.exit("Pesanan telah dihapus semua atau membatalkan pesanan, Sistem automatis berhenti")
                    break;
                    
                elif kode_clear == "no":                   
                    print("Terimakasih atas Pembeliannya!")
                    break;
                    
                else :
                    print("Inputan Kode Salah ! input ulang kode")
                    
            except ValueError:
                continue
            
            
    def cek_out(self):
        """Function ini kelanjutan dari function sebelumnya yang
         bertujuan untuk melihat pesanan user yang telah dibuat."""
        
        dict_transaksi = {'Pesanan' : list_pesanan,
                          'Jumlah pesanan':list_jumlah,
                          'Harga pesanan':list_harga, 
                          'Total Pembayaran' : list_pembayaran}
        tabel_transaksi = pd.DataFrame(dict_transaksi)
        
        while True:
            try :
                kode_periksa = str(input("Apakah ingin periksa pesanan anda ? (yes/no/cancel)"))
                if kode_periksa == "yes":
                    print("List Pesanan baru !")
                    print (tabel_transaksi)
                    break;
                    
                elif kode_periksa == "no":
                    break;
                    
                elif kode_periksa == "cancel":
                    sys.exit("Pembatalan Proses...")  
                    
                else :
                    print("Inputan Kode Salah ! input ulang kode")
                    
            except ValueError:
                continue
                
                
    def cek_diskon(self):
        """Function ini kelanjutan dari function sebelumnya dan proses trakir yang
         bertujuan untuk melihat apakah user mendapatkan diskon? proses perhitungannya
         jumlahkan semua kolom pada tabel(pembayaran) lalu hasil tersebut dimasukan kedalam
         variabel baru = Total_belanja. Jika pesanan > 200_000 maka diskon 5%, pesanan > 300_000
         maka diskon 8%, dan pesanan > 500_000 diskon 10%. Perhitungannya yaitu Total harga pesanan
         * diskon, kemudian hasilnya di kurangkan dengan total harga sebelumnya."""
        
        self.name = str(input("Atas Nama ?"))
        dict_transaksi = {'Pesanan' : list_pesanan,
                          'Jumlah pesanan':list_jumlah,
                          'Harga pesanan':list_harga, 
                          'Total Pembayaran' : list_pembayaran}
        tabel_transaksi = pd.DataFrame(dict_transaksi)
        Total_belanja = tabel_transaksi['Total Pembayaran'].sum()
        
        while True:
            try :
                kode_diskon = str(input("Cek diskon anda ?(yes) "))
                if kode_diskon == "yes":
                    if Total_belanja > 200_000 and Total_belanja <= 300_000:
                        diskon = Total_belanja * 0.05
                        diskon_total = Total_belanja - diskon
                        print(f'Pembeli a/n : {self.name} Selamat Anda Mendapatkan Diskon Sebesar 5 %')
                        print(f'Harga yang anda bayar adalah Rp. {diskon_total}')
                        return tabel_transaksi
                        break;
                        
                    elif Total_belanja > 300_000 and Total_belanja <= 500_000:
                        diskon = Total_belanja * 0.08
                        diskon_total = Total_belanja - diskon
                        print(f'Pembeli a/n : {self.name} Selamat Anda Mendapatkan Diskon Sebesar 8 %')
                        print(f'Harga yang anda bayar adalah Rp. {diskon_total}')
                        print(tabel_transaksi)
                        return tabel_transaksi
                        break;
                        
                    elif Total_belanja > 500_000:
                        diskon = Total_belanja * 0.1
                        diskon_total = Total_belanja - diskon
                        print(f'Pembeli a/n : {self.name} Selamat Anda Mendapatkan Diskon Sebesar 10 %')
                        print(f'Harga yang anda bayar adalah Rp. {diskon_total}') 
                        return tabel_transaksi
                        break;
                        
                    else :
                        print(f'Pembeli a/n : {self.name} Sayang Sekali Anda Belum Mendapatkan Diskon')
                        print('Terimakasih Sudah belanja!') 
                        return tabel_transaksi
                else :
                    print("Inputan Kode Salah ! input ulang kode")
                    
            except ValueError:
                continue       
                        
                    
            """Di bawah ini merupakan proses pemanggilan class dan fuction yang telah dibuat."""  
            
            
calculasi_pesanan = Transaction()
calculasi_pesanan.Calculasi()
hapus_index_kolom = Transaction()
hapus_index_kolom.Delete_rows()
hapus_semua_kolom = Transaction()
hapus_semua_kolom.reset()
periksa_pesanan = Transaction()
periksa_pesanan.cek_out()
diskon = Transaction()
diskon.cek_diskon()