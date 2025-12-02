# import yt_dlp
#
#
# class VideoEngine:
#     def __init__(self):
#         self.base_opts = {
#             'quiet': True,
#             'no_warnings': True,
#             'noplaylist': True,
#             'geo_bypass': True,
#             # Force Generic: Bilinmeyen sitelerde gömülü video ara
#             'extract_flat': 'in_playlist',
#             'http_headers': {
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#             }
#         }
#
#     def extract_stream_data(self, page_url):
#         # Platforma Özel Stratejiler
#         if "youtube.com" in page_url or "youtu.be" in page_url:
#             print("Tespit: YouTube -> MP4 Modu")
#             self.base_opts['format'] = 'best[ext=mp4][protocol^=http]/best[ext=mp4]/best'
#         elif "twitch.tv" in page_url:
#             print("Tespit: Twitch -> Best Modu")
#             self.base_opts['format'] = 'best'  # Twitch genelde m3u8 verir
#         else:
#             print("Tespit: Genel Platform -> HLS/Standart Mod")
#             self.base_opts['format'] = 'best[protocol^=m3u8]/best[ext=mp4]/best'
#
#         try:
#             with yt_dlp.YoutubeDL(self.base_opts) as ydl:
#                 info_dict = ydl.extract_info(page_url, download=False)
#
#                 if 'entries' in info_dict:
#                     info_dict = info_dict['entries'][0]
#
#                 video_url = info_dict.get('url', None)
#                 video_title = info_dict.get('title', 'Bilinmeyen Video')
#
#                 # Eğer URL yoksa hata fırlat
#                 if not video_url:
#                     raise Exception("Video linki ayıklanamadı (DRM veya Desteklenmeyen Site).")
#
#                 print(f"DEBUG -> Başlık: {video_title}")
#                 print(f"DEBUG -> URL: {video_url}")
#
#                 return {
#                     "status": "success",
#                     "url": video_url,
#                     "title": video_title
#                 }
#
#         except Exception as e:
#             error_msg = str(e)
#             # Kullanıcı dostu hata mesajları
#             if "HTTP Error 403" in error_msg:
#                 return {"status": "error", "message": "Erişim Reddedildi (403). Site bot koruması kullanıyor."}
#             elif "DRM" in error_msg or "This video is DRM protected" in error_msg:
#                 return {"status": "error", "message": "Bu video DRM korumalı (Netflix/Exxen vb.). Oynatılamaz."}
#             elif "Unsupported URL" in error_msg:
#                 return {"status": "error", "message": "Bu site henüz desteklenmiyor."}
#             else:
#                 return {"status": "error", "message": f"Hata: {error_msg[:100]}..."}
#
#
# if __name__ == "__main__":
#     # Testler
#     # 1. Show TV Canlı (Genelde youtube veya kendi sitesi) - Çalışır
#     # 2. Twitch - Çalışır
#     # 3. Korsan Film Sitesi - Muhtemelen Çalışmaz (Embed sorunu)
#     test_link = "https://www.showtv.com.tr/canli-yayin"
#     engine = VideoEngine()
#     print(engine.extract_stream_data(test_link))


import yt_dlp


class VideoEngine:
    def __init__(self):
        self.base_opts = {
            'quiet': True,
            'no_warnings': True,
            'noplaylist': True,
            'geo_bypass': True,
            # Force Generic: Bilinmeyen sitelerde gömülü video ara
            'extract_flat': 'in_playlist',
            'http_headers': {
                # 1. Kimlik: Chrome Tarayıcı
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                # 2. Referans: Google'dan geliyormuş gibi yap (Kapıları açar)
                'Referer': 'https://www.google.com/',
                # 3. Dil: Türkçe/İngilizce konuşan gerçek bilgisayar
                'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            }
        }

    def extract_stream_data(self, page_url):
        # Platform Specific Strategies
        if "youtube.com" in page_url or "youtu.be" in page_url:
            print("Detection: YouTube -> MP4 Mode (Safe 720p)")
            # 720p limitini ekledik ki VLC sesi ve görüntüyü %100 birleşik alabilsin.
            self.base_opts['format'] = 'best[ext=mp4][height<=720][protocol^=http]/best[ext=mp4][height<=720]/best'

        elif "twitch.tv" in page_url:
            print("Detection: Twitch -> Best Mode")
            self.base_opts['format'] = 'best'

        else:
            print("Detection: General Platform -> HLS/Standard Mode")
            self.base_opts['format'] = 'best[protocol^=m3u8]/best[ext=mp4]/best'

        try:
            with yt_dlp.YoutubeDL(self.base_opts) as ydl:
                info_dict = ydl.extract_info(page_url, download=False)

                if 'entries' in info_dict:
                    info_dict = info_dict['entries'][0]

                video_url = info_dict.get('url', None)
                video_title = info_dict.get('title', 'Unknown Video')

                if not video_url:
                    raise Exception("Could not extract video URL (DRM or Unsupported Site).")

                print(f"DEBUG -> Title: {video_title}")
                print(f"DEBUG -> URL: {video_url}")

                return {
                    "status": "success",
                    "url": video_url,
                    "title": video_title
                }

        except Exception as e:
            error_msg = str(e)
            # User Friendly Error Messages (English)
            if "HTTP Error 403" in error_msg:
                return {"status": "error", "message": "Access Denied (403). Site uses bot protection."}
            elif "DRM" in error_msg or "This video is DRM protected" in error_msg:
                return {"status": "error", "message": "This video is DRM protected (Netflix/Exxen etc.). Cannot play."}
            elif "Unsupported URL" in error_msg:
                return {"status": "error", "message": "This website is not supported yet."}
            else:
                return {"status": "error", "message": f"Error: {error_msg[:100]}..."}


if __name__ == "__main__":
    # Test
    test_link = "https://www.youtube.com/watch?v=AH-bFgk2mRU"
    engine = VideoEngine()
    print(engine.extract_stream_data(test_link))