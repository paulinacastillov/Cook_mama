recetas = [
    
{'Nombre': 'licuado_desayuno', 'Ingredientes': ['fresas', 'yogurt natural', 'estevia', 'naranja'], 'Instrucciones': 'Tomas diez fresas les añades una taza de yogurt natural, adicionas un sobre de estevia (edulcorante) y el jugo de media naranja, mezclas todo y lo licuas de 2 a 3 minutos.', 'img_url': ''} ,
{'Nombre': 'jambalaya_pollo', 'Ingredientes': ['jamon', 'caldo', 'pollo', 'pimienta', 'aceite oliva', 'apio', 'cebolla', 'pimenton pimiento', 'ajo', 'arroz'], 'Instrucciones': 'En una cazuela colocas 450g de jamón y 1 1/2 vasos de agua, los cocinas por minutos, mientras cortas 450g de pollo y 1 rama de apio en cubos, pasado el tiempo escurres el jamón, luego colocas 2 cucharadas de aceite de oliva y sofries el apio previamente cortado, 2 dientes de ajo y 1/4 de cebolla. Una vez sofreido, salpimentas el pollo y lo añades a la mezcla para freirlo, ya todo freido, agregas el jamón y 1 taza de arroz, después agregas 2 1/2 tazas de caldo y dejas que cueza el arroz, una vez cocido puedes servir.', 'img_url': ''} ,
{'Nombre': 'latte_calabaza', 'Ingredientes': ['puren calabaza', 'estevia', 'canela', 'jengibre', 'nuez moscada', 'leche', 'cafe', 'nata'], 'Instrucciones': 'Falta instrucciones', 'img_url': ''} ,
{'Nombre': 'Carapulca chinchana', 'Ingredientes': ['fideos', 'pollo', 'ajo molido', 'cebolla', 'comino', 'achiote molido', 'tomate', 'albahaca', 'perejil', 'aceite', 'cerdo', 'papa', 'ají', 'pimienta', 'yuca'], 'Instrucciones': 'Falta instrucciones', 'img_url': ''} ,
{'Nombre': 'Olluquitos con carne', 'Ingredientes': ['ollucos', 'carne', 'ají mirasol', 'cebolla', 'aceite', 'ajo', 'oregano', 'sal', ' pimienta'], 'Instrucciones': 'Falta instrucciones', 'img_url': ''} ,
{'Nombre': 'Ají de gallina', 'Ingredientes': ['gallina', 'papa', 'ají panca', 'ají amarillo', 'cebollas', 'ajos', 'pan', 'leche', 'queso parmesano', 'maní', 'pecanas', 'sal', 'pimientas', 'aceitunas', 'huevo'], 'Instrucciones': 'Falta instrucciones', 'img_url': ''} ,
{'Nombre': 'Salpicón de pollo', 'Ingredientes': ['pechuga de pollo', 'arvejas', 'papa', 'lechuga', 'mayonesa', 'zanahoria', 'sal', 'pimienta'], 'Instrucciones': 'Falta instrucciones', 'img_url': ''} ,
{'Nombre': 'Papa a la huancaína', 'Ingredientes': ['papa', 'ají amarillo', 'cebolla', 'aceite', 'leche', 'queso crema', 'galleta soda', 'sal', 'pimienta'], 'Instrucciones': 'Falta instrucciones', 'img_url': ''} ,
{'Nombre': 'Escabeche de pollo', 'Ingredientes': ['pollo', 'cebolla', 'aceituna negra', 'ají verde', 'vinagre', 'ajo', 'azucar', 'aceite', 'huevo duro', 'sal', 'pimienta'], 'Instrucciones': 'Falta instrucciones', 'img_url': ''} ,
{'Nombre': 'Sopa de olluco', 'Ingredientes': ['ollucos', 'leche', 'aceite', 'queso', 'papas', 'cebolla', 'perejil', 'culantro', 'ají', 'oregano', 'ajo', 'huevo', 'hierbabuena', 'caldo de carne', 'sal', 'pimienta'], 'Instrucciones': 'Falta instrucciones', 'img_url': ''} ,
{'Nombre': 'Arroz con langostinos', 
'Ingredientes': ['arroz', 'langostinos', 'aceite vegetal', 'cebolla roja', 'ajos', 'tomates', 'pasta de tomate', 'zanahoria', 'alverjas', 'orégano', 'vino blanco', 'pimientos morrones', 'culantro', 'sal', 'pimienta'], 
'Instrucciones': 'Falta instrucciones', 
'img_url': 'https://drive.google.com/file/d/1xKDzb3cBpYFZIoLxPCsoc5C4OzDqPetr/view?usp=sharing'} 

]



#https://drive.google.com/file/d/1xKDzb3cBpYFZIoLxPCsoc5C4OzDqPetr/view?usp=sharing
#https://drive.google.com/uc?id=1xKDzb3cBpYFZIoLxPCsoc5C4OzDqPetr


alergiasData = {'Mariscos': ['camaron, cangrejo','almeja','pulpo','langostinos'],'Lácteos':['leche','queso'],
'Gluten':['trigo', 'avena', 'cebada', 'centeno']} #alimentos en 

ingredientes_recetas = set()
for receta in recetas:
  if receta["img_url"] != "":
    receta["img_url"] = receta["img_url"].replace("file/d/","uc?id=")
    receta["img_url"] = receta["img_url"].replace("/view?usp=sharing","")

  for ingrediente in receta['Ingredientes']:
    ingredientes_recetas.add(ingrediente)