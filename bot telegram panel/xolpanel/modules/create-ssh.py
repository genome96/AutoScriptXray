from xolpanel import *

@bot.on(events.CallbackQuery(data=b'create-ssh'))
async def create_ssh(event):
	async def create_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Password:**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**Choose Expiry Day**",buttons=[
[Button.inline("• 7 Day •","7"),
Button.inline("• 15 Day •","15")],
[Button.inline("• 30 Day •","30"),
Button.inline("• Lifetime •","500")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
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
**⟨ SSH Account ⟩**
**━━━━━━━━━━━━━━━━**
**» Host:** `{DOMAIN}`
**» Username:** `{user.strip()}`
**» Password:** `{pw.strip()}`
**━━━━━━━━━━━━━━━━**
**» OpenSSH:** `22`
**» SSL/TLS:** `222`, `777`, `443`
**» Dropbear:** `109`,`143`
**» WS SSL:** `443`
**» WS HTTP:** `80`, `8080`
**» Squid:** `8080`, `3128` `(Limit To IP Server)`
**» BadVPN UDPGW:** `7100` **-** `7300`
**━━━━━━━━━━━━━━━━**
**⟨ Payload WS  ⟩**
`GET / HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Upgrade: websocket[crlf][crlf]`
**⟨ Payload WS SSL ⟩**
`GET wss:/// HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Upgrade: websocket[crlf]Connection: Keep-Alive[crlf][crlf]`
**━━━━━━━━━━━━━━━━**
**» 🗓Expired Until:** `{later}`
**» 🤖@driwwvpn**
**━━━━━━━━━━━━━━━━**
"""
			inline = [
[Button.url("[ Contact ]","t.me/givpn"),
Button.url("[ Channel ]","t.me/givpn_grup")]]
			await event.respond(msg,buttons=inline)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
