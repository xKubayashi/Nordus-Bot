import nextcord
from nextcord.ext import commands
from nextcord import Intents, Embed, Color, SlashOption, Member

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client



    # Info na temat użytkownika
    @commands.cooldown(1, 5, commands.BucketType.user) # Ogranicza czas wywoływania tej samej komendy od 1-5 sekund
    @commands.command(name="profil", description="`Informacje na temat użytkownika`")
    async def profil(self, ctx, uzytkownik:nextcord.Member=""):
        if uzytkownik is None or uzytkownik == "":
            uzytkownik = ctx.author
        infoEmbed = nextcord.Embed(title=f"Informacje o {uzytkownik.display_name}", color=Color.blue())
        infoEmbed.add_field(name=f"ID", value=uzytkownik.id)
        infoEmbed.add_field(name=f"Nazwa", value=uzytkownik.name)
        infoEmbed.add_field(name=f"Nick", value=uzytkownik.nick)
        infoEmbed.add_field(name=f"Stworzono", value=uzytkownik.created_at.strftime("%b %d %Y"))
        infoEmbed.add_field(name=f"Dołączono", value=uzytkownik.joined_at.strftime("%b %d %Y"))
        infoEmbed.add_field(name=f"Top rola", value=uzytkownik.top_role)
        infoEmbed.set_footer(text=f"Komenda użyta przez: {ctx.author.display_name}")
        infoEmbed.add_field(name=f"Liczba roli", value=str(len(uzytkownik.roles)-1))
        infoEmbed.set_thumbnail(uzytkownik.display_avatar)
        #await ctx.send(embed=infoEmbed, delete_after=10)
        await ctx.send(embed=infoEmbed)


    # Info o Serverze
    @commands.cooldown(1, 5, commands.BucketType.user) # Ogranicza czas wywoływania tej samej komendy od 1-5 sekund
    @commands.command(name="server", description="`Informacje na temat serwera`")
    async def server(self, ctx):
        guild = ctx.message.author.guild
        embed=Embed(title=guild.name, color=0x0080ff)
        serverData = {
            "Właściciel" : guild.owner.mention,
            "Kanały" : len(guild.channels),
            "Obywatele" : guild.member_count,
            "Stworzono" : guild.created_at.strftime("%b %d, %Y, %T"),
            "Opis" : guild.description,
        }
        for [fieldName, fieldVal] in serverData.items():
            embed.add_field(name=fieldName+":", value=fieldVal, inline=True)
        embed.set_footer(text=f"ID: {guild.id}")
        embed.set_footer(text=f"Komenda użyta przez: {ctx.author.display_name}")

        embed.set_thumbnail(guild.icon)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Info(client))