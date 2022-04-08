import random
import os

def readData():
    try:        
        with open ("data_hangman/data.txt", "r", encoding='UTF-8') as f: 
            palabra = [line.replace('\n','') for line in f]        
        #print(random.choice(palabra))
        return random.choice(palabra)
    except:
        print('No se encontro el archivo')


def run():
    
    cls = lambda: os.system ("cls")
    inputWords= []
    word=readData()
    
    continuar = True
    #inputWord = input("Ingresa una letra")
    
    while continuar: 
       
        print("ingresa una letra o la palabra")        
        inputWord = input().lower()#normalize word

        #when inputWord is not number and not exist in inputwords and enter just one word
        if(inputWord.isalpha() and (inputWord not in inputWords) and len(inputWord) == 1):
            #clean window       
            cls()
            inputWords.append(inputWord)
            espacios = [lyrics if lyrics in inputWords else '_'  for lyrics in word ] 
            print("".join(espacios))

            if(word == "".join(espacios)):
                print('!!Felicidades la palabra es:'+word)
                continuar = False

        elif (len(inputWord) > 1):
            #when try guess word
            if(inputWord == word):
                print('!!Felicidades la palabra es:'+word)
                continuar = False
            else:
                print('La palabra no es:'+inputWord)
        else:
            print('No ingresaste una palabra valida o ya esta repetida')
        


if __name__ == '__main__':
    run()