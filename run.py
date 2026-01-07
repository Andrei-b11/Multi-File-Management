#!/usr/bin/env python3
"""
Script de ejecución para el Gestor de Archivos y Carpetas
"""

import sys
import os
from pathlib import Path

# Agregar el directorio actual al path para importar módulos
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

try:
    from main import main

    if __name__ == "__main__":
        # Verificar que PyQt6 esté instalado
        try:
            from PyQt6.QtWidgets import QApplication
        except ImportError:
            print("❌ Error: PyQt6 no está instalado.")
            print("📦 Por favor instala las dependencias con:")
            print("   pip install -r requirements.txt")
            sys.exit(1)

        print("🚀 Iniciando Gestor de Archivos y Carpetas...")
        main()

except ImportError as e:
    print(f"❌ Error importando módulos: {e}")
    print("📁 Asegúrate de estar en el directorio correcto del proyecto")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error inesperado: {e}")
    sys.exit(1)
