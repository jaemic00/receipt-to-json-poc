from sys import argv
from pathlib import Path
from src.json_generator.json_generator import generate_json

def handle_receipt(receipt_path : Path) -> None:
    receipt_json = generate_json(receipt_path)
    print(receipt_json)
    return

def main() -> None:
    if len(argv == 1):
        print("No args provided. Exiting.")
        return
    elif len(argv) > 2:
        print("Invalid number of args. Exiting.")
        return
    else: #len(argv) == 2
        path = Path(argv[1])
        if path.is_file:
            if path.suffix in [".jpg", ".jpeg", ".png"]:
                handle_receipt(path)
                return
            else:
                print("Unsupported file. Currently supports: .jpg, .png. Exiting.")
                return
        else:
            print("File not found. Exiting.")
            return


        

    
