import discord
from discord.ext import commands
from discord.ext.commands.core import command
import asyncio
import os
import random
import re
import asyncpraw
from pretty_help import PrettyHelp
import datetime

TOKEN = str(os.environ['TOKEN'])

#bot configs
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="amanda ", intents = intents)

#pretty help configs
color = 0x179c34
bot.help_command = PrettyHelp(color=color)

# REGULAR EXPRESSIONS
marcos_regex = re.compile(r"\bmarcos\b")

#reddit config
reddit = asyncpraw.Reddit(client_id = "oZjbB_dKb_RUhw",
                     client_secret = os.environ['secret'],
                     username = "_marcos123",
                     password = os.environ['password'],
                     user_agent = "marcos")


sapos = ["https://cdn.wallpapersafari.com/41/15/xZomb3.jpg", "http://2.bp.blogspot.com/-VirjBRtnyIU/TyfUR2dSi_I/AAAAAAAAB8E/8jDDSBmWs1E/s1600/Cute+Frog4.jpg",
         "https://shopzoki.com/wp-content/uploads/2019/09/IMG_5617.jpg", "https://shopzoki.com/wp-content/uploads/2019/09/DSC_1370.jpg", 
         "https://i.pinimg.com/236x/f1/1f/c9/f11fc918f1aafa2ec38dccb0e5e3b338.jpg", "https://i.pinimg.com/474x/df/33/5e/df335ea92fe0a565859a1dbe0aeed2e0.jpg",
         "https://i.pinimg.com/474x/8e/d9/64/8ed9641c7ce86176250727efd8f80d75.jpg", "https://cdn.discordapp.com/attachments/813841826666250291/823972345882345492/Waldo.png",
         "https://i.pinimg.com/564x/61/e3/67/61e3671e1a30d3d6369d9923f884dd2f.jpg", "https://i.pinimg.com/564x/fb/c1/4d/fbc14d43bf507209c379fd32be9c5e16.jpg",
         "https://i.pinimg.com/564x/c1/9a/27/c19a27513bba99b27755395b329414e0.jpg", "https://i.pinimg.com/564x/85/d4/b8/85d4b80df2a79db4d429f51ca5792431.jpg",
         "https://i.pinimg.com/474x/be/a6/5f/bea65f563cd5993ebf6b52bd4ae9f3d2.jpg", "https://i.pinimg.com/564x/39/77/de/3977debb17a4aac4c78e7aff4f1c668a.jpg",
         "https://i.pinimg.com/474x/7b/e5/ce/7be5ceb27a15b131cc8c276162b4ae17.jpg", "https://tenor.com/view/h%C3%A2m-frog-toad-frog-l%E1%BA%AFc-wiggle-gif-14557565",
         "https://tenor.com/view/frog-spinning-vinyl-animal-carnivorous-gif-17270183", "https://tenor.com/view/frog-gail-fail-let-me-have-it-gif-12024489"]

sexos = ["https://tenor.com/view/horny-jail-bonk-dog-hit-head-stop-being-horny-gif-17298755", "https://media.discordapp.net/attachments/409313701888393218/715292714622517328/meme.gif",
        "https://media.discordapp.net/attachments/635466696609759232/762026840457871390/caption.gif"]

#changes discord presence
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('Shawty'))
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

#send random frog image
@bot.command(help = "🐸")
async def sapinho(ctx):
    sapo = random.choice(sapos)
    await ctx.reply(sapo)

#send shawty
@bot.command(help = "na na na na everyday")
async def shawty(ctx):
    await ctx.reply("https://www.youtube.com/watch?v=c6gV5J5C1Cg")

#send sexo gif
@bot.command(help = "bonk, go to horny jail")
async def sexo(ctx):
    sexo = random.choice(sexos)
    await ctx.reply(sexo)

#replies with class link
@bot.command(help = "link po lima")
async def aulas(ctx):
    guild = bot.get_guild(759849368966004767)
    embed_aulas1 = discord.Embed()
    embed_aulas1.title = "Aulas MIEIC"
    embed_aulas1.description = '''\nCMAT \n([seg](https://videoconf-colibri.zoom.us/j/87558364347?pwd=MStyUVpPSlEycmZvbWcrNGF0NnJxZz09) 9:00-10:00 | [qua](https://videoconf-colibri.zoom.us/j/86166483975?pwd=VlRZelRvbjJzMmtXc1dsMDlnNTh0QT09) 10:00-11:00)
    [FIS1](https://videoconf-colibri.zoom.us/j/82373725282?pwd=S1VrNEp4VkZYR2o1TUlPUW1hLzVhZz09)      \n(seg 10:00-11:00 | qua 9:00-10:00)
    [PROG](https://teams.microsoft.com/l/channel/19%3a0a486ea7628247de956d27755601308e%40thread.tacv2/Geral?groupId=b05f83cd-100e-4c31-a797-146513c69887&tenantId=b7821bc8-67cc-447b-b579-82f7854174fc) \n(seg 11:00-12:30 | qui 9:00-10:30)
    [MPCP](https://videoconf-colibri.zoom.us/j/81799571785?pwd=T0U2NEdCTkd6ODhFMmVoTTJ3bHA2dz09) \n(qui 10:30-12:30)
    [MEST](https://videoconf-colibri.zoom.us/j/83335195718?pwd=QW1mTisxZkdFOVM4Y1lHSDRoUU84UT09) \n(qua 11:00-13:00)

    -- TURMA 3 --   
    [FISI](https://us02web.zoom.us/j/5187730519?pwd=VUpVUGFjVVZXeE1PakFKSHBIa2IwZz09)
    [CMAT](https://videoconf-colibri.zoom.us/j/89216289853)
    [MPCP](https://videoconf-colibri.zoom.us/j/84523046353?pwd=bTNVemVqQk1YQ0lTcDVTMEtiUDNKUT09)
    [MEST](https://videoconf-colibri.zoom.us/j/85894404142?pwd=N09zK29OaVFoWVZEaVRPMXZuYnQwZz09)'''

    embed_aulas2 = discord.Embed()
    embed_aulas2.title = "Aulas Turma 3"
    embed_aulas2.description = '''[FISI](https://us02web.zoom.us/j/5187730519?pwd=VUpVUGFjVVZXeE1PakFKSHBIa2IwZz09)
    [CMAT](https://videoconf-colibri.zoom.us/j/89216289853)
    [MPCP](https://videoconf-colibri.zoom.us/j/84523046353?pwd=bTNVemVqQk1YQ0lTcDVTMEtiUDNKUT09)
    [MEST](https://videoconf-colibri.zoom.us/j/85894404142?pwd=N09zK29OaVFoWVZEaVRPMXZuYnQwZz09)'''

    if (guild.get_member(809036224957513748).status == discord.Status.offline):  #replacing botinha's shifts
        await ctx.reply(embed = embed_aulas1)
    else:
        await ctx.reply(embed = embed_aulas2)

#gets reddit frog
@bot.command(help = "sends top forggo on reddit !")
async def sapo(ctx):
    subreddit = await reddit.subreddit("frog")
    all_subs = []

    top = subreddit.top("month", limit = 100)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title = name, timestamp=datetime.datetime.utcnow())
    emb.set_image(url = url)
    emb.color = 0xc4ffed

    await ctx.reply(embed = emb)

#gets reddit danger noodle
@bot.command(help = "sends top danger noodles on reddit !")
async def snek(ctx):
    subreddit = await reddit.subreddit("Sneks")
    all_subs = []

    top = subreddit.top("month", limit = 70)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title = name, timestamp=datetime.datetime.utcnow())
    emb.set_image(url = url)
    emb.color = 0xc4ffed

    await ctx.reply(embed = emb)

#gets reddit star wars meme
@bot.command(help = "sends poggers prequel meme")
async def palpatine(ctx):
    subreddit = await reddit.subreddit("PrequelMemes")
    all_subs = []

    top = subreddit.top("month", limit = 70)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title = name, timestamp=datetime.datetime.utcnow())
    emb.set_image(url = url)
    emb.color = 0xc4ffed

    await ctx.reply(embed = emb)

#gets super awesome kanye meme
@bot.command(help = "kayne")
async def kanye(ctx):
    subreddit = await reddit.subreddit("WestSubEver")
    all_subs = []

    top = subreddit.top("month", limit = 50)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title = name, timestamp=datetime.datetime.utcnow())
    emb.set_image(url = url)
    emb.color = 0xe6c655

    await ctx.reply(embed = emb)

#replies with nerdices
@bot.command(help = "sends relatable nerd shid")
async def src(ctx):
    subreddit = await reddit.subreddit("ProgrammerHumor")
    all_subs = []

    top = subreddit.top("month", limit = 70)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title = name, timestamp=datetime.datetime.utcnow())
    emb.set_image(url = url)
    emb.color = 0xc4ffed

    await ctx.reply(embed = emb)

#replies with nerdices
@bot.command(help = "communism")
async def comuna(ctx):
    subreddit = await reddit.subreddit("CommunismMemes")
    all_subs = []

    top = subreddit.top("month", limit = 50)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title = name, timestamp=datetime.datetime.utcnow())
    emb.set_image(url = url)
    emb.color = 0xff0015
    await ctx.reply(embed = emb)

#replies with epicc anime meme
@bot.command(help = "epicc anime")
async def weeb(ctx):
    subreddit = await reddit.subreddit("animememes")
    all_subs = []

    top = subreddit.top("month", limit = 70)

    async for submission in top:
        if ("i.redd.it" in submission.url) and (len(submission.title) < 256):
            all_subs.append(submission)

    random_submission = random.choice(all_subs)

    name = random_submission.title
    url = random_submission.url

    emb = discord.Embed(title = name, timestamp=datetime.datetime.utcnow())
    emb.set_image(url = url)
    emb.color = 0xbdfffd
    await ctx.reply(embed = emb)

#replies to marcos
@bot.event
async def on_message(msg: discord.Message):
    await bot.process_commands(msg) 
    m: str = msg.content.lower()

    if marcos_regex.search(m) is not None:
        emb = discord.Embed(url = "https://cdn.discordapp.com/attachments/796509327997403156/823914978397388831/badady.mp4")

        print(msg.author)
        if ("footvaalvica" in str(msg.author)):
            await msg.reply(emb)
        else:
            await msg.reply("https://cdn.discordapp.com/attachments/796509327997403156/823914978397388831/badady.mp4")


bot.run(TOKEN)