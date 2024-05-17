import csv
import pandas
#Program Warpath
def welcome_message():
    print("==============================================================")
    print("                  SELAMAT DATANG DI WARPATH!")
    print("      Silahkan Memesan makanan minuman ataupun snack sesuai menu kami")
    print("==============================================================")

#input nama
def input_customer():
    nama_customer = input("Masukkan Nama Anda")
     
def jenis_makanan():
    print("1. Nasi Goreng")
    print("2. Nasi Lauk")
    print("3. Mie")
    print("4. Bubur")

def jenis_nasi_goreng():
    print("1. Nasi Goreng")
    print("2. Nasi Goreng Bule")
    print("3. Nasi Goreng Bakso")
    print("4. Nasi Goreng Ayam")
    print("5. Nasi Goreng Ampela")
    print("6. Nasi Goreng Spesial")
    print("7. Magelangan")
    print("8. Magelangan Rendang")
    print("9. Magelangan Spesial")

def jenis_nasi_lauk():
    print("1. Nasi Telur Dadar")
    print("2. Nasi Telur Balado")
    print("3. Nasi Ayam Opor")
    print("4. Nasi Ayam Balado")
    print("5. Nasi Ayam Kentaki")
    print("6. Nasi Ayam Geprek")
    print("7. Nasi Orak Arik")
    print("8. Nasi Sayur")

def jenis_mie():
    print("1. Mie Goreng/Kuah")
    print("2. Mie Tante Goreng/Kuah")
    print("3. Mie Dokdok")
    print("4. Mie Dokdok Bakso")
    print("5. Mie Dokdok Ayam")
    print("6. Mie Dokdok Spesial")
    print("7. Mie Tektek")
    print("8. Mie Tektek Bakso")
    print("9. Mie Tektek Ayam")
    print("10. Mie Tektek Spesial")

def jenis_bubur():
    print("1. Bubur Kacang Ijo")
    print("2. Bubur Ketan Hitam")
    print("3. Bubur Campur")
    print("4. Bubur Ayam")

def jenis_minuman():
    print("1. Es/Hangat Teh")
    print("2. Es/Hangat Jeruk")
    print("3. Es/Hangat Kampul")
    print("4. Es/Hangat Beng-Beng")
    print("5. Es/Hangat Goodday")
    print("6. Es/Hangat Chocolatos")
    print("7. Es/Hangat Hilo")
    print("8. Es Joshua")
    print("9. Es Soda Gembira")
    print("10. Es Kuku Bima/ Extra Joss")
    print("11. Kopi Hitam")

def jenis_snack():
    print("1. Mendoan ")
    print("2. Bakwan")
    print("3. Pisang Goreng")
    print("4. Tahu Isi")
    print("5. Bakso")
    print("6. Sosis")
    print("7. French Fries")
    print("8. Mix Platter")


#pemilihan jenis menu
def show_jenis_menu():
    print("Pilih Jenis Menu:")
    print("1. Makanan")
    print("2. Minuman")
    print("3. Snack")
    print("4.Keluar")
    print("\n===============================")
print(show_jenis_menu())

def get_jenis_choice():
    choice = input("\nMasukkan jenis menu yang Anda pilih: ")
    
    if choice == 1 :
        print()
        


