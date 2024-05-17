from PIL import Image

def misal_total_pembelian(misal_total_pembelian = 10000):
    return misal_total_pembelian

def bayar_tunai():
    total = misal_total_pembelian()
    print("Silahkan ambil nota dan siapkan uang sebesar Rp", total," lalu transaksi di kasir")
    
def bayar_qris():
    total = misal_total_pembelian()
    print("Silahkan bayar sebesar", total)
    qris = Image.open("kiris.jpg")
    qris.show()

def bayar_transfer():
    total = misal_total_pembelian()
    print("1.Bank Jago\n2.Bank Rakyat Indonesia\n3.Bank Negara Indonesia\n4.Bank Syariah Indonesia")
    rekening_tujuan = int(input("Pilih jenis bank:"))
    if rekening_tujuan == 1:
        print("Bayar pesanan anda sebesar", total, "ke rekening tujuan *uiasfhe*3")
    elif rekening_tujuan == 2:
        print("Bayar pesanan anda sebesar", total, "ke rekening tujuan hjsdfg")
    elif rekening_tujuan == 3:
        print("Bayar pesanan anda sebesar", total, "ke rekening tujuan jdfhsasjd")
    elif rekening_tujuan == 4:
        print("Bayar pesanan anda sebesar", total, "ke rekening tujuan jhasdsajgd")
    else:
        print("Maaf, kode tidak valid")
              
def coba_metode_pembayaran():
    print("========Pilih Metode Pembayaran=========")
    print("1.Tunai\n2.Qris\n3.Transfer")
    pilih_metode = int(input("Pilih metode pembayaran:"))
    if pilih_metode == 1:
        bayar_tunai()
    elif pilih_metode == 2:
        bayar_qris()
    elif pilih_metode == 3:
        bayar_transfer()
    else:
        print("Metode pembayaran tidak valid")

if __name__ == "__main__":
    coba_metode_pembayaran()
