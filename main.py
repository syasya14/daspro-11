from ecommerce.pricing import hitung_diskon, hitung_total, hitung_pajak
from ecommerce.order import generate_order_id

def main():
    nama_pelanggan = input("Masukan nama pelanggan: ")
    nama_produk = input("Masukan nama produk: ")
    harga_asli = float(input("Masukan harga asli: "))
    persentase_diskon = float(input("Masukan persentase diskon: "))
    persentase_pajak = float(input("Masukan persentase pajak: "))

    diskon = hitung_diskon(harga_asli, persentase_diskon)
    pajak = hitung_pajak(harga_asli - diskon, persentase_pajak)
    total = hitung_total(harga_asli, diskon, pajak)
    order_id = generate_order_id()

    print("="*40)
    print("RINCIAN PEMBELIAN")
    print("="*40)
    print(f"{'ID pesanan' :20} {order_id}")
    print(f"{'Nama pelanggan' :20} {nama_pelanggan}")
    print(f"{'Nama produk' :20} {nama_produk}")
    print(f"{'Harga asli' :20} {harga_asli}")
    print(f"{'Diskon' :20} {diskon:,.2f}")
    print(f"{'Pajak' :20} {pajak:,.2f}")
    print("-"*40)
    print(f"{'Total Belanja' :20} {total:,.2f}")
    print("="*40)

if __name__ == "__main__":
    main()