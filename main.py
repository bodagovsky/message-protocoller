from telethon import TelegramClient, events
from kafka_client import AIOProducer

with open("api_id") as api_id_file:
    api_id = api_id_file.readline()

with open("api_hash") as api_hash_file:
    api_hash = api_hash_file.readline()


client = TelegramClient('anon', api_id, api_hash)

kafka_producer = AIOProducer()

@client.on(events.NewMessage(chats=[844182202]))
async def new_message_handle(message):
    await kafka_producer.produce("chan-msg", message.message.message)

def run():
    client.start()
    client.run_until_disconnected()

if __name__ == "__main__":
    run()


