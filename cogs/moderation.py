import nextcord
from nextcord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Banowanie
    @commands.has_permissions(ban_members=True)
    @commands.command(description="`Banuje chuja`")
    async def ban(self, ctx, uzytkownik:nextcord.Member, *, powod):
        await ctx.channel.purge(limit=1)
        await uzytkownik.ban(reason=powod)

    # Odbanowanie
    @commands.has_permissions(ban_members=True)
    @commands.command(description="`Odbanuje chuja`")
    async def unban(self, ctx, uzytkownik:nextcord.Member):
        await ctx.channel.purge(limit=1)
        await uzytkownik.unban()

    # Wyrzucanie
    @commands.has_permissions(kick_members = True)
    @commands.command(description="`Wyrzucam chuja`")
    async def kick(self, ctx, uzytkownik:nextcord.Member, *, powod):
        await ctx.channel.purge(limit=1)
        await uzytkownik.kick(reason=powod)


def setup(client):
    client.add_cog(Moderation(client))