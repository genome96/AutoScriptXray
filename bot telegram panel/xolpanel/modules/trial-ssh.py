from xolpanel import *

@bot.on(events.CallbackQuery(data=b'trial-ssh'))
async def trial_ssh(event):
	async def trial_ssh_(event):
		user = "trialX"+str(random.randint(100,1000))
		pw = "1"
		exp = "1"
		cmd = f'useradd -e `date -d "{exp} days" +"%Y-%m-%d"` -s /bin/false -M {user} && echo "{pw}\n{pw}" | passwd {user}'
		try:
			subprocess.check_output(cmd,shell=True)
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			msg = f"""
**━━━━━━━━━━━━━━━━**
**⟨ Trial SSH Account ⟩**
**━━━━━━━━━━━━━━━━**
**» Host:** `{DOMAIN}`
**» Username:** `{user.strip()}`
**» Password:** `{pw.strip()}`
**━━━━━━━━━━━━━━━━**
**» OpenSSH:** `22`
**» SSL/TLS:** `222`, `777`, `443`
**» Dropbear:** `109`,`143`
**» WS SSL:** `443`
**» WS HTTP:** `80`
**» Squid:** `8080`, `3128` `(Limit To IP Server)`
**» BadVPN UDPGW:** `7100` **-** `7300`
**━━━━━━━━━━━━━━━━**
**⟨ Payload WS CDN ⟩**
`GET / HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Connection: Keep-Alive[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]`
**━━━━━━━━━━━━━━━━**
**» 🗓Expired Until:** `{later}`
**» 🤖@driwwvpn**
**━━━━━━━━━━━━━━━━**
"""
			inline = [
[Button.url("[ Contact ]","t.me/driwwvpn"),
Button.url("[ Channel ]","t.me/driwwvpn_grup")]]
			await event.respond(msg,buttons=inline)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
