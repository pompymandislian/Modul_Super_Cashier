<h1> Super Cashier Project </h1>
Super Cashier Sederhana yang dibuat menggunakan bahasa pemerograman python 

<h3> Latar Belakang Problem </h3>
Terdapat perusahaan supermarket besar yang terkenal di kota Malang, owner berpikir untuk memperluas marketnya dengan memudahkan pelanggannya agar tidak perlu langsung datang ke supermarket untuk membeli produknya. Owner perusahaan ingin meningkatkan perusahaannya dengan cara membuat sistem kasir yang lebih modern dan nantinya customer dapat membeli barang tersebut dari jarak jauh. Owner berkeinginan customer dapat memasukan nama pesanan, jumlah pesanan, dan harga pesanan. Maka owner tersebut mencari programmer untuk membuatkan sistem yang disebut "self-service" agar keinginannya tercapai. Dari latar belakang problem tersebut maka project ini dibuat untuk kebutuhan supermarket.

<h3> Tujuan Pengerjaan Project (requirements) </h3>
Membuat sistem kasir sederhana yang dapat melakukan : 
<p>
</li><li> Membuat inputan oleh user : nama pesanan, jumlah pesanan, dan harga pesanan 
</li><li> Membuat inputan pengecekan pesanan oleh user : Menambahkan, mengganti, dan membatalkan pesanan
</li><li> Mengoreksi pesanan oleh user : Menghapus 1 baris atau lebih (rows) berdasarkan index
</li><li> Menghapus semua pesanan oleh user jika ingin dibatalkan atau memesan ulang
</li><li> Menampilkan pesanan yang telah dibuat oleh user
</li><li> Pengecekan diskon yang didapatkan oleh user

<h3> Alur Program / FlowChart </h3>
![Blank diagram](https://user-images.githubusercontent.com/57421096/202975733-137065b6-112c-497a-a96e-f47cb296e862.png)


<h3> Penjelasan Code!</h3>
</li><li> Class Transaction untuk mencangkup semua function program
</li><li> Function __init__ sebagai pendefinisian sebuah atribut
</li><li> Function calculasi memberikan user memilih untuk memasukan pesanan, menghapus pesanan, menambahkan pesanan, pengecekan pesanan atau membatalkan pesanan sesuai kode yang disediakan dan jumlah proses yang diinginkan, jika kode yang dimasukan salah maka user diminta validasi kode hingga benar dan jika ingin membatalkan proses user dapat pilih "cancel" lalu proses berhenti. data tersebut dimasukan ke dalam list yang sudah disediakan sebelumnya, kemudian list tersebut dibuat ke 
dalam dictionary dan mengubahnya ke dalam bentuk dataframe.
</li><li> Function delete_rows bertujuan untuk melakukan penghapusan oleh user dengan cara memilih row sesuai jumlah yang diinginkan dan bisa juga tidak dihapus. 
Jika user ingin membatalkan pesanan dapat memilih "cancel" lalu proses berhenti.
</li><li> Function reset yang bertujuan untuk reset semua pesanan dan automatis proses berhenti.
</li><li> Function ini kelanjutan dari function sebelumnya yang bertujuan untuk melihat pesanan user yang telah dibuat.
</li><li> Function ini bertujuan untuk melihat apakah user mendapatkan diskon? proses perhitungannya jumlahkan semua kolom pada tabel(pembayaran) lalu hasil tersebut dimasukan kedalam variabel baru = Total_belanja. Jika pesanan > 200_000 maka diskon 5%, pesanan > 300_000 maka diskon 8%, dan pesanan > 500_000 diskon 10%. Perhitungannya yaitu Total harga pesanan * diskon, kemudian hasilnya di kurangkan dengan total harga sebelumnya.

