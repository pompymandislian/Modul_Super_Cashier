<h1> Super Cashier Project </h1>
Super Cashier Sederhana yang dibuat menggunakan bahasa pemerograman python 

<h3> Latar Belakang Problem </h3>
Terdapat perusahaan supermarket besar yang terkenal di kota Malang, owner berpikir untuk memperluas marketnya dengan memudahkan pelanggannya agar tidak perlu langsung datang ke supermarket untuk membeli produknya. Owner perusahaan ingin meningkatkan perusahaannya dengan cara membuat sistem kasir yang lebih modern dan nantinya customer dapat membeli barang tersebut dari jarak jauh. Owner berkeinginan customer dapat memasukan nama pesanan, jumlah pesanan, dan harga pesanan. Maka owner tersebut mencari programmer untuk membuatkan sistem yang disebut "self-service" agar keinginannya tercapai. Dari latar belakang problem tersebut maka project ini dibuat untuk kebutuhan supermarket.

<h3> Tujuan Pengerjaan Project </h3>
Membuat sistem kasir sederhana yang dapat melakukan : 
<p>
</li><li> Membuat inputan oleh user : nama pesanan, jumlah pesanan, dan harga pesanan. 
</li><li> Membuat inputan pengecekan pesanan oleh user : menambahkan, mengganti, dan membatalkan pesanan.
</li><li> Mengoreksi pesanan oleh user : menghapus 1 baris atau lebih (rows) berdasarkan index.
</li><li> Menghapus semua pesanan oleh user jika ingin dibatalkan atau memesan ulang.
</li><li> Menampilkan pesanan yang telah dibuat oleh user.
</li><li> Pengecekan diskon yang didapatkan oleh user.

<h3> Alur Program / FlowChart </h3>
    <img src="images/Flowchart_1.png" width="1020" height="640" />
    <img src="images/Flowchart_2.png" width="720" height="640" />

<h3> Penjelasan Code (requirements) </h3>
</li><li> Modul pandas : untuk pembuatan dataframe dan Modul sys untuk membuat sistem exit program.
</li><li> Class Transaction untuk mencangkup semua function program.
<p>
   "Class Transaction(object):"
</p>
</li><li> Function calculasi memberikan user memilih untuk memasukan pesanan, menghapus pesanan, menambahkan pesanan, pengecekan pesanan atau membatalkan pesanan sesuai kode yang disediakan dan jumlah proses yang diinginkan, jika kode yang dimasukan salah maka user diminta validasi kode hingga benar dan jika ingin membatalkan proses user dapat pilih "cancel" lalu proses berhenti. data tersebut dimasukan ke dalam list yang sudah disediakan sebelumnya, kemudian list tersebut dibuat ke dalam dictionary dan mengubahnya ke dalam bentuk dataframe.
<p>
    <img src="images/code_2.PNG" width="520" height="440" />
<p> 
    <img src="images/code_2a.PNG" width="520" height="440" />
</p>
</li><li> Function delete_rows bertujuan untuk melakukan penghapusan oleh user dengan cara memilih row sesuai jumlah yang diinginkan dan bisa juga tidak dihapus. 
Jika user ingin membatalkan pesanan dapat memilih "cancel" lalu proses berhenti.
<p>
    <img src="images/code_3.PNG" width="520" height="440" />
</p>
</li><li> Function reset yang bertujuan untuk reset semua pesanan dan automatis proses berhenti.
<p>
    <img src="images/code_4.PNG" width="520" height="440" />
</p>    
</li><li> Function cek_out bertujuan untuk melihat pesanan user yang telah dibuat.
<p>
    <img src="images/code_5.PNG" width="520" height="440" />
</p>    
</li><li> Function cek_diskon ini bertujuan untuk melihat apakah user mendapatkan diskon? proses perhitungannya jumlahkan semua kolom pada tabel(pembayaran) lalu hasil tersebut dimasukan kedalam variabel baru = Total_belanja. Jika pesanan > 200_000 maka diskon 5%, pesanan > 300_000 maka diskon 8%, dan pesanan > 500_000 diskon 10%. Perhitungannya yaitu Total harga pesanan * diskon, kemudian hasilnya di kurangkan dengan total harga sebelumnya.
<p>
    <img src="images/code_6.PNG" width="520" height="440" />
</p>
</li><li> Pemanggilan dan menjalankan semua function yang ada di dalam class Transaction.
<p>
    <img src="images/code_7.PNG" width="320" height="240" />
</p>

<h3> Cara menjalankan program </h3>
</li><li> Download semua file python yang ada di Github.
</li><li> Gunakan jupyter Notebook atau semacamnya yang mendukung file.
</li><li> Jika menjalankan menggunakan modul, upload modul terlebih dahulu di jupyter atau semacamnya. Kemudian ketik import transaksi dan run program untuk menjalankan. Jika menjalankan menggunakan codingan jupyter langsung run program.

<h3> Hasil Test Case </h3>
<ul></li><li> Pertama, sistem akan menawarkan pada user ingin belanja berapa jenis item ?, kemudian user diminta untuk memasukan nama pesanan, jumlah, dan harga sesuai keinginan user sebelumnya yang nantinya jumlah dan harga akan dikalkulasi menjadi total pembayaran per.item
<p>
    <img src="images/test_case1.PNG" width="420" height="340" />
</p> 
</li><li> Kedua, sistem menawarkan pengecekan pesanan kepada user yang terdapat beberapa pilihan kode yaitu : (yes, no, Newlist, dan cancel) jika kode yang dimasukan user salah maka sistem akan meminta validasi user untuk input kode hingga benar .
<p>
    <img src="images/tes_case1b.PNG" width="420" height="200" />
 
<ul id="tabbar"> 
    <li data-item="tab-one tab-active" data-initial="true"> Pilihan yes : sistem akan mengganti pesanan berdasarkan index dan berapa pesanan yang ingin             diganti? Disini user diminta memilih index yang ingin dihapus terlebih dahulu lalu input pesanan baru dan index yang dimasukan dimulai dari index terbesar           hingga terkecil.
<p>
    <img src="images/test_case1a.PNG" width="420" height="340" 
</p>
    <li data-item="tab-two"> Pilihan Newlist : Sistem akan menambahkan pesanan baru sesuai permintaan user (disini dapat lebih dari 1 tambahan list).
<p>
    <img src="images/test_case1b.PNG" width="420" height="340" 
</p> 
    <li data-item="tab-two"> Pilihan no : Sistem akan lanjut ke proses selanjutnya.
    <li data-item="tab-two"> Pilihan cancel : Pesanan akan dibatalkan dan sistem akan berhenti, untuk menjalankan kembali perlu dilakukan run ulang.
</ul>

</li><li> Ketiga, sistem akan menawarkan apakah user ingin menghapus 1 baris pesanan atau tidak jika ya maka user diminta row berapa atau index berapa yang mau dihapus, jika memilih no ke proses selanjutnya.
<p>
    <img src="images/test_case3.PNG" width="480" height="80" 
</p> 
</li><li> Keempat, Sistem akan menawarkan apakah mau menghapus semua kolom pesanan? jika ya maka kolom akan terhapus semua dan sistem akan berhenti.
</li><li> Kelima, Sistem menawarkan apakah ingin melihat pesanan saat ini? jika ya, maka akan menampilkan data pesanan dan jika tidak maka ke proses selanjutnya.
</li><li> keenam, Sistem akan mengkalkulasi apakah total belanja user mendapatkan diskon?.
<p>
    <img src="images/test_case6.PNG" width="480" height="170" 
</p> 

<h3> Kesimpulan </h3>
Hasil pembuatan sistem Super Cashier perusahaan supermarket tersebut dapat melakukan banyak hal yaitu : 
<p>
</li><li> User dapat memasukan pesanan sendiri tanpa harus datang ke supermarket.
</li><li> Penghapusan rows dan penggantian pesanan jika dilakukan lebih dari 2 kali sebaiknya gunakan kode cancel agar pesanan dapat dimulai ulang.
</li><li> Sistem memberikan banyak pilihan untuk meminimalisir kesalahan input oleh user yaitu : pengecekan pesanan (penambahan list, menghapus pesanan, dan cancel pesanan). 
</li><li> Untuk proses input pesanan, penambahan list, penghapusan row dan penggantian pesanan dapat dilakukan sebanyak keinginan user karena disediakan jumlah proses yang akan dilakukan.
</li><li> User dapat membatalkan atau memulai ulang sewaktu-waktu di setiap proses.
</li><li> User dapat melihat pesanan setiap proses yang telah dilakukan agar meminimalisir kesalahan input.
</li><li> Agar pemesanan terdapat a/n pemesan, maka diakhir sebelum proses selesai user diminta untuk memasukan nama.
</li><li> Proses terakhir merupakan hasil akhir apakah user mendapatkan diskon atau tidak berdasarkan jumlah pembelian, dan sistem akan menampilkan total pembayaran akhir dan juga daftar list pesanan yang telah dibeli.

<h3> Saran Perbaikan </h3>
</li><li> Programmer perlu menambahkan daftar list item apa saja yang ada disupermarket agar user tidak melakukan banyak inputan.
</li><li> Perlu penambahan sistem IoT agar dapat diakses melalui online dan membuat interface seperti API agar user lebih muda dalam melakukan proses order.
</li><li> Perbaikan lainnya yang mungkin ditemukan setelah program digunakan oleh beberapa user.

<h3> Penjelasan vidio dapat dilihat pada link dibawah ini </h3>
https://www.youtube.com/watch?v=Nq7DoYaTv18
