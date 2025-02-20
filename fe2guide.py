import discord, random, os, requests
from discord.ext import commands
from configuration import settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def fe2guide(ctx):
    await ctx.send(f"""
    Hola, soy un bot {bot.user}!
    """)
    #comentarios
 
    await ctx.send("Quieres conocer quien es guide?")
    # Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content:
            await ctx.send(""" 
            Guide es un personaje del fe series (Flood Escape) el cual te guiaba y te decia informacion sobre el juego
            """)
 
        else:
            await ctx.send("Está bien, si alguna vez necesitas saber sobre otro tema, estaremos en contacto.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
 
    await ctx.send("Quieres saber más de guide? 'si' o 'no'.")
    def check1(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response1 = await bot.wait_for('message', check=check1)
    if response1:
        if response1.content == "si":
            await ctx.send("""
            El Guide ahora esta en la secuela del juego: fe2 (Flood Escape 2) pero en vez de ser un guía, ahora se volvio
            uno de los principales personajes de la serie y ahora es uno de las personas que tiene que escapar de la inundación
            """) 
        else:
            await ctx.send("Está bien, si alguna vez necesitas hablar sobre otro tema, estaremos en contacto.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("Te gustaria que te envie una foto de quien es él?")
    def check2(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response2 = await bot.wait_for('message', check=check2)
    if response2:
        if response1.content == "si":
            image_path = 'images/FE2WARRIORS_WIKI_GUIDE.webp'
 
        # Verificar si el archivo existe antes de enviarlo
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                picture = discord.File(f)
                await ctx.send("Aquí tienes a Guide:", file=picture)
        else:
            await ctx.send("Lo siento, no pude encontrar la imagen. Verifica que la ruta sea correcta.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")

bot.run(settings["TOKEN"])
