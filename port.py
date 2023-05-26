import socket
import argparse

default = "\033[0m"
green = "\033[32m"
yellow = "\033[1;33m"
cyan = "\033[9;36m"
red = "\033[1;31m"
red_bg = "\033[41m"

def banner():
	print(f"""{green}
██████╗  ██████╗ ██████╗ ████████╗   ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝   ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║█████╗███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║╚════╝╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║      ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝{default}
{red_bg}v1.7 | YT : Termux Enthusiast{default}\n""")

parser = argparse.ArgumentParser(description=banner())
parser.add_argument("-d","--domain",help="ex, google.com, ip juga bisa ex, 127.0.0.1",required=True)
argumen = parser.parse_args()

web = argumen.domain

try:
	if web:
		site = socket.gethostbyname(web)
		print(f"{yellow}IP {default}:{yellow}",site+"\033[0m")
		host = site

		daftar_port = [
		"20",
		"21",
		"22",
		"25",
		"53",
		"79",
		"80",
		"110",
		"123",
		"137",
		"138",
		"139",
		"143",
		"192",
		"389",
		"443",
		"445",
		"465",
		"500",
		"515",
		"548",
		"554",
		"587",
		"631",
		"636",
		"749",
		"993",
		"995",
		"1900",
		"2195",
		"2196",
		"2197",
		"3031",
		"3283",
		"3284",
		"3285",
		"3478",
		"3689",
		"3690",
		"4398",
		"4500",
		"5100",
		"5223",
		"5228",
		"5297",
		"5350",
		"5351",
		"5353",
		"5900",
		"8000",
		"8080",
		"9100",
		"9418",
		"16384",
		"16384",
		"16393",
		"16403",
		"42000",
		"49152"
		]

		print(f"{cyan}--- scanning ---{default}")
		for port in daftar_port:
			socket.setdefaulttimeout(1)
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			hasil = s.connect_ex((host,int(port)))

			if hasil == 0:
				print("port",str(port),"open")
				s.close()
			else:
				print("port",str(port),"closed")
				s.close()

except socket.gaierror:
	print(f"{red}Gak ada web tsb/check koneksi internet kamu")

except KeyboardInterrupt:
	print(f"{red}Yah keluar...")
