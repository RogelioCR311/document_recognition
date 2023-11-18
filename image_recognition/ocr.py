import cv2
import easyocr
from django.conf import settings
import os

reader = easyocr.Reader(["es"], gpu=False)

def readImage(imageURL, type):
    image = cv2.imread(imageURL)
    result = reader.readtext(image, paragraph=True)

    if(type == 'credential'):
        word1 = searchKeyword(result, 'CREDENCIAL')
        word2 = searchKeyword(result, 'ELECTORAL')
        word3 = searchKeyword(result, 'VOTAR')

        if(word1 == True & word2 == True & word3 == True):
            return True
        else:
            return False
    
    elif(type == 'curp'):
        word1 = searchKeyword(result, 'CLAVE')
        word2 = searchKeyword(result, 'CONSTANCIA')
        word3 = searchKeyword(result, 'REGISTRO')

        if(word1 == True & word2 == True & word3 == True):
            return True
        else:
            return False

    elif(type == 'rfc'):
        word1 = searchKeyword(result, 'RFC')
        word2 = searchKeyword(result, 'FISCAL')
        word3 = searchKeyword(result, 'CONTRIBUYENTE')

        if(word1 == True & word2 == True & word3 == True):
            return True
        else:
            return False

    elif(type == 'acta'):
        word1 = searchKeyword(result, 'ACTA')
        word2 = searchKeyword(result, 'NACIMIENTO')
        word3 = searchKeyword(result, 'REGISTRO')

        if(word1 == True & word2 == True & word3 == True):
            return True
        else:
            return False
    
    elif(type == 'nss'):
        word1 = searchKeyword(result, 'SEGURO')
        word2 = searchKeyword(result, 'SOCIAL')
        word3 = searchKeyword(result, 'MEXICANO')

        if(word1 == True & word2 == True & word3 == True):
            return True
        else:
            return False


def searchKeyword(result, word):
    for res in result:
        search = word in res[1].upper()
        if search:
            print(f'Se encuentra {word}')
            return True
    return False

def prueba():
    image_path = os.path.join(settings.BASE_DIR, 'media/user_1/ID_1.png')
    readImage(image_path, 'credential')