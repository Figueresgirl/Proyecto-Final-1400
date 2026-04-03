Proyecto-Final-1400 - Widget Pomodoro
Integrantes
    - Thais Medina
    - Pedro Ibanez
    - Jesús Hernan (c)

Descripción del Proyecto
Este programa es un Widget Pomodoro desarrollado en Python con Tkinter. Permite al usuario:
- Agregar tareas
- Asignar prioridad
- Definir tiempo de trabajo
- Iniciar un temporizador
- Pausar y reiniciar
- Completar tareas
- Realizar descansos automáticos
El sistema está dividido en bloques que organizan la lógica del programa.
--------------------------------------------------
BLOQUE 1: DATOS DEL SISTEMA
Código:
class Pomodoro:
 def __init__(self):
 self.archivo = "tareas.json"
 self.tareas = []
 self.tiempo_restante = 0
Qué hace:
- Guarda el nombre del archivo
- Almacena tareas
- Controla tiempo restante
Explicación:
Este bloque representa el modelo de datos del sistema.
--------------------------------------------------
BLOQUE 2: INICIO E INTERFAZ
Código:
class PomodoroApp:
 def __init__(self):
 self.root = tk.Tk()
 self.root.title("Widget Pomodoro")
 self.root.attributes("-topmost", True)
 self.pomodoro = Pomodoro()
 self.en_cuenta = False
 self.en_descanso = False
 self.tarea_actual = None
 self.setup_ui()
 self.mostrar_tareas()
def setup_ui(self):
 self.marco = tk.Frame(self.root)
 self.entrada = tk.Entry(self.marco)
 self.lista = tk.Listbox(self.marco)
 self.timer_label = tk.Label(self.marco)
Qué hace:
- Crea ventana
- Inicializa variables
- Construye interfaz
Explicación:
Este bloque construye todo lo visual.
--------------------------------------------------
BLOQUE 3: LÓGICA Y TEMPORIZADOR
Código:
def agregar(self):
 nombre = self.entrada.get().strip()
 tiempo = self.tiempo_entry.get().strip()
 if nombre == "" or tiempo == "":
 return
 nueva_tarea = {
 "nombre": nombre,
 "tiempo": int(tiempo),
 "completada": False
 }
 self.pomodoro.tareas.append(nueva_tarea)
def iniciar(self):
 self.pomodoro.tiempo_restante = tarea["tiempo"] * 60
 self.en_cuenta = True
 self.contar()
def contar(self):
 if self.en_cuenta and self.pomodoro.tiempo_restante > 0:
 self.pomodoro.tiempo_restante -= 1
 self.root.after(1000, self.contar)
Qué hace:
- Maneja tareas
- Valida datos
- Ejecuta temporizador
Explicación:
Usa after() para repetir sin congelar la interfaz.
--------------------------------------------------
Conclusión
El programa se divide en:
- Datos
- Interfaz
- Lógica
El temporizador usa after() en lugar de while.

Estructura del Programa
    Proyecto/
        main.py              -    lógica principal
        tareas.json         -    almacenamiento (no implementado completamente)
        pomodoroApp.py  - interfaz gráfica
        README.md

        Verificar que el tiempo sea válido

        Si es válido:
            Convertir minutos a segundos
            Iniciar temporizador

    Mientras tiempo > 0:
        Actualizar cronómetro cada segundo usando after()

    Cuando tiempo termina:
        Mostrar mensaje dentro del widget
        Esperar acción del usuario

    Si tarea se completa:
        Marcar como completada
        Iniciar descanso automático

    Durante descanso:
        Ejecutar temporizador de descanso
        Mostrar mensaje correspondiente

    Fin

Pseudocódigo
    INICIO

        Crear lista de tareas

        Crear interfaz gráfica

        MIENTRAS programa activo

            SI usuario presiona "Agregar"
                Leer nombre
                Leer tiempo
                Leer prioridad

                SI datos válidos
                    Crear tarea
                    Guardar en lista
                    Actualizar interfaz
                SINO
                    Mostrar error
                FIN SI
            FIN SI

            SI usuario selecciona tarea
                Guardar índice seleccionado
            FIN SI

            SI usuario presiona "Eliminar"
                Verificar selección
                Eliminar tarea de lista
                Actualizar interfaz
            FIN SI

            SI usuario presiona "Comenzar"

                SI ya está corriendo
                    Mostrar mensaje
                SINO

                    SI hay tarea seleccionada

                        SI tiempo válido

                            tiempo_restante = tiempo * 60

                            MIENTRAS tiempo_restante > 0
                                Mostrar tiempo
                                Esperar 1 segundo (after)
                                tiempo_restante = tiempo_restante - 1
                            FIN MIENTRAS

                            Mostrar mensaje "Tiempo terminado"

                        SINO
                            Mostrar error
                        FIN SI

                    SINO
                        Mostrar mensaje "Selecciona tarea"
                    FIN SI

                FIN SI

            FIN SI

            SI usuario presiona "Pausar"
                Detener temporizador
            FIN SI

            SI usuario presiona "Completar"
                Marcar tarea como completada
                Iniciar descanso
            FIN SI

        FIN MIENTRAS

    FIN

Conceptos Aplicados
    - Condicionales (if / else)
    - Eventos de interfaz (botones)
    - Temporizador con after()
    - Manejo de listas y diccionarios
    - Programación orientada a objetos
    - Validación de datos del usuario

Decisiones Técnicas
    1. Uso de after() en lugar de while
        Evita que la interfaz se congele

    2. Separación por clases
        Pomodoro -> datos
        PomodoroApp -> interfaz y control

    3. Interfaz dinámica
        Se ocultan y muestran controles según el estado

    4. Colores por prioridad
        Alta -> rojo
        Media -> naranja
        Baja -> verde
        Completada -> gris

Requisitos
    - Python 3.x
    - Tkinter (incluido por defecto)

Conclusión
    Este proyecto implementa una aplicación funcional que integra
    interfaz gráfica, control de flujo y manejo de eventos.

    Demuestra la aplicación práctica de los conceptos aprendidos en clase
    y representa una solución real para la gestión del tiempo y tareas.

