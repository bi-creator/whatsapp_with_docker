from fastapi import FastAPI
from twilio.rest import Client
app = FastAPI()
sid='AC27c6d54d21daaf6a3e2e87a54cdd6ce5'
authtoken='92945d8aac8e7d2ef03a7b612bd801b9'
@app.post('/Sendtowhatsapp')

def  send(message):
     client=Client(sid,authtoken)

     messa=client.messages.create (to='whatsapp:+917659807765',from_='whatsapp:+14155238886',body=f'hi {message} refer https://reports-dev.effigo.in/report')
     return messa.body

