from pytesseract import Output, image_to_string, image_to_data
from PIL import Image, ImageOps
from pandas import DataFrame

imagem= Image.open('n1.jpeg')
imagem_cinza = ImageOps.grayscale(imagem)

textos = image_to_string(imagem_cinza)
#print(textos)

dicionario = image_to_data(imagem_cinza, output_type=Output.DICT)
print(dicionario.keys())

arquivo_csv = DataFrame.from_dict(dicionario)
arquivo_csv.to_csv('dados.csv', index= False ,header= True)

dicionario_limpo = {}
for chave in dicionario:
    lista_limpa = []
    for indice, item in enumerate(dicionario[chave]):
        if dicionario ['conf'][indice] >=50:
            lista_limpa.append(item)
    dicionario_limpo[chave] = lista_limpa

arquivo_csv2 = DataFrame.from_dict(dicionario_limpo)
arquivo_csv2.to_csv('dados_limpos.csv', index= False ,header= True)



