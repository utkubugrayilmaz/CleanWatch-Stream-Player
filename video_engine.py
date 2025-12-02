import yt_dlp


class VideoEngine:
    def __init__(self):
        # yt-dlp ayarları
        self.ydl_opts = {
            'format': 'best',  # En iyi kaliteyi seç
            'quiet': True,  # Terminali loglarla doldurma
            'no_warnings': True,  # Uyarıları gizle
        }

    def extract_stream_data(self, page_url):
        """
        Verilen web linkinden (PuhuTV vb.) video başlığını ve
        stream (m3u8/mp4) linkini çeker.
        """
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                # download=False çok önemli, yoksa videoyu indirmeye başlar!
                info_dict = ydl.extract_info(page_url, download=False)

                video_url = info_dict.get('url', None)
                video_title = info_dict.get('title', 'Bilinmeyen Video')

                return {
                    "status": "success",
                    "url": video_url,
                    "title": video_title
                }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }


# --- TEST ALANI ---
# Bu dosya direkt çalıştırılırsa burası çalışır.
# Modül olarak çağrıldığında burası çalışmaz.
if __name__ == "__main__":
    print("Test başlıyor...")
    # Behzat Ç. 1. Bölüm Linki (Örnek)
    test_link = "https://puhutv.com/behzat-c-43-bolum-izle"

    engine = VideoEngine()
    sonuc = engine.extract_stream_data(test_link)

    print("-" * 30)
    print(f"Durum: {sonuc['status']}")
    if sonuc['status'] == 'success':
        print(f"Başlık: {sonuc['title']}")
        print(f"Stream Linki: {sonuc['url']}")
    else:
        print(f"Hata: {sonuc['message']}")
    print("-" * 30)