from src.utils.terminal import clear
from src.utils.generator import generateuuid
from src.services.resource_pack import buat_resource_pack
from src.services.skin_pack import buat_skin_pack
from src.services.mcpack import mcpack

def main():
    while True:
        clear()
        print(r"""
  ____  _    _      _______ _____        _____ _  ____  __ _    _ 
 |  _ \| |  | |  /\|__   __|  __ \ /\   / ____| |/ /  \/  | |  | |
 | |_) | |  | | /  \  | |  | |__) /  \ | |    | ' /| \  / | |  | |
 |  _ <| |  | |/ /\ \ | |  |  ___/ /\ \| |    |  < | |\/| | |  | |
 | |_) | |__| / ____ \| |  | |  / ____ \ |____| . \| |  | | |__| |
 |____/ \____/_/    \_\_|  |_| /_/    \_\_____|_|\_\_|  |_|\____/ 
                                                                                                                       
        """)
        print("===================================================================\n")
        print("1. generate UUID")
        print("2. template resource pack")
        print("3. template skin pack")
        print("4. buat mcpack")
        print("5. keluar\n")

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
                buat_skin_pack()
            case 4:
                mcpack()
            case 5:
                clear()
                print("Software by ArselAdy. 👋")
                break
            case _:
                input("Pilihan tidak valid! Tekan Enter...")

if __name__ == "__main__":
    main()