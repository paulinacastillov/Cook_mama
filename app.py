from flask import Flask, redirect, url_for, session, flash
from flask.templating import render_template
from recetas.diccionario_recetas import recetas, alergiasData, ingredientes_recetas
from algoritmos.filtrado import funciónFiltroRecetas
from form import SearchForm
import os

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        if form.searchButton.data:
            ingredients = form.input_ingredients.data
            allergies = form.input_allergies.data
            ingredients_list = list( set([elem.lower() for elem in ingredients.split()]) & ingredientes_recetas )
            
            if len(allergies) == 0:
                allergies = None
            
            session["recetas_filtradas"] = funciónFiltroRecetas(allergies,ingredients_list)
                   
            return redirect(url_for("mostrar_recetas"))
        
    return render_template('index.html', form=form)


@app.route('/resultados', methods=['GET', 'POST'])
def mostrar_recetas():
    resultado = session.get("recetas_filtradas")
    try:
        if len(resultado) != 0:
            return render_template('resultados.html', resultado = resultado)
        else:
            return render_template('resultados.html', mensaje = True)
    except:
        return render_template('resultados.html', mensaje = True)


    
@app.route('/recetas', methods=['GET', 'POST'])
def recetas_completas():
    return render_template('resultados.html', resultado = recetas)           
    
@app.route('/nosotros', methods=['GET', 'POST'])
def nosotros():
    return render_template('nosotros.html')   



if __name__ == '__main__':
    app.run(debug=False)