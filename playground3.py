

def message_creator(text):
    dict_menssages = {
        'computadora': '    ',
        'celular': 'En mi celular puedo aprender usando la app de Platzi',
        'cable': '¡Hay un cable en mi bota!',
        'NA': 'Artículo no encontrado'
    }
    if text in dict_menssages.keys():
        print('existe', dict_menssages[text])
        return dict_menssages[text]
    else:
        print('no exite ', dict_menssages['NA'])
        return dict_menssages['NA']
    
    
def choose_opcion():
    text = input('selecciona entre computadora, celular , cable =>')
    message_creator(text)    

choose_opcion()