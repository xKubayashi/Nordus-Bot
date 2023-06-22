import os
import nextcord
from nextcord.ext import commands
from nextcord import Embed, Color
import datetime, asyncio

# Prefix: .
client = commands.Bot(command_prefix=".", intents=nextcord.Intents.all())
client.remove_command("help")

# Bot się uruchamia:
@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Game(name="Pornhub Premium"))
    print(f"Zalogowany jako: {client.user.name}")

# Info o komendach
@commands.cooldown(1, 5, commands.BucketType.user) # Ogranicza czas wywoływania tej samej komendy od 1-5 sekund
@client.command(name="ovo", description="Komendy Nordusia")
async def komendy(ctx):
    em = nextcord.Embed(title="UwU ŇỖŘĎЎŇÃŴĮÃ UwU", description=" # Komendy Nordusia:", color=Color.blue()) # color=Color.green() - Zmieniasz kolor obramówki
    for command in client.walk_commands():
        description = command.description
        if not description or description == None or description == "":
            description = "Nic"
        em.add_field(name=f".{command.name} {command.signature}", value=description, inline=False) # inline=False - Ustawia komendy jedna pod drugą
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/804617909983903744/1113479950192881754/Zazdrosny_Nordus3.png")
        em.set_footer(text = f"Komenda użyta przez: {ctx.author.name}")
    await ctx.send(embed=em)







# Wysyłanie wiadomości wyznaczonych porach:
async def schedule_daily_message(h, m, s, msg, channelid):
    while True:
        now = datetime.datetime.now()
        # then = now+datetime.timedelta(days=1)
        then = now.replace(hour=h, minute=m, second=s)
        if then < now:
            then += datetime.timedelta(days=1)
        wait_time = (then-now).total_seconds()
        await asyncio.sleep(wait_time)

        channel = client.get_channel(channelid)

        await channel.send(msg)
        #await channel.send(random.choice(links["play"])) # Wysyła Gif, z links od json 
        await asyncio.sleep(1)



# codziennie "dzień dobry" 15 58 0
@commands.cooldown(1, 5, commands.BucketType.user) # Ogranicza czas wywoływania tej samej komendy od 1-5 sekund
@client.command(name="codziennie", description="Norduś przypomina. Wysyłaj wiadomość o wyznaczonej godzinie.")
async def codziennie(ctx, wiadomosc:str, godzina:int, minuta:int, sekunda:int):
    print(wiadomosc, godzina, minuta, sekunda)

    if not (0 < godzina < 24 and 0 <= minuta <= 60 and 0 <= sekunda < 60):
        raise commands.BadArgument()
    
    time = datetime.time(godzina, minuta, sekunda)
    timestr = time.strftime("%I:%M:%S %p")
    await ctx.send(f"Codzienna wiadomość będzie wysyłana {timestr} codziennie na tym kanale.\nCodzienna wiadomość:\"{wiadomosc}\"\nPotwierdź, pisząc po prostu: `tak`")
    try:
        msg = await client.wait_for("message", timeout=60, check=lambda message: message.author == ctx.author)
    except asyncio.TimeoutError:
        await ctx.send("Zbyt długo zwlekałeś z odpowiedzią!")
        return
    
    if msg.content == "tak":
        await ctx.send("Codzienna wiadomość zostanie wysłana!")
        await schedule_daily_message(godzina, minuta, sekunda, wiadomosc, ctx.channel.id)
    else:
        await ctx.send("Codzienna wiadomość anulowana")

@codziennie.error
async def codziennie_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("""Niepoprawny format. Użyj polecenia w ten sposób: `.codziennie "wiadomość" godzina minuta sekunda`.
Na przykład: `.codziennie "dzień dobry" 22 30 0` dla wiadomości wysyłanej codziennie o 22:30:00""")





# Zwolnij
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        em = Embed(title=f"Zwolnij!", description=f"Spróbuj ponownie za {error.retry_after:.2f}s.", color=Color.red())
        await ctx.send(embed=em)

# Importuje inne komendy .py
for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        client.load_extension(f"cogs.{fn[:-3]}")

if __name__ == "__main__":
    client.run()