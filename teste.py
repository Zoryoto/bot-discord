from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice, create_permission


bot = commands.Bot(command_prefix="!", description="Bot tuto")
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    print("Ready !")


@slash.slash(name="farmer", guild_ids=[918208956357312552], description="Choisiser votre article", options=[
            create_option(
                name="farmer",
                description="Choisiser votre types article.",
                option_type=3,
                required=True,
                choices=[
                    create_choice(
                        name="graine de Blé = 150$/stack",
                        value="graine de Blé"
                    ),
                    create_choice(
                        name="graine d'améthyste = 500$/stack",
                        value="graine d'améthyste"
                    ),
                    create_choice(
                        name="graine de Titane = 750$/stack",
                        value="graine de Titane"
                    ),
                    create_choice(
                        name="Seed Planter en Améthyste = 4000$/u",
                        value="Seed Planter en Améthyste"
                    ),
                    create_choice(
                        name="XP Bush = 8k Le Stack",
                        value="XP Bush"
                    ),
                    create_choice(
                        name="XP Berry = 20$/u ou 1280$/stack",
                        value="XP Berry"
                    ),
                    create_choice(
                        name="base claime",
                        value="base claime"
                    ),
                    create_choice(
                        name="Compresses XPberry = 12000$/stack",
                        value="Compresses XPberry"
                    ),
                    create_choice(
                        name="Terre Fertile = 999$/stack",
                        value="Terre Fertile"
                    ),
                    create_choice(
                        name="Os = 400$/stack",
                        value="Os"
                    ),
                    create_choice(
                        name="Blé = 300$/stack/ Limité à 20 stack par jour",
                        value="Blé"
                    ),
                    create_choice(
                        name="Bottle avec 1008 ou 1025 sp de farmer = 1500$/u",
                        value="Bottle avec 1008 ou 1025 sp de farmer"
                    )
                ]
            ),create_option(name="pseudo",
                            description="veiller entrer votre pseudo minecraft.",
                            option_type=3,
                            required=True),
        create_option(name="quantiter",
                            description="veiller entrer la quantiter du produit que vous avier selectioner",
                            option_type=3,
                            required=False),
])

async def lancer(ctx, farmer, pseudo, quantiter = 1 ):


    await ctx.send(f"{pseudo} veut acheter {quantiter} {farmer}")


@slash.slash(name="pvp", guild_ids=[918208956357312552], description="Choisiser votre article", options=[
    create_option(
        name="pvp",
        description="Choisiser votre types article.",
        option_type=3,
        required=True,
        choices=[
            create_choice(
                name="Casque  en Paladium P4 U3 = 6000$/u",
                value="Casque  en Paladium P4 U3"
            ),
            create_choice(
                name="Plastron en Paladium P4 U3 = 6499$/u",
                value="Plastron en Paladium P4 U3"
            ),
            create_choice(
                name="Jambières en Paladium P4 U3 = 6499$/u",
                value="Jambières en Paladium P4 U3"
            ),
            create_choice(
                name="Bottes en Paladium P4 U3 = 6000$/u",
                value="Bottes en Paladium P4 U3"
            ),
            create_choice(
                name="Full Paladium P4 U3 = 24999dollars",
                value="Full Paladium P4 U3"
            ),
            create_choice(
                name="Épée en Paladium T5 U3 F2 = 6500$/u",
                value="Épée en Paladium T5 U3 F2"
            ),
            create_choice(
                name="Stick of God = 26999$/u",
                value="Stick of God"
            ),
            create_choice(
                name="Stick of God U3 = 29999$/u",
                value="Stick of God U3"
            ),
            create_choice(
                name="Strength Stick = 8999$/u",
                value="Strength Stick"
            ),
            create_choice(
                name="Strenght Stick U3 =11999$/u",
                value="Strenght Stick U3"
            ),
            create_choice(
                name="Heal Stick = 8999$/u",
                value="Heal Stick"
            ),
            create_choice(
                name="Heal Stick U3 = 11999$/u ",
                value="Heal Stick U3"
            ),
            create_choice(
                name="Potion jetable de Heal II = 300$/u",
                value="Potion jetable de Heal II"
            ),
            create_choice(
                name="Potion de Fire résistance 8min = 999$/u",
                value="Potion de Fire résistance 8min"
            ),
            create_choice(
                name="hang lider = 999$/u",
                value="hang lider"
            ),
            create_choice(
                name="potion launcher = 1500$/u",
                value="potion launcher"
            )

        ]
    ),create_option(name="pseudo",
                    description="veiller entrer votre pseudo minecraft.",
                    option_type=3,
                    required=True),
create_option(name="quantiter",
                    description="veiller entrer la quantiter du produit que vous avier selectioner",
                    option_type=3,
                    required=False),
])

async def lancer(ctx,pvp , pseudo, quantiter = 1 ):


    await ctx.send(f"{pseudo} veut acheter {quantiter} {pvp}")


@slash.slash(name="outils", guild_ids=[918208956357312552], description="Choisiser votre article", options=[
    create_option(
        name="outils",
        description="Choisiser votre types article.",
        option_type=3,
        required=True,
        choices=[
            create_choice(
                name="Duplication = gratuit",
                value="Duplication"
            ),
            create_choice(
                name="hammerF2/ SMELT = 7k$",
                value="Hammer F2/ SMELT"
            ),
            create_choice(
                name="Hameer SPEED3 = 12k$",
                value="Hameer SPEED3 "
            ),
            create_choice(
                name="Pioche Parfaite (minimum E4 U3) = 4.999$",
                value="Pioche Parfaite (minimum E4 U3)"
            ),
            create_choice(
                name="Pickaxe of The God niveau 1 = 1500$",
                value="Pickaxe of The God niveau 1"
            ),
            create_choice(
                name="Pickaxe of The God niveau 5 = 5000$",
                value="Pickaxe of The God niveau 5 = 5000$"
            ),
            create_choice(
                name="Pickaxe of The God niveau 10 = 10000$",
                value="Pickaxe of The God niveau 10"
            ),
            create_choice(
                name="Pickaxe of The God niveau 11 = 13000$",
                value="Pickaxe of The God niveau 11"
            ),
            create_choice(
                name="Pickaxe of The God niveau 12  = 18000$",
                value="Pickaxe of The God niveau 12"
            ),
            create_choice(
                name="Pickaxe of The God niveau 13 = 24000$",
                value="Pickaxe of The God niveau 13"
            ),
            create_choice(
                name="Pickaxe of The God niveau 14 =35000$",
                value="Pickaxe of The God niveau 14"
            ),
            create_choice(
                name="Pickaxe of The God niveau 15 = 45000$",
                value="Pickaxe of The God niveau 15"
            ),
            create_choice(
                name="Pickaxe of The God niveau 16 = 55000$",
                value="Pickaxe of The God niveau 16"
            ),
            create_choice(
                name="Pickaxe of The God niveau 17 = 75000$",
                value="Pickaxe of The God niveau 17"
            ),
            create_choice(
                name="Pickaxe of The God niveau 18 = 100k$",
                value="Pickaxe of The God niveau 18"
            ),
            create_choice(
                name="Pickaxe of The God niveau 19 = 150k$",
                value="Pickaxe of The God niveau 19"
            ),
            create_choice(
                name="Pickaxe of The God niveau 20 = 190k$",
                value="Pickaxe of The God niveau 20"
            )

        ]
    ),create_option(name="pseudo",
                    description="veiller entrer votre pseudo minecraft.",
                    option_type=3,
                    required=True),
create_option(name="quantiter",
                    description="veiller entrer la quantiter du produit que vous avier selectioner",
                    option_type=3,
                    required=False),
])

async def lancer(ctx, outils, pseudo, quantiter = 1 ):


    await ctx.send(f"{pseudo} veut acheter {quantiter} {outils}")


@slash.slash(name="hunter", guild_ids=[918208956357312552], description="Choisiser votre article", options=[
    create_option(
        name="hunter",
        description="Choisiser votre types article.",
        option_type=3,
        required=True,
        choices=[
            create_choice(
                name="Épée SmiteV U3 Loot3 Mending 1 = 12000$",
                value="Épée SmiteV U3 Loot3 Mending 1"
            ),
            create_choice(
                name="BackPack en Amethyst = 15000$",
                value="BackPack en Amethyst"
            ),
            create_choice(
                name="BackPack en Titane = 20000 $",
                value="BackPack en Titane"
            )

        ]
    ),create_option(name="pseudo",
                    description="veiller entrer votre pseudo minecraft.",
                    option_type=3,
                    required=True),
create_option(name="quantiter",
                    description="veiller entrer la quantiter du produit que vous avier selectioner",
                    option_type=3,
                    required=False),
])

async def lancer(ctx, hunter, pseudo, quantiter = 1 ):


    await ctx.send(f"{pseudo} veut acheter {quantiter} {hunter}")

@slash.slash(name="minerais", guild_ids=[918208956357312552], description="Choisiser votre article", options=[
    create_option(
        name="minerais",
        description="Choisiser votre types article.",
        option_type=3,
        required=True,
        choices=[
create_choice(
                name="Iron ore = 2999$ stack",
                value="Iron ore"
            ),
            create_choice(
                name="Gold ore le stack = 10k stack",
                value="Gold ore le stack"
            ),
            create_choice(
                name="Amethyst ore = 3999$/ stack",
                value="Amethyst ore"
            ),
            create_choice(
                name="Titane ore = 4999$/stack",
                value="Titane ore"
            ),
            create_choice(
                name="Paladium ore = 32k$/ stack",
                value="Paladium ore"
            ),
            create_choice(
                name="Lingot de paladium = 300$/u",
                value="Lingot de paladium"
            ),
            create_choice(
                name="Lingot d'amethyst = 1750$/stack",
                value="Lingot d'amethyst"
            ),
            create_choice(
                name="Lingot de titane = 2200$/stack",
                value="Lingot de titane"
            ),
            create_choice(
                name="Lingot de fer = 800 $/stack",
                value="Lingot de fer"
            ),
            create_choice(
                name="Diamant = 2000$/stack",
                value="Diamant"
            ),
            create_choice(
                name="Findium = 800$/u",
                value="Findium"
            )

        ]
    ),create_option(name="pseudo",
                    description="veiller entrer votre pseudo minecraft.",
                    option_type=3,
                    required=True),
    create_option(name="quantiter",
                    description="veiller entrer la quantiter du produit que vous avier selectioner",
                    option_type=3,
                    required=False),
])

async def lancer(ctx, minerais, pseudo, quantiter = 1 ):


    await ctx.send(f"{pseudo} veut acheter {quantiter} {minerais}")

@slash.slash(name="alchimiste", guild_ids=[918208956357312552], description="Choisiser votre article", options=[
    create_option(
        name="alchimiste",
        description="Choisiser votre types article.",
        option_type=3,
        required=True,
        choices=[
create_choice(
                name="Bloc de verre = 1$/u",
                value="Bloc de verre"
            ),
            create_choice(
                name="Fleur Vanilla = 299$/stack",
                value="Fleur Vanilla"
            ),
            create_choice(
                name="Lightning Potion = 9999$/u (max 10 par semaine)",
                value="Lightning Potion"
            ),
            create_choice(
                name="Extractor = 2500$/u",
                value="Extractor "
            ),
            create_choice(
                name="Bois Moddé = 2000$/stack",
                value="Bois Moddé"
            ),
            create_choice(
                name="Fiole Vanilla = 100$/les 16",
                value="Fiole Vanilla"
            ),
            create_choice(
                name="Fiole Moddé = 150$/ les 16",
                value="Fiole Moddé"
            )

        ]
    ),create_option(name="pseudo",
                    description="veiller entrer votre pseudo minecraft.",
                    option_type=3,
                    required=True),
    create_option(name="quantiter",
                    description="veiller entrer la quantiter du produit que vous avier selectioner",
                    option_type=3,
                    required=False),
])

async def lancer(ctx, alchimiste, pseudo, quantiter = 1 ):


    await ctx.send(f"{pseudo} veut acheter {quantiter} {alchimiste}")

@slash.slash(name="base_claime", guild_ids=[918208956357312552], description="Choisiser votre article", options=[
    create_option(
        name="base_claime",
        description="Choisiser votre types article.",
        option_type=3,
        required=True,
        choices=[
            create_choice(
                name="Sables = 100$/stack",
                value="Sables"
            ),
            create_choice(
                name="Fake Water = 200$/u",
                value="Fake Water"
            ),
            create_choice(
                name="Spike en Titane = 19999$/stack",
                value="Spike en Titane"
            ),
            create_choice(
                name="Enclumes =20000$/stack",
                value="Enclumes"
            ),
            create_choice(
                name="Lave = 10$/u",
                value="Lave"
            ),
            create_choice(
                name="Table d'enchantement = 399$/u",
                value="Table d'enchantement"
            ),
            create_choice(
                name="Table de Craft = 10$/u",
                value="Table de Craft"
            ),
            create_choice(
                name="Slime pads = 22000$/stack",
                value="Slime pads"
            ),
            create_choice(
                name="Dark Oak Sapling = 3999$/stack",
                value="Dark Oak Sapling "
            ),
            create_choice(
                name="Obsidiennes = 2500$/stack",
                value="Obsidiennes"
            ),
            create_choice(
                name="Lava Obsidiennes = 3500$/stack",
                value="Lava Obsidiennes"
            ),
            create_choice(
                name="Fake Obsidiennes = 10000$/stack",
                value="Fake Obsidiennes"
            ),
            create_choice(
                name="Boom Obsidiennes = 7000$/stack",
                value="Boom Obsidiennes"
            )

        ]
    ),create_option(name="pseudo",
                    description="veiller entrer votre pseudo minecraft.",
                    option_type=3,
                    required=True),
    create_option(name="quantiter",
                    description="veiller entrer la quantiter du produit que vous avier selectioner",
                    option_type=3,
                    required=False),
])

async def lancer(ctx, base_claime, pseudo, quantiter = 1 ):


    await ctx.send(f"{pseudo} veut acheter {quantiter} {base_claime}")


@slash.slash(name="diver", guild_ids=[918208956357312552], description="Choisiser votre article", options=[
    create_option(
        name="diver",
        description="Choisiser votre types article.",
        option_type=3,
        required=True,
        choices=[
            create_choice(
                name="Coffre en Diamant = 1000$",
                value="Coffre en Diamant"
            ),
            create_choice(
                name="Coffre en Améthyste = 8000$",
                value="Coffre en Améthyste"
            ),
            create_choice(
                name="Coffre en Titane = 18000$",
                value="Coffre en Titane"
            ),
            create_choice(
                name="Paladium machine = 15k$",
                value="Paladium machine"
            ),
            create_choice(
                name="Full grinder = 34999$",
                value="Full grinder"
            ),
            create_choice(
                name="Cobble Breaker = 2000$/u",
                value="Cobble Breaker"
            ),
            create_choice(
                name="Paladium Furnace = 1000$/u",
                value="Paladium Furnace"
            ),
            create_choice(
                name="Guardian Kepper = 40k$/u",
                value="Guardian Kepper"
            ),
            create_choice(
                name="Full boîte à golem = 20k$",
                value="Full boîte à golem"
            )

        ]
    ),create_option(name="pseudo",
                    description="veiller entrer votre pseudo minecraft.",
                    option_type=3,
                    required=True),
    create_option(name="quantiter",
                    description="veiller entrer la quantiter du produit que vous avier selectioner",
                    option_type=3,
                    required=False),
])

async def lancer(ctx, diver, pseudo, quantiter = 1 ):


    await ctx.send(f"{pseudo} veut acheter {quantiter} {diver}")


@slash.slash(name="kits", guild_ids=[918208956357312552], description="Choisiser votre article", options=[
    create_option(
        name="kits",
        description="Choisiser votre types article.",
        option_type=3,
        required=True,
        choices=[
            create_choice(
                name="Kit Minage = 10000$",
                value="Kit Minage"
            ),
            create_choice(
                name="Kit Pvp = 21999$",
                value="Kit Pvp"
            ),
            create_choice(
                name="Kit Pillage = 7000$ sans les unclaim Finder",
                value="Kit Pillage sans les unclaim Finder"
            ),
            create_choice(
                name="Kit Pillage avec Unclaim Finder rouge = 18000$",
                value="Kit Pillage avec Unclaim Finder rouge"
            ),
            create_choice(
                name="Kit Pillage avec Unclaim Finder vert = 5000$",
                value="Kit Pillage avec Unclaim Finder vert"
            )

        ]
    ),create_option(name="pseudo",
                    description="veiller entrer votre pseudo minecraft.",
                    option_type=3,
                    required=True),
    create_option(name="quantiter",
                    description="veiller entrer la quantiter du produit que vous avier selectioner",
                    option_type=3,
                    required=False),
])

async def lancer(ctx, kits, pseudo, quantiter = 1 ):


    await ctx.send(f"{pseudo} veut acheter {quantiter} {kits} ")


@slash.slash(name="pillage", guild_ids=[918208956357312552], description="Choisiser votre article", options=[
    create_option(
        name="pillage",
        description="Choisiser votre types article.",
        option_type=3,
        required=True,
        choices=[create_choice(
                name="Dynamite = 6.999$/les 16",
                value="Dynamite"
            ),
            create_choice(
                name="Big Dynamite = 17.999$/les 16",
                value="Big Dynamite"
            ),
            create_choice(
                name="Soul Sand = 100$/stack ou 2$/u",
                value="Soul Sand"
            ),
            create_choice(
                name="Cave Block = 1.000$ /u",
                value="Cave Block"
            ),
            create_choice(
                name="Hood Helmet = 2.500$",
                value="Hood Helmet"
            ),
            create_choice(
                name="Slimy Helmet = 999$/u",
                value="Slimy Helmet"
            ),
            create_choice(
                name="Scuba Helmet = 750$/u",
                value="Scuba Helmet"
            ),
            create_choice(
                name="Jump Chestplate = 750$/u",
                value="Jump Chestplate"
            ),
            create_choice(
                name="Travel Leggings =  600$/u",
                value="Travel Leggings"
            ),
            create_choice(
                name="Travel Boots = 500$/u",
                value="Travel Boots"
            ),
            create_choice(
                name="Unclaim Finder Vert = 5000$",
                value="Unclaim Finder Vert"
            ),
            create_choice(
                name="Unclaim Finder Rouge = 18000$",
                value="Unclaim Finder Rouge"
            )

        ]
    ),create_option(name="pseudo",
                    description="veiller entrer votre pseudo minecraft.",
                    option_type=3,
                    required=True),
    create_option(name="quantiter",
                    description="veiller entrer la quantiter du produit que vous avier selectioner",
                    option_type=3,
                    required=False),
])

async def lancer(ctx, pillage, pseudo, quantiter = 1 ):


    await ctx.send(f"{pseudo} veut acheter {quantiter} {pillage} ")


@slash.slash(name="location", guild_ids=[918208956357312552], description="Choisiser votre article", options=[
    create_option(
        name="location",
        description="Choisiser votre types article.",
        option_type=3,
        required=True,
        choices=[
            create_choice(
                name="louer une grande farm a eggplant/chevril 1000$/30 min",
                value="loue une grande farm a eggplant/chevril"
            )

        ]
    ),create_option(name="pseudo",
                    description="veiller entrer votre pseudo minecraft.",
                    option_type=3,
                    required=True),
    create_option(name="quantiter",
                    description="veiller entrer le temp dont vous vouler louer",
                    option_type=3,
                    required=False),
])

async def on_message(ctx, location, pseudo, quantiter = 1 ):
    await ctx.send(f"{pseudo} veut acheter {quantiter} {location} ")







bot.run("OTI1MDY4NjkxNDcxNzMyNzc2.YcnvWg.WdRwkCX7P-ADrnO372ahT-NX49A")
