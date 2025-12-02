import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


# Ana penceremizi tanımlayan sınıf
class CleanWatchApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Pencere Başlığı ve Boyutları
        self.setWindowTitle("CleanWatch - Reklamsız İzle")
        self.setGeometry(100, 100, 800, 600)  # x, y, genişlik, yükseklik

        # Şimdilik sadece pencereyi gösterelim
        self.show()


# Uygulamanın giriş noktası
if __name__ == "__main__":
    # 1. Uygulama nesnesini oluştur (Her PyQt uygulamasında şarttır)
    app = QApplication(sys.argv)

    # 2. Penceremizi oluştur
    window = CleanWatchApp()

    # 3. Uygulama döngüsünü başlat (Kapatılana kadar çalışır)
    sys.exit(app.exec_())