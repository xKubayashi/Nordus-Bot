import nextcord
from nextcord.ext import commands
from nextcord import Color

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Witanie
    @commands.cooldown(1, 5, commands.BucketType.user) # Ogranicza czas wywoływania tej samej komendy od 1-5 sekund
    @commands.command(description="Norduś cię wita")
    async def witaj(self, ctx, uzytkownik:nextcord.Member):
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{ctx.author.mention} wita chuja {uzytkownik.mention}!")

    # Furry Pornos
    @commands.cooldown(1, 5, commands.BucketType.user) # Ogranicza czas wywoływania tej samej komendy od 1-5 sekund
    @commands.command(description="Furry Porno")
    async def cosinus(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("# Furry Porno")

    # Ping
    @commands.cooldown(1, 5, commands.BucketType.user) # Ogranicza czas wywoływania tej samej komendy od 1-5 sekund
    @commands.command(description="Chujowy Ping")
    async def ping(self, ctx):
        await ctx.send("Pong!")
    
    # Tags
    @commands.cooldown(1, 5, commands.BucketType.user) # Ogranicza czas wywoływania tej samej komendy od 1-5 sekund
    @commands.command(description="Nwm")
    async def nwm(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("newem")

    # Pokazuje Avatar Usera
    @commands.cooldown(1, 5, commands.BucketType.user) # Ogranicza czas wywoływania tej samej komendy od 1-5 sekund
    @commands.command(description="Pokazuje avatar użytkownika")
    async def avatar(self, ctx, *, uzytkownik:nextcord.Member = ""):
        if uzytkownik is None or uzytkownik == "":
            uzytkownik = ctx.author
    
        avatarUrl = uzytkownik.avatar.url
        avatarEmbed = nextcord.Embed(title=f"Avatar {uzytkownik.name} :", color=Color.blue())
        avatarEmbed.set_thumbnail(url=avatarUrl)
        avatarEmbed.set_footer(text = f"Komenda użyta przez: {ctx.author.name}")
        #avatarEmbed.set_footer(text=f"Komendę użył {ctx.author.display_name}")

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=avatarEmbed)

def setup(client):
    client.add_cog(Fun(client))