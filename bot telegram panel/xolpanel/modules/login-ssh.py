from xolpanel import *

@bot.on(events.CallbackQuery(data=b'login-ssh'))
async def login_ssh(event):
	async def login_ssh_(event):
		x = subprocess.check_output('bash xolpanel/cek.sh',shell=True).decode("ascii")
		date = DT.date.now()
		text2png(u"%s" % x, 'login.png', fontfullpath = "xolpanel/font.ttf")
		await event.respond(f"""
**Dropbear, OpenSSH, & OpenVPN Login Check**
**Date:** `{date}`
""",file="login.png")
		os.remove("login.png")
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await login_ssh_(event)
	else:
		await event.answer("Access Denied",alert=True)
