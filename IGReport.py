from instabot import Bot
import random as r

def pass_gen(length):
	lower = "abcdefghijklmnñopqrstuvwxyz"
	upper = lower.upper()
	numbers = "123456789"
	symbols = "+{}/&=?¿¡!#$%.,_-"
	whole = lower+upper+numbers+symbols
	password01 = ""
	for i in range(length):
		password=password01+r.choice(whole)

def gen_user(length):
	lower = "abcdefghijklmnñopqrstuvwxyz"
	upper = lower.upper()
	numbers = "123456789"
	whole = lower+upper+numbers
	user01 = ""
	for i in range(length):
		user=user01+r.choice(whole)

my_bot = Bot()

print(
'''
_______________________                          _____ 
____  _/_  ____/__  __ \___________________________  /_
 __  / _  / __ __  /_/ /  _ \__  __ \  __ \_  ___/  __/
__/ /  / /_/ / _  _, _//  __/_  /_/ / /_/ /  /   / /_  
/___/  \____/  /_/ |_| \___/_  .___/\____//_/    \__/  
                            /_/                                  
''')
print("Instagram: vicxssj")
print("TikTok: JK-KP")
print("WhatsApp: {unknown}")
print("\033[93m"+"NO ME HAGO RESPONSABLE DEL MAL USO QUE SE LE DE A LA HERRAMIENTA"+"\033[0m")

user_banned = input("Inserta el username de la persona que quieres reportar: ")
#times_reports = input("Inserta las veces que lo quieres tratar de reportar(Sugerido 100): ")

while True:
	user=gen_user(8)
	password=pass_gen(8)
	my_bot.login(username=user, password=password)
	my_bot.follow(user_banned)
	numero=0
	print("Cuenta reportada "+numero+" veces.")
	numero+=1
