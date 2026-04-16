from flask import Flask
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # 1. Leemos los datos limpios
        df = pd.read_csv("datos_limpios.csv")
        
        # 2. Generamos el HTML de la tabla, pero ahora le ponemos clases de Bootstrap
        tabla_html = df.to_html(classes="table table-hover table-striped align-middle", border=0, index=False)
        
        # 3. Creamos una plantilla HTML completa (como una página web real)
        html_completo = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Dashboard de Datos - Jesús Juárez</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
            <link href="https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css" rel="stylesheet">
            
            <style>
                body {{ background-color: #f4f6f9; padding-top: 40px; }}
                .card {{ border-radius: 12px; border: none; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
                .table thead {{ background-color: #2c3e50; color: white; }}
                h1 {{ color: #2c3e50; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="row mb-4">
                    <div class="col">
                        <h1>🚀 Pipeline ETL de Jesús</h1>
                        <p class="text-muted">Datos extraídos, limpios y servidos automáticamente con Python y Docker.</p>
                    </div>
                </div>
                
                <div class="card p-4">
                    <div class="table-responsive">
                        {tabla_html}
                    </div>
                </div>
            </div>

            <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
            <script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
            <script src="https://cdn.datatables.net/1.13.6/js/dataTables.bootstrap5.min.js"></script>
            
            <script>
                $(document).ready(function() {{
                    $('.table').DataTable({{
                        "language": {{
                            "url": "//cdn.datatables.net/plug-ins/1.13.6/i18n/es-ES.json"
                        }},
                        "pageLength": 10
                    }});
                }});
            </script>
        </body>
        </html>
        """
        return html_completo
    except Exception as e:
        return f"<div style='color:red; font-family:sans-serif; padding: 20px;'><h1>⚠️ Error en el servidor</h1><p>{e}</p></div>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)