import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QLineEdit, QPushButton, QLabel, QMessageBox)
from PyQt5.QtCore import Qt

# 1. YENİ: Yazdığımız motoru buraya çağırıyoruz
from video_engine import VideoEngine


class CleanWatchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CleanWatch - Universal Stream Player")  # İsmi güncelledik :)
        self.setGeometry(100, 100, 600, 250)

        # Motorumuzu hazırlayalım (Örnekleme)
        self.engine = VideoEngine()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.status_label = QLabel("İzlemek istediğiniz video linkini yapıştırın:")
        self.status_label.setStyleSheet("font-size: 14px; font-weight: bold;")

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Örn: https://puhutv.com/behzat-c-bir-ankara-polisiyesi-1-bolum-izle")
        self.url_input.setStyleSheet("padding: 8px;")

        self.watch_button = QPushButton("Videoyu Çözümle 🎬")
        self.watch_button.setCursor(Qt.PointingHandCursor)
        self.watch_button.setStyleSheet(
            "padding: 10px; background-color: #3498db; color: white; font-weight: bold; border-radius: 5px;")

        layout.addWidget(self.status_label)
        layout.addWidget(self.url_input)
        layout.addSpacing(10)
        layout.addWidget(self.watch_button)
        layout.addStretch()

        self.watch_button.clicked.connect(self.on_watch_clicked)

    def on_watch_clicked(self):
        link = self.url_input.text().strip()  # Boşlukları temizle
        if not link:
            self.status_label.setText("❌ Lütfen geçerli bir link girin!")
            return

        self.status_label.setText("⏳ Video kaynağı aranıyor... (Biraz sürebilir)")
        self.watch_button.setEnabled(False)  # Butona tekrar basılmasın
        QApplication.processEvents()  # Arayüzün donmasını engellemek için tazeleyelim

        # 2. YENİ: Motoru çalıştırıyoruz
        # Normalde bunu Thread (iş parçacığı) ile yapmak gerekir ama
        # şimdilik basit olsun diye direkt çağırıyoruz.
        try:
            result = self.engine.extract_stream_data(link)

            if result['status'] == 'success':
                video_title = result['title']
                stream_url = result['url']

                self.status_label.setText(f"✅ Bulundu: {video_title[:40]}...")
                print(f"Oynatılacak URL: {stream_url}")

                # BURAYA BİRAZDAN OYNATICIYI EKLEYECEĞİZ
                QMessageBox.information(self, "Başarılı",
                                        f"Video bulundu!\n\n{video_title}\n\nTamam'a basınca oynatma mantığını kuracağız.")

            else:
                self.status_label.setText("❌ Video bulunamadı.")
                QMessageBox.critical(self, "Hata", f"Hata detayı:\n{result['message']}")

        except Exception as e:
            self.status_label.setText("❌ Beklenmedik hata.")
            print(e)

        finally:
            self.watch_button.setEnabled(True)  # Butonu tekrar aç


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CleanWatchApp()
    window.show()
    sys.exit(app.exec_())