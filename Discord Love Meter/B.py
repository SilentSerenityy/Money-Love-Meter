from flask import Flask
from threading import Thread
app = Flask('')
@app.route('/')
def main():
    return 'Snuggle is a go'

def run():
    app.run(host='0.0.0.0', port=9492)

def b():
    server = Thread(target=run)
    server.start()
