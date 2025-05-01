from PySide6.QtWidgets import QLabel, QFileDialog
from PySide6.QtGui import QPainter, QPixmap, QTransform
from PySide6.QtCore import QPoint, QRect, Qt, QSize
from math import atan2, degrees


class WatermarkLabel(QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.watermark = None
        self.watermark_pos = QPoint(50, 50)  # Starting position
        self.dragging = False
        self.drag_offset = QPoint()
        self.scale = 1.0  # default: no scaling
        self.rotation = 0.0  # default: no rotation

        self.interaction_mode = None  # "resize", "rotate", or None
        self.rotate_center = None
        self.original_angle = 0
        self.original_mouse_pos = None
        self.original_scale = 1.0

    def setWatermark(self, pixmap):
        self.watermark = pixmap
        self.update()

    def setTransform(self, pos=None, scale=None, rotation=None):
        if pos:
            self.watermark_pos = pos
        if scale is not None:
            self.scale = scale
        if rotation is not None:
            self.rotation = rotation
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.watermark:
            painter = QPainter(self)

            # Set up transform for drawing
            transform = QTransform()
            transform.translate(self.watermark_pos.x(), self.watermark_pos.y())
            transform.rotate(self.rotation if self.rotation is not None else 0)
            transform.scale(self.scale if self.scale is not None else 1.0,
                            self.scale if self.scale is not None else 1.0)
            painter.setTransform(transform)

            # Draw watermark
            painter.drawPixmap(0, 0, self.watermark)

            # Reset transform to draw handles in correct position
            painter.resetTransform()

            # Calculate actual watermark rect
            scaled_width = self.watermark.width() * (self.scale if self.scale else 1.0)
            scaled_height = self.watermark.height() * (self.scale if self.scale else 1.0)
            top_left = self.watermark_pos
            bottom_right = QPoint(top_left.x() + scaled_width, top_left.y() + scaled_height)

            # Draw resize handle (bottom-right)
            handle_size = 10
            resize_handle_rect = QRect(bottom_right.x() - handle_size,
                                       bottom_right.y() - handle_size,
                                       handle_size, handle_size)
            painter.fillRect(resize_handle_rect, Qt.white)

            # Draw rotation handle (above top-center)
            top_center = QPoint(top_left.x() + scaled_width // 2, top_left.y())
            rotate_handle_center = QPoint(top_center.x(), top_center.y() - 30)
            painter.setBrush(Qt.white)
            painter.drawEllipse(rotate_handle_center, 6, 6)

            painter.end()

    def mousePressEvent(self, event):
        if not self.watermark or event.button() != Qt.LeftButton:
            return

        # Calculate scaled watermark area
        scale = self.scale if self.scale else 1.0
        w = self.watermark.width() * scale
        h = self.watermark.height() * scale
        top_left = self.watermark_pos
        bottom_right = QPoint(top_left.x() + w, top_left.y() + h)

        # Resize handle (bottom-right corner)
        handle_size = 10
        resize_rect = QRect(bottom_right.x() - handle_size,
                            bottom_right.y() - handle_size,
                            handle_size, handle_size)

        if resize_rect.contains(event.pos()):
            self.interaction_mode = "resize"
            self.original_mouse_pos = event.pos()
            self.original_scale = scale
            return

        # Rotation handle (above center top)
        rotate_center = QPoint(top_left.x() + w // 2, top_left.y() - 30)
        if (rotate_center - event.pos()).manhattanLength() < 10:
            self.interaction_mode = "rotate"
            self.rotate_center = QPoint(top_left.x() + w // 2, top_left.y() + h // 2)
            self.original_angle = self.rotation if self.rotation else 0
            self.original_mouse_pos = event.pos()
            return

        # Default dragging
        watermark_rect = QRect(self.watermark_pos, QSize(w, h))
        if watermark_rect.contains(event.pos()):
            self.dragging = True
            self.drag_offset = event.pos() - self.watermark_pos

    def mouseMoveEvent(self, event):
        if self.interaction_mode == "resize":
            delta = event.pos() - self.original_mouse_pos
            new_scale = max(0.1, self.original_scale + delta.x() / 100.0)
            self.scale = new_scale
            self.update()

        elif self.interaction_mode == "rotate":
            center = self.rotate_center
            v1 = self.original_mouse_pos - center
            v2 = event.pos() - center
            angle1 = degrees(atan2(v1.y(), v1.x()))
            angle2 = degrees(atan2(v2.y(), v2.x()))
            angle_delta = angle2 - angle1
            self.rotation = self.original_angle + angle_delta
            self.update()

        elif self.dragging:
            self.watermark_pos = event.pos() - self.drag_offset
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            self.interaction_mode = None

