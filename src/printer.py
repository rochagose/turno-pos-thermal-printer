from escpos.printer import Usb
from datetime import datetime
import os
import json


ARCHIVO_CONTADOR = "contador.json"

# Identificadores de la impresora
VENDOR_ID = 0x0416  # ID de fabricante (ejemplo, puede variar)
PRODUCT_ID = 0x5011  # ID de producto (ejemplo, puede variar)


def cargar_contador():
    """Carga el contador desde un archivo o crea uno nuevo si no existe."""
    if os.path.exists(ARCHIVO_CONTADOR):
        with open(ARCHIVO_CONTADOR, "r") as file:
            datos = json.load(file)
            return datos["contador"], datos["fecha"]
    else:
        return 0, datetime.now().strftime("%Y-%m-%d")


def guardar_contador(contador):
    """Guarda el contador en un archivo con la fecha actual."""
    with open(ARCHIVO_CONTADOR, "w") as file:
        json.dump({"contador": contador, "fecha": datetime.now().strftime("%Y-%m-%d")}, file)


def actualizar_contador():
    """Verifica si es un nuevo día y reinicia el contador si es necesario."""
    contador, fecha_guardada = cargar_contador()
    fecha_actual = datetime.now().strftime("%Y-%m-%d")

    if fecha_actual != fecha_guardada:
        contador = 0  # Reiniciar si es un nuevo día

    contador += 1  # Incrementar el contador
    guardar_contador(contador)
    
    return contador


def print_turn():
    contador = actualizar_contador()
    
    try:
        # Conectar con la impresora POS-8330 (puede que necesite permisos para acceder a USB)
        impresora = Usb(VENDOR_ID, PRODUCT_ID)
        
        # Imprimir el número de turno con formato adecuado
        impresora.text("\n\n---   TURNO ---\n")
        impresora.text(f"{contador}\n")
        impresora.text(datetime.now().strftime("Fecha: %Y-%m-%d Hora: %H:%M:%S\n"))
        impresora.text("----------------\n")
        
        # Corte de papel
        impresora.cut()
        print("Turno impreso correctamente.")
    except Exception as e:
        print(f"Error al imprimir: {e}")
