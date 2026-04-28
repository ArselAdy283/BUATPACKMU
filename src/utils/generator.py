import uuid
from src.utils.terminal import clear

def generateuuid():
    while True:
        clear()
        generate_uuid = uuid.uuid4()
        print("Ini UUID yang sudah digenerate:\n")
        print(generate_uuid)

        buat_lagi = input("\nApakah kamu mau buat lagi? [y/n]: ")
        if buat_lagi != "y":
            break