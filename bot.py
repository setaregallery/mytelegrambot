from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = '8437611346:AAEIf5jO6p1qCLxlg12o6nAfJhFDtEaY8oU'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = update.message.text

    if text == '/start':
        await update.message.reply_text('سلام! لطفاً شماره تماس خودت رو وارد کن.')
        context.user_data['waiting_for_phone'] = True
    elif context.user_data.get('waiting_for_phone'):
        await update.message.reply_text(f'شماره {text} ثبت شد. ثبت‌نامت با موفقیت انجام شد. لینک وبینار به زودی ارسال می‌شود.')
        context.user_data['waiting_for_phone'] = False
    else:
        await update.message.reply_text('لطفاً روی /start بزن و شماره‌ات رو وارد کن.')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.add_handler(MessageHandler(filters.COMMAND, handle_message))
    app.run_polling()
