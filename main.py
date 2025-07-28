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

def buat_pack_icon(path):
    from PIL import Image, ImageDraw, ImageFont

    img = Image.new("RGBA", (256, 256), (0, 102, 204, 255))
    draw = ImageDraw.Draw(img)
    text = "RESOURCE PACK\n BUATPACKMU"

    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    posisi = ((256 - text_width) // 2, (256 - text_height) // 2)

    draw.text(posisi, text, fill=(255, 255, 255), font=font)
    img.save(path)

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
            "description": f"{description} \nPowered by BUATBACKMU",
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
    
    biomes_client = {
        "biomes" : {
            "bamboo_jungle" : {
                "fog_identifier" : "minecraft:fog_bamboo_jungle",
                "fog_ids_to_merge" : [ "minecraft:fog_bamboo_jungle" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#14A2C5"
            },
            "bamboo_jungle_hills" : {
                "fog_identifier" : "minecraft:fog_bamboo_jungle_hills",
                "fog_ids_to_merge" : [ "minecraft:fog_bamboo_jungle_hills" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#1B9ED8"
            },
            "basalt_deltas" : {
                "fog_identifier" : "minecraft:fog_basalt_deltas",
                "fog_ids_to_merge" : [ "minecraft:fog_basalt_deltas" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#3f76e4"
            },
            "beach" : {
                "fog_identifier" : "minecraft:fog_beach",
                "fog_ids_to_merge" : [ "minecraft:fog_beach" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#157cab"
            },
            "birch_forest" : {
                "fog_identifier" : "minecraft:fog_birch_forest",
                "fog_ids_to_merge" : [ "minecraft:fog_birch_forest" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#0677ce"
            },
            "birch_forest_hills" : {
                "fog_identifier" : "minecraft:fog_birch_forest_hills",
                "fog_ids_to_merge" : [ "minecraft:fog_birch_forest_hills" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#0a74c4"
            },
            "cold_beach" : {
                "fog_identifier" : "minecraft:fog_cold_beach",
                "fog_ids_to_merge" : [ "minecraft:fog_cold_beach" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#1463a5"
            },
            "cold_ocean" : {
                "fog_identifier" : "minecraft:fog_cold_ocean",
                "fog_ids_to_merge" : [ "minecraft:fog_cold_ocean" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#2080C9"
            },
            "cold_taiga" : {
                "fog_identifier" : "minecraft:fog_cold_taiga",
                "fog_ids_to_merge" : [ "minecraft:fog_cold_taiga" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#205e83"
            },
            "cold_taiga_hills" : {
                "fog_identifier" : "minecraft:fog_cold_taiga_hills",
                "fog_ids_to_merge" : [ "minecraft:fog_cold_taiga_hills" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#245b78"
            },
            "cold_taiga_mutated" : {
                "fog_identifier" : "minecraft:fog_cold_taiga_mutated",
                "fog_ids_to_merge" : [ "minecraft:fog_cold_taiga_mutated" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#205e83"
            },
            "crimson_forest" : {
                "fog_identifier" : "minecraft:fog_crimson_forest",
                "fog_ids_to_merge" : [ "minecraft:fog_crimson_forest" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#905957"
            },
            "deep_cold_ocean" : {
                "fog_identifier" : "minecraft:fog_deep_cold_ocean",
                "fog_ids_to_merge" : [ "minecraft:fog_deep_cold_ocean" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#2080C9"
            },
            "deep_frozen_ocean" : {
                "fog_identifier" : "minecraft:fog_deep_frozen_ocean",
                "fog_ids_to_merge" : [ "minecraft:fog_deep_frozen_ocean" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#2570B5"
            },
            "deep_lukewarm_ocean" : {
                "fog_identifier" : "minecraft:fog_deep_lukewarm_ocean",
                "fog_ids_to_merge" : [ "minecraft:fog_deep_lukewarm_ocean" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#0D96DB"
            },
            "deep_ocean" : {
                "fog_identifier" : "minecraft:fog_deep_ocean",
                "fog_ids_to_merge" : [ "minecraft:fog_deep_ocean" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#1787D4"
            },
            "deep_warm_ocean" : {
                "fog_identifier" : "minecraft:fog_deep_warm_ocean",
                "fog_ids_to_merge" : [ "minecraft:fog_deep_warm_ocean" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#02B0E5"
            },
            "default" : {
                "fog_identifier" : "minecraft:fog_default",
                "fog_ids_to_merge" : [ "minecraft:fog_default" ],
                "inherit_from_prior_fog" : False,
                "remove_all_prior_fog" : False,
                "water_surface_color" : "#44AFF5",
                "water_surface_transparency" : 0.650
            },
            "desert" : {
                "fog_identifier" : "minecraft:fog_desert",
                "fog_ids_to_merge" : [ "minecraft:fog_desert" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#32A598"
            },
            "desert_hills" : {
                "fog_identifier" : "minecraft:fog_desert_hills",
                "fog_ids_to_merge" : [ "minecraft:fog_desert_hills" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#1a7aa1"
            },
            "extreme_hills" : {
                "fog_identifier" : "minecraft:fog_extreme_hills",
                "fog_ids_to_merge" : [ "minecraft:fog_extreme_hills" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#007BF7"
            },
            "extreme_hills_edge" : {
                "fog_identifier" : "minecraft:fog_extreme_hills_edge",
                "fog_ids_to_merge" : [ "minecraft:fog_extreme_hills_edge" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#045cd5"
            },
            "extreme_hills_mutated" : {
                "fog_identifier" : "minecraft:fog_extreme_hills_mutated",
                "fog_ids_to_merge" : [ "minecraft:fog_extreme_hills_mutated" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#0E63AB"
            },
            "extreme_hills_plus_trees" : {
                "fog_identifier" : "minecraft:fog_extreme_hills_plus_trees",
                "fog_ids_to_merge" : [ "minecraft:fog_extreme_hills_plus_trees" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#0E63AB"
            },
            "extreme_hills_plus_trees_mutated" : {
                "fog_identifier" : "minecraft:fog_extreme_hills_plus_trees_mutated",
                "fog_ids_to_merge" : [ "minecraft:fog_extreme_hills_plus_trees_mutated" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#0E63AB"
            },
            "flower_forest" : {
                "fog_identifier" : "minecraft:fog_flower_forest",
                "fog_ids_to_merge" : [ "minecraft:fog_flower_forest" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#20A3CC"
            },
            "forest" : {
                "fog_identifier" : "minecraft:fog_forest",
                "fog_ids_to_merge" : [ "minecraft:fog_forest" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#1E97F2"
            },
            "forest_hills" : {
                "fog_identifier" : "minecraft:fog_forest_hills",
                "fog_ids_to_merge" : [ "minecraft:fog_forest_hills" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#056bd1"
            },
            "frozen_ocean" : {
                "fog_identifier" : "minecraft:fog_frozen_ocean",
                "fog_ids_to_merge" : [ "minecraft:fog_frozen_ocean" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#2570B5"
            },
            "frozen_river" : {
                "fog_identifier" : "minecraft:fog_frozen_river",
                "fog_ids_to_merge" : [ "minecraft:fog_frozen_river" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#185390"
            },
            "hell" : {
                "fog_identifier" : "minecraft:fog_hell",
                "fog_ids_to_merge" : [ "minecraft:fog_hell" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#905957"
            },
            "ice_mountains" : {
                "fog_identifier" : "minecraft:fog_ice_mountains",
                "fog_ids_to_merge" : [ "minecraft:fog_ice_mountains" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#1156a7"
            },
            "ice_plains" : {
                "fog_identifier" : "minecraft:fog_ice_plains",
                "fog_ids_to_merge" : [ "minecraft:fog_ice_plains" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#14559b"
            },
            "ice_plains_spikes" : {
                "fog_identifier" : "minecraft:fog_ice_plains_spikes",
                "fog_ids_to_merge" : [ "minecraft:fog_ice_plains_spikes" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#14559b"
            },
            "jungle" : {
                "fog_identifier" : "minecraft:fog_jungle",
                "fog_ids_to_merge" : [ "minecraft:fog_jungle" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#14A2C5"
            },
            "jungle_edge" : {
                "fog_identifier" : "minecraft:fog_jungle_edge",
                "fog_ids_to_merge" : [ "minecraft:fog_jungle_edge" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#0D8AE3"
            },
            "jungle_hills" : {
                "fog_identifier" : "minecraft:fog_jungle_hills",
                "fog_ids_to_merge" : [ "minecraft:fog_jungle_hills" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#1B9ED8"
            },
            "jungle_mutated" : {
                "fog_identifier" : "minecraft:fog_jungle_mutated",
                "fog_ids_to_merge" : [ "minecraft:fog_jungle_mutated" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#1B9ED8"
            },
            "lukewarm_ocean" : {
                "fog_identifier" : "minecraft:fog_lukewarm_ocean",
                "fog_ids_to_merge" : [ "minecraft:fog_lukewarm_ocean" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#0D96DB"
            },
            "mega_spruce_taiga" : {
                "fog_identifier" : "minecraft:fog_mega_spruce_taiga",
                "fog_ids_to_merge" : [ "minecraft:fog_mega_spruce_taiga" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#2d6d77"
            },
            "mega_spruce_taiga_mutated" : {
                "fog_identifier" : "minecraft:fog_mega_spruce_taiga_mutated",
                "fog_ids_to_merge" : [ "minecraft:fog_mega_spruce_taiga_mutated" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#2d6d77"
            },
            "mega_taiga" : {
                "fog_identifier" : "minecraft:fog_mega_taiga",
                "fog_ids_to_merge" : [ "minecraft:fog_mega_taiga" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#2d6d77"
            },
            "mega_taiga_hills" : {
                "fog_identifier" : "minecraft:fog_mega_taiga_hills",
                "fog_ids_to_merge" : [ "minecraft:fog_mega_taiga_hills" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#286378"
            },
            "mega_taiga_mutated" : {
                "fog_identifier" : "minecraft:fog_mega_taiga_mutated",
                "fog_ids_to_merge" : [ "minecraft:fog_mega_taiga_mutated" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#2d6d77"
            },
            "mesa" : {
                "fog_identifier" : "minecraft:fog_mesa",
                "fog_ids_to_merge" : [ "minecraft:fog_mesa" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#4E7F81"
            },
            "mesa_bryce" : {
                "fog_identifier" : "minecraft:fog_mesa_bryce",
                "fog_ids_to_merge" : [ "minecraft:fog_mesa_bryce" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#497F99"
            },
            "mesa_mutated" : {
                "fog_identifier" : "minecraft:fog_mesa_mutated",
                "fog_ids_to_merge" : [ "minecraft:fog_mesa_mutated" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#497F99"
            },
            "mesa_plateau" : {
                "fog_identifier" : "minecraft:fog_mesa_plateau",
                "fog_ids_to_merge" : [ "minecraft:fog_mesa_plateau" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#55809E"
            },
            "mesa_plateau_stone" : {
                "fog_identifier" : "minecraft:fog_mesa_plateau_stone",
                "fog_ids_to_merge" : [ "minecraft:fog_mesa_plateau_stone" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#55809E"
            },
            "mushroom_island" : {
                "fog_identifier" : "minecraft:fog_mushroom_island",
                "fog_ids_to_merge" : [ "minecraft:fog_mushroom_island" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#8a8997"
            },
            "mushroom_island_shore" : {
                "fog_identifier" : "minecraft:fog_mushroom_island_shore",
                "fog_ids_to_merge" : [ "minecraft:fog_mushroom_island_shore" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#818193"
            },
            "ocean" : {
                "fog_identifier" : "minecraft:fog_ocean",
                "fog_ids_to_merge" : [ "minecraft:fog_ocean" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#1787D4"
            },
            "plains" : {
                "fog_identifier" : "minecraft:fog_plains",
                "fog_ids_to_merge" : [ "minecraft:fog_plains" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#44AFF5"
            },
            "river" : {
                "fog_identifier" : "minecraft:fog_river",
                "fog_ids_to_merge" : [ "minecraft:fog_river" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#0084FF"
            },
            "roofed_forest" : {
                "fog_identifier" : "minecraft:fog_roofed_forest",
                "fog_ids_to_merge" : [ "minecraft:fog_roofed_forest" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#3B6CD1"
            },
            "savanna" : {
                "fog_identifier" : "minecraft:fog_savanna",
                "fog_ids_to_merge" : [ "minecraft:fog_savanna" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#2C8B9C"
            },
            "savanna_mutated" : {
                "fog_identifier" : "minecraft:fog_savanna_mutated",
                "fog_ids_to_merge" : [ "minecraft:fog_savanna_mutated" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#2590A8"
            },
            "savanna_plateau" : {
                "fog_identifier" : "minecraft:fog_savanna_plateau",
                "fog_ids_to_merge" : [ "minecraft:fog_savanna_plateau" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#2590A8"
            },
            "soulsand_valley" : {
                "fog_identifier" : "minecraft:fog_soulsand_valley",
                "fog_ids_to_merge" : [ "minecraft:fog_soulsand_valley" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#905957"
            },
            "stone_beach" : {
                "fog_identifier" : "minecraft:fog_stone_beach",
                "fog_ids_to_merge" : [ "minecraft:fog_stone_beach" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#0d67bb"
            },
            "sunflower_plains" : {
                "fog_identifier" : "minecraft:fog_sunflower_plains",
                "fog_ids_to_merge" : [ "minecraft:fog_sunflower_plains" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#44AFF5"
            },
            "swampland" : {
                "fog_identifier" : "minecraft:fog_swampland",
                "fog_ids_to_merge" : [ "minecraft:fog_swampland" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#4c6559",
                "water_surface_transparency" : 1.0
            },
            "swampland_mutated" : {
                "fog_identifier" : "minecraft:fog_swampland_mutated",
                "fog_ids_to_merge" : [ "minecraft:fog_swampland_mutated" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#4c6156",
                "water_surface_transparency" : 1.0
            },
            "taiga" : {
                "fog_identifier" : "minecraft:fog_taiga",
                "fog_ids_to_merge" : [ "minecraft:fog_taiga" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#287082"
            },
            "taiga_hills" : {
                "fog_identifier" : "minecraft:fog_taiga_hills",
                "fog_ids_to_merge" : [ "minecraft:fog_taiga_hills" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#236583"
            },
            "taiga_mutated" : {
                "fog_identifier" : "minecraft:fog_taiga_mutated",
                "fog_ids_to_merge" : [ "minecraft:fog_taiga_mutated" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#1E6B82"
            },
            "the_end" : {
                "fog_identifier" : "minecraft:fog_the_end",
                "fog_ids_to_merge" : [ "minecraft:fog_the_end" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#62529e"
            },
            "warm_ocean" : {
                "fog_identifier" : "minecraft:fog_warm_ocean",
                "fog_ids_to_merge" : [ "minecraft:fog_warm_ocean" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#02B0E5",
                "water_surface_transparency" : 0.550
            },
            "warped_forest" : {
                "fog_identifier" : "minecraft:fog_warped_forest",
                "fog_ids_to_merge" : [ "minecraft:fog_warped_forest" ],
                "inherit_from_prior_fog" : False,
                "water_surface_color" : "#905957"
            }
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
        
    biomes_client_path = os.path.join(folder_pack, "biomes_client.json")
    with open(biomes_client_path, "w") as f:
        json.dump(biomes_client, f, indent=4)

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

    pack_icon_path = os.path.join(folder_pack, "pack_icon.png")
    buat_pack_icon(pack_icon_path)

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
