import html
import random
import time

from zerotwobot import dispatcher
from zerotwobot.modules.disable import DisableAbleCommandHandler
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext


def mewtwo(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Normal - Timid, modest")
    reply_text(r"Best Y  -  Timid, hasty")
    reply_text(r"Best X - Naive and jolly")
    
def tyranitar(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Adamant, brave")
    
def articuno(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Careful")
    
def tapu(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Koko - Jolly, naive, adamant      For Bulu- Adamant, impish      For Lele- Timid, modest      For Fini- Modest, calm, bold")
    
def celebi(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Modest, Quiet")
    
def hooh(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Careful, adamant")
    
def entei(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant, careful, jolly, impish")
    
def suicune(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Careful")
    
def melloetta(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Normal- Modest, calm       For Pirouette form - Jolly, hasty, naive, adamant")
    
def deoxys(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Normal - Timid, modest      For Attack - Naive, hasty, timid, jolly      Speed - Naive, hasty, timid, modest      Defence - Relaxed, sassy")
    
def regirock(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Relaxed")
    
def registeel(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Relaxed, sassy")
    
def regice(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Calm, careful")
    
def latias(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Calm, modest, timid")
    
def kommoo(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant, impish, careful, jolly")
    
def venusaur(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, calm, bold")
    
def charizard(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Normal - Modest, hasty, timid")
    reply_text(r"Best For X  - Jolly, naive")
    reply_text(r"Best For Y  - Modest, hasty, timid")

def butterfree(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, timid")

def beedrill(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly, hasty, naive")

def pidgeot(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly")

def raticate(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly, adamant")

def fearow(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant, jolly")

def arbok(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly,adamant")

def raichu(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, timid")

def nidoran(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best (m)- Adamant, impish")
    reply_text(r"Best (f)- Adamant")

def nidoking(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best - Adamant, impish")

def ninetales(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Alolan- Timid, modest")

def golbat(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly, naive, hasty")

def vileplume(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- gay")

def parasect(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- gay")

def persian(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly")

def arcanine(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Jolly, hasty, naive")

def alakazam(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Timid, hasty, naive")

def victreebel(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, adamant")

def tentacruel(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Timid")

def rapidash(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, timid")

def slowbro(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest, calm")

def dodrio(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant, jolly")

def dewgong(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"gey")

def muk(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best Alolan- Adamant, sassy, brave, careful")

def cloyster(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Relaxed, sassy")

def gengar(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Timid, hasty")

def hypno(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Modest")

def kingler(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Adamant")

def voltorb(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"Best- Timid, hasty, naive")
    
def fp(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"God of Gay")
    reply_text(r"Legendary gay")
    reply_text(r"Gay of all time")
    reply_text(r"Gay af")
    reply_text(r"Woh to gay h")
    reply_text(r"huh bahut bol liya ... dil par mat lena")
    
MEWTWO_HANDLER = DisableAbleCommandHandler("mewtwo_fuck", mewtwo, run_async=True)
TYRANITAR_HANDLER = DisableAbleCommandHandler("tyranitar", tyranitar, run_async=True)
ARTICUNO_HANDLER = DisableAbleCommandHandler("articuno", articuno, run_async=True)
TAPU_HANDLER = DisableAbleCommandHandler("tapu", tapu, run_async=True)
CELEBI_HANDLER = DisableAbleCommandHandler("celebi", celebi, run_async=True)
HOOH_HANDLER = DisableAbleCommandHandler("hooh", hooh, run_async=True)
ENTEI_HANDLER = DisableAbleCommandHandler("entei", entei, run_async=True)
SUICUNE_HANDLER = DisableAbleCommandHandler("suicune", suicune, run_async=True)
MELLOETTA_HANDLER = DisableAbleCommandHandler("melloetta", melloetta, run_async=True)
DEOXYS_HANDLER = DisableAbleCommandHandler("deoxys", deoxys, run_async=True)
REGIROCK_HANDLER = DisableAbleCommandHandler("regirock", regirock, run_async=True)
REGISTEEL_HANDLER = DisableAbleCommandHandler("registeel", registeel, run_async=True)
REGICE_HANDLER = DisableAbleCommandHandler("regice", regice, run_async=True)
LATIAS_HANDLER = DisableAbleCommandHandler("latias", latias, run_async=True)
KOMMO_HANDLER = DisableAbleCommandHandler("kommoo", kommoo, run_async=True)
VENUSAUR_HANDLER = DisableAbleCommandHandler(("venusaur", "ivysaur", "bulbasaur"), venusaur, run_async=True)
CHARIZARD_HANDLER = DisableAbleCommandHandler(("charizard", "charmeleon", "charmander"), charizard, run_async=True)
BUTTERFREE_HANDLER = DisableAbleCommandHandler(("butterfree", "metapod", "caterpie", "arceus", "mew"), butterfree, run_async=True)
BEEDRILL_HANDLER = DisableAbleCommandHandler(("beedrill", "kakuna", "weedle"), beedrill, run_async=True)
PIDGEOT_HANDLER = DisableAbleCommandHandler(("pidgeot", "pidgeotto", "pidgey"), pidgeot, run_async=True)
RATICATE_HANDLER = DisableAbleCommandHandler(("raticate", "rattata", "sharpedo", "rayquaza", "pinsir"), raticate, run_async=True)
FEAROW_HANDLER = DisableAbleCommandHandler(("fearow", "spearow"), fearow, run_async=True)
ARBOK_HANDLER = DisableAbleCommandHandler(("arbok", "ekans"), arbok, run_async=True)
RAICHU_HANDLER = DisableAbleCommandHandler(("raichu", "pikachu"), raichu, run_async=True)
NIDORAN_HANDLER = DisableAbleCommandHandler("nidoran", nidoran, run_async=True)
NIDOKING_HANDLER = DisableAbleCommandHandler(("nidoking", "nidorino", "groudon", "buzzwole", "golem", "graveler", "geodude"), nidoking, run_async=True)
NINETALES_HANDLER = DisableAbleCommandHandler(("ninetales", "vulpix"), ninetales, run_async=True)
GOLBAT_HANDLER = DisableAbleCommandHandler(("golbat", "zubat"), golbat, run_async=True)
VILEPLUME_HANDLER = DisableAbleCommandHandler(("vileplume", "gloom", "oddish"), vileplume, run_async=True)
PARASECT_HANDLER = DisableAbleCommandHandler(("parasect", "paras"), parasect, run_async=True)
PERSIAN_HANDLER = DisableAbleCommandHandler(("persian", "meowth", "kangaskhan"), persian, run_async=True)
ARCANINE_HANDLER = DisableAbleCommandHandler(("arcanine", "growlithe", "scyther"), arcanine, run_async=True)
ALAKAZAM_HANDLER = DisableAbleCommandHandler(("alakazam", "alakazam", "abra", "porygon"), alakazam, run_async=True)
VICTREEBEL_HANDLER = DisableAbleCommandHandler(("victreebel", "weepinbell", "bellsprout"), victreebel, run_async=True)
TENTACRUEL_HANDLER = DisableAbleCommandHandler(("tentacruel", "tentacool", "raikou", "blastoise", "wartortle", "squirtle"), tentacruel, run_async=True)
RAPIDASH_HANDLER = DisableAbleCommandHandler(("rapidash", "ponyta", "starmie", "staryu", "electabuzz"), rapidash, run_async=True)
SLOWBRO_HANDLER = DisableAbleCommandHandler(("slowbro", "slowpoke", "kyogre", "latios", "lapras"), slowbro, run_async=True)
DODRIO_HANDLER = DisableAbleCommandHandler(("dodrio", "doduo"), dodrio, run_async=True)
DEWGONG_HANDLER = DisableAbleCommandHandler(("dewgong", "seel"), dewgong, run_async=True)
MUK_HANDLER = DisableAbleCommandHandler(("muk", "grimer"), muk, run_async=True)
CLOYSTER_HANDLER = DisableAbleCommandHandler(("cloyster", "shellder"), cloyster, run_async=True)
GENGAR_HANDLER = DisableAbleCommandHandler(("gengar", "haunter", "gastly"), gengar, run_async=True)
HYPNO_HANDLER = DisableAbleCommandHandler(("hypno", "vaporeon", "drowzee", "exeggutor", "exeggcute", "zapdos", "moltres", "jirachi", "dialga", "wigglytuff", "clefable", "venomoth", "golduck", "magneton", "jigglypuff", "clefairy", "venonat", "psyduck", "magnemite"), hypno, run_async=True)
KINGLER_HANDLER = DisableAbleCommandHandler(("kingler", "flareon", "tauros", "krabby", "seaking", "goldeen", "rhyhorn", "rhydon", "cubone", "marowak", "hitmonlee", "hitmonchan" "lugia", "mamoswine", "guzzlord", "sandslash", "sandshrew", "nidoqueen", "nidorina", "dugtrio", "diglett", "primeape", "mankey", "poliwrath", "poliwhirl", "poliwag", "machamp", "machoke", "machop", "farfetchd", "onix"), kingler, run_async=True)
VOLTORB_HANDLER = DisableAbleCommandHandler(("voltorb", "electrode"), voltorb, run_async=True)
FP_HANDLER = DisableAbleCommandHandler("fp", fp, run_async=True)

dispatcher.add_handler(MEWTWO_HANDLER)
dispatcher.add_handler(TYRANITAR_HANDLER)
dispatcher.add_handler(ARTICUNO_HANDLER)
dispatcher.add_handler(TAPU_HANDLER)
dispatcher.add_handler(CELEBI_HANDLER)
dispatcher.add_handler(HOOH_HANDLER)
dispatcher.add_handler(ENTEI_HANDLER)
dispatcher.add_handler(SUICUNE_HANDLER)
dispatcher.add_handler(MELLOETTA_HANDLER)
dispatcher.add_handler(DEOXYS_HANDLER)
dispatcher.add_handler(REGIROCK_HANDLER)
dispatcher.add_handler(REGISTEEL_HANDLER)
dispatcher.add_handler(REGICE_HANDLER)
dispatcher.add_handler(LATIAS_HANDLER)
dispatcher.add_handler(KOMMO_HANDLER)
dispatcher.add_handler(VENUSAUR_HANDLER)
dispatcher.add_handler(CHARIZARD_HANDLER)
dispatcher.add_handler(BUTTERFREE_HANDLER)
dispatcher.add_handler(BEEDRILL_HANDLER)
dispatcher.add_handler(PIDGEOT_HANDLER)
dispatcher.add_handler(RATICATE_HANDLER)
dispatcher.add_handler(FEAROW_HANDLER)
dispatcher.add_handler(ARBOK_HANDLER)
dispatcher.add_handler(RAICHU_HANDLER)
dispatcher.add_handler(NIDORAN_HANDLER)
dispatcher.add_handler(NIDOKING_HANDLER)
dispatcher.add_handler(NINETALES_HANDLER)
dispatcher.add_handler(GOLBAT_HANDLER)
dispatcher.add_handler(VILEPLUME_HANDLER)
dispatcher.add_handler(PARASECT_HANDLER)
dispatcher.add_handler(PERSIAN_HANDLER)
dispatcher.add_handler(ARCANINE_HANDLER)
dispatcher.add_handler(ALAKAZAM_HANDLER)
dispatcher.add_handler(VICTREEBEL_HANDLER)
dispatcher.add_handler(TENTACRUEL_HANDLER)
dispatcher.add_handler(RAPIDASH_HANDLER)
dispatcher.add_handler(SLOWBRO_HANDLER)
dispatcher.add_handler(DODRIO_HANDLER)
dispatcher.add_handler(DEWGONG_HANDLER)
dispatcher.add_handler(MUK_HANDLER)
dispatcher.add_handler(CLOYSTER_HANDLER)
dispatcher.add_handler(GENGAR_HANDLER)
dispatcher.add_handler(HYPNO_HANDLER)
dispatcher.add_handler(KINGLER_HANDLER)
dispatcher.add_handler(VOLTORB_HANDLER)
dispatcher.add_handler(FP_HANDLER)
