#two main functions to gather tweets within the given timeline and import them as a list
import twint
import sys

def get_tweets(user_id, start_time,filename):
    result = "no error"
    try:
        c = twint.Config()
        c.Username = user_id
        c.Since = start_time
        open(filename, 'w').close()
        c.Output = filename

        twint.run.Search(c)

    except ValueError:
        result = "valueerror"
    return result

def get_txt_of_tweets(filename):
    arr_of_messages = []
    ourfile = open(filename, "r")
    ourlist = ourfile.readlines()
    ourtext = ""
    counter = 0
    arr_counter = 0
    while(arr_counter < len(ourlist)):
        while(counter < 1200 and arr_counter < len(ourlist)):
            toAdd = ourlist[arr_counter][ourlist[arr_counter].find('-')-4:ourlist[arr_counter].find('<')-7] +"\n"+ ourlist[arr_counter][ourlist[arr_counter].find('>')+2:] +"\n"
            ourtext += toAdd
            counter += len(toAdd)
            arr_counter += 1
        arr_of_messages.append(ourtext)
        ourtext = ''
        counter = 0
    ourfile.close()
    return arr_of_messages
