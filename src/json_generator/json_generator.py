from pathlib import Path
import cv2 as cv
from receipt_to_array.array_generator import generate_array
from receipt_enhancer.enhancer import enhance_receipt
from receipt_parser.parser import parse_receipt


def generate_json(receipt_path : Path) -> str:
    receipt_array = generate_array(str(receipt_path))
    enhanced_receipt = enhance_receipt(receipt_array)
    parsed_receipt = parse_receipt(enhanced_receipt)
    return "placeholder"