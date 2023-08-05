import pytube,os

print('-'*10)
video = input('cole o link do video aqui:')
os.system('clear')
try:
  yt = pytube.YouTube(video)
except TypeError:
  print('video não encontrado')

titulo = yt.title
canal = yt.author
tempo = yt.length

if tempo > 60 and tempo < 3200:
   tempo = tempo/60
   tempo = f'duração: {round(tempo,0)} minuto'
elif tempo >= 3200:
   tempo = tempo/3200
   tempo = f'duração: {round(tempo,0)} horas'
else:
   tempo = f'duraçao: {round(tempo,0)} segundos'

#resolucao alta
alta = yt.streams.filter(progressive=True)
alta = alta.get_highest_resolution()

#resolucao baixa
baixa = yt.streams.filter(progressive=True)
baixa = baixa.get_lowest_resolution()

tamanho = yt.streams.filter(progressive=True)
tamanho_min = tamanho.get_lowest_resolution()
tamanho_min = tamanho_min.filesize_kb
tamanho_max = tamanho.get_highest_resolution()
tamanho_max = tamanho_max.filesize_kb

#max
if tamanho_max > 1024 and tamanho_max < 1048576:
   tamanho_max = tamanho_max/1024
   tamanho_max = f'{round(tamanho_max,2)} mb'
elif tamanho_max > 1048576:
   tamanho_max = tamanho_max/(1024*1024)
   tamanho_max = f'{round(tamanho_max,2)} gb'
else:
   tamanho_max = f'{round(tamanho_max,2)} kb'
   
#min
if tamanho_min > 1024 and tamanho_min < 1048576:
   tamanho_min = tamanho_min/1024
   tamanho_min = f'{round(tamanho_min,2)} mb'
elif tamanho_min > 1048576:
   tamanho_min = tamanho_min/(1024*1024)
   tamanho_min = f'{round(tamanho_min,2)} gb'
else:
   tamanho_min = f'{round(tamanho_min,2)} kb'

print(f'Titulo: {titulo}')
print(f'Canal: {canal}')
print(tempo)
print(f'resolução alta: {alta.resolution} ({tamanho_max})')
print(f'resolução baixa: {baixa.resolution} ({tamanho_min})')



while True:
   resolucao = input('escolha a resolução [A]lta [B]aixa:').upper()
   if resolucao == 'A':
       baixar = yt.streams.get_highest_resolution()
       break
   elif resolucao == 'B':
       baixar = yt.streams.get_lowest_resolution()
       break
   else:
      continue
   
while True:
   destino = input('coloque o nome da pasta:')
   caminho = os.path.expanduser('~')
   pasta = os.path.exists(f'{caminho}/{destino}')
   if pasta == False:
       os.system('clear')
       print('esta pasta não foi encontrada')
       continue
   else:
       break


while True:
   avancar = input('deseja continuar [S]im [N]ão:').upper()
   if avancar == 'S':
       baixar.download(f'{caminho}/{destino}')
       print('dowload concluido')
       break
   elif avancar == 'N':
       print('dowload cancelado')
       break
   else:
       print('escolha entre sim ou não')
       continue
      








