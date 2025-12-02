import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QLineEdit, QPushButton, QLabel)
from PyQt5.QtCore import Qt


class CleanWatchApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Pencere Ayarları
        self.setWindowTitle("CleanWatch - Reklamsız İzle")
        self.setGeometry(100, 100, 500, 200)  # Biraz daha kompakt bir boyut

        # 1. Ana Taşıyıcı (Central Widget)
        # PyQt'de her şey bir ana panelin üstünde durmalıdır.
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 2. Düzenleyici (Layout)
        # Elemanları alt alta (Vertical) dizecek yönetici
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # 3. Arayüz Elemanları (Widgets)

        # Bilgi Etiketi
        self.status_label = QLabel("Video linkini aşağıya yapıştırın:")
        self.status_label.setStyleSheet("font-size: 14px; font-weight: bold;")

        # Link Giriş Kutusu (Input)
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Örn: https://puhutv.com/behzat-c-bir-ankara-polisiyesi-1-bolum-izle")
        self.url_input.setStyleSheet("padding: 8px;")  # Biraz ferah olsun

        # İzle Butonu
        self.watch_button = QPushButton("Videoyu Getir ve Oynat 🎬")
        self.watch_button.setCursor(Qt.PointingHandCursor)  # Mouse üstüne gelince el işareti çıksın
        self.watch_button.setStyleSheet(
            "padding: 10px; background-color: #2ecc71; color: white; font-weight: bold; border-radius: 5px;")

        # 4. Elemanları Düzene Ekleme (Sırası önemli!)
        layout.addWidget(self.status_label)
        layout.addWidget(self.url_input)
        layout.addSpacing(10)  # Araya 10px boşluk
        layout.addWidget(self.watch_button)
        layout.addStretch()  # En alta boşluk itici koyar, elemanları yukarı toplar

        # 5. Butona Tıklanma Olayı (Signal & Slot)
        self.watch_button.clicked.connect(self.on_watch_clicked)

    def on_watch_clicked(self):
        """Butona basılınca çalışacak fonksiyon"""
        link = self.url_input.text()
        if not link:
            self.status_label.setText("❌ Lütfen geçerli bir link girin!")
            return

        # Şimdilik sadece terminale yazdırıp, etiketi güncelleyelim
        print(f"Alınan Link: {link}")
        self.status_label.setText("⏳ Link işleniyor, lütfen bekleyin...")


# Uygulamayı Başlat
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CleanWatchApp()
    window.show()
    sys.exit(app.exec_())