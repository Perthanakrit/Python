#914146965124689981
import discord
from discord.ext import commands


'''chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()'''

print("Client running....")

#client = discord.Client()
client = commands.Bot(command_prefix="!")


'''@client.event
async def on_ready():
    print('We have logged in as{0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.content.author == client.user:
        return

    if message.content.startswith('$chat'):    
        await message.channel.send('Hi')
'''
@client.command()
async def playsong(ctx, url:str,):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name ='General')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if not voice.is_conneted():
        await voiceChannel.connet()

@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await  ctx.send('')

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_pause():
        voice.resume()
    else:
        await  ctx.send('')


client.run('OTE0MTQ2OTY1MTI0Njg5OTgx.YaIztA.MpHviwFSb1FiU1B7Gl18SFch3Wk')
