from xolpanel import *

@bot.on(events.CallbackQuery(data=b'show-ssh'))
async def show_ssh(event):
	async def show_ssh_(event):
		cmd = "awk -F: '($3>=1000)&&($1!='nobody'){print $1}' /etc/passwd"
		x = subprocess.check_output(cmd,shell=True).decode("ascii").split("\n")
		z = []
		for us in x:
			z.append("`"+us+"`")
		zx = "\n".join(z)
		await event.respond(f"""
**Showing All SSH User**

{zx}
`
**Total SSH Account:** `{str(len(z))}`
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await show_ssh_(event)
	else:
		await event.answer("Access Denied",alert=True)
