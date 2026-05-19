import logging as log 

from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor
from PySide6.QtCore import Qt, QSize

_icon_cache = {}
log.info(f"Инициализация кэша иконок: {_icon_cache}")

def render_svg_icon_color(svg_path: str, color_hex: str, size=QSize(40, 40)) -> QIcon:
    """Предбразуют цвет SVG-иконки в нужный"""
    
    cache_key = f"{svg_path}_{color_hex}_{size.width()}"
    
    log.info("Проверка иконки в кэше")
    if cache_key in _icon_cache:
        log.info("Иконка найдена")
        return _icon_cache[cache_key]
    
    log.info("Проверка на существование иконки")
    pixmap = QPixmap(svg_path)
    if pixmap.isNull():
        log.warning(f"Внимание: иконки по пути {svg_path} не существует")
        return QIcon()
    
    log.info("Масштабирование иконки под необходимый маштаб, а также её сглаживание")
    pixmap = pixmap.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    
    log.info("Создание прозрачного фона для иконки")
    colored_pixmap = QPixmap(size)
    colored_pixmap.fill(Qt.transparent)
    
    log.info("Создание кисти с включённым сглаживанием")
    painter = QPainter(colored_pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setRenderHint(QPainter.SmoothPixmapTransform)
    
    log.info("Рисование иконки на прозрачном фоне")
    painter.drawPixmap(0, 0, pixmap)
    
    log.debug("Перекраска иконки")
    painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
    painter.fillRect(colored_pixmap.rect(), QColor(color_hex))
    painter.end()

    log.info("Обёртка иконки в QIcon и её кеширование")
    icon = QIcon(colored_pixmap)
    _icon_cache[cache_key] = icon
    return icon
