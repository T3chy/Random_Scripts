from flask import Flask
app = Flask(__name__)
import wordoftheday
@app.route('/')
def help():
    final = wordoftheday.main()
    return("Right now, the most used word in article titles is  " + final[0] + ", being used " + str(final[1])+ " times!")
    
