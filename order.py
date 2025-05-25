print(">>> Ini file order.py yang sedang digunakan <<<")
from datetime import datetime
import random

def generate_order_id():
    tanggal = datetime.now().strftime("%Y%m%d")
    random_number = random.randint(100000, 999999)
    return f"ORDER-{tanggal}-{random_number}"