def on_forever():
    # Obtener el nivel de luz
    luz = input.light_level()
    
    # Mostrar el nivel de luz en la pantalla LED
    basic.show_number(luz)

# Iniciar la ejecución continua de la función on_forever
basic.forever(on_forever)
