import nextcord
from nextcord.ext import commands
import requests
from nextcord import Color

class Psy(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Fotki Psów
    @commands.cooldown(1, 5, commands.BucketType.user) # Ogranicza czas wywoływania tej samej komendy od 1-5 sekund
    @commands.command(name="psy", description="Zdjęcia Psów")
    async def Dog(self, ctx):
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        image_link = response.json()["message"]
        await ctx.send(image_link)
    
def setup(client):
    client.add_cog(Psy(client))