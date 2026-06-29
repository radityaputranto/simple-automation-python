import os
import shutil
import argparse
from pathlib import Path

def move_selected_files(list_file_path, source_folder):
    list_path = Path(list_file_path)
    source_path = Path(source_folder)
    
    # Validasi path
    if not list_path.is_file():
        print(f"Error: File list '{list_file_path}' tidak ditemukan.")
        return
        
    if not source_path.is_dir():
        print(f"Error: Folder sumber '{source_folder}' tidak ditemukan.")
        return

    # Membuat folder 'selected' di dalam folder sumber yang dimasukkan
    selected_folder = source_path / "selected"
    selected_folder.mkdir(parents=True, exist_ok=True)
    
    # Membaca daftar nama file dari txt
    with open(list_path, 'r', encoding='utf-8') as f:
        # Membaca setiap baris dan membersihkan spasi/newline (termasuk mengabaikan baris kosong)
        files_to_move = [line.strip() for line in f if line.strip()]
        
    print(f"Ditemukan {len(files_to_move)} nama file di dalam list.")
    
    success_count = 0
    not_found_count = 0
    
    for filename in files_to_move:
        # Asumsi path source file adalah gabungan source_folder dan nama file
        source_file = source_path / filename
        destination_file = selected_folder / filename
        
        if source_file.is_file():
            try:
                shutil.move(str(source_file), str(destination_file))
                print(f"[OK] Dipindahkan: {filename}")
                success_count += 1
            except Exception as e:
                print(f"[ERROR] Gagal memindahkan {filename}: {e}")
        else:
            print(f"[NOT FOUND] File tidak ada di folder: {filename}")
            not_found_count += 1
            
    print("\n" + "="*40)
    print("PROSES SELESAI")
    print(f"Berhasil dipindah : {success_count} file")
    print(f"Tidak ditemukan   : {not_found_count} file")
    print(f"Lokasi folder     : {selected_folder.absolute()}")
    print("="*40)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pindahkan file ke folder 'selected' berdasarkan list dari file txt.")
    parser.add_argument("list_file", help="Path file .txt yang berisi list file terpilih (contoh: selection_data/selection_testing.txt)")
    parser.add_argument("source_folder", help="Path folder sumber di mana file-file tersebut berada (contoh: Download/WTB)")
    
    args = parser.parse_args()
    move_selected_files(args.list_file, args.source_folder)
