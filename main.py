import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ============================================================
# CONFIG — isi BOT TOKEN kamu di sini
# atau taruh di Replit Secrets dengan nama TELEGRAM_BOT_TOKEN
# ============================================================
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8490458713:AAHluyYpra-BCVbePGUCoFUtq11kftoJ4AQ")

# ============================================================
# PESAN WELCOME
# ============================================================
WELCOME_MESSAGE = """
🎯 *PARISBOLA OFFICIAL* 🎯

Selamat datang di layanan resmi Parisbola! 👋

✅ Transaksi deposit QRIS proses hanya *1 detik*
✅ Penarikan berapapun dibayar tuntas tanpa ribet
✅ Sistem cepat, stabil & pelayanan terbaik untuk Anda

━━━━━━━━━━━━━━━━━━━━━
🔗 *Link Alternatif:*
https://cutt.ly/GtFHqLcQ

💬 *Group WhatsApp Resmi:*
https://chat.whatsapp.com/FXUaLyPrORfAGQfVU8ov8C

🎧 *Live Chat 24 Jam:*
https://direct.lc.chat/16556181

━━━━━━━━━━━━━━━━━━━━━
Akses sekarang & rasakan pengalaman terbaik bersama *PARISBOLA* 🏆
"""

# ============================================================
# KEYBOARD BUTTONS
# ============================================================
def get_main_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🔗 Link Alternatif", url="https://cutt.ly/GtFHqLcQ"),
            InlineKeyboardButton("💬 Group WhatsApp", url="https://chat.whatsapp.com/FXUaLyPrORfAGQfVU8ov8C"),
        ],
        [
            InlineKeyboardButton("🎧 Live Chat 24 Jam", url="https://direct.lc.chat/16556181"),
            InlineKeyboardButton("📱 Daftar Sekarang", url="https://cutt.ly/GtFHqLcQ"),
        ],
        [
            InlineKeyboardButton("ℹ️ Info Lengkap", callback_data="info"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

# ============================================================
# HANDLER: /start
# ============================================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME_MESSAGE,
        parse_mode="Markdown",
        reply_markup=get_main_keyboard(),
        disable_web_page_preview=True
    )

# ============================================================
# HANDLER: /help
# ============================================================
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
🤖 *PARISBOLA BOT - Menu Bantuan*

Perintah yang tersedia:

/start — Tampilkan pesan selamat datang
/link — Dapatkan link alternatif terbaru
/cs — Hubungi customer service
/info — Informasi tentang Parisbola
/help — Tampilkan menu ini

━━━━━━━━━━━━━━━━━━━━━
Ada pertanyaan? Hubungi CS kami 24 jam!
"""
    await update.message.reply_text(
        help_text,
        parse_mode="Markdown",
        reply_markup=get_main_keyboard()
    )

# ============================================================
# HANDLER: /link
# ============================================================
async def link_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link_text = """
🔗 *LINK RESMI PARISBOLA*

━━━━━━━━━━━━━━━━━━━━━
🌐 *Link Utama:*
https://cutt.ly/GtFHqLcQ

💬 *Group WhatsApp:*
https://chat.whatsapp.com/FXUaLyPrORfAGQfVU8ov8C

🎧 *Live Chat 24 Jam:*
https://direct.lc.chat/16556181
━━━━━━━━━━━━━━━━━━━━━

⚠️ Hati-hati penipuan! Gunakan hanya link resmi di atas.
"""
    await update.message.reply_text(
        link_text,
        parse_mode="Markdown",
        reply_markup=get_main_keyboard(),
        disable_web_page_preview=True
    )

# ============================================================
# HANDLER: /cs
# ============================================================
async def cs_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cs_text = """
🎧 *CUSTOMER SERVICE PARISBOLA*

━━━━━━━━━━━━━━━━━━━━━
✅ CS kami siap melayani *24 jam penuh*

💬 *Live Chat:*
https://direct.lc.chat/16556181

📱 *WhatsApp Group:*
https://chat.whatsapp.com/FXUaLyPrORfAGQfVU8ov8C
━━━━━━━━━━━━━━━━━━━━━

Kami siap membantu deposit, withdraw, 
dan semua pertanyaan Anda! 🏆
"""
    await update.message.reply_text(
        cs_text,
        parse_mode="Markdown",
        reply_markup=get_main_keyboard(),
        disable_web_page_preview=True
    )

# ============================================================
# HANDLER: /info
# ============================================================
async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_text = """
ℹ️ *TENTANG PARISBOLA*

━━━━━━━━━━━━━━━━━━━━━
🏆 Situs taruhan bola terpercaya No.1
📅 Berdiri sejak 2015
👥 989.000+ pelanggan aktif per hari

*Keunggulan Parisbola:*
⚡ Deposit QRIS hanya 1 detik
💰 Kemenangan berapapun pasti dibayar
🔒 Sistem keamanan berlapis
📱 Bisa diakses via HP & desktop
🎧 CS profesional 24 jam

*Tersedia:*
⚽ Pasang Bola & Mix Parlay
🎰 Online 10.000+ game
🎲 Live Casino HD
━━━━━━━━━━━━━━━━━━━━━
"""
    await update.message.reply_text(
        info_text,
        parse_mode="Markdown",
        reply_markup=get_main_keyboard()
    )

# ============================================================
# HANDLER: Pesan biasa (auto reply)
# ============================================================
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME_MESSAGE,
        parse_mode="Markdown",
        reply_markup=get_main_keyboard(),
        disable_web_page_preview=True
    )

# ============================================================
# HANDLER: Callback button
# ============================================================
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "info":
        info_text = """
ℹ️ *TENTANG PARISBOLA*

🏆 Situs taruhan bola terpercaya No.1
📅 Berdiri sejak 2015
👥 989.000+ pelanggan aktif per hari

⚡ Deposit QRIS hanya 1 detik
💰 Kemenangan berapapun pasti dibayar
🎧 CS profesional 24 jam
"""
        await query.edit_message_text(
            info_text,
            parse_mode="Markdown",
            reply_markup=get_main_keyboard()
        )

# ============================================================
# MAIN — jalankan bot
# ============================================================
def main():
    print("🤖 Parisbola Bot sedang berjalan...")
    app = Application.builder().token(BOT_TOKEN).build()

    # Daftarkan semua command handler
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("link", link_command))
    app.add_handler(CommandHandler("cs", cs_command))
    app.add_handler(CommandHandler("info", info_command))

    # Auto reply untuk semua pesan biasa
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    # Callback untuk tombol inline
    from telegram.ext import CallbackQueryHandler
    app.add_handler(CallbackQueryHandler(button_callback))

    print("✅ Bot aktif! Tekan Ctrl+C untuk berhenti.")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
