import os
from pathlib import Path

def hapus_screenshot_desktop():
    # Mendeteksi folder Desktop di Mac kamu secara otomatis
    desktop_path = Path.home() / "Desktop"
    
    if not desktop_path.exists():
        print("Folder Desktop tidak ditemukan.")
        return

    # Menampung daftar file screenshot yang ditemukan
    screenshot_files = []

    # Mencari file di Desktop
    for file_path in desktop_path.iterdir():
        # Memastikan itu adalah file (bukan folder) dan namanya diawali kata 'Screenshot'
        if file_path.is_file() and file_path.name.startswith("Screenshot"):
            screenshot_files.append(file_path)

    # Jika tidak ada screenshot yang ditemukan
    if not screenshot_files:
        print("Hebat! Tidak ada file screenshot yang ditemukan di Desktop kamu.")
        return

    # Menampilkan file yang ditemukan ke user
    print(f"Ditemukan {len(screenshot_files)} file screenshot di Desktop:")
    for file in screenshot_files:
        print(f"- {file.name}")
    
    print("\n" + "="*40)
    # Meminta konfirmasi keamanan dari user sebelum menghapus
    pilihan = input("Apakah kamu yakin ingin MENGHAPUS SEMUA file di atas secara permanen? (y/n): ").lower()

    if pilihan == 'y':
        print("\nMemulai proses penghapusan...")
        berhasil_dihapus = 0
        
        for file in screenshot_files:
            try:
                os.remove(file)
                print(f"Terhapus: {file.name}")
                berhasil_dihapus += 1
            except Exception as e:
                print(f"Gagal menghapus {file.name}: {e}")
                
        print(f"\nSelesai! {berhasil_dihapus} file screenshot berhasil dibersihkan dari Desktop.")
    else:
        print("\nPenghapusan dibatalkan. File kamu aman.")

if __name__ == "__main__":
    hapus_screenshot_desktop()
