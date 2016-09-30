'''
def is_abecedarian(word):
    n = 0  
    if len(word)<=1:
        return True
              
    elif word[n] > word[n+1]:
        return False
    else:        
        word = word[n+1:]
        return(is_abecedarian(word))


def is_abecedarian(word):
    n = 0
    previous = word[n]
    a = len(word)
    while n < a-1:
        if word [n+1] < word[n]: 
            return False
        n+=1
    return True

print(is_abecedarian('cba'))


def cattalk():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        i=0
        while i <= (len(word)-6):
            if word[i] == word[i+1]:
                if word[i+2]==word[i+3]:
                    if word [i+4] == word[i+5]:
                        print(word)
            i+=1
 '''           
          
cattalk()
