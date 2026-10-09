import funcoesatv01 as f
notas = f.coletardados()
f.criar_arquivo(notas)
medias = f.fazer_media()
for linha in medias:
        print(linha["nome"], linha["media"], linha["status"])