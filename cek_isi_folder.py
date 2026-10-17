import os

ROOT_FOLDER = r"G:\Android"

folder_sizes = []

for root, dirs, files in os.walk(ROOT_FOLDER):

    total_size = 0

    for file in files:

        file_path = os.path.join(root, file)

        try:
            total_size += os.path.getsize(file_path)

        except (PermissionError, FileNotFoundError):
            continue

    if total_size > 0:
        folder_sizes.append((root, total_size))


# Terbesar -> terkecil
folder_sizes.sort(key=lambda x: x[1], reverse=True)


print("=" * 80)
print("FOLDER TERBESAR")
print("=" * 80)

for folder, size in folder_sizes:

    size_gb = size / (1024 ** 3)

    print(f"{size_gb:>10.2f} GB | {folder}")