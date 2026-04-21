import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("8490458713:AAHluyYpra-BCVbePGUCoFUtq11kftoJ4AQ")

if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN tidak ditemukan! Tambahkan di Railway Variables.")

WELCOME_MESSAGE = """
🎯 *PARISBOLA OFFICIAL* 🎯

Selamat datang di layanan resmi Parisbola\! 👋

✅ Transaksi deposit QRIS proses hanya *1 detik*
✅ Penarikan berapapun dibayar tuntas tanpa ribet
✅ Sistem cepat, stabil & pelayanan terbaik untuk Anda

━━━━━━━━━━━━━━━━━━━━━
🔗 *Link Alternatif:*
https://parisbolaid\.bola1\.net/

💬 *Group WhatsApp Resmi:*
https://chat\.whatsapp\.com/FXUaLyPrORfAGQfVU8ov8C

🎧 *Live Chat 24 Jam:*
https://direct\.lc\.chat/16556181

━━━━━━━━━━━━━━━━━━━━━
Akses sekarang & rasakan pengalaman terbaik bersama *PARISBOLA* 🏆
"""

def get_main_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🔗 Link Alternatif", url="https://parisbolaid.bola1.net/"),
            InlineKeyboardButton("💬 Group WhatsApp", url="https://chat.whatsapp.com/FXUaLyPrORfAGQfVU8ov8C"),
        ],
        [
            InlineKeyboardButton("🎧 Live Chat 24 Jam", url="https://direct.lc.chat/16556181"),
            InlineKeyboardButton("📱 Daftar Sekarang", url="https://parisbolaid.bola1.net/"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME_MESSAGE,
        parse_mode="MarkdownV2",
        reply_markup=get_main_keyboard(),
        disable_web_page_preview=True
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME_MESSAGE,
        parse_mode="MarkdownV2",
        reply_markup=get_main_keyboard(),
        disable_web_page_preview=True
    )

async def link_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME_MESSAGE,
        parse_mode="MarkdownV2",
        reply_markup=get_main_keyboard(),
        disable_web_page_preview=True
    )

async def cs_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME_MESSAGE,
        parse_mode="MarkdownV2",
        reply_markup=get_main_keyboard(),
        disable_web_page_preview=True
    )

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME_MESSAGE,
        parse_mode="MarkdownV2",
        reply_markup=get_main_keyboard(),
        disable_web_page_preview=True
    )

def main():
    print("Parisbola Bot sedang berjalan...")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("link", link_command))
    app.add_handler(CommandHandler("cs", cs_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
    print("Bot aktif!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
