```python
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Olá! Eu sou o Gpt dos Gênios 🤖. Envie /ajuda para ver o que posso fazer!")

def ajuda(update, context):
    mensagem = """
Sou um bot inteligente 🤖✨

Comandos disponíveis:
/start - Iniciar
/ajuda - Mostrar comandos

(Em breve: baixar músicas, filmes, imagens geradas por IA e mais!)
"""
    update.message.reply_text(mensagem)

def main():
    updater = Updater("8471925241;AAGylvJlqa-sOxH_FnGd_sfjHOzbzP0K9BI", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ajuda", ajuda))
    updater.start_polling()
    updater.idle()

if _name_ == '_main_':
    main()
``
