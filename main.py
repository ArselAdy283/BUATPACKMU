# buatan ArselAdy

import os
import json
import uuid
import shutil
from PIL import Image, ImageDraw, ImageFont

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def generateuuid():
    while True:
        clear()
        generate_uuid = uuid.uuid4()
        print("Ini UUID yang sudah digenerate:\n")
        print(generate_uuid)

        buat_lagi = input("\nApakah kamu mau buat lagi? [y/n]: ")
        if buat_lagi != "y":
            break
            
def buat_resource_pack():
    clear()
    print("==== Buat Resource Pack ====\n")

    name = input("Nama resource pack (nama folder): ").strip()
    if (name == ""):
        input("\nTekan Enter untuk kembali ke menu...")
        return
    
    author = input("Nama author: ").strip()
    description = input("Deskripsi: ").strip()

    header_uuid = str(uuid.uuid4())
    module_uuid = str(uuid.uuid4())

    manifest = {
        "format_version": 2,
        "header": {
            "name": name,
            "description": f"{description} \n§ePowered by BUATBACKMU",
            "uuid": header_uuid,
            "version": [1, 0, 0],
            "min_engine_version": [1, 20, 0]
        },
        "modules": [
            {
                "type": "resources",
                "uuid": module_uuid,
                "version": [1, 0, 0]
            }
        ],
        "metadata": {
            "authors": [author]
        }
    }
    
    folder_utama = "ResourcePacks"
    folder_pack = os.path.join(folder_utama, name)
    os.makedirs(folder_pack, exist_ok=True)

    textures_folder = os.path.join(folder_pack, "textures")    
    blocks_folder = os.path.join(textures_folder, "blocks")
    items_folder = os.path.join(textures_folder, "items")
    os.makedirs(textures_folder, exist_ok=True)   
    os.makedirs(blocks_folder, exist_ok=True)
    os.makedirs(items_folder, exist_ok=True)

    manifest_path = os.path.join(folder_pack, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=4, ensure_ascii=False)

    source_biome = 'file/biomes_client.json'
    if os.path.exists(source_biome):
        shutil.copy2(source_biome, os.path.join(folder_pack, 'biomes_client.json'))

    source_icon = 'file/pack_icon.png'
    if os.path.exists(source_icon):
        shutil.copy2(source_icon, os.path.join(folder_pack, 'pack_icon.png'))
        
    source_language = 'file/texts'
    if os.path.exists(source_language):
        shutil.copytree(source_language, os.path.join(folder_pack, 'texts'))

    terrain_texture_path = os.path.join(textures_folder, "terrain_texture.json") 
    with open(terrain_texture_path, "w") as f:
        f.write(f'''{{
        "resource_pack_name": "{name}",
        "texture_name": "atlas.terrain",
        "padding": 2,
        "num_mip_levels": 1
    }}''')
        
    information_blocks_path = os.path.join(blocks_folder, "information.txt")
    with open(information_blocks_path, "w") as f:
        f.write('tambahkan texture block di folder blocks ini seperti "grass.png", "dirt.png", dll \ndengan ukuran defualt 16x16')
        
    information_items_path = os.path.join(items_folder, "information.txt")
    with open(information_items_path, "w") as f:
        f.write('tambahkan texture item di folder items ini seperti "diamond.png", "stone_sword.png", dll \ndengan ukuran defualt 16x16')
             
    print(f"\n✅ Resource pack '{name}' berhasil dibuat di folder: '{folder_pack}'")
    
    input("Tekan Enter untuk kembali ke menu...")

# menampilkan folder resourcepacks

def list_resource_packs(folder_path):
    try:
        items = os.listdir(folder_path)
        packs = [item for item in items if os.path.isdir(os.path.join(folder_path, item))]
        return sorted(packs)
    except FileNotFoundError:
        print("\n❌ Folder ResourcePacks tidak ditemukan. \nbuat ResourcePack dulu")
        return []
def tampilkan_pilihan(packs):
    print("\n📦 Daftar Resource Pack yang tersedia:\n")
    if not packs:
        print("⚠ Tidak ada folder resource pack.")
    for i, pack in enumerate(packs, 1):
        print(f"{i}. [DIR] {pack}")
    print()
    
def buat_mcpack(source_folder, pack_name, output_folder):
    full_path = os.path.join(source_folder, pack_name)
    temp_zip = os.path.join(source_folder, pack_name + ".zip")
    final_mcpack = os.path.join(output_folder, pack_name + ".mcpack")

    try:
        os.makedirs(output_folder, exist_ok=True)

        shutil.make_archive(full_path, 'zip', full_path)

        os.rename(temp_zip, final_mcpack)

        print(f"\n✅ Resource pack '{pack_name}' berhasil dikonversi dan disimpan di: {final_mcpack}")
    except Exception as e:
        print(f"❌ Gagal membuat mcpack: {e}")
        
def mcpack():
    resource_folder = "ResourcePacks"
    output_folder = "KumpulanMcpack"

    while True:
        clear()
        print("=== Konversi Resource Pack ke MCPACK ===")
        packs = list_resource_packs(resource_folder)

        if not packs:
            input("\nTekan Enter untuk keluar...")
            break

        tampilkan_pilihan(packs)

        try:
            pilihan = input("Pilih nomor folder yang ingin dikonversi: ").strip()
            if pilihan.lower() == '':
                input("\nTekan Enter untuk keluar...")
                break

            index = int(pilihan) - 1
            if 0 <= index < len(packs):
                selected_pack = packs[index]
                buat_mcpack(resource_folder, selected_pack, output_folder)
            else:
                print("❌ Nomor tidak valid.")
        except ValueError:
            print("❌ Input tidak valid.")
        
        input("\nTekan Enter untuk kembali ke menu...")
    
def main():
    while True:
        clear()
        print("===========================")
        print("SELAMAT DATANG DI BUATPACKMU")
        print("===========================\n")
        print("1. generate UUID")
        print("2. template resource pack")
        print("3. buat mcpack")
        print("4. keluar\n")

        try:
            pilih = int(input("pilih: "))
        except ValueError:
            input("Masukkan angka yang valid! Tekan Enter...")
            continue

        match pilih:
            case 1:
                generateuuid()
            case 2:
                buat_resource_pack()
            case 3:
                mcpack()
            case 4:
                clear()
                print("Software by ArselAdy. 👋")
                break
            case _:
                input("Pilihan tidak valid! Tekan Enter...")

main()

