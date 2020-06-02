
import requests
import sys
from termcolor import cprint
import time

class Main():
	def __init__(self):
		self.banner()
		if (len(sys.argv) > 1):
			self.help()
			sys.exit()
		cprint("Enter Site (example.com): ","white",end="")
		self.site = input()
		if (self.site == "Exit" or self.site == "exit"):
			sys.exit()
		else:
			cprint("/\/\/\/ Running /\/\/\/","cyan")
			self.subdomainFinder()


	def subdomainFinder(self):
		response = requests.get('https://crt.sh/?q=%s'%(self.site))
		all_unfiltered_Subdomains = []
		if response:
			all_list = response.text.split("\n")
			for i in all_list:
				if (self.site in i and "TD" in i and 'class="outer"' not in i):
					i = i.replace("<TD>","")
					i = i.replace("</TD>","")
					i = i.replace(" ","")

					filtered = i.split("<BR>")
					for subdomain in filtered:
						all_unfiltered_Subdomains.append(subdomain)

				elif ("None found" in i):
					print("")
					cprint("[-] Found None !!!","red")
					sys.exit()

			all_filtered_Subdomains = list(set(all_unfiltered_Subdomains))
			print("")
			time.sleep(1)
			cprint("[ Found Subdomains]","yellow")
			cprint("\n".join(all_filtered_Subdomains),"blue")
			print("\n")

		else:
			print("")
			cprint("Invaild Site","red")
			sys.exit()


	def banner(self):
		cprint('''
┌─┐┬ ┬┌┐ ╔╦╗┌─┐┌┬┐┌─┐┬┌┐┌  ╔═╗┬┌┐┌┌┬┐┌─┐┬─┐
└─┐│ │├┴┐ ║║│ ││││├─┤││││  ╠╣ ││││ ││├┤ ├┬┘
└─┘└─┘└─┘═╩╝└─┘┴ ┴┴ ┴┴┘└┘  ╚  ┴┘└┘─┴┘└─┘┴└─
					--- ShaFdo
			''',"cyan")

	def help(self):
		cprint('''
[ USAGE ]
	python3 subdomianFinder.py
			''',"white")


run = Main()
