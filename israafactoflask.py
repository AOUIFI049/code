from flask import Flask, request, render_template_string

app = Flask(__name__)

def factorielle(n):
    return 1 if n == 0 else n * factorielle(n - 1)

@app.route('/', methods=['GET', 'POST'])
def home():
    resultat, erreur, n = None, None, None
    if request.method == 'POST':
        try:
            n = int(request.form.get('n'))
            if n < 0 or n > 20:
                erreur = "Entrez un nombre entre 0 et 20."
            else:
                resultat = factorielle(n)
        except (ValueError, TypeError):
            erreur = "Entrez un entier valide."

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Factorielle</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; height: 100vh; background: #f4f4f9; }
                .container { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); text-align: center; }
                input[type="number"] { padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; }
                button { padding: 10px 20px; background: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; }
                button:hover { background: #218838; }
                .resultat, .erreur { margin-top: 20px; padding: 10px; border-radius: 5px; }
                .resultat { background: #d4edda; color: #155724; }
                .erreur { background: #f8d7da; color: #721c24; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Calcul de la factorielle</h1>
                <form method="POST">
                    <input type="number" name="n" min="0" max="20" placeholder="Entrez un nombre (0-20)" required>
                    <button type="submit">Calculer</button>
                </form>
                {% if resultat is not none %}
                    <div class="resultat">La factorielle de {{ n }} est {{ resultat }}.</div>
                {% endif %}
                {% if erreur %}
                    <div class="erreur">{{ erreur }}</div>
                {% endif %}
            </div>
        </body>
        </html>
    ''', resultat=resultat, erreur=erreur, n=n)

if __name__ == '__main__':
    app.run(debug=True)