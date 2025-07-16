import os 
import shutil
from pathlib import Path

casa = r"C:\Users\Juan\OneDrive\Área de Trabalho"

print(f"Detectado: {casa}")

casa = str(casa)
all_arq = os.listdir(casa)



#Criando Pastas
disorder = os.path.join(casa, "mess")
if not os.path.exists(disorder):
    os.makedirs(disorder)
    print(f"a pasta {disorder} foi criada com sucesso!")

pastas = {
"pdf":os.path.join(casa, "mess", "PDF"),
"plan":os.path.join(casa, "mess", "Planilhas"),
"fotos":os.path.join(casa, "mess", "Fotos"),
"video":os.path.join(casa, "mess", "videos")
}

for pasta in pastas.values():
          os.makedirs(pasta, exist_ok=True)


contador = {
"count_pdf": 0,
"count_mp4": 0,
"count_xlsx": 0,
"count_ft": 0}

for a in all_arq:
    origem = os.path.join(casa, a)

    if a.lower().endswith(".pdf"):
       destino = os.path.join(pastas["pdf"],a)
       if not os.path.exists(destino):
        shutil.move(origem, destino)
        contador["count_pdf"] += 1
        print(f"{a} movido para PDF")
       else:
          print(f"{a} já existe na pasta PDF e foi ignorado")

    elif a.endswith(".mp4"):
       destino = os.path.join(pastas["video"],a)
       if not os.path.exists(destino):
          shutil.move(origem, destino)
          contador["count_mp4"] += 1
          print(f"{a} movido em video")
       else:
           print(f"{a} já existe na pasta video e foi ignorado")
       
    elif a.endswith(".jpg") or a.endswith(".jpeg"):
        destino = os.path.join(pastas["fotos"],a)
        if not os.path.exists(destino):
           shutil.move(origem, destino) 
           contador["count_ft"] += 1  
           print(f"{a} movido para imagens")
        else:
            print(f"{a} já existe na pasta fotos e foi ignorado")
    

    elif a.endswith(".xlsx"):
        destino = os.path.join(pastas["plan"], a)
        if not os.path.exists(destino):
           shutil.move(origem, destino)
           contador["count_xlsx"] += 1
           print(f" {a} movida para planilhas")
        else:
           print(f"{a} já existe na pasta Planilhas e foi ignorado")

relatorio_path = os.path.join(disorder, "relatorio.txt")
with open(relatorio_path,"w") as rel: 
     rel.write("Relatório de arquivos organizados:\n")
     for tipo,qtde in contador.items():
          rel.write(f" - {tipo}: {qtde}\n")

print("Arquivos organizados com sucesso")

print("todos os arquivos foram processados com sucesso")
print(f"foram processados:")
for tipo, qtde in contador.items():
      print(f" - {tipo}: {qtde}")


