import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from get_tweets import get_tweets, get_txt_of_tweets
import twint

app = Flask(__name__)

@app.route("/sms", methods = ['GET','POST'])
def sms_reply():
    resp = MessagingResponse()
    body = request.values.get('Body', None)
    if(len(body) != 0 and len(body) < 12):
        resp.message("Hello, friend. \nI am an SMS Twitter Bot 'Igor'\n\nTo get the latest tweets, "+
        "send me a twitter ID you want to read. For example,\n\nelonmusk 2021-01-01 13:00:00 or just elonmusk 2021-01-01\n"+
        "\nThis will show you all of the tweets posted by Elon Musk since 1pm January 1, 2021")
    else:    
        tw_id = body[:body.find(' ')] 
        date = body[body.find(' ')+1:]
        
        filename = "tweets.txt"
        isThereError = get_tweets(tw_id,date,filename)
        if(isThereError == "valueerror"):
            resp.message("Sorry, invalid request." +
            "\nPlease type in your request as the example:\n\nelonmusk 2021-01-01 13:00:00 or just elonmusk 2021-01-01\n"+
            "\nThis will show you all of the tweets posted by Elon Musk since 1pm January 1, 2021")
        else:  
            arr_of_sms = get_txt_of_tweets(filename)
            if(len(arr_of_sms) == 0):
                resp.message("No tweet from "+tw_id+" since "+date)
            else:    
                for sms in arr_of_sms:
                    resp.message(sms)
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
