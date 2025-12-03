# 📺 CleanWatch - Universal Stream Player

<p align="center">
  <img src="app_icon.ico" alt="CleanWatch Logo" width="100">
</p>

<p align="center">
  <strong>Watch streams without ads, trackers, or browser lag. / Reklamsız, takılmadan, doğrudan masaüstünde izleyin.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/GUI-PyQt5-green?style=for-the-badge&logo=qt">
  <img src="https://img.shields.io/badge/Engine-VLC-orange?style=for-the-badge&logo=vlc">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge">
</p>

---

<p align="center">
  <img src="screenshots/demo.jpg" alt="CleanWatch Demo" width="800">
</p>

## 🇬🇧 English Description

**CleanWatch** is an open-source, lightweight desktop player that allows you to watch videos from platforms like **YouTube, PuhuTV, Twitch** directly on your desktop, bypassing web-based ads and trackers.

It extracts the raw stream using `yt-dlp` and renders it via the `VLC` engine, providing a smooth, high-performance viewing experience without the heavy resource usage of web browsers.

### Key Features

* **Ad-Free Experience:** Bypasses web player ads entirely by extracting the direct stream source.
* **Lightweight & Fast:** Consumes significantly less RAM/CPU compared to Chrome or Edge.
* **Smart Engine:** Automatically detects the platform and selects the best stream format (HLS/m3u8 for PuhuTV, Safe MP4 for YouTube).
* **Pro Controls:**
    * **Smart Seek:** Click anywhere on the slider to jump instantly.
    * **Shortcuts:** `Space` to Pause/Play, `Arrow Keys` to Seek, `Double Click` for Fullscreen.
* **Modern UI:** Dark mode interface designed for focus.

### ✅ Supported Platforms

| Platform | Status | Notes |
| :--- | :---: | :--- |
| **YouTube** | ✅ | Videos, Shorts, Live Streams (720p Optimized) |
| **PuhuTV** | ✅ | Series & Movies (Full Support) |
| **Twitch** | ✅ | VODs, Clips, and Live Streams |
| **Twitter (X)** | ✅ | Video playback from Tweets |
| **Live TV** | ✅ | TV Channels streaming via YouTube infrastructure |

---

### 🛠️ Installation & Usage

#### Option 1: Standalone EXE (Recommended)
No Python installation required.
1.  Go to the **[Releases](../../releases)** page on the right sidebar.
2.  Download `CleanWatch_Pro.exe`.
3.  **Requirement:** Ensure **[VLC Media Player (64-bit)](https://www.videolan.org/vlc/)** is installed on your system.
4.  Run the app, paste a video link, and enjoy!

#### Option 2: Run from Source (For Developers)
```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/CleanWatch.git](https://github.com/YOUR_USERNAME/CleanWatch.git)

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

⚠️ Disclaimer
This project is for educational purposes only. The developer is not responsible for any misuse of this software.

## 🇹🇷 Türkçe Açıklama

**CleanWatch** YouTube, PuhuTV, Twitch gibi platformlardaki videoları, web tabanlı reklamlara ve takipçilere (tracker) maruz kalmadan, doğrudan masaüstünüzde izlemenizi sağlayan açık kaynaklı, hafif bir oynatıcıdır.

yt-dlp kullanarak ham yayın akışını çeker ve VLC motoru üzerinden işler; böylece web tarayıcılarının ağır kaynak kullanımı olmadan akıcı, yüksek performanslı bir izleme deneyimi sunar.

### Öne Çıkan Özellikler

* **Reklamsız Deneyim:** Doğrudan yayın kaynağını çekerek web oynatıcı reklamlarını tamamen atlar.
* **Hafif ve Hızlı:** Chrome veya Edge'e kıyasla önemli ölçüde daha az RAM/CPU tüketir.
* **Akıllı Motor:** Platformu otomatik olarak algılar ve en iyi yayın formatını seçer (PuhuTV için HLS/m3u8, YouTube için Güvenli MP4).
* **Profesyonel Kontroller:**
    * **Akıllı Sarma:** Çubuğun herhangi bir yerine tıklayarak anında atlayın.
    * **Kısayollar:** `Boşluk tuşu` ile Durdur/Oynat, `Yön tuşları` ile İleri/Geri, `Çift Tık` ile Tam Ekran.
* **Modern Arayüz:** Odaklanmak için tasarlanmış karanlık mod arayüzü.

### ✅ Desteklenen Platformlar

| Platform | Durum | Notlar                                           |
| :--- |:-----:|:-------------------------------------------------|
| **YouTube** |   ✅   | Videolar, Shorts, Canlı Yayınlar (720p Optimize)    |
| **PuhuTV** |   ✅   | Diziler ve Filmler (Tam Destek)                   |
| **Twitch** |   ✅   | VOD'lar (Geçmiş Yayınlar), Klipler ve Canlı Yayınlar                    |
| **Twitter (X)** |   ✅   | Tweet içinden video oynatma                       |
| **Live TV** |   ✅   | YouTube altyapısını kullanan TV Kanalları |

---

### 🛠️ Kurulum ve Kullanım

#### Seçenek 1: Hazır EXE (Önerilen)
Python kurulumu gerekmez.
1.  Sağ taraftaki [suspicious link removed] sayfasına gidin.
2.  CleanWatch_Pro.exe dosyasını indirin.
3.  **Gereksinim:** Sisteminizde **[VLC Media Player (64-bit)](https://www.videolan.org/vlc/)** kurulu olduğundan emin olun.
4.  Uygulamayı çalıştırın, bir video linki yapıştırın ve keyfini çıkarın!

#### Seçenek 2: Kaynak Koddan Çalıştırma (Geliştiriciler İçin)
```bash
# Repoyu klonlayın
git clone [https://github.com/KULLANICI_ADINIZ/CleanWatch.git](https://github.com/KULLANICI_ADINIZ/CleanWatch.git)

# Gereksinimleri yükleyin
pip install -r requirements.txt

# Uygulamayı başlatın
python main.py
```

⚠️ Yasal Uyarı
Bu proje sadece eğitim amaçlı geliştirilmiştir. Yazılımın kötüye kullanımından geliştirici sorumlu değildir.
