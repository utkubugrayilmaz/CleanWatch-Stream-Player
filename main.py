import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLineEdit, QPushButton, QLabel,
                             QFrame, QMessageBox, QSlider, QStyle)
from PyQt5.QtCore import Qt, QTimer

# --- VLC YOLUNU GÖSTERME KODU ---
vlc_path = r"C:\Program Files\VideoLAN\VLC"
if os.path.exists(vlc_path):
    os.add_dll_directory(vlc_path)
# --------------------------------

import vlc
from video_engine import VideoEngine


# --- ÖZEL SLIDER SINIFI (Tıklayınca Işınlanan) ---
class ClickableSlider(QSlider):
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            val = self.minimum() + ((self.maximum() - self.minimum()) * event.x()) / self.width()
            self.setValue(int(val))
            event.accept()
            # Tıklandığı an sinyalleri tetikle
            self.sliderMoved.emit(int(val))
            self.sliderPressed.emit()
        super().mousePressEvent(event)


# -------------------------------------------------

class CleanWatchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CleanWatch - Universal Stream Player")
        self.setGeometry(100, 100, 1000, 700)
        self.setStyleSheet("background-color: #2c3e50; color: white;")

        # Motor Hazırlığı
        self.engine = VideoEngine()

        # --- VLC HAZIRLIĞI (DÜZELTİLDİ) ---
        # Sadece çalışan parametreyi bıraktık. Hata veren silindi.
        self.instance = vlc.Instance("--avcodec-hw=none")
        self.media_player = self.instance.media_player_new()

        # Zamanlayıcı
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_ui_status)

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)

        # 1. Video Alanı
        self.video_frame = QFrame()
        self.video_frame.setStyleSheet("background-color: black; border: 2px solid #34495e;")
        self.video_frame.mouseDoubleClickEvent = self.toggle_fullscreen
        self.main_layout.addWidget(self.video_frame, stretch=1)

        # 2. Kontrol Paneli
        self.controls_layout = QVBoxLayout()

        # Tıklanabilir Slider
        self.position_slider = ClickableSlider(Qt.Horizontal)
        self.position_slider.setMaximum(1000)
        self.position_slider.sliderPressed.connect(self.slider_pressed)
        self.position_slider.sliderReleased.connect(self.slider_released)
        self.controls_layout.addWidget(self.position_slider)

        # Alt Butonlar
        self.buttons_layout = QHBoxLayout()

        # Oynat/Durdur Butonu
        self.play_button = QPushButton()
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.play_button.clicked.connect(self.play_pause)
        self.play_button.setFixedSize(40, 40)
        self.play_button.setStyleSheet("background-color: #e67e22; border-radius: 5px;")

        # Ses Kontrolü
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(70)
        self.volume_slider.setFixedWidth(100)
        self.volume_slider.valueChanged.connect(self.set_volume)

        # Link Girişi
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Paste Video Link Here (YouTube, PuhuTV, Twitch etc.)...")
        self.url_input.setStyleSheet("padding: 8px; color: black; background-color: #ecf0f1; border-radius: 5px;")

        # Yükle Butonu
        self.load_button = QPushButton("Load & Play")
        self.load_button.setCursor(Qt.PointingHandCursor)
        self.load_button.setStyleSheet(
            "background-color: #27ae60; padding: 8px; font-weight: bold; border-radius: 5px;")
        self.load_button.clicked.connect(self.load_video)

        self.buttons_layout.addWidget(self.play_button)
        self.buttons_layout.addWidget(self.volume_slider)
        self.buttons_layout.addWidget(self.url_input)
        self.buttons_layout.addWidget(self.load_button)

        self.controls_layout.addLayout(self.buttons_layout)
        self.main_layout.addLayout(self.controls_layout)

        # Durum Etiketi
        self.status_label = QLabel("Ready - Space: Play/Pause | Arrows: Seek | Dbl Click: Fullscreen")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-size: 11px; color: #bdc3c7;")
        self.main_layout.addWidget(self.status_label)

    def load_video(self):
        link = self.url_input.text().strip()
        if not link:
            self.status_label.setText("Please enter a valid link!")
            return

        self.status_label.setText("Processing link...")
        self.load_button.setEnabled(False)
        QApplication.processEvents()

        try:
            result = self.engine.extract_stream_data(link)

            if result['status'] == 'success':
                self.media_player.stop()

                media = self.instance.media_new(result['url'])
                self.media_player.set_media(media)

                if sys.platform.startswith('linux'):
                    self.media_player.set_xwindow(self.video_frame.winId())
                elif sys.platform == "win32":
                    self.media_player.set_hwnd(self.video_frame.winId())
                elif sys.platform == "darwin":
                    self.media_player.set_nsobject(int(self.video_frame.winId()))

                self.media_player.play()
                self.timer.start()

                self.status_label.setText(f"Playing: {result['title']}")
                self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

                # --- ODAK DÜZELTME ---
                self.setFocus()
                # ---------------------

            else:
                self.status_label.setText("Error: Video not found")
                QMessageBox.critical(self, "Error", f"Failed to load video:\n{result['message']}")

        except Exception as e:
            self.status_label.setText(f"Critical Error: {str(e)}")

        finally:
            self.load_button.setEnabled(True)

    def play_pause(self):
        if self.media_player.is_playing():
            self.media_player.pause()
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.status_label.setText("Paused")
        else:
            self.media_player.play()
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            self.status_label.setText("Playing")

    def set_volume(self, volume):
        self.media_player.audio_set_volume(volume)

    def update_ui_status(self):
        if self.media_player.is_playing() and not self.position_slider.isSliderDown():
            length = self.media_player.get_length()
            time = self.media_player.get_time()

            if length > 0:
                new_pos = int((time / length) * 1000)
                self.position_slider.blockSignals(True)
                self.position_slider.setValue(new_pos)
                self.position_slider.blockSignals(False)

    def slider_pressed(self):
        self.timer.stop()

    def slider_released(self):
        position = self.position_slider.value()
        length = self.media_player.get_length()

        if length > 0:
            target_time = int((position / 1000) * length)
            self.media_player.set_time(target_time)

        self.timer.start()
        self.setFocus()  # Slider bırakılınca odağı pencereye ver

    def keyPressEvent(self, event):
        """Klavye Kısayolları"""
        if event.key() == Qt.Key_Space:
            self.play_pause()

        elif event.key() == Qt.Key_Right:
            if self.media_player.is_playing():
                current = self.media_player.get_time()
                total = self.media_player.get_length()
                self.media_player.set_time(min(current + 10000, total))
                self.status_label.setText("⏩ +10 Seconds")

        elif event.key() == Qt.Key_Left:
            if self.media_player.is_playing():
                current = self.media_player.get_time()
                self.media_player.set_time(max(current - 10000, 0))
                self.status_label.setText("⏪ -10 Seconds")

        elif event.key() == Qt.Key_Escape:
            if self.isFullScreen():
                self.toggle_fullscreen(None)

    def toggle_fullscreen(self, event):
        if self.isFullScreen():
            self.showNormal()
            self.controls_layout.parentWidget().show()
        else:
            self.showFullScreen()

    def closeEvent(self, event):
        self.media_player.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CleanWatchApp()
    window.show()
    sys.exit(app.exec_())