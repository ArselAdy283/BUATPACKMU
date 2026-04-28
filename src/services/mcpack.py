import os
import shutil
from src.utils.terminal import clear

def list_packs(folder_path):
    try:
        items = os.listdir(folder_path)
        packs = [item for item in items if os.path.isdir(os.path.join(folder_path, item))]
        return sorted(packs)
    except FileNotFoundError:
        return []

def tampilkan_pilihan(packs):
    if not packs:
        print("⚠ Tidak ada folder yang tersedia.")
    for i, pack in enumerate(packs, 1):
        print(f"{i}. [DIR] {pack}")
    print()

def konversi_pack(source_folder, pack_name, output_folder, ekstensi):
    full_path = os.path.join(source_folder, pack_name)
    temp_zip = os.path.join(source_folder, pack_name + ".zip")
    final_pack = os.path.join(output_folder, pack_name + ekstensi)

    try:
        os.makedirs(output_folder, exist_ok=True)
        shutil.make_archive(full_path, 'zip', full_path)
        os.rename(temp_zip, final_pack)
        print(f"\n✅ '{pack_name}' berhasil dikonversi dan disimpan di: {final_pack}")
    except Exception as e:
        print(f"❌ Gagal membuat pack: {e}")

def mcpack():
    clear()
    print("=== Konversi Pack ke MCPACK ===\n")
    print("1. Resource Pack  →  .mcpack")
    print("2. Skin Pack      →  .mcpack\n")

    try:
        pilih_tipe = int(input("Pilih tipe pack: ").strip())
    except ValueError:
        input("❌ Input tidak valid! Tekan Enter...")
        return

    if pilih_tipe == 1:
        source_folder = "ResourcePacks"
        output_folder = "KumpulanMcpack"
        label = "Resource Pack"
    elif pilih_tipe == 2:
        source_folder = "SkinPacks"
        output_folder = "KumpulanMcpack"
        label = "Skin Pack"
    else:
        input("❌ Pilihan tidak valid! Tekan Enter...")
        return

    packs = list_packs(source_folder)

    if not packs:
        print(f"\n❌ Folder '{source_folder}' tidak ditemukan atau kosong.")
        print(f"Buat {label} dulu!")
        input("\nTekan Enter untuk keluar...")
        return
    
    clear()
    print("=== Konversi Pack ke MCPACK ===\n")
    print(f"\n📦 Daftar {label} yang tersedia:\n")
    tampilkan_pilihan(packs)

    try:
        pilihan = input("Pilih nomor folder yang ingin dikonversi: ").strip()
        if pilihan == '':
            return

        index = int(pilihan) - 1
        if 0 <= index < len(packs):
            selected_pack = packs[index]
            konversi_pack(source_folder, selected_pack, output_folder, ".mcpack")
        else:
            print("❌ Nomor tidak valid.")
    except ValueError:
        print("❌ Input tidak valid.")

    input("\nTekan Enter untuk kembali ke menu utama...")