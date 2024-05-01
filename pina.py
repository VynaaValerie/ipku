def read_allowed_ips():
    with open('allowed_ips.txt', 'r') as file:
        return [line.strip() for line in file]

def write_allowed_ips(allowed_ips):
    with open('allowed_ips.txt', 'w') as file:
        for ip in allowed_ips:
            file.write(ip + '\n')

def add_ip(allowed_ips):
    ip = input("Masukkan alamat IP yang ingin ditambahkan: ")
    allowed_ips.append(ip)
    write_allowed_ips(allowed_ips)
    print(f"Alamat IP {ip} telah ditambahkan.")

def remove_ip(allowed_ips):
    ip = input("Masukkan alamat IP yang ingin dihapus: ")
    if ip in allowed_ips:
        allowed_ips.remove(ip)
        write_allowed_ips(allowed_ips)
        print(f"Alamat IP {ip} telah dihapus.")
    else:
        print("Alamat IP tidak ditemukan dalam daftar.")

def main():
    allowed_ips = read_allowed_ips()
    while True:
        print("\nSelamat datang di VynaaMD IP Access Control\n")
        print("Pilihan:")
        print("1. Tambahkan alamat IP")
        print("2. Hapus alamat IP")
        print("3. Keluar")

        choice = input("Masukkan pilihan Anda (1/2/3): ")

        if choice == '1':
            add_ip(allowed_ips)
        elif choice == '2':
            remove_ip(allowed_ips)
        elif choice == '3':
            print("Terima kasih telah menggunakan VynaaMD IP Access Control. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1, 2, atau 3.")

if __name__ == "__main__":
    main()
