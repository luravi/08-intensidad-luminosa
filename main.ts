let luz = 0
// Iniciar la ejecución continua de la función on_forever
basic.forever(function () {
    // Obtener el nivel de luz
    luz = input.lightLevel()
    // Mostrar el nivel de luz en la pantalla LED
    basic.showNumber(luz)
})
