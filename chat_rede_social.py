#Chat com Telegram Bot API
import os
from langchain_groq import ChatGroq
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

os.environ["GROQ_API_KEY"] = "GROQ_API_KEY"
TELEGRAM_BOT_TOKEN = "TELEGRAM_BOT_TOKEN"

#Criar o modelo de IA Llama 3
chat = ChatGroq(
    model="llama-3.1-8b-instant", 
    temperature=0
    )

# Função para interagir com o chatbot
def conversar_com_chatbot(pergunta:str) -> str:
    resposta = chat.invoke([
        ("system", "Você é um assistente."),
        ("human", pergunta)
    ])
    return resposta.content

# Função para lidar com mensagens recebidas
async def handle_message(update: Update, 
        context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Boa boa meu jogador, o menino Ney está pensando e ja vai te ajudar!")
    
    
async def responder_mensagem(update: Update, 
        context: ContextTypes.DEFAULT_TYPE) -> None:
    pergunta = update.message.text
    resposta = conversar_com_chatbot(pergunta)
    await update.message.reply_text(resposta)

def main() -> None:
    # Criar a aplicação do bot
    application = ApplicationBuilder().token(
        TELEGRAM_BOT_TOKEN).build()

    # Adicionar manipuladores de comandos e mensagens
    application.add_handler(
        CommandHandler("start", handle_message))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, 
        responder_mensagem))

    # Iniciar o bot
    application.run_polling()

if __name__ == "__main__":
    main()
