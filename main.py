luz = 0
# Iniciar la ejecución continua de la función on_forever

def on_forever():
    global luz
    # Obtener el nivel de luz
    luz = input.light_level()
    # Mostrar el nivel de luz en la pantalla LED
    basic.show_number(luz)
basic.forever(on_forever)
