
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters, ConversationHandler
import logging


GROUP_TAB = range(1)
#ersal tabligh be grohah
def send_tab_group(bot, update):
    chat_type = update.message.chat.type
    chat_id = update.message.chat_id
    text = update.message.text
    if chat_type == 'private' and chat_id in admin_id:
        if update.message.photo != []:
            file_id = update.message.photo[-1]['file_id']
            for i in get_gapinfo_fordel():
                bot.send_photo(i, file_id , caption=update.message.caption)
            bot.send_message(chat_id, "تبلیغات ارسال شد !\n برای پایان تبلیغ کامند /cancel_tab را بزنید")
            logging.getLogger().info('admin With {0} send tabliq in groups. text tabliq is {1} '.format(chat_id,text))

        else:
            try:
                for i in get_gapinfo_fordel():
                    bot.send_message(i, text)
                bot.send_message(chat_id,"تبلیغات ارسال شد !\n برای پایان تبلیغ کامند /cancel_tab را بزنید")
                logging.getLogger().info('admin With {0} send tabliq in groups. text tabliq is {1} '.format(chat_id, text))

            except:,
                pass


def tabliq_group(bot, update):
    chat_type = update.message.chat.type
    chat_id = update.message.chat_id
    if chat_type == 'private' and chat_id in admin_id:
        pm2 ="""   لطفا پیام تبلیغاتی برای ارسال به گروه ها را ارسال کنید و بعد از ارسال برای پایان تبلیغ کامند   /cancel_tab را بزنید . 
              """
        bot.send_message(update.message.chat_id, pm2)
    return GROUP_TAB

#conversation group
def cancel_tab(bot, update):
    chat_type = update.message.chat.type
    chat_id = update.message.chat_id
    if chat_type == 'private' and chat_id in admin_id:
        pm4 = """ برای ارسال مجدد تبلیغ به گروه ها کامند /tabliq_group را بزنید . 
            """
        bot.send_message(update.message.chat_id, pm4)
    return ConversationHandler.END


grouptab_ = ConversationHandler(
        entry_points=[CommandHandler('tabliq_group', tabliq_group)],
    states={GROUP_TAB: [MessageHandler(Filters.photo | Filters.text, send_tab_group)]},

    fallbacks=[CommandHandler('cancel_tab', cancel_tab)]
    )
updater.dispatcher.add_handler(grouptab_)
