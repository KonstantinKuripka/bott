import discord
from main import neon
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$pass'):
        await message.channel.send(neon(10))
    else:
        await message.channel.send(message.content)

client.run("MTIwMTg5NTQxNDk2Njc4NDAxMA.GLmddr.gnWqbgg7jOOHNShEN9DRGm2Ggy1VjD2diYgrZg")
