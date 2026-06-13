import os
import shutil
from pathlib import Path

# Mendeteksi folder Downloads di Mac secara otomatis
download_path = Path.home() / "Downloads"

# Daftar kategori folder dan ekstensi file yang akan dipindahkan
FILE_TYPES = {
    "Dokumen": [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".txt", ".csv", ".pages", ".numbers", ".key"],
    "Gambar": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".heic"],
    "Audio": [".mp3", ".wav", ".m4a", ".flac"],
    "Video": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "Aplikasi_Installer": [".dmg", ".pkg", ".app", ".zip"],
    "Compressed_Zip": [".rar", ".7z", ".tar", ".gz"]
}

def rapikan_downloads():
    if not download_path.exists():
        print("Folder Downloads tidak ditemukan.")
        return

    print("Memulai proses perapian folder Downloads...")
    
    for file_path in download_path.iterdir():
        # Lewati jika itu adalah folder bawaan atau folder yang kita buat
        if file_path.is_dir():
            continue
            
        # Lewati file sistem tersembunyi milik Mac (seperti .DS_Store)
        if file_path.name.startswith('.'):
            continue
            
        file_extension = file_path.suffix.lower()
        moved = False

        # Cek tipe file dan pindahkan ke folder yang sesuai
        for folder_name, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                target_folder = download_path / folder_name
                target_folder.mkdir(exist_ok=True) # Buat folder baru jika belum ada
                
                try:
                    shutil.move(str(file_path), str(target_folder / file_path.name))
                    print(f"Berhasil memindahkan: {file_path.name} -> {folder_name}")
                except Exception as e:
                    print(f"Gagal memindahkan {file_path.name}: {e}")
                
                moved = True
                break
        
        # Jika format file tidak terdaftar, masukkan ke folder 'Lainnya'
        if not moved and file_extension != "":
            target_folder = download_path / "Lainnya"
            target_folder.mkdir(exist_ok=True)
            try:
                shutil.move(str(file_path), str(target_folder / file_path.name))
                print(f"Berhasil memindahkan: {file_path.name} -> Lainnya")
            except Exception as e:
                print(f"Gagal memindahkan {file_path.name}: {e}")

if __name__ == "__main__":
    rapikan_downloads()
    print("Selesai! Folder Downloads kamu sudah rapi sekarang.")
