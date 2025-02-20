import discord, random, os, requests
from discord.ext import commands
from configuration import settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def joined(ctx, member: discord.Member):
    # Says when a member joined.
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def suma(ctx, n1:int, n2:int):
    await ctx.send(f"La suma de {n1} con {n2} es {n1 + n2}")

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def mem(ctx):
    with open('images/meme1.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def memes(ctx):
    images = os.listdir('images')
    with open(f'images/{random.choice(images)}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)
    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un pokemon")

@bot.command()
async def contaminacion(ctx):
    await ctx.send(f"""
    Hola, soy un bot {bot.user}!
    """)
    #comentarios
 
    await ctx.send("Quieres conocer de que trata la contaminación?")
    # Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content:
            await ctx.send(""" 
            La contaminacion afecta a los grandes ecosistemas naturales que tenemos, como las selvas y los bosques...
            También hace que la temperatura en el planeta aumente, generando el calentamiendo global.
            """)
 
        else:
            await ctx.send("Está bien, si alguna vez necesitas saber sobre otro tema, estaremos en contacto.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
 
    await ctx.send("Quieres mas ejemplos sobre contaminación'si' o 'no'.")
    def check1(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response1 = await bot.wait_for('message', check=check1)
    if response1:
        if response1.content == "si":
            await ctx.send("""
            El calentamiento global hace que los polos se descongelen, por lo tanto el nivel de los mares aumenta.
            Provocando así la muerte de la fauna y la flora que habita en esas zonas.
            """) 
        else:
            await ctx.send("Está bien, si alguna vez necesitas hablar sobre otro tema, estaremos en contacto.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("Te gustaria que te envie una foto sobre un ejemplo de contaminación?")
    def check2(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response2 = await bot.wait_for('message', check=check2)
    if response2:
        if response1.content == "si":
            image_path = 'images/contaminacion.jpeg'
 
        # Verificar si el archivo existe antes de enviarlo
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                picture = discord.File(f)
                await ctx.send("Aquí tienes un ejemplo de contaminación:", file=picture)
        else:
            await ctx.send("Lo siento, no pude encontrar la imagen. Verifica que la ruta sea correcta.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")

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

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

bot.run(settings["TOKEN"])
