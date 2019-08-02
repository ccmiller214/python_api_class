#!/usr/bin/python3

from flask import Flask, render_template, request
# app = Flask(__name__, templates_folder='any/path/you/want')
app = Flask(__name__)

@app.route("/ciscoios/")
def ciscoios():
    try:
        qparams = {}
        ## user passes switchname= or we default to "bootstrapped switch"
        ## http://127.0.0.1:5006/ciscoios/?switchname=larrytheswitch
        qparams['switchname'] = request.args.get('switchname','bootstrapped switch')
        qparams['username'] = request.args.get('username','admin')
        qparams['defaultgateway'] = request.args.get('gateway','0.0.0.0')
        qparams['switchIP'] = request.args.get('ip','0.0.0.0')
        qparams['netmask'] = request.args.get('mask','255.255.255.0')
        qparams['mtusize'] = request.args.get('mtu','1450')
        return render_template("baseIOS.conf.j2", **qparams )
    except Exception as err:
        return "uh-oh! " + err

if __name__ == "__main__":
    app.run(port=5006)

