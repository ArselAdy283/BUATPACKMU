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

# def buat_pack_icon(path):
#     from PIL import Image, ImageDraw, ImageFont

#     img = Image.new("RGBA", (256, 256), (0, 102, 204, 255))
#     draw = ImageDraw.Draw(img)
#     text = "RESOURCE PACK\n BUATPACKMU"

#     try:
#         font = ImageFont.truetype("arial.ttf", 24)
#     except:
#         font = ImageFont.load_default()

#     bbox = draw.textbbox((0, 0), text, font=font)
#     text_width = bbox[2] - bbox[0]
#     text_height = bbox[3] - bbox[1]
#     posisi = ((256 - text_width) // 2, (256 - text_height) // 2)

#     draw.text(posisi, text, fill=(255, 255, 255), font=font)
#     img.save(path)

def buat_resource_pack():
    clear()
    print("==== Buat Resource Pack ====\n")

    name = input("Nama resource pack (nama folder): ").strip()
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
    texts_folder = os.path.join(folder_pack, "texts")
    blocks_folder = os.path.join(textures_folder, "blocks")
    items_folder = os.path.join(textures_folder, "items")
    os.makedirs(textures_folder, exist_ok=True)
    os.makedirs(texts_folder, exist_ok=True)
    os.makedirs(blocks_folder, exist_ok=True)
    os.makedirs(items_folder, exist_ok=True)

    manifest_path = os.path.join(folder_pack, "manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=4)

    source_biome = 'file/biomes_client.json'
    if os.path.exists(source_biome):
        shutil.copy2(source_biome, os.path.join(folder_pack, 'biomes_client.json'))

    source_icon = 'file/pack_icon.png'
    if os.path.exists(source_icon):
        shutil.copy2(source_icon, os.path.join(folder_pack, 'pack_icon.png'))

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

    lang_file_path = os.path.join(texts_folder, "en_US.lang")
    with open(lang_file_path, "w") as f:
        f.write("# Language file\n")
        
    print(f"\n✅ Resource pack '{name}' berhasil dibuat di folder: '{folder_pack}'")
    
    #Buat file .mcpack
    mcpack_path = folder_pack + ".mcpack"
    shutil.make_archive(folder_pack, 'zip', folder_pack)
    os.rename(folder_pack + ".zip", mcpack_path)
    
    input("Tekan Enter untuk kembali ke menu...")

def main():
    while True:
        clear()
        print("===========================")
        print("SELAMAT DATANG DI BUATPACKMU")
        print("===========================\n")
        print("1. generate UUID")
        print("2. template resource pack")
        print("3. keluar\n")

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
                print("Keluar dari program. 👋")
                break
            case _:
                input("Pilihan tidak valid! Tekan Enter...")

main()
