from twilio.rest import Client 
 
account_sid = 'ACa0ce1ed34a63f8a4222427d548164fc0' 
auth_token = 'Your Token From Twilio' 
client = Client(account_sid, auth_token) 
#Function To send message  
def send_msg(): 
    message = client.messages.create( 
                                from_='whatsapp:Number From Twilio',  
                                body='You are Best',      
                                to='whatsapp:+918127****01' 
                            )  
 
    print(message.sid)