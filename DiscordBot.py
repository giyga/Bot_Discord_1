import time
import requests
import discord
from bs4 import BeautifulSoup

#Variables
url = "https://" #ACÁ VA EL LINK DEL SITIO DEL CUAL SE EXTRAE LA INFO PARA ENVIARLA AL DISCORD
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
token = '' #ACÁ VA EL TOKEN, ENTRE LAS COMILLAS / TOKEN GOES HERE BETWEEN THE QUOTATION MARKS
channel_id = '''ACÁ VA EL ID DEL CANAL A DONDE IRÁN LOS MSJS. NO HACE FALTA PONERLO ENTRE COMILLAS / HERE GOES THE CHANNEL ID WHERE MESSAGES WILL BE SENT. THERE'S NO
NEED TO PUT IT BETWEEN QUOTATION MARKS IF IT'S ALL NUMBERS'''
old_thread_num = 0

#Comprobar funcionamiento del bot en la consola
@client.event
async def on_ready():
    print('Discord bot is ready!') #Por algún motivo esto ya no funciona

#Enviar mensaje
def EnviaMsj(token, message):
    url = f"https://discord.com/api/v8/channels/{channel_id}/messages"
    data = {"content": message}
    header = {"authorization": f"Bot {token}"}
    req = requests.post(url, data = data, headers = header)
    print(req.status_code)
    
#Obtener enlace del hilo
while True:
  fetch = requests.get(url)
  soup = BeautifulSoup(fetch.text, 'html.parser')
  thread = soup.find_all('a')
  for a in thread:
    if a == thread[8]:
      thread_num = int(a.get('href')[slice(18, len(a.get('href')))])
      if thread_num > old_thread_num:
        old_thread_num = thread_num
        EnviaMsj(token, "https://example.com/" + a.get('href'))
      else:
        break
  time.sleep(2)

#Iniciar el bot
client.run(token)
'''Me llama la atención que esto haya que ponerlo de último para que funcione el código de arriba. Por qué será?'''
