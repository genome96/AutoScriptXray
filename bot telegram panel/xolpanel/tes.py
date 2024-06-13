@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply("@darkanonc")


print("welcome")
