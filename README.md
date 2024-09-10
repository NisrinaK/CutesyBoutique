1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
-Pertama saya membuat repositori baru dengan nama CutesyBoutique, lalu menambahkan file .gitignore untuk Python agar file virtual environment tidak di-commit
-


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   ![S__37502985](https://github.com/user-attachments/assets/8e904cd8-6f58-406d-8371-6efe5baadfd9)

  File urls.py berfungsi untuk mengatur jalur permintaan dari pengguna (HTTP Request). Dalam urls.py, kita melakukan konfigurasi routing URL untuk aplikasi. File views.py bertugas untuk mendefinisikan dictionary context dalam fungsi show_main, yang kemudian akan ditampilkan di aplikasi. Fungsi show_main juga mengembalikan nilai untuk me-render tampilan Template (file HTML). File models.py digunakan untuk mendefinisikan model-model database yang digunakan dalam aplikasi. Data dari database hanya dapat diakses melalui models.py dan tidak boleh langsung dari views.py. Jadi, jika views.py membutuhkan data dari database, data tersebut harus diambil melalui models.py. File HTML digunakan untuk menampilkan data dan tampilan antarmuka kepada pengguna.

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
	Git adalah sistem kontrol versi terdistribusi yang sangat penting dalam pengembangan perangkat lunak. Fungsinya adalah untuk melacak perubahan dalam kode, memungkinkan beberapa pengembang untuk bekerja secara bersamaan tanpa mengganggu satu sama lain. Dengan Git, pengembang dapat membuat cabang (branch) untuk mengembangkan fitur baru atau memperbaiki bug secara terpisah dari versi utama (main branch), yang memudahkan pengelolaan perubahan. Git juga memungkinkan rollback atau pengembalian ke versi sebelumnya jika terdapat kesalahan. Selain itu, Git memfasilitasi kolaborasi tim dengan memadukan perubahan dari berbagai kontributor secara efisien dan memastikan bahwa riwayat perubahan kode terdokumentasi dengan baik.


4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
	Django sering dijadikan permulaan dalam pembelajaran pengembangan perangkat lunak karena menawarkan pendekatan yang "batteries included," di mana framework ini menyediakan banyak fitur siap pakai yang memudahkan pemula memahami konsep-konsep dasar web development. Django dirancang dengan arsitektur Model-View-Template (MVT), yang membantu pemula memahami cara memisahkan logika bisnis, data, dan tampilan secara terstruktur. Selain itu, Django memiliki dokumentasi yang sangat lengkap dan komunitas yang besar, sehingga banyak sumber belajar yang tersedia. Django juga mempromosikan praktik pengkodean yang baik, seperti keamanan, skalabilitas, dan manajemen database, sehingga menjadi fondasi yang baik bagi pemula untuk mengembangkan proyek dengan standar yang tinggi.


5. Mengapa model pada Django disebut sebagai ORM?
	Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena menyediakan sebuah cara untuk berinteraksi dengan database menggunakan objek-objek Python alih-alih menulis SQL secara langsung. ORM memungkinkan konversi data antara sistem database relasional (yang menggunakan tabel) dan objek Python (yang menggunakan class dan instance).
