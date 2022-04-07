import random

def readData():
    try:        
        with open ("data_hangman/data.txt", "r", encoding='UTF-8') as f: 
            palabra = [line.replace('\n','') for line in f]        
        #print(random.choice(palabra))
        return random.choice(palabra)
    except:
        print('No se encontro el archivo')


def run():
    discovered_word = ''
    #while 
    inputWord= ['a','b','m','e']
    
    #word=readData()
    word = 'embarcacion'
    #for lyri
    espacios = [lyrics if lyrics in inputWord else '_'  for lyrics in word ] 
    print("".join(espacios))
    #print('a' in inputWord)


if __name__ == '__main__':
    run()