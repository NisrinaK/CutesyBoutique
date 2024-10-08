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
   - Pertama, Saya membuat input form untuk menambahkan objek model: Menambahkan form di aplikasi Django untuk memungkinkan penambahan objek model baru. Buat form berbasis model menggunakan forms.ModelForm. Contohnya, jika kamu memiliki model Product, buat form ProductForm di berkas forms.py. Di dalam form ini, tentukan field yang sesuai dengan atribut model, seperti name, price, dan description. Kemudian, buat view di views.py untuk menangani penambahan produk baru. Pastikan dalam view ini kamu memproses form, dan jika form valid, simpan objek baru ke database.

	- Lalu, Saya menambahkan 4 fungsi views baru (XML dan JSON): Buat 4 fungsi views yang akan menampilkan data produk yang sudah ditambahkan. Dua dari fungsi tersebut harus menampilkan semua produk dalam format XML dan JSON. Fungsi pertama akan mengambil semua objek produk dari database, kemudian mengubahnya menjadi format XML menggunakan serializers.serialize('xml', ...) dan mengembalikannya dalam respons HTTP dengan content_type='application/xml'. Fungsi kedua akan melakukan hal yang sama untuk format JSON. Selanjutnya, tambahkan dua fungsi lagi untuk menampilkan produk berdasarkan ID tertentu, satu dalam format XML dan satu lagi dalam format JSON. Gunakan filter untuk mendapatkan produk berdasarkan ID, lalu kembalikan hasilnya dalam format yang sesuai.

	- Terakhir, Membuat routing URL untuk views baru: Setelah menambahkan keempat views baru, buat URL routing yang sesuai di urls.py untuk mengakses data dalam format XML dan JSON. Misalnya, tambahkan routing /xml/ untuk menampilkan semua produk dalam format XML, dan /json/ untuk menampilkan semua produk dalam format JSON. Selain itu, tambahkan URL dengan parameter ID, misalnya /xml/<int:id>/ dan /json/<int:id>/ untuk menampilkan produk berdasarkan ID dalam format XML atau JSON.



![Screenshot 2024-09-18 062827](https://github.com/user-attachments/assets/acfb61c2-531c-4971-8777-485f29d0604e)

![Screenshot 2024-09-18 062846](https://github.com/user-attachments/assets/82ec8fc2-2088-4e56-980d-997107d3b5fe)

![Screenshot 2024-09-18 071744](https://github.com/user-attachments/assets/7c6b7517-bf59-443e-b881-679aca80c614)

![Screenshot 2024-09-18 071804](https://github.com/user-attachments/assets/97fdcb34-c3c5-40bb-90da-f297b6c90185)


# 📝 **ASSIGNMENT**<br>
**Name** : Nisrina Kamilya Nisyya <br>
**NPM** : 2306275456 <br>
**Class** : PBP A

## **TUGAS 4**<br>

1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah form bawaan yang disediakan oleh Django untuk mempermudah proses pendaftaran pengguna baru. Form ini sudah terintegrasi dengan sistem otentikasi Django dan secara otomatis menyediakan input untuk username, password, serta validasi password ganda. Kelebihan utama dari UserCreationForm adalah kemudahannya dalam digunakan karena sudah terhubung langsung dengan model User Django, memiliki validasi bawaan seperti pengecekan kesesuaian password, serta mengelola keamanan dengan hashing password secara otomatis. Form ini juga fleksibel, karena dapat diperluas dengan menambahkan field lain sesuai kebutuhan aplikasi. Namun, UserCreationForm juga memiliki beberapa kekurangan. Form ini sangat mendasar dan hanya menyediakan field username dan password, sehingga jika membutuhkan field tambahan seperti email, developer harus menambahkannya secara manual. Selain itu, form ini tidak menyertakan validasi password yang lebih kompleks, seperti pengecekan kekuatan password atau validasi email, yang perlu ditambahkan secara terpisah. Form ini juga secara default menggunakan username sebagai identifikasi utama, sehingga jika ingin menggunakan email sebagai pengenal, modifikasi tambahan diperlukan. Meskipun sangat fungsional, tampilan UserCreationForm juga sederhana, sehingga developer perlu menambahkan styling untuk menyesuaikan dengan desain aplikasi.

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi dan otorisasi adalah dua konsep penting dalam keamanan aplikasi Django yang memiliki peran berbeda namun saling melengkapi. Autentikasi (authentication) adalah proses verifikasi identitas pengguna, memastikan bahwa seseorang yang mencoba masuk ke sistem adalah benar-benar siapa yang mereka klaim, biasanya melalui username dan password. Django menangani autentikasi melalui sistem login, di mana jika kredensial pengguna cocok dengan data yang tersimpan, pengguna diizinkan mengakses aplikasi. Sementara itu, otorisasi (authorization) adalah proses untuk menentukan hak akses pengguna setelah mereka terautentikasi, yaitu mengontrol apa yang boleh diakses atau dilakukan oleh pengguna tersebut. Misalnya, meskipun pengguna telah login, mereka mungkin tidak memiliki izin untuk melihat atau mengedit data tertentu, dan otorisasi memastikan mereka hanya dapat mengakses fitur yang sesuai dengan peran mereka. Keduanya sangat penting dalam menjaga keamanan aplikasi—autentikasi melindungi dari akses yang tidak sah, sedangkan otorisasi mencegah pengguna yang sah melakukan tindakan di luar izin mereka.

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies dalam konteks aplikasi web adalah file kecil yang disimpan di browser pengguna oleh server untuk menyimpan data tertentu tentang interaksi pengguna dengan situs web. Cookies memungkinkan server untuk mengenali pengguna ketika mereka mengunjungi kembali situs tersebut, mempertahankan data seperti preferensi atau status login. Di Django, cookies digunakan untuk mengelola data sesi pengguna. Django menyimpan ID sesi sebagai cookie di browser pengguna, sementara data sesi yang sebenarnya, seperti informasi login atau preferensi, disimpan di server, biasanya dalam database atau file. Saat pengguna berinteraksi dengan aplikasi, ID sesi dari cookie dikirimkan ke server untuk mencocokkan dengan data sesi yang relevan, memungkinkan Django untuk mengenali pengguna dan mempertahankan status mereka di antara permintaan HTTP. Dengan cara ini, Django memastikan pengalaman pengguna yang konsisten tanpa perlu menyimpan terlalu banyak data di browser pengguna, menjaga keseimbangan antara kemudahan penggunaan dan keamanan.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web tidak sepenuhnya aman secara default, dan ada beberapa risiko potensial yang harus diwaspadai. Cookies dapat diekspos ke berbagai jenis serangan, seperti session hijacking, di mana penyerang mencuri cookie untuk mengakses sesi pengguna tanpa otentikasi ulang, atau cross-site scripting (XSS), di mana skrip berbahaya menyuntikkan kode untuk mencuri cookie dari pengguna. Selain itu, cookies yang tidak dienkripsi atau tidak diamankan dengan baik dapat rentan terhadap man-in-the-middle attacks, di mana data cookie disadap selama transmisi. Untuk mengurangi risiko ini, penting untuk mengaktifkan opsi keamanan seperti HTTPOnly, yang mencegah akses cookie melalui JavaScript, Secure, yang memastikan cookie hanya dikirim melalui koneksi HTTPS, serta SameSite, yang membatasi pengiriman cookie ke permintaan lintas situs. Meskipun cookies adalah alat yang berguna untuk mengelola sesi dan preferensi pengguna, pengembang harus berhati-hati dan menggunakan praktik keamanan terbaik untuk mencegah eksploitasi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Saya mulai dengan menambahkan fungsi registrasi untuk memungkinkan pengguna membuat akun baru. Dengan menggunakan UserCreationForm bawaan Django, saya membuat form registrasi di views.py dan menambahkan template register.html. Pengguna bisa memasukkan username dan password, lalu jika berhasil, mereka diarahkan ke halaman login. Lalu, Saya mengimplementasikan fungsi login dengan menggunakan AuthenticationForm dari Django. Fungsi ini mengautentikasi pengguna berdasarkan input form, lalu melakukan login jika data valid. Setelah login berhasil, pengguna diarahkan ke halaman utama. Kemudian, Saya membuat fungsi logout yang menggunakan fungsi logout bawaan Django untuk menghapus sesi pengguna dan mengarahkan mereka kembali ke halaman login.
Membuat Dua Akun Pengguna dengan Masing-Masing Tiga Dummy Data:

Setelah implementasi fungsi registrasi dan login, saya membuat dua akun pengguna secara manual melalui halaman registrasi aplikasi. Setelah login ke setiap akun, saya menambahkan tiga produk dummy untuk masing-masing akun melalui fitur penambahan produk yang sudah ada.

Pada model Product, saya menambahkan relasi ForeignKey ke model User. Ini memungkinkan setiap produk yang ditambahkan terkait dengan pengguna yang membuatnya. Saya juga memodifikasi fungsi add_product di views.py agar setiap produk yang disimpan dikaitkan dengan pengguna yang sedang login.
Selanjutnya, saya memodifikasi tampilan daftar produk (product_list) sehingga hanya produk milik pengguna yang sedang login yang ditampilkan.
Menampilkan Detail Pengguna yang Logged In dan Menggunakan Cookies Last Login:

Di halaman utama, saya menampilkan detail informasi pengguna yang sedang login, seperti username, dengan menggunakan request.user.username. Selain itu, saya menambahkan cookie bernama last_login saat pengguna login. Cookie ini menyimpan waktu login terakhir pengguna, dan ditampilkan di halaman utama setiap kali mereka login.
Ketika pengguna logout, cookie last_login akan dihapus untuk menjaga konsistensi data.


# 📝 **ASSIGNMENT**<br>
**Name** : Nisrina Kamilya Nisyya <br>
**NPM** : 2306275456 <br>
**Class** : PBP A

## **TUGAS 5**<br>

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Ketika sebuah elemen HTML memiliki beberapa CSS selector yang diterapkan padanya, urutan prioritas (specificity) dari CSS selector tersebut dihitung berdasarkan aturan berikut:
- Inline Styles (misalnya, style="..." di dalam tag HTML) memiliki prioritas tertinggi.
- ID Selector (misalnya, #header) memiliki prioritas yang lebih tinggi dibandingkan class atau elemen selector.
- Class, Pseudo-class, dan Attribute Selector (misalnya, .class, :hover, [type="text"]) berada di bawah ID selector.
- Type Selector dan Pseudo-element Selector (misalnya, div, p, ::before) memiliki prioritas yang lebih rendah.
- Universal Selector (*), combinator (+, >, ~), dan negasi (:not()) memiliki prioritas terendah.
- Jika selector memiliki specificity yang sama, urutan penulisan di dalam stylesheet akan menentukan prioritas (yang terakhir ditulis akan diambil).
- Deklarasi menggunakan !important akan mengesampingkan prioritas selector, tetapi tetap mengikuti aturan spesifik lainnya.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design penting karena perangkat yang mengakses aplikasi web beragam (desktop, tablet, ponsel), dan setiap perangkat memiliki ukuran layar serta orientasi yang berbeda. Konsep ini memungkinkan tampilan web menyesuaikan secara dinamis agar user experience tetap optimal di berbagai perangkat.

-Contoh aplikasi yang menerapkan responsive design: YouTube. YouTube secara otomatis menyesuaikan tampilan videonya tergantung pada ukuran layar, baik itu di desktop, tablet, atau smartphone.
-Contoh aplikasi yang belum menerapkan responsive design: Sebuah situs web lama tanpa media queries yang tampilan desktopnya tidak disesuaikan untuk layar ponsel, seperti situs berbasis tabel tanpa fleksibilitas tata letak.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
-Margin: Jarak antara batas luar elemen dan elemen di sekitarnya. Margin tidak memengaruhi ukuran elemen itu sendiri, hanya jarak antar elemen.
-Border: Garis pembatas di sekitar elemen yang berada di antara padding dan margin. Border dapat memiliki lebar, gaya, dan warna.
-Padding: Ruang antara konten elemen dan batas dalam elemen (border). Padding memengaruhi ukuran total elemen karena menambah ruang di dalam elemen itu sendiri.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
-Flexbox: Layout yang dirancang untuk menyusun elemen dalam satu dimensi (baris atau kolom). Flexbox sangat efektif untuk mengatur item di dalam wadah yang fleksibel dan responsif, seperti membangun layout navigasi atau galeri foto yang fleksibel.
-Grid Layout: Layout yang bekerja dalam dua dimensi (baris dan kolom). Ini digunakan untuk membuat layout yang lebih kompleks dengan pengaturan area di grid seperti membuat dashboard atau tata letak halaman yang multi-kolom.
Flexbox sangat berguna untuk menyusun item yang dinamis secara linier, sedangkan grid layout ideal untuk struktur tata letak yang lebih statis dan dua dimensi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Hal pertama yang saya lakukan adalah menambahkan Tailwind CSS ke dalam aplikasi agar saya bisa melakukan styling secara lebih mudah dan efisien pada tampilan aplikasi CutesyBoutique. Tailwind memudahkan saya untuk mengatur berbagai elemen seperti grid, padding, dan shadow tanpa harus menulis banyak CSS manual.

Selanjutnya, saya membuat view di views.py untuk menangani permintaan pengeditan produk. Di sini, saya membuat template HTML yang berisi form pengeditan produk, lalu saya menggunakan data produk yang ingin diedit dan menampilkannya dalam form tersebut. Pada form ini, saya menggunakan method POST agar data yang baru dapat langsung disimpan ke database setelah pengeditan dilakukan. Saya juga menambahkan tombol "Edit" di setiap card produk yang mengarahkan pengguna ke halaman edit produk.

Untuk fitur penghapusan produk, saya membuat view tambahan di views.py yang khusus menangani permintaan penghapusan produk. Agar pengguna dapat menghapus produk dengan aman, saya menggunakan link konfirmasi di halaman daftar produk atau melalui modals. Saya juga menambahkan tombol "Delete" pada setiap card produk sehingga pengguna dapat langsung menghapus produk dengan mudah.

Dalam mengatur tampilan form login dan register, saya memanfaatkan Tailwind CSS untuk mengatur layout dan gaya agar lebih menarik. Pada halaman tambah produk, saya mendesain form agar terlihat lebih rapi. Saya juga menambahkan elemen visual seperti ikon dan warna pada input fields agar pengguna merasa lebih nyaman saat menambahkan produk baru.

Ketika tidak ada produk yang tersimpan di database, saya memastikan untuk mengeceknya di view terlebih dahulu. Jika tidak ada produk, saya menampilkan gambar ilustrasi atau emoji sedih dengan pesan "Belum ada produk yang terdaftar." Tampilan ini saya atur agar tetap menarik dan responsif menggunakan Tailwind CSS.

Jika produk sudah ada, saya membuat tampilan daftar produk menggunakan desain card yang berbeda dari tutorial. Setiap card produk menampilkan nama, deskripsi singkat, harga, serta stok yang tersedia. Saya juga menambahkan tombol edit dan delete di setiap card produk agar pengguna dapat langsung melakukan aksi terhadap produk tersebut. Untuk menjaga keselarasan tema CutesyBoutique, saya menggunakan padding, shadow, border-radius, serta warna-warna lembut seperti pink untuk latar belakang card. Selain itu, saya mengimplementasikan grid yang responsif agar produk tetap tersusun rapi meskipun dilihat pada layar yang lebih kecil.

Terakhir, saya mengimplementasikan navigasi bar menggunakan Tailwind CSS. Pada navigasi bar ini, saya menambahkan link untuk mengarahkan pengguna ke halaman Home, Products, Categories, dan Cart.


# 📝 **ASSIGNMENT**<br>
**Name** : Nisrina Kamilya Nisyya <br>
**NPM** : 2306275456 <br>
**Class** : PBP A

## **TUGAS 6**<br>

1.  Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript memberikan interaktivitas dan dinamisme pada aplikasi web. Ini memungkinkan pengembang untuk memanipulasi elemen HTML, menangani event pengguna (seperti klik atau input), dan mengupdate konten halaman tanpa harus me-refresh seluruh halaman (seperti dengan AJAX). Selain itu, JavaScript dapat digunakan di frontend dan backend (dengan Node.js), memungkinkan pengembangan full-stack menggunakan satu bahasa.

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
await digunakan untuk menunggu penyelesaian operasi asynchronous. Ketika kita menggunakan fetch(), kita melakukan permintaan jaringan (network request) yang bersifat asynchronous. Dengan await, kita menunggu respons dari server sebelum melanjutkan kode selanjutnya. Tanpa await, kode selanjutnya akan dieksekusi sebelum respons diterima, yang dapat menyebabkan penggunaan data yang belum siap (misalnya, nilai undefined atau error).

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
csrf_exempt digunakan untuk menonaktifkan pengecekan CSRF (Cross-Site Request Forgery) pada view tertentu. AJAX POST yang dilakukan dari JavaScript biasanya tidak secara otomatis menyertakan token CSRF, yang menyebabkan request tersebut ditolak oleh server. Dengan decorator csrf_exempt, kita mengizinkan request AJAX POST untuk diproses tanpa pengecekan token CSRF. Namun, ini harus digunakan dengan hati-hati karena dapat menimbulkan kerentanan keamanan.

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan data input di backend sangat penting untuk keamanan dan keandalan aplikasi. Jika hanya dilakukan di frontend, data dapat dengan mudah dimanipulasi oleh pengguna yang mengabaikan validasi frontend (misalnya dengan memodifikasi JavaScript di browser). Oleh karena itu, backend harus memverifikasi dan membersihkan data input untuk memastikan bahwa hanya data yang aman dan valid yang diproses oleh sistem. Ini melindungi aplikasi dari serangan seperti SQL injection, XSS, atau data yang rusak.

5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Pertama, Saya menambahkan error message pada login jadi saat ada user yang login dengan username atau password yang salah, atau belum buat akun, maka ada ada error message "Invalid username or password. Please try again.".

Untuk melakukan pengambilan data produk menggunakan AJAX GET, langkah-langkahnya meliputi membuat view yang akan menangani request GET dan mengembalikan data produk dalam format JSON, hanya untuk produk yang dimiliki oleh pengguna yang sedang login. Setelah data produk berhasil diambil, frontend akan menampilkan data tersebut secara dinamis tanpa perlu me-refresh halaman. Kamu bisa menggunakan Django's JsonResponse untuk mengembalikan data. Selain itu, pastikan kamu menambahkan CSRF token pada request AJAX untuk keamanan. Path untuk view ini juga perlu ditambahkan ke dalam file urls.py.

AJAX GET untuk Menampilkan Produk: Saya memodifikasi tampilan halaman produk sehingga produk ditampilkan secara dinamis menggunakan AJAX GET. Proses ini dimulai dengan mengganti kode template yang sebelumnya menggunakan {% for product in products %} dengan sebuah div placeholder (<div id="product_cards"></div>), di mana produk-produk nantinya akan dimuat secara asinkron. Saya membuat fungsi JavaScript yang bertugas untuk mengambil data produk dari server menggunakan AJAX GET. Hanya produk yang dimiliki oleh pengguna yang sedang login yang diambil. Fungsi ini kemudian menampilkan produk-produk tersebut dalam layout grid dengan desain pink yang sesuai dengan tema CutesyBoutique, dan memastikan pengalaman pengguna yang seamless tanpa reload halaman.

AJAX POST untuk Menambahkan Produk: Saya menambahkan tombol di halaman yang ketika diklik, membuka modal berisi form untuk menambahkan produk baru. Tombol ini didesain dengan gaya pink dan animasi hover agar sesuai dengan tampilan CutesyBoutique. Form ini mengirimkan data produk baru ke server menggunakan AJAX POST. Di server, saya membuat view baru yang menangani permintaan POST ini. Pada view tersebut, data produk seperti nama, harga, deskripsi, ukuran, dan stok diambil dari form. Sebelum disimpan ke database, saya menggunakan strip_tags() untuk memastikan bahwa input pengguna bebas dari HTML tags yang berpotensi membahayakan.

Validasi Data Produk: Pada model form yang digunakan untuk menambah produk, saya menambahkan metode clean untuk memvalidasi input. Sebagai contoh, fungsi clean_name dan clean_description digunakan untuk memverifikasi bahwa nama dan deskripsi produk yang diinput tidak mengandung tag HTML. Hal ini dilakukan untuk meningkatkan keamanan dan memastikan bahwa input yang diterima aman untuk disimpan ke database.

Update Produk Secara Asinkron: Setelah produk baru berhasil ditambahkan melalui form modal, halaman utama diperbarui secara asinkron tanpa reload penuh menggunakan AJAX. Fungsi JavaScript yang menangani pengambilan data produk (refreshProducts()) dipanggil untuk memperbarui daftar produk pada halaman. Hal ini membuat pengalaman pengguna lebih dinamis karena mereka bisa melihat produk yang baru saja ditambahkan secara instan tanpa perlu melakukan refresh manual pada halaman.

Path untuk View Tambah Produk: Untuk mendukung fitur ini, saya menambahkan path baru pada urls.py, yaitu /create-ajax/, yang mengarah ke view yang baru saya buat. View ini bertanggung jawab untuk menerima permintaan POST dan menambah produk baru ke database.
