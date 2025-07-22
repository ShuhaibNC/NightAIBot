HELP_TEXT = """
I dont know how to help you, but you can try these commands:    

SYSTEM COMMANDS:
 /start - <code>to start the bot</code>
 /help - <code>to get help</code>
 /stats - <code>Get bot statistics</code>
 /ping - <code>Check the bot's response time</code>
 /speedtest - <code>Run a speed test</code>
 
BASIC COMMANDS:
 /msone - <code>to get the malayalam subtitle file from msone</code>
 /github - <code>Returns info about a GitHub user or organization.</code>
 /lyrics - <code>returns the lyrics of that song.</code>
 /tts - <code>Convert text to speech</code>
 /gifid - <code>Get the ID of a gif</code>
 /stickerid - <code>Get the ID of a sticker</code>
 /getsticker - <code>Get a sticker png by replying it</code>
 
MATH COMMANDS:
 /simplify - <code>simplify a mathematical expression</code>
 /factor - <code>factor a mathematical expression</code>
 /derive - <code>find the derivative of a mathematical expression</code>
 /integrate - <code>find the integral of a mathematical expression</code>
 /zeroes - <code>find the zeroes of a mathematical expression</code>
 /tangent - <code>find the tangent line of a mathematical expression at a given point</code>
 /area - <code>find the area under a mathematical expression between two points</code>
 /cos - <code>find the cosine of a number</code>
 /sin - <code>find the sine of a number</code>
 /tan - <code>find the tangent of a number</code>
 /arccos - <code>find the arccosine of a number</code>
 /arcsin - <code>find the arcsine of a number</code>
 /arctan - <code>find the arctangent of a number</code>
 /abs - <code>find the absolute value of a number</code>
 /log - <code>find the logarithm of a number</code>
 
FUN COMMANDS:
 /love - <code>love siren ❤️</code>
 /hack - <code>hack a user 👨‍💻</code>
 /bombs - <code>bombing 💣</code>
 /blockanimation - <code>block animation ⬜</code>
 /police - <code>police siren 🚨</code>

JOKE COMMANDS:
 /runs - <code>reply a random string from an array of replies.</code>
 /shrug - <code>get shrug XD.</code>
 /table - <code>get flip/unflip :v.</code>
 /decide - <code>Randomly answers yes/no/maybe</code>
 /toss - <code>Tosses A coin</code>
 /bluetext - <code>check urself :V</code>
 /roll - <code>Roll a dice.</code>
 /rlg - <code>Join ears,nose,mouth and create an emo ;-;</code>
 /pings - <code>Get a random ping string.</code>
 /abuse - <code>Get a random abuse string.</code>
 /items - <code>Get a random item from an array of items.</code>
 /hit - <code>Get a random hit string.</code>
 /throw - <code>Get a random throw string.</code>
"""

START_TEXT = """
It's NightAI Bot 🤖
<blockquote>A failed attempt of multipurpose experimental bot</blockquote>

For help hit /help
"""

ID_TEXT = """
<b>Firstname</b>: <code>{}</code>
<b>Lastname</b>: <code>{}</code>
<b>Username</b>: <code>{}</code>
<b>ID</b>: <code>{}</code>
<b>Datacenter</b>: <code>{}</code>
<b>ChatID</b>: <code>{}</code>
"""

STATUS_TXT = """<b>

👤 Total Users: <code>{}</code>

🗄️ Server: <code>AWS</code>

💾 Memory: <code>64GB</code>

🖥️ CPU: <code>8 Cores Xeon</code>

🌐 Uptime: <code>69.99%</code>

🧩 Bot Version: <code>v0.1.0</code>
</b>

"""

block_chain = [
             "🟥",
             "🟧",
             "🟨",
             "🟩",
             "🟦",
             "🟪",
             "🟫",
             "⬛",
             "⬜",
             "🟥",
             "🟧",
             "🟨",
             "🟩",
             "🟦",
             "🟪",
             "🟫",
             "⬛",
             "⬜"
]

love_siren = [
            "❤️❤️❤️🧡🧡🧡💚💚💚\n💙💙💙💜💜💜🖤🖤🖤",
            "🖤🖤🖤💜💜💜💙💙💙\n❤️❤️❤️🧡🧡🧡💚💚💚",
            "💛💛💛💙💙💙❤️❤️❤️\n💜💜💜❤️❤️❤️🧡🧡🧡",
            "❤️❤️❤️🧡🧡🧡💚💚💚\n💙💙💙💜💜💜🖤🖤🖤",
            "🖤🖤🖤💜💜💜💙💙💙\n❤️❤️❤️🧡🧡🧡💚💚💚",
            "💛💛💛💙💙💙❤️❤️❤️\n💜💜💜❤️❤️❤️🧡🧡🧡",
            "❤️❤️❤️🧡🧡🧡💚💚💚\n💙💙💙💜💜💜🖤🖤🖤",
            "🖤🖤🖤💜💜💜💙💙💙\n❤️❤️❤️🧡🧡🧡💚💚💚",
            "💛💛💛💙💙💙❤️❤️❤️\n💜💜💜❤️❤️❤️🧡🧡🧡"
]


hack_you = [
            "Looking for Telegram databases in targeted person...",
            " User online: True\nTelegram access: True\nRead Storage: True ",
            "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]",    
            "Hacking... 86.21%\n[███████████████░░░░░]",
            "Hacking... 93.50%\n[█████████████████░░░]",
            "hacking....  100%\n[████████████████████]",
]

police_siren = [
            "🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵\n🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵",
            "🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴\n🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴"
]




bomb_ettu = [
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️",
             "💣💣💣💣\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️", 
             "▪️▪️▪️▪️\n💣💣💣💣\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n💣💣💣💣\n▪️▪️▪️▪️\n▪️▪️▪️▪️",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💣💣💣💣\n▪️▪️▪️▪️",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💣💣💣💣",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💥💥💥💥",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n💥💥💥💥\n💥💥💥💥",
             "▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n▪️▪️▪️▪️\n😵😵😵😵",
]

RUN_STRINGS = (
    "Where do you think you're going?",
    "Huh? what? did they get away?",
    "ZZzzZZzz... Huh? what? oh, just them again, nevermind.",
    "Get back here!",
    "Not so fast...",
    "Look out for the wall!",
    "Don't leave me alone with them!!",
    "You run, you die.",
    "Jokes on you, I'm everywhere",
    "You're gonna regret that...",
    "You could also try /punchme, I hear that's fun.",
    "Go bother someone else, no-one here cares.",
    "You can run, but you can't hide.",
    "Is that all you've got?",
    "I'm behind you...",
    "You've got company!",
    "We can do this the easy way, or the hard way.",
    "You just don't get it, do you?",
    "Yeah, you better run!",
    "Please, remind me how much I care?",
    "I'd run faster if I were you.",
    "That's definitely the droid we're looking for.",
    "May the odds be ever in your favour.",
    "Famous last words.",
    "And they disappeared forever, never to be seen again.",
    "\"Oh, look at me! I'm so cool, I can run from a bot!\" - this person",
    "Yeah yeah, just tap /punchme already.",
    "Here, take this ring and head to Mordor while you're at it.",
    "Legend has it, they're still running...",
    "Unlike Harry Potter, your parents can't protect you from me.",
    "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might "
    "be the next Vader.",
    "Multiple calculations later, I have decided my interest in your shenanigans is exactly 0.",
    "Legend has it, they're still running.",
    "Keep it up, not sure we want you here anyway.",
    "You're a wiza- Oh. Wait. You're not Harry, keep moving.",
    "NO RUNNING IN THE HALLWAYS!",
    "Hasta la vista, baby.",
    "Who let the dogs out?",
    "It's funny, because no one cares.",
    "Ah, what a waste. I liked that one.",
    "Frankly, my dear, I don't give a damn.",
    "My milkshake brings all the boys to yard... So run faster!",
    "You can't HANDLE the truth!",
    "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",
    "Hey, look at them! They're running from the inevitable banhammer... Cute.",
    "Han shot first. So will I.",
    "What are you running after, a white rabbit?",
    "As The Doctor would say... RUN!",
)


PING_STRING = (
    "PONG!!",
    "I am here!",
)

ITEMS = (
    "cast iron skillet",
    "angry meow",
    "cricket bat",
    "wooden cane",
    "shovel",
    "toaster",
    "book",
    "laptop",
    "rubber chicken",
    "spiked bat",
    "heavy rock",
    "chunk of dirt",
    "ton of bricks",
    "rasengan",
    "spirit bomb",
    "100-Type Guanyin Bodhisattva",
    "rasenshuriken",
    "Murasame",
    "ban",
    "chunchunmaru",
    "Kubikiribōchō",
    "rasengan",
    "spherical flying kat",
)

THROW = (
    "എറിഞ്ഞു",
    "വിക്ഷേപിച്ചു",
    "തട്ടി",
    "വീശിയെറിഞ്ഞു",
)

HIT = (
    "അടിച്ചു",
    "ശക്തിയായി പ്രഹരിച്ചു",
    "തല്ലി",
    "ഇടിച്ചു",
    "തൊഴിച്ചു",

)

ABUSE_STRINGS = (
    "Fuck off",
    "Stfu go fuck yourself",
    "Ur mum gey",
    "Ur dad lesbo",
    "Bsdk",
    "Nigga",
    "Ur granny tranny",
    "you noob",
    "Relax your Rear,ders nothing to fear,The Rape train is finally here",
    "Stfu bc",
    "Stfu and Gtfo U nub",
    "GTFO bsdk",
    "CUnt",
    " Gay is here",
    "Ur dad gey bc ",
)

EYES = [
    ['⌐■', '■'],
    [' ͠°', ' °'],
    ['⇀', '↼'],
    ['´• ', ' •`'],
    ['´', '`'],
    ['`', '´'],
    ['ó', 'ò'],
    ['ò', 'ó'],
    ['⸌', '⸍'],
    ['>', '<'],
    ['Ƹ̵̡', 'Ʒ'],
    ['ᗒ', 'ᗕ'],
    ['⟃', '⟄'],
    ['⪧', '⪦'],
    ['⪦', '⪧'],
    ['⪩', '⪨'],
    ['⪨', '⪩'],
    ['⪰', '⪯'],
    ['⫑', '⫒'],
    ['⨴', '⨵'],
    ['⩿', '⪀'],
    ['⩾', '⩽'],
    ['⩺', '⩹'],
    ['⩹', '⩺'],
    ['◥▶', '◀◤'],
    ['◍', '◎'],
    ['/͠-', '┐͡-\\'],
    ['⌣', '⌣”'],
    [' ͡⎚', ' ͡⎚'],
    ['≋'],
    ['૦ઁ'],
    ['  ͯ'],
    ['  ͌'],
    ['ළ'],
    ['◉'],
    ['☉'],
    ['・'],
    ['▰'],
    ['ᵔ'],
    [' ﾟ'],
    ['□'],
    ['☼'],
    ['*'],
    ['`'],
    ['⚆'],
    ['⊜'],
    ['>'],
    ['❍'],
    ['￣'],
    ['─'],
    ['✿'],
    ['•'],
    ['T'],
    ['^'],
    ['ⱺ'],
    ['@'],
    ['ȍ'],
    ['  '],
    ['  '],
    ['x'],
    ['-'],
    ['$'],
    ['Ȍ'],
    ['ʘ'],
    ['Ꝋ'],
    [''],
    ['⸟'],
    ['๏'],
    ['ⴲ'],
    ['◕'],
    ['◔'],
    ['✧'],
    ['■'],
    ['♥'],
    [' ͡°'],
    ['¬'],
    [' º '],
    ['⨶'],
    ['⨱'],
    ['⏓'],
    ['⏒'],
    ['⍜'],
    ['⍤'],
    ['ᚖ'],
    ['ᴗ'],
    ['ಠ'],
    ['σ'],
    ['☯']
]

MOUTHS = [
    ['v'],
    ['ᴥ'],
    ['ᗝ'],
    ['Ѡ'],
    ['ᗜ'],
    ['Ꮂ'],
    ['ᨓ'],
    ['ᨎ'],
    ['ヮ'],
    ['╭͜ʖ╮'],
    [' ͟ل͜'],
    [' ͜ʖ'],
    [' ͟ʖ'],
    [' ʖ̯'],
    ['ω'],
    [' ³'],
    [' ε '],
    ['﹏'],
    ['□'],
    ['ل͜'],
    ['‿'],
    ['╭╮'],
    ['‿‿'],
    ['▾'],
    ['‸'],
    ['Д'],
    ['∀'],
    ['!'],
    ['人'],
    ['.'],
    ['ロ'],
    ['_'],
    ['෴'],
    ['ѽ'],
    ['ഌ'],
    ['⏠'],
    ['⏏'],
    ['⍊'],
    ['⍘'],
    ['ツ'],
    ['益'],
    ['╭∩╮'],
    ['Ĺ̯'],
    ['◡'],
    [' ͜つ']
]

EARS = [
    ['q', 'p'],
    ['ʢ', 'ʡ'],
    ['⸮', '?'],
    ['ʕ', 'ʔ'],
    ['ᖗ', 'ᖘ'],
    ['ᕦ', 'ᕥ'],
    ['ᕦ(', ')ᕥ'],
    ['ᕙ(', ')ᕗ'],
    ['ᘳ', 'ᘰ'],
    ['ᕮ', 'ᕭ'],
    ['ᕳ', 'ᕲ'],
    ['(', ')'],
    ['[', ']'],
    ['¯\\_', '_/¯'],
    ['୧', '୨'],
    ['୨', '୧'],
    ['⤜(', ')⤏'],
    ['☞', '☞'],
    ['ᑫ', 'ᑷ'],
    ['ᑴ', 'ᑷ'],
    ['ヽ(', ')ﾉ'],
    ['\\(', ')/'],
    ['乁(', ')ㄏ'],
    ['└[', ']┘'],
    ['(づ', ')づ'],
    ['(ง', ')ง'],
    ['⎝', '⎠'],
    ['ლ(', 'ლ)'],
    ['ᕕ(', ')ᕗ'],
    ['(∩', ')⊃━☆ﾟ.*'],
]

TOSS = (
    "Heads",
    "Tails",
)

DECIDE = (
    "Yes.",
    "NoU.",
    "Maybe."
)

TABLE = (
    "(╯°□°）╯彡 ┻━┻",
    "I ran out of tables, will order more.",
    "Go do some work instead of flippin tables."
)
