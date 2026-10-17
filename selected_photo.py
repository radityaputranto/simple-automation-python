import os
import shutil
from pathlib import Path

# ==========================================
# KONFIGURASI PATH
# ==========================================
# 1. Folder foto JPG terpilih di Desktop
JPG_DIR = r"C:\Users\radit\OneDrive\Desktop\selected-photo"

# 2. File TXT untuk menyimpan daftar nama file
OUTPUT_TXT = r"C:\Users\radit\OneDrive\Desktop\selected_photos.txt"

# 3. Folder asal file RAW di SD Card
RAW_DIR = r"G:\DCIM\RAW"

# 4. Folder tujuan RAW terpilih (subfolder "selected-raw" di dalam G:\DCIM\RAW)
DEST_RAW_DIR = r"G:\DCIM\RAW\selected-raw"

# Ekstensi file RAW umum (termasuk .RAF Fujifilm, .CR2/CR3, .NEF, .ARW, dll.)
RAW_EXTENSIONS = {".raf", ".cr2", ".cr3", ".nef", ".arw", ".dng", ".orf", ".rw2"}


def get_selected_stems(jpg_folder, txt_output):
    """Mencatat nama file JPG dan menyimpannya ke file TXT."""
    jpg_path = Path(jpg_folder)

    if not jpg_path.exists():
        print(f"[Error] Folder JPG tidak ditemukan: {jpg_folder}")
        return set()

    # Ambil nama file tanpa ekstensi (.jpg / .jpeg)
    jpg_stems = {
        f.stem for f in jpg_path.iterdir()
        if f.is_file() and f.suffix.lower() in [".jpg", ".jpeg"]
    }

    if not jpg_stems:
        print("[Info] Tidak ada file JPG yang ditemukan di folder selected-photo.")
        return set()

    # Simpan daftar nama file ke file TXT
    with open(txt_output, "w", encoding="utf-8") as f:
        for name in sorted(jpg_stems):
            f.write(f"{name}\n")

    print(f"✓ Berhasil mencatat {len(jpg_stems)} nama foto ke: {txt_output}")
    return jpg_stems


def copy_raw_files(selected_stems, raw_folder, dest_folder):
    """
    Menyalin file RAW yang cocok dari G:\DCIM\RAW ke subfolder G:\DCIM\RAW\selected-raw
    """
    raw_path = Path(raw_folder)
    dest_path = Path(dest_folder)

    if not raw_path.exists():
        print(f"[Error] Folder RAW tidak ditemukan: {raw_folder}")
        print("Pastikan SD Card terhubung di Drive G:")
        return

    # Membuat subfolder 'selected-raw' otomatis jika belum ada
    dest_path.mkdir(parents=True, exist_ok=True)

    found_count = 0

    print(f"\n[Menyalin File RAW ke {dest_folder}...]")

    # Ambil hanya file di folder utama (mengabaikan isi subfolder agar tidak looping)
    raw_files = [
        f for f in raw_path.iterdir()
        if f.is_file() and f.suffix.lower() in RAW_EXTENSIONS
    ]

    for raw_file in raw_files:
        if raw_file.stem in selected_stems:
            target_path = dest_path / raw_file.name

            # Menyalin file RAW ke subfolder
            shutil.copy2(str(raw_file), str(target_path))
            print(f"  [Disalin] {raw_file.name}")
            found_count += 1

    print(f"\n✓ Selesai! Total {found_count} dari {len(selected_stems)} file RAW berhasil disalin ke:")
    print(f"  {dest_folder}")

    if found_count < len(selected_stems):
        print(f"⚠ Ada {len(selected_stems) - found_count} foto JPG yang file RAW-nya tidak ditemukan di folder G:\\DCIM\\RAW.")


if __name__ == "__main__":
    # 1. Ekspor daftar nama foto JPG ke TXT
    stems = get_selected_stems(JPG_DIR, OUTPUT_TXT)

    # 2. Salin file RAW ke G:\DCIM\RAW\selected-raw
    if stems:
        copy_raw_files(stems, RAW_DIR, DEST_RAW_DIR)