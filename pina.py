def read_allowed_ips():
    with open('allowed_ips.txt', 'r') as file:
        return [line.strip() for line in file]

def write_allowed_ips(allowed_ips):
    with open('allowed_ips.txt', 'w') as file:
        for ip in allowed_ips:
            file.write(ip + '\n')

def add_ip(allowed_ips):
    ip = input("\033[36mMasukkan alamat IP yang ingin ditambahkan: \033[0m")
    allowed_ips.append(ip)
    write_allowed_ips(allowed_ips)
    print(f"\033[32mAlamat IP {ip} telah ditambahkan.\033[0m")

def remove_ip(allowed_ips):
    ip = input("\033[36mMasukkan alamat IP yang ingin dihapus: \033[0m")
    if ip in allowed_ips:
        allowed_ips.remove(ip)
        write_allowed_ips(allowed_ips)
        print(f"\033[32mAlamat IP {ip} telah dihapus.\033[0m")
    else:
        print("\033[91mAlamat IP tidak ditemukan dalam daftar.\033[0m")

def main():
    allowed_ips = read_allowed_ips()
    while True:
        print("\n\033[33mSelamat datang di VynaaMD IP Access Control\n\033[0m")
        print("\033[96mPilihan:\033[0m")
        print("\033[96m1. Tambahkan alamat IP\033[0m")
        print("\033[96m2. Hapus alamat IP\033[0m")
        print("\033[96m3. Lihat daftar alamat IP\033[0m")
        print("\033[96m4. Keluar\033[0m")

        choice = input("\033[36mMasukkan pilihan Anda (1/2/3/4): \033[0m")

        if choice == '1':
            add_ip(allowed_ips)
        elif choice == '2':
            remove_ip(allowed_ips)
        elif choice == '3':
            print("\033[96mDaftar alamat IP yang diizinkan:\033[0m")
            for ip in allowed_ips:
                print(ip)
        elif choice == '4':
            print("\033[33mTerima kasih telah menggunakan VynaaMD IP Access Control. Sampai jumpa!\033[0m")
            break
        else:
            print("\033[91mPilihan tidak valid. Silakan pilih antara 1, 2, 3, atau 4.\033[0m")

if __name__ == "__main__":
    main()
    
