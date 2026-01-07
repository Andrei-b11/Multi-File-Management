"""
Configuración de la aplicación Gestor de Archivos y Carpetas
"""

import os
from pathlib import Path


class Config:
    """Configuración principal de la aplicación"""

    # Información de la aplicación
    APP_NAME = "Gestor de Archivos y Carpetas"
    APP_VERSION = "1.0.0"
    APP_AUTHOR = "Tu Nombre"

    # Archivos de datos
    DATA_FILE = "file_manager_data.json"
    BACKUP_FILE = "file_manager_backup.json"
    LOG_FILE = "file_manager.log"

    # Configuración de la interfaz
    WINDOW_MIN_WIDTH = 600
    WINDOW_MIN_HEIGHT = 400
    WINDOW_DEFAULT_WIDTH = 800
    WINDOW_DEFAULT_HEIGHT = 600

    # Configuración de monitoreo
    FILE_CHECK_INTERVAL = 2000  # milisegundos
    AUTO_SAVE_INTERVAL = 30000  # milisegundos

    # Configuración visual
    ITEM_HEIGHT = 80
    ITEM_SPACING = 5
    SCROLL_BAR_WIDTH = 12

    # Colores del tema
    COLORS = {
        "background": "#1a1a1a",
        "surface": "#2a2a2a",
        "surface_variant": "#3a3a3a",
        "surface_hover": "#454545",
        "primary": "#4a90e2",
        "primary_hover": "#357abd",
        "secondary": "#6c757d",
        "text_primary": "#ffffff",
        "text_secondary": "#cccccc",
        "text_tertiary": "#aaaaaa",
        "text_disabled": "#888888",
        "border": "#555555",
        "border_hover": "#777777",
        "error": "#dc3545",
        "error_hover": "#c82333",
        "success": "#28a745",
        "warning": "#ffc107",
        "info": "#17a2b8",
    }

    # Configuración de archivos
    MAX_FILE_SIZE_MB = 1024  # Tamaño máximo para mostrar información detallada
    SUPPORTED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"}
    SUPPORTED_VIDEO_EXTENSIONS = {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"}
    SUPPORTED_AUDIO_EXTENSIONS = {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"}
    SUPPORTED_DOCUMENT_EXTENSIONS = {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"}
    SUPPORTED_ARCHIVE_EXTENSIONS = {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"}

    # Configuración de logging
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_MAX_SIZE = 5 * 1024 * 1024  # 5 MB
    LOG_BACKUP_COUNT = 3

    @classmethod
    def get_data_dir(cls) -> Path:
        """Obtener directorio de datos de la aplicación"""
        if os.name == "nt":  # Windows
            data_dir = Path(os.environ.get("APPDATA", Path.home())) / cls.APP_NAME
        else:  # Linux/macOS
            data_dir = Path.home() / f".{cls.APP_NAME.lower().replace(' ', '_')}"

        data_dir.mkdir(exist_ok=True)
        return data_dir

    @classmethod
    def get_data_file_path(cls) -> Path:
        """Obtener ruta completa del archivo de datos"""
        return cls.get_data_dir() / cls.DATA_FILE

    @classmethod
    def get_backup_file_path(cls) -> Path:
        """Obtener ruta completa del archivo de backup"""
        return cls.get_data_dir() / cls.BACKUP_FILE

    @classmethod
    def get_log_file_path(cls) -> Path:
        """Obtener ruta completa del archivo de log"""
        return cls.get_data_dir() / cls.LOG_FILE

    @classmethod
    def get_file_icon(cls, filepath: str) -> str:
        """Obtener icono emoji según el tipo de archivo"""
        if os.path.isdir(filepath):
            return "📁"

        ext = Path(filepath).suffix.lower()

        if ext in cls.SUPPORTED_IMAGE_EXTENSIONS:
            return "🖼️"
        elif ext in cls.SUPPORTED_VIDEO_EXTENSIONS:
            return "🎬"
        elif ext in cls.SUPPORTED_AUDIO_EXTENSIONS:
            return "🎵"
        elif ext in cls.SUPPORTED_DOCUMENT_EXTENSIONS:
            return "📄"
        elif ext in cls.SUPPORTED_ARCHIVE_EXTENSIONS:
            return "📦"
        elif ext in {".exe", ".msi", ".app", ".deb", ".rpm"}:
            return "⚙️"
        elif ext in {".py", ".js", ".html", ".css", ".cpp", ".java", ".c", ".h"}:
            return "💻"
        elif ext in {".xlsx", ".xls", ".csv"}:
            return "📊"
        elif ext in {".pptx", ".ppt"}:
            return "📊"
        else:
            return "📄"

    @classmethod
    def get_file_category(cls, filepath: str) -> str:
        """Obtener categoría del archivo"""
        if os.path.isdir(filepath):
            return "Carpeta"

        ext = Path(filepath).suffix.lower()

        if ext in cls.SUPPORTED_IMAGE_EXTENSIONS:
            return "Imagen"
        elif ext in cls.SUPPORTED_VIDEO_EXTENSIONS:
            return "Video"
        elif ext in cls.SUPPORTED_AUDIO_EXTENSIONS:
            return "Audio"
        elif ext in cls.SUPPORTED_DOCUMENT_EXTENSIONS:
            return "Documento"
        elif ext in cls.SUPPORTED_ARCHIVE_EXTENSIONS:
            return "Archivo"
        elif ext in {".exe", ".msi", ".app", ".deb", ".rpm"}:
            return "Ejecutable"
        elif ext in {".py", ".js", ".html", ".css", ".cpp", ".java", ".c", ".h"}:
            return "Código"
        elif ext in {".xlsx", ".xls", ".csv"}:
            return "Hoja de Cálculo"
        elif ext in {".pptx", ".ppt"}:
            return "Presentación"
        else:
            return "Archivo"


# Configuración de estilos CSS-like para PyQt6
STYLES = {
    "main_window": f"""
        QMainWindow {{
            background-color: {Config.COLORS["background"]};
            color: {Config.COLORS["text_primary"]};
        }}
        QMenuBar {{
            background-color: {Config.COLORS["surface"]};
            color: {Config.COLORS["text_primary"]};
            padding: 4px;
        }}
        QMenuBar::item {{
            background-color: transparent;
            padding: 8px 12px;
            border-radius: 4px;
        }}
        QMenuBar::item:selected {{
            background-color: {Config.COLORS["primary"]};
        }}
        QMenu {{
            background-color: {Config.COLORS["surface"]};
            color: {Config.COLORS["text_primary"]};
            border: 1px solid {Config.COLORS["border"]};
            border-radius: 4px;
        }}
        QMenu::item {{
            padding: 8px 20px;
            border-radius: 4px;
            margin: 2px;
        }}
        QMenu::item:selected {{
            background-color: {Config.COLORS["primary"]};
        }}
        QStatusBar {{
            background-color: {Config.COLORS["surface"]};
            color: {Config.COLORS["text_secondary"]};
            border-top: 1px solid {Config.COLORS["border"]};
        }}
    """,
    "scroll_area": f"""
        QScrollArea {{
            border: none;
            background-color: {Config.COLORS["background"]};
        }}
        QScrollBar:vertical {{
            background-color: {Config.COLORS["surface_variant"]};
            width: {Config.SCROLL_BAR_WIDTH}px;
            border-radius: 6px;
        }}
        QScrollBar::handle:vertical {{
            background-color: {Config.COLORS["secondary"]};
            border-radius: 6px;
            min-height: 20px;
        }}
        QScrollBar::handle:vertical:hover {{
            background-color: {Config.COLORS["border_hover"]};
        }}
    """,
    "item_widget": f"""
        QFrame {{
            background-color: {Config.COLORS["surface_variant"]};
            border: 1px solid {Config.COLORS["border"]};
            border-radius: 8px;
            margin: 2px;
        }}
        QFrame:hover {{
            background-color: {Config.COLORS["surface_hover"]};
            border-color: {Config.COLORS["border_hover"]};
        }}
        QPushButton {{
            background-color: {Config.COLORS["primary"]};
            border: none;
            border-radius: 4px;
            color: white;
            font-weight: bold;
            padding: 4px;
        }}
        QPushButton:hover {{
            background-color: {Config.COLORS["primary_hover"]};
        }}
    """,
    "dialog": f"""
        QDialog {{
            background-color: {Config.COLORS["surface"]};
            color: {Config.COLORS["text_primary"]};
        }}
        QLabel {{
            color: {Config.COLORS["text_primary"]};
            font-weight: bold;
        }}
        QTextEdit {{
            background-color: {Config.COLORS["surface_variant"]};
            border: 1px solid {Config.COLORS["border"]};
            border-radius: 4px;
            color: {Config.COLORS["text_primary"]};
            padding: 5px;
        }}
        QPushButton {{
            background-color: {Config.COLORS["primary"]};
            border: none;
            border-radius: 4px;
            color: white;
            padding: 8px 16px;
            font-weight: bold;
        }}
        QPushButton:hover {{
            background-color: {Config.COLORS["primary_hover"]};
        }}
    """,
    "instruction_label": f"""
        QLabel {{
            color: {Config.COLORS["text_disabled"]};
            font-size: 12pt;
            padding: 40px;
            border: 2px dashed {Config.COLORS["border"]};
            border-radius: 10px;
            background-color: {Config.COLORS["surface"]};
        }}
    """,
    "remove_button": f"""
        QPushButton {{
            background-color: {Config.COLORS["error"]};
            border: none;
            border-radius: 12px;
            color: white;
            font-weight: bold;
        }}
        QPushButton:hover {{
            background-color: {Config.COLORS["error_hover"]};
        }}
    """,
}
