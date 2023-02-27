from telethon import TelegramClient, events
from kafka_client import AIOProducer

api_id = 29016752
api_hash = 'c157aba1d9ca2aefbc34e51118c040d6'
client = TelegramClient('anon', api_id, api_hash)

kafka_producer = AIOProducer()

@client.on(events.NewMessage(chats=[844182202]))
async def new_message_handle(message):
    # print(message)
    await kafka_producer.produce("chan-msg", message.message.message)

def run():
    client.start()
    client.run_until_disconnected()

if __name__ == "__main__":
    run()


