import pandas as pd
import os
from datetime import datetime

class ProgramaAcuicola:
    def __init__(self, presupuesto_inicial):
        self.archivo_datos = "beneficiarios.csv"
        self.presupuesto_total = presupuesto_inicial
        self.columnas = ["Nombre", "Semilla", "Monto", "Fecha", "Lugar"]
        self._inicializar_archivo()

    def _inicializar_archivo(self):
        """Crea el archivo CSV si no existe."""
        if not os.path.exists(self.archivo_datos):
            df = pd.DataFrame(columns=self.columnas)
            df.to_csv(self.archivo_datos, index=False)

    def calcular_presupuesto_restante(self):
        """Calcula cuánto dinero queda disponible."""
        df = pd.read_csv(self.archivo_datos)
        total_gastado = df["Monto"].sum()
        return self.presupuesto_total - total_gastado

    def registrar_beneficiario(self, nombre, semilla, monto, lugar):
        """Registra un nuevo apoyo y actualiza el presupuesto."""
        presupuesto_actual = self.calcular_presupuesto_restante()

        if monto > presupuesto_actual:
            print(f"❌ Error: Fondos insuficientes. Disponible: ${presupuesto_actual:,.2f}")
            return

        nuevo_registro = {
            "Nombre": nombre,
            "Semilla": semilla,
            "Monto": monto,
            "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Lugar": lugar
        }

        df = pd.read_csv(self.archivo_datos)
        df = pd.concat([df, pd.DataFrame([nuevo_registro])], ignore_index=True)
        df.to_csv(self.archivo_datos, index=False)
        
        print(f"✅ Registro exitoso para {nombre}.")
        print(f"💰 Nuevo saldo del presupuesto: ${self.calcular_presupuesto_restante():,.2f}")

# --- CONFIGURACIÓN Y USO ---

PRESUPUESTO_INICIAL = 35723233.13
programa = ProgramaAcuicola(PRESUPUESTO_INICIAL)

# Ejemplo de uso:
# programa.registrar_beneficiario("Cooperativa del Mar", "Cría de Tilapia", 150000.00, "Sinaloa")
# programa.registrar_beneficiario("Juan Pérez", "Semilla de Ostión", 45200.50, "Ensenada")

print(f"Saldo actual en sistema: ${programa.calcular_presupuesto_restante():,.2f}")