from flask import Flask, Response
# import cv2
import subprocess

app = Flask(__name__)

# Функция генерации видеопотока
def video_feed():
    # cap = cv2.VideoCapture(0)
    # Размер кадров
    frame_size = (640, 480)
    # Качество видео (битрейт)
    quality = "medium"
    # Формат видео (HLS или DASH)
    video_format = "hls"
    # Формат аудио
    audio_format = "aac"
    # Адрес сервера для потоковой передачи
    server_url = "http://localhost:5000/"
    # Параметры кодека
    codec_params = {
        "medium": "-b:v 750k -bufsize 1500k",
        "high": "-b:v 1500k -bufsize 3000k",
        "ultra": "-b:v 3000k -bufsize 6000k"
    }
    # Команда для запуска FFmpeg
    ffmpeg_cmd = f"ffmpeg -re -i - -c:v libx264 -preset veryfast {codec_params[quality]} -maxrate 1000k -bufsize 2000k -pix_fmt yuv420p -g 60 -hls_time 2 -hls_list_size 5 -hls_segment_filename {video_format}/%03d.ts -f {video_format} {video_format}/index.m3u8 -c:a {audio_format} -b:a 128k -f mp4 -movflags frag_keyframe+empty_moov {server_url}/video.mp4"
    # Запуск FFmpeg
    ffmpeg_proc = subprocess.Popen(ffmpeg_cmd.split(), stdin=subprocess.PIPE)
    while True:
        pass #
