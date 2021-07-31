from pytube import YouTube

link = input("Digite o link do video que deseja baixar: ")
path = input("Digite o diretório que deseja salvar o video: ")
yt = YouTube(link)
print("Título",yt.title)
print("Número do video",yt.views)
print("Tamanho do vídeo",yt.length,"segundos")
print("Avaliação do video",yt.rating)

ys = yt.streams.get_highest_resolution()

print("Baixando....")
ys.download(path)
print("download completo!")

