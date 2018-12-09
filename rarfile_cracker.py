import rarfile


def unrar(passwd, rar_file):
	fileload = rarfile.RarFile(rar_file)
	fileload.UNRAR_TOOL = "UnRAR.exe"
	fileload.extractall("cracked_file", pwd = passwd)



while True:
	rar_file = input("enter rar file path: ")
	pass_file = input("enter password list path: ")

	passfile = open(pass_file, "r")
	passwords = passfile.readlines()
	for passwd in passwords:
		passwd = passwd.rstrip("\n")
		try:
			unrar(passwd, rar_file)
			print ("[+] PASSWORD FOUND & FILE CRACKED: " + passwd)
			break;
		except:
			print ("[-] wrong password: " + passwd)

	input("press <enter> to continue ...")
	