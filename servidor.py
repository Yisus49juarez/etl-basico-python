from flask import Flask
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        df = pd.read_csv("datos_limpios.csv")
        return df.to_html(classes="table table-striped table-dark", border=0)
    except:
        return "<h1>Aún no hay datos procesados.</h1>"

if __name__ == "__main__":
    # Railway asigna el puerto automáticamente
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)