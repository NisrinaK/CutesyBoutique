# ⚙️ **USAGE**<br>
You can access the live web application directly from the link below:
[LINK TO WEBPAGE](http://nisrina-kamilya-cutesyboutique.pbp.cs.ui.ac.id/)

<br>

# 📝 **ASSIGNMENT**<br>
**Name** : Nisrina Kamilya Nisyya <br>
**NPM** : 2306275456 <br>
**Class** : PBP A

## **TUGAS 2**<br>
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
-Pertama, saya membuat folder CutesyBoutique.
-Saya menginisialisasi virtual environment dengan nama venv (berguna untuk menyimpan library yang saya instal).
-Membuat file .gitignore untuk memastikan venv dan cache Python tidak di-push ke GitHub.
-Membuat requirements.txt untuk mendokumentasikan library yang ada di venv (di GitHub, ini berguna untuk memberitahu orang lain tentang dependensi proyek).
-Menginstal library dari requirements.txt.
-Menjalankan perintah "django-admin startproject CutesyBoutique ." untuk membuat proyek Django. Titik di akhir perintah memastikan proyek dibuat di folder ini tanpa membuat folder baru.
-Menjalankan perintah "python manage.py startapp main" untuk membuat aplikasi main, yang dalam proyek ini digunakan untuk menampilkan dan mendaftarkan produk.
-Mem-push progres ke GitHub dan PWS, lalu menambahkan allowed host agar bisa diakses secara lokal maupun melalui tautan PWS.
-Menghubungkan proyek dengan aplikasi main dengan menambahkan "main" ke INSTALLED_APPS dan memasukkan path('', include('main.urls')) ke dalam urlpatterns agar Django dapat mengakses urls.py di aplikasi main (meskipun pada tahap ini urls.py belum ada).
-Menambahkan BASE_DIR / "templates" untuk memastikan template main dapat meng-extend template base.html.
-Membuat urls.py di dalam aplikasi main untuk memetakan tampilan utama proyek dengan views.py.
-Membuat model sesuai dengan ketentuan, dan melakukan migrasi untuk memperbarui bentuk database.
-Membuat folder templates yang berisi file .html untuk tampilan web.
-Mengembangkan views.py untuk mengubah tampilan html agar dinamis, tidak statis.
-Membuat forms.py untuk merekam input yang nantinya akan disimpan ke database.
-Menjalankan server.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   ![S__37502985](https://github.com/user-attachments/assets/8e904cd8-6f58-406d-8371-6efe5baadfd9)

  File urls.py berfungsi untuk mengatur jalur permintaan dari pengguna (HTTP Request). Dalam urls.py, kita melakukan konfigurasi routing URL untuk aplikasi. File views.py bertugas untuk mendefinisikan dictionary context dalam fungsi show_main, yang kemudian akan ditampilkan di aplikasi. Fungsi show_main juga mengembalikan nilai untuk me-render tampilan Template (file HTML). File models.py digunakan untuk mendefinisikan model-model database yang digunakan dalam aplikasi. Data dari database hanya dapat diakses melalui models.py dan tidak boleh langsung dari views.py. Jadi, jika views.py membutuhkan data dari database, data tersebut harus diambil melalui models.py. File HTML digunakan untuk menampilkan data dan tampilan antarmuka kepada pengguna.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
	Git adalah sistem kontrol versi terdistribusi yang sangat penting dalam pengembangan perangkat lunak. Fungsinya adalah untuk melacak perubahan dalam kode, memungkinkan beberapa pengembang untuk bekerja secara bersamaan tanpa mengganggu satu sama lain. Dengan Git, pengembang dapat membuat cabang (branch) untuk mengembangkan fitur baru atau memperbaiki bug secara terpisah dari versi utama (main branch), yang memudahkan pengelolaan perubahan. Git juga memungkinkan rollback atau pengembalian ke versi sebelumnya jika terdapat kesalahan. Selain itu, Git memfasilitasi kolaborasi tim dengan memadukan perubahan dari berbagai kontributor secara efisien dan memastikan bahwa riwayat perubahan kode terdokumentasi dengan baik.


4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
	Django sering dijadikan permulaan dalam pembelajaran pengembangan perangkat lunak karena menawarkan pendekatan yang "batteries included," di mana framework ini menyediakan banyak fitur siap pakai yang memudahkan pemula memahami konsep-konsep dasar web development. Django dirancang dengan arsitektur Model-View-Template (MVT), yang membantu pemula memahami cara memisahkan logika bisnis, data, dan tampilan secara terstruktur. Selain itu, Django memiliki dokumentasi yang sangat lengkap dan komunitas yang besar, sehingga banyak sumber belajar yang tersedia. Django juga mempromosikan praktik pengkodean yang baik, seperti keamanan, skalabilitas, dan manajemen database, sehingga menjadi fondasi yang baik bagi pemula untuk mengembangkan proyek dengan standar yang tinggi.


5. Mengapa model pada Django disebut sebagai ORM?
	Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena menyediakan sebuah cara untuk berinteraksi dengan database menggunakan objek-objek Python alih-alih menulis SQL secara langsung. ORM memungkinkan konversi data antara sistem database relasional (yang menggunakan tabel) dan objek Python (yang menggunakan class dan instance).



# 📝 **ASSIGNMENT**<br>
**Name** : Nisrina Kamilya Nisyya <br>
**NPM** : 2306275456 <br>
**Class** : PBP A

## **TUGAS 3**<br>

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? Data delivery adalah elemen penting dalam pengoperasian sebuah platform karena mendukung pertukaran data yang efisien, interaksi real-time, keamanan, sinkronisasi, dan pengalaman pengguna yang lancar. Tanpa sistem data delivery yang baik, platform akan kesulitan dalam memberikan layanan yang optimal dan responsif kepada penggunanya.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML? Menurut Saya, JSON lebih baik dibandingkan dengan XML, dikarnakan JSON lebih sederhana dan lebih fleksibel . XML lebih kompleks dan kurang fleksibel. JSON mendukung angka, objek, string, dan array Boolean. XML mendukung semua tipe data JSON dan tipe tambahan seperti Boolean, tanggal, gambar, dan namespace.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut? Method is_valid() pada form Django digunakan untuk memvalidasi data yang dikirimkan melalui form. Fungsinya adalah untuk memastikan bahwa data yang dimasukkan pengguna sesuai dengan aturan yang telah ditetapkan dalam form.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang? csrf_token diperlukan untuk melindungi aplikasi Django dari serangan CSRF yang dapat menyebabkan eksekusi permintaan berbahaya tanpa izin pengguna. Tanpa csrf_token, aplikasi rentan terhadap penyalahgunaan kredensial atau sesi pengguna, yang dapat digunakan oleh penyerang untuk melakukan tindakan yang tidak sah atas nama pengguna.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).




![Screenshot 2024-09-18 062827](https://github.com/user-attachments/assets/acfb61c2-531c-4971-8777-485f29d0604e)

![Screenshot 2024-09-18 062846](https://github.com/user-attachments/assets/82ec8fc2-2088-4e56-980d-997107d3b5fe)

![Screenshot 2024-09-18 071744](https://github.com/user-attachments/assets/7c6b7517-bf59-443e-b881-679aca80c614)

![Screenshot 2024-09-18 071804](https://github.com/user-attachments/assets/97fdcb34-c3c5-40bb-90da-f297b6c90185)




