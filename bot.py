#ada ini gegara ntar kalo mau di tambah2in bisa. soalnya aku ga ngerti
import discord
from discord.ext import commands, tasks
from discord.ext.commands import bot
from itertools import cycle
import asyncio
import datetime
import random
from discord import Embed

#!!!!!HATI HATI DENGAN INDENTASI!!!!!
#no cmd prefix
#this bot just for fun
    
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

        activity = discord.Game(name="Sedang melayani anda o(^▽^)o • ketik '+help' untuk melihat info Nadira")
        await client.change_presence(status=discord.Status.idle, activity=activity)

    async def on_member_join(member): ## welcome message for new member but doesn't work bruh
        print("** " + member.name + " joined")
        welcome_message = member.name + "Selamat datang di Urumachi server!! Nyaaaa! (⁎˃ᆺ˂)♡*✲ﾟ*｡"
        channel = client.get_channel("715276743250018394")
        await client.send_message(channel, welcome_message)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong (^･ｪ･^)')

        if message.content == 'halo':
            await message.channel.send('Haloooowww ฅ•ω•ฅ {0.author.mention}'.format(message))
        
        if message.content == 'hai':
            await message.channel.send('Haloooowww ฅ•ω•ฅ {0.author.mention}'.format(message))

        if message.content == 'pagi':
            await message.channel.send('Pagi jugaaaaa!! ฅ•ω•ฅ {0.author.mention}'.format(message))
        
        if message.content == 'selamat pagi':
            await message.channel.send('Selamat pagiiiii (=^ェ^=){0.author.mention}'.format(message))
        
        if message.content == 'selamat siang':
            await message.channel.send('Selamat siangggg (=^ェ^=){0.author.mention}'.format(message))

        if message.content == 'siang':
            await message.channel.send('Selamat ugaaaa (⁎˃ᆺ˂){0.author.mention}'.format(message))
        
        if message.content == 'malam':
            await message.channel.send('Malam jugaaa (ฅ￫ω￩ฅ){0.author.mention}'.format(message))

        if message.content == 'selamat malam':
            await message.channel.send('Selamat malammm (^･ｪ･^){0.author.mention}'.format(message))

        if message.content == 'sore':
            await message.channel.send('Sore jugaaaaaa =^∇^*={0.author.mention}'.format(message))

        if message.content == 'selamat sore':
            await message.channel.send('Selamat soree! (=ﾟωﾟ=){0.author.mention}'.format(message))

        if message.content == 'psps':
            await message.channel.send('Nyaaaaaan!!!! (⁎˃ᆺ˂)')

 ##       if message.content == 'tes':
   ##         await message.channel.send('tis')


        if message.content == "+help":
            embed = discord.Embed(title="Nadira Nanami", description="Hai! Namaku Nadira Nanami. Aku seorang Maid-Cat Girl yang akan melayani kalian di server ini! (▰∀◕)ﾉ Semoga betah ya!!!! Maaf keberadaanku masih dalam perkembangan. Jika ada masalah, minta maaf ya :wbm:\nTugas Nadira di server ini:", color=0x00f0ff)
            embed.add_field(name="1. Menyapa orang yang ada di server\n2. Mengingatkan orang untuk tidak berkata kasar (beta & dinonaktikan)\n3. (Masih dalam pengembangan dan kedepannya akan di tambahkan fitur fitur keren)\nDan sementara hanya itu (✿ヘᴥヘ)", value="Note:\nBot ini hanya dipakai di server Urumachi, bertujuan dan digunakan hanya untuk senang-senang saja. Jika ada masukkan hubungi chief ;)")
            await message.channel.send(content=None, embed=embed)

        ##if message.content == "+rules":
            ##channel=("rules-and-announcement")
            ##await message.channel.send(file=discord.File('urumachi_1.gif'))
            ##await message.channel.send("Selamat Datang di Urumachi Server! (ﾉ≧ڡ≦)\nUrumachi adalah sebuah desa kecil virtual yang memiliki rakyat yang jumlahnya sedikit. Tidak hanya manusia, tetapi ada beberapa Dewa yang hidup disini. Para pedatang baru biasanya akan menjadi rakyat dari desa ini.\nINTINYA TOLONG BACA PERATURAN SERVER INI DULU YA!")
            ##await message.channel.send("1. First of all, server ini digunakan hanya untuk bersenang-senang saja.\n2. Boleh mengisi dan berkata apapun di #main-channel kecuali NSFW Content dan dilarang membagi NUKE CODE.\n3. NSFW dan Nuke code bisa di bagikan secara puas di channel #nsfwplusnuke\n4. Jika ingin membagikan sesuatu agar mudah ternotice orang, kalian bisa mengirim kontennya di papan pengumuman, channel #sharing\n5. Jika kalian ingin melelang dan gacha wanita/pria impian anda, bisa dilakukan di #gacha-waifu\n6. Boleh gunakan bot music di voice chat, asalkan satu aja dan commandnya di tulis di channel #music biar main channel gak kespam.\n7. Boleh usul saran apa aja misal role dan sebagainya ke Dewa atau Chief.\n8. Saling membantu dan menghargai (ゝω･) intinya HAFE VUN\nwelcome!! (⁎˃ᆺ˂)")

        if message.content.startswith('+rules'):
            embedVar = discord.Embed(title='Selamat Datang di Urumachi Server! (ﾉ≧ڡ≦)', description='Urumachi adalah sebuah desa kecil virtual yang memiliki rakyat yang jumlahnya sedikit. Tidak hanya manusia, tetapi ada beberapa Dewa yang hidup disini. Para pedatang baru biasanya akan menjadi rakyat dari desa ini.\nINTINYA TOLONG BACA PERATURAN SERVER INI DULU YA!\n1. First of all, server ini digunakan hanya untuk bersenang-senang saja.\n2. Boleh mengisi dan berkata apapun di #main-channel kecuali NSFW Content dan dilarang membagi NUKE CODE.\n3. NSFW dan Nuke code bisa di bagikan secara puas di channel #nsfwplusnuke\n4. Jika ingin membagikan sesuatu agar mudah ternotice orang, kalian bisa mengirim kontennya di papan pengumuman, channel #sharing\n5. Jika kalian ingin melelang dan gacha wanita/pria impian anda, bisa dilakukan di #gacha-waifu\n6. Boleh gunakan bot music di voice chat, asalkan satu aja dan commandnya di tulis di channel #music biar main channel gak kespam.\n7. Boleh usul saran apa aja misal role dan sebagainya ke Dewa atau Chief.\n8. Saling membantu dan menghargai (ゝω･) intinya HAFE VUN', color=0x00f0ff)
            await message.channel.send(file=discord.File('urumachi_1.gif'))
            await message.channel.send(embed=embedVar)

        ## BETA 1.0
##        bad_words = ["asu", "jancok", "bajingan", "nigga", "bangsat", "penis", "nigger", "fuck", "tolol", "cock", "kontol", "memek", "titit", "goblok", "asw", "pussy", "tai", "jembod", "jembud", "jembut", "jembot"]
##        for word in bad_words:
##            if message.content.count(word) > 0:
##                await message.channel.purge(limit=1)
##            if message.content.count(word) > 0:
##                await message.channel.send('Jangan omong kasar yaa! (=ﾟωﾟ=){0.author.mention}'.format(message))
            
        if message.content.startswith('+update'):
            embed=discord.Embed(title="Nadira Update v1.0 beta", description="Added new command welcome message to new member who join to the server (BETA) - Nonactivated\nAdded update command", color=0x00fffb)
            embed.set_author(name="suprcream", url="https://twitter.com/suprcream_gg")
            embed.set_footer(text="still no prefix command bruh\nhubungi chief untuk memberi saran fitur bot!")
            await message.channel.send(embed=embed)


@commands.command()
async def join_voice(self, ctx):
    connected = ctx.author.voice
    if connected:
        await connected.channel.connect() # use the channel object you put into a variable

client = MyClient()
client.run('token') ##ini token bot