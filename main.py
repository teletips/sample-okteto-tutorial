#This is the main file that helps to run the bot properly.


from pyrogram import Client, filters
import os

bot=Client(
    "Sample Bot",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

@bot.on_message(filters.command("start"))
async def start(client, message):
  await bot.send_message(message.chat.id, "Hello user, This is a very simple bot.")
  
bot.run()  
  
  
