# Automation Scripts

Proyek ini berisi kumpulan script Python untuk mengotomatisasi tugas-tugas pengelolaan file sehari-hari di Mac.

## Daftar Script

1. [pindah_file_seleksi.py](#1-pindah_file_seleksipy)
2. [hapus_screenshot.py](#2-hapus_screenshotpy)
3. [rapikan_downloads.py](#3-rapikan_downloadspy)

---

### 1. `pindah_file_seleksi.py`
Script ini berfungsi untuk memindahkan file secara massal ke dalam folder `selected` berdasarkan daftar nama file yang ada di dalam sebuah file `.txt`.

**Cara Penggunaan:**
Jalankan melalui terminal dengan memasukkan *path* ke file txt yang berisi daftar nama file, serta *path* ke folder sumber di mana file-file tersebut berada.

```bash
python pindah_file_seleksi.py <path_file_txt> <path_folder_sumber>
```

**Contoh:**
```bash
python pindah_file_seleksi.py "selection_data/selection_testing.txt" "/Users/user/Downloads/WTB"
```
Script akan mencari setiap file yang tertulis di `selection_testing.txt` di dalam folder `/Users/user/Downloads/WTB` lalu memindahkannya ke dalam folder `/Users/user/Downloads/WTB/selected`. Jika folder `selected` belum ada, script akan membuatnya secara otomatis.

---

### 2. `hapus_screenshot.py`
Script ini berguna untuk mendeteksi dan menghapus semua file Screenshot yang menumpuk di area Desktop Mac Anda.

**Cara Penggunaan:**
Jalankan script tanpa argumen tambahan:

```bash
python hapus_screenshot.py
```

**Alur Kerja:**
1. Script akan mencari semua file di Desktop yang berawalan dengan nama "Screenshot".
2. Menampilkan daftar file yang ditemukan.
3. Meminta konfirmasi keamanan (y/n) sebelum melakukan penghapusan secara permanen.
4. Jika Anda mengetik `y`, file akan dihapus.

---

### 3. `rapikan_downloads.py`
Script ini dirancang untuk merapikan folder Downloads di Mac Anda secara otomatis dengan mengelompokkan file berdasarkan ekstensinya ke dalam folder-folder kategori.

**Kategori yang didukung:**
- Dokumen (`.pdf`, `.docx`, `.xlsx`, dll.)
- Gambar (`.jpg`, `.png`, dll.)
- Audio (`.mp3`, `.wav`, dll.)
- Video (`.mp4`, `.mkv`, dll.)
- Aplikasi & Installer (`.dmg`, `.pkg`, `.zip`)
- Compressed / Zip (`.rar`, `.7z`)
- Lainnya (format yang tidak terdaftar di atas)

**Cara Penggunaan:**
Jalankan script tanpa argumen tambahan:

```bash
python rapikan_downloads.py
```

Script akan langsung berjalan, memindai folder Downloads Anda, membuat folder kategori (jika belum ada), dan memindahkan file ke kategori yang sesuai secara otomatis.

---

## Persyaratan (Requirements)
Semua script di atas ditulis menggunakan Python murni dan hanya bergantung pada *built-in library* Python (`os`, `shutil`, `argparse`, `pathlib`). Anda tidak perlu melakukan instalasi library eksternal via `pip`. Cukup pastikan Python 3 sudah terinstal di komputer Anda.
