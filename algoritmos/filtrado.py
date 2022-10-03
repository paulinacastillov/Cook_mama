from recetas.diccionario_recetas import recetas, alergiasData

def verifica(elemento,rec):
  return(elemento in rec['Ingredientes'] )


# retorna un diccionario con las posibles recetas ya filtradas
def funciónFiltroRecetas(alergias=None, ingredientes=None ): #sería una lista de alergias y lista de ingredientes ya definidos

  recetasFiltradas = []
  recetasFiltradasAlergia = []
  ingredientes_alergias = []


  if ingredientes == None and alergias == None: #Caso sin restricciones
    return []
  
  if ingredientes == None and alergias != None :

    for alergia in alergias:
      for ing_alergia in alergiasData[alergia]:
        ingredientes_alergias.append(ing_alergia)

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
        if not ing_alergia in ingredientes_alergias:
          ingredientes_alergias.append(ing_alergia)
          
  
    for receta in recetas:
      ing_recetas = []
      for ing in ingredientes_alergias:
        ing_recetas.append( not(verifica(ing,receta)))
        
      if all(ing_recetas) and not receta in recetasFiltradasAlergia:
          recetasFiltradasAlergia.append(receta)
       
  

    for receta in recetasFiltradasAlergia:
      for ing in ingredientes:
        if verifica(ing,receta) and not receta in recetasFiltradas:
          recetasFiltradas.append(receta)

    
  return(recetasFiltradas)
