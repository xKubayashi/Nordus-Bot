import nextcord
from nextcord.ext import commands
from nextcord import Color

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Info na temat użytkownika
    @commands.cooldown(1, 5, commands.BucketType.user) # Ogranicza czas wywoływania tej samej komendy od 1-5 sekund
    @commands.command(description="Informacje na temat użytkownika")
    async def info(self, ctx, uzytkownik:nextcord.Member=""):
        if uzytkownik is None or uzytkownik == "":
            uzytkownik = ctx.author
        infoEmbed = nextcord.Embed(title=f"Informacje o {uzytkownik.display_name}", color=Color.blue())
        infoEmbed.add_field(name=f"ID", value=uzytkownik.id)
        infoEmbed.add_field(name=f"Nazwa", value=uzytkownik.name)
        infoEmbed.add_field(name=f"Nick", value=uzytkownik.nick)
        infoEmbed.add_field(name=f"Stworzono", value=uzytkownik.created_at.strftime("%b %d %Y"))
        infoEmbed.add_field(name=f"Dołączono", value=uzytkownik.joined_at.strftime("%b %d %Y"))
        infoEmbed.add_field(name=f"Top rola", value=uzytkownik.top_role)
        infoEmbed.set_footer(text=f"Komendę użył {ctx.author.display_name}")
        infoEmbed.add_field(name=f"Liczba roli", value=str(len(uzytkownik.roles)-1))
        #await ctx.send(embed=infoEmbed, delete_after=10)
        await ctx.send(embed=infoEmbed)


def setup(client):
    client.add_cog(Info(client))