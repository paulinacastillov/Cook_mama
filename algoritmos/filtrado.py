from recetas.diccionario_recetas import recetas, alergiasData

def verifica(elemento,rec):
  return(elemento in rec['Ingredientes'] )


# retorna un diccionario con las posibles recetas ya filtradas
def funciónFiltroRecetas(alergias=None, ingredientes=None ): #sería una lista de alergias y lista de ingredientes ya definidos

  recetasFiltradas = []
  recetasFiltradasAlergia = []
  recetasFiltradasIngredientes = set()
  ingredientes_alergias = set()
  ingredientes_casa = set()

  if ingredientes == None and alergias == None: #Caso sin restricciones
    return []
  
  if ingredientes == None and alergias != None :

    for alergia in alergias:
      for ing_alergia in alergiasData[alergia]:
        ingredientes_alergias.add(ing_alergia)

    for receta in recetas:
      for ing in ingredientes_alergias:
        if not verifica(ing,receta) and not receta in recetasFiltradas:
          recetasFiltradas.append(receta)

  if ingredientes != None and alergias == None:

    for receta in recetas:
      for ing in ingredientes:
        if verifica(ing,receta) and not receta in recetasFiltradas:
          recetasFiltradas.append(receta)

  if ingredientes != None and alergias != None :

    for alergia in alergias:
      for ing_alergia in alergiasData[alergia]:
        ingredientes_alergias.add(ing_alergia)

    for receta in recetas:
      for ing in ingredientes_alergias:
        if not verifica(ing,receta) and not receta in recetasFiltradasAlergia:
          recetasFiltradasAlergia.append(receta)
  

    for receta in recetasFiltradasAlergia:
      for ing in ingredientes:
        if verifica(ing,receta) and not receta in recetasFiltradas:
          recetasFiltradas.append(receta)

    
  return(recetasFiltradas)

  #hasta acá funciona, quiero hacerle una puntuación de receta más cercana a los ingredientes que tiene