import os
import json
import uuid
import shutil
from src.utils.terminal import clear

def buat_skin_pack():
    clear()
    print("==== Buat Skin Pack ====\n")
    
    name = input("Nama skin pack: ").strip()
    if name == "":
        input("\nTekan Enter untuk kembali ke menu...")
        return
    
    name_code = name.replace(" ", "_")
    
    author = input("Nama author: ").strip()
    description = input("Deskripsi: ").strip()
    
    while True:
        try:
            amount_skin = int(input("Jumlah Skin: "))
            if amount_skin <= 0:
                print("❌ Jumlah skin harus lebih dari 0.")
                continue
            break
        except ValueError:
            print("❌ Masukkan angka yang valid.")
    
    skins_list = []
    skin_names = []
    for i in range(amount_skin):
        skin_name = input(f"  Nama skin ke-{i+1}: ").strip()
        skin_names.append(skin_name)
        skins_list.append({
            "localization_name": f"skin{i+1}",
            "geometry": "geometry.humanoid.custom",
            "texture": f"{skin_name}.png",
            "type": "free"
        })

    header_uuid = str(uuid.uuid4())
    module_uuid = str(uuid.uuid4())

    manifest = {
        "format_version": 1,
        "header": {
            "name": name,
            "description": f"{description}\n§ePowered by BUATPACKMU",
            "uuid": header_uuid,
            "version": [1, 0, 0],
        },
        "modules": [
            {
                "type": "skin_pack",
                "uuid": module_uuid,
                "version": [1, 0, 0]
            }
        ],
        "metadata": {
            "authors": [author]
        }
    }

    skins_json = {
        "geometry": "skinpacks\/skins.json",
        "skins": skins_list,
        "serialize_name": name_code,
        "localization_name": name_code
    }

    # buat folder
    folder_utama = "SkinPacks"
    folder_pack = os.path.join(folder_utama, name)
    os.makedirs(folder_pack, exist_ok=True)

    # manifest.json
    manifest_path = os.path.join(folder_pack, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=4, ensure_ascii=False)

    # skins.json
    skins_path = os.path.join(folder_pack, "skins.json")
    with open(skins_path, "w", encoding="utf-8") as f:
        json.dump(skins_json, f, indent=4, ensure_ascii=False)

    # folder texts
    texts_folder = os.path.join(folder_pack, "texts")
    os.makedirs(texts_folder, exist_ok=True)

    # info texture
    info_path = os.path.join(folder_pack, "information.txt")
    with open(info_path, "w") as f:
        f.write("Tambahkan file texture skin (nama skin.png) di root.\nUkuran default: 64x64")

    #lang
    lang_lines = []
    for i, skin_name in enumerate(skin_names):
        lang_lines.append(f"skin.{name_code}.skin{i+1}={skin_name}")
    lang_lines.append(f"skinpack.{name_code}={name}")

    texts_path = os.path.join(texts_folder, "en_US.lang")
    with open(texts_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lang_lines))

    # copy pack_icon jika ada
    source_icon = "file/pack_icon.png"
    if os.path.exists(source_icon):
        shutil.copy2(source_icon, os.path.join(folder_pack, "pack_icon.png"))

    print(f"\n✅ Skin pack '{name}' berhasil dibuat di folder: '{folder_pack}'")
    input("\nTekan Enter untuk kembali ke menu...")