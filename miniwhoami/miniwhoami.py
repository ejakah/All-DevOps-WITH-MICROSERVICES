from flask import Flask, render_template, request
from urllib.parse import quote as url_quote
from requests import get
import socket
import urllib.request
import psutil
import helper
import os
import hashlib
import secrets  # Import the secrets module

global numberOfCalls
numberOfCalls = 1

def get_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def valueCalculation(requestEnvironment):
    global numberOfCalls
    numberOfCalls = numberOfCalls + 1

    WHOAMICOLOR = os.getenv('WHOAMICOLOR')
    print(WHOAMICOLOR)
    if WHOAMICOLOR == None:
        # Generate a random background color
        bgColor = "#" + secrets.token_hex(3)
    else:
        # evaluate WHOAMICOLOR
        if WHOAMICOLOR == "red":
            bgColor = "#ff3030"
        elif WHOAMICOLOR == "green":
            bgColor = "#76ee00"
        elif WHOAMICOLOR == "blue":
            bgColor = "#4876ff"
        elif WHOAMICOLOR == "yellow":
            bgColor = "#eeee00"
        elif WHOAMICOLOR == "purple":  # Corrected the spelling mistake
            bgColor = "#9b30ff"
        else:
            # Generate a random background color
            bgColor = "#" + secrets.token_hex(3)

    if helper.rgb_brightness(bgColor) < 150:
        txtColor = "#ffffff"
    else:
        txtColor = "#000000"

    try:
        IP4 = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET)[1][4][0]
    except:
        IP4 = "no IPv4"

    try:
        IP6 = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)[1][4][0]
    except:
        IP6 = "no IPv6"

    if IP4 == IP6:
        IP6 = "no IPv6"

    # Collect all values
    Werte = {
        "numberOfCalls": numberOfCalls,
        "bgColor": bgColor,
        "txtColor": txtColor,
        "hostname": socket.gethostname(),
        "IP4": IP4,
        "IP6": IP6,
        "hitnumber": numberOfCalls,
    }
    return Werte

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    Werte = valueCalculation(request.environ)
    return render_template('/index.html', Werte=Werte)

if __name__ == '__main__':
    app.run(host='::', port=80)
