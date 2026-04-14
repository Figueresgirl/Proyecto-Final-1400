# Importa la clase desde PomodoroApp.py
from pomodoroapp import PomodoroApp


# Función principal (punto de entrada del programa)
def main():
    app = PomodoroApp()  # Crear la aplicación
    app.run()            # Ejecutarla


# Ejecutar solo si este archivo es el principal
if __name__ == "__main__":
    main()
