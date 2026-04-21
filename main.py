import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

WELCOME = (
    "PARISBOLA OFFICIAL\n\n"
    "Selamat datang di layanan resmi Parisbola!\n\n"
    "Transaksi deposit QRIS proses hanya 1 detik\n"
    "Penarikan berapapun dibayar tuntas tanpa ribet\n"
    "Sistem cepat, stabil & pelayanan terbaik\n\n"
    "Link Alternatif: https://cutt.ly/GtFHqLcQ\n"
    "Group WhatsApp: https://chat.whatsapp.com/FXUaLyPrORfAGQfVU8ov8C\n"
    "Live Chat 24 Jam: https://direct.lc.chat/16556181\n\n"
    "Akses sekarang & rasakan pengalaman terbaik bersama PARISBOLA!"
)

def keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Link Alternatif", url="https://cutt.ly/GtFHqLcQ"),
         InlineKeyboardButton("Group WhatsApp", url="https://chat.whatsapp.com/FXUaLyPrORfAGQfVU8ov8C")],
        [InlineKeyboardButton("Live Chat 24 Jam", url="https://direct.lc.chat/16556181"),
         InlineKeyboardButton("Daftar Sekarang", url="https://cutt.ly/GtFHqLcQ")]
    ])

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME, reply_markup=keyboard(), disable_web_page_preview=True)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", reply))
    app.add_handler(CommandHandler("help", reply))
    app.add_handler(CommandHandler("link", reply))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    print("Bot aktif!")
    app.run_polling()

if __name__ == "__main__":
    main()
