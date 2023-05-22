from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

yt = YouTube(video_url)

print("Resoluções disponíveis:")
for stream in yt.streams.filter(progressive=True):
    print(stream.resolution)

resolution = input("Digite a resolução desejada: ")
format = input("Digite o formato de saída desejado (por exemplo, 'mp4' ou 'webm'): ")
stream = yt.streams.filter(resolution=resolution, file_extension=format, progressive=True).first()
output_path = "caminho/do/arquivo/de/saida." + format
stream.download(output_path)
print("Download concluído!")
