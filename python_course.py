# commento, può essere solo in riga

# per dichiarare una variabile basta scrivere NOMEVARIABILE = VALORE, oppure NOMEVARIABILE

x = 3  # dichiarazione variabile
y, z = 4, 5  # dichiarazione variabili multiple
print(x)
print(y)
print(z)

print("*" * 10)  # stampa dieci volte asterisco '*'

# TIPI DI DATO
argomento = " (TIPI DI DATO) "
integer = 4
stringa1 = (
    "testo"  # tipo 'str'(stringa), può essere scritta anche con i double quotes""
)
lista = [1, 2, 3]  # sarebbe l'array
tupla = (1, 2, 3)  # una specie di array con funzioni differenti
range = range(
    4
)  # una lista composta da 4 elementi integer(range escluso, quindi 0,1,2,3)
set
dict = {"nome": " luca", "et� ": 20}  # associabile ad un oggetto

# grazie alla funzione 'type(DATO/VARIABILE)' ci viene restituito il tipo del dato specificato


# RICORDA
# Anche la funzione è un oggetto, di tipo function:
def funzione():
    pass


print(type(funzione()))  # output = function
print(id(funzione()))  # output = 16554651351311

# CASTING
argomento = " (CASTING) "
numero = 5
stringanumero = "5"
print(
    str(numero) + stringanumero + argomento
)  # grazie al metodo "str(stringa)" è possibile eseguire il casting da integer a string

# STRINGHE
argomento = " (STRINGHE) "
stringa2 = "ciao dall'altra parte"  # utilizzando il backslash'\' vicino ad un carattere si esegue l'escape, quindi viene visto comunque come un carattere

stringamultilinea = """ciao
    a
    tutti"""  # stringa multilinea (vale anche per apice singolo " ' ")

##RICORDA !!!
# le stringhe multilinea in realt�  sono molto usate in python per creare le docstring,
# ovvero sia, come si può intuire dal nome, stringhe contenenti la documentazione
# di una funzione che abbiamo creato.
# Queste stringhe sono recuperate dall'interprete python attraverso l'attributo '__doc__' ed
# attraverso la funzione "help()"


def funzioneEsempio():
    """Questa funzione permette di poter stampare la parola "Esempio" """
    print("Esempio")


# adesso, facendo print(funzioneEsempio.__doc__), ci uscir�  il testo inserito.
# stessa cosa con help(funzioneEsempio)
# le stringhe vengono viste come array di caratteri, quindi sono disponibili metodi utilizzati per gli array(che python base include), esempio:
stringa3 = "pyhton"
# però, non possiamo trattarle propriamente come array, infatti gli elementi della stringa non possono cambiare:
stringa3[3] = "s"  # ERRORE

# STRINGA RAW
# le stringhe raw sono delle stringhe dove é possibile inserire il carattere "backslash"
stringaRaw = r"C:\users\alessandro"

# SLICE
# è possibile fare lo "slicing", ovvero prendere un pezzo di stringa definito da 2 valori, ovvero inizio e fine
print(str(stringa3[0:5]))
# per fare un reverse della stringa è possibile utilizzare lo slicing:
# in pratica il primo argomento (vuoto = primo) sta per il carattere di partenza, il secondo argomento sta
# per il carattere finale da predere, che viene escluso (in questo caso vuoto = ultimo), e come terzo argomento
# viene data la "distanza" tra i caratteri, che di default è a 1 (quindi senza distanza, prende 'p','y','t','h','o','n').
# se il parametro della distanza è un valore negativo, allora si parte dagli ultimi caratteri
# non riesco a spiegarlo meglio, vedere la sezione
print(stringa3[::-1] + argomento)  # output = 'nohtyp'

# con il metodo "upper()" rendiamo la stringa all'interno delle parentesi in UPPERCASE
print(stringa3.upper() + argomento)
# con il metodo ".find()" troviamo l'index di un carattere o sequenza di caratteri all'interno di una stringa
print(str(stringa3.find("n")) + argomento)
# con ".replace(x, y)" rimpiazziamo il valore x con y in una stringa, creando una COPIA della stringa
print(stringa3.replace("n", "m") + argomento)

stringaIndex = "ciao da python"
print(stringaIndex[0:3])  # output = 'cia', le graffe prendono il valore indicato
# e se ci sono 2 valori separati dai due punti ':' prende il valore dagli indici
# specificati, indici stessi compresi.
print(stringaIndex[0:-1])  # output = 'ciao da pytho'

print(f"{stringaIndex} di prova")  # output = 'ciao da puthon di prova'

# la stringa è immutabile, ciò significa che gli elementi della stringa non possono
# mutare, a differenza di un array ad esempio:
stringaImmutabile = "Alessandro"
stringaImmutabile[0] = "E"  # output = errore

# "base string with {} placeholders".format(variables)

# STRING FORMATTING
example = "formatting"
formatted_string = "this is an example of using the {} on a string".format(example)

# il modo migliore per formattare le stringhe però, da python 3 è la functional string:
formatted_string = f"this is a new way of using the {example} formatting string"

# è possibile anche eseguire operazioni o parti di codice all'interno delle graffe:
formatted_string = f"the sum of all single numbers will be {1+2+3+4+5+6+7+8+9}"  # output = "the sum of all single numbers will be 45"

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""

# INDIRIZZO DI MEMORIA
# Python, a volte, per poter ottimizzare la memoria, utilizza l'OBJECT INTERNING, ovvero per variabili aventi
# stesso e PICCOLO valore, viene assegnato lo stesso indirizzo di memoria.
variabileA = "ciao"
variabileB = "ciao"
# per stampare l'indirizzo di memoria, si usa il metodo di default "id()":
print(id(variabileA))  # output = 156132154351254
print(id(variabileB))  # output = 156132154351254

# lo stesso risultato lo ottengo quando imposto, come valore di una variabile, un'altra variabile gi�  esistente:
variabileA_2 = variabileA
print(id(variabileA_2))  # output = 156132154351254
# questo perchè, quando associamo ad una variabile un'altra variabile, in realt�  stiamo associando l'indirizzo
# di memoria della variabile "copiata"

variabileC = "troppo lungo per eseguire l'Object Interning"
variabileD = "troppo lungo per eseguire l'Object Interning"

print(id(variabileC))  # output = 123153456123156
print(id(variabileD))  # output = 123666874548899

# da ricordare però che le stringhe, così come le tuple, sono elementi non modificabili,
# quindi io non posso fare questo:
variabileA[0] = "m"  # ERRORE
# questo per agevolare l'Object Interning, in modo tale da non dover far risultare errori di modifica di
# codice indesiderato (come ad esempio la modifica involontaria di altre variabili che puntano allo stesso indirizzo di memoria)


# CONVERSIONI
# Se facessimo la somma di un integer (7) ed un float(8.5) cosa succederebbe?
print(7 + 8.5)  # output: 15.5
# questo perché avviene la cosiddetta CONVERSIONE IMPLICITA, dove il 7 viene convertito in float prima di operare
# essa poteva essere svolta anche:
print(7 + 8.5)
# qui invece abbiamo la CONVERSIONE ESPLICITA
int()
float()
bool()
str()

esempio = 5
print(type(int(esempio)))

lenEsempio = "8Lettere"
print(len(lenEsempio))  # output: '8'
print(lenEsempio.upper())  # output: '8LETTERE'
print(lenEsempio.lower())  # output: '8lettere'
print(lenEsempio.find("8"))  # output: '0', riferito all'indice del carattere '8'
print(lenEsempio.replace("8Lettere", "8letterE"))  # output: '8letterE'
print(
    "8" in lenEsempio
)  # output: true, controlla se c'é il carattere o la serie di caratteri specificati

# NUMERI

#
# a=5
# b=2
# a + b = addizione

# a - b = sottrazione

# a * b = moltiplicazione

# a / b = divide a per b, ed il tipo e' float

# a ** b = Eleva a per b. Per i valori non Integer, il risultato e' una radice (Es. a**(1/2) risulta la radice quadrata di a)

# a // b = Il risultato sara' un dato di tipo Integer, quindi cifra intera

# a % b = Da come risultato il resto della divisione tra a e b

print(abs(-2.9))  # output: '2.9', abs rende sempre positivo il numero

# inoltre, python utilizza la precedenza degli operatori a cui siamo abituati (moltiplicazione e divisione > somma e sottrazione)


# FUNZIONI
    # Per dichiarare una funzione si usa "def"
def nomefunzione():
    print("stampa testo")
    pass
    # non essendoci ";", dobbiamo rispettare l'identazione del testo, come nell'esempio precedente
    # inoltre, se definisco una funzione con un certo nome, posso creare una variabile con lo stesso nome
    # ricordando pero', che non vado a definire una variabile con lo stesso nome in AGGIUNTA, ma vado
    # invece a sostituire il pezzo di memoria contenente il nome "area_del_cilindro" di tipo function
    # con un nuovo pezzo di memoria con il nome "area_del_cilindro", questa volta di tipo integer
    # Esempio :
def area_quadrato():
    print("4*4")
    #
area_quadrato = 25 # non da errore, poiche' e' una variabile e non un'altra funzione
    #
def area_quadrato():
    print(6*6) #da errore, perche' esiste gia' una funzione con questo nome
    
# PARAMETRI OPZIONALI
    # In python abbiamo anche la possibilità di specificare dei parametri opzionali che la nostra funzione
    # può accettare, semplicemente assegnandole un valore di default:
def stampa_numeri(a,b,c=3,d=4):
    print(a,b,c,d)
    
print(stampa_numeri(1), sep=",") # output = ERRORE, manca un parametro obbligatorio
print(stampa_numeri(1,2,3,4,5,6), sep=",") # output = ERRORE, troppi parametri, la funzione accetta massimo 4
print(stampa_numeri(1,2), sep=",") # output = 1,2,3,4
print(stampa_numeri(1,2,8,9), sep=",") # output = 1,2,8,9

    # ATTENZIONE però, poichè se noi utilizziamo un parametro opzionale all'interno della funzione, e ne
    # modifichiamo il valore, il valore di quel parametro DI DEFAULT resterà cambiato all'interno del codice
    # questo perchè l'indirizzo di memoria di un parametro di default rimane lo stesso ad ogni chiamata della
    # funzione:
def aggiungi_numero(a=[]):
    a.append(17)
    
print(aggiungi_numero()) # output = [17]
print(aggiungi_numero()) # output = [17,17]
print(aggiungi_numero()) # output = [17,17,17]
print(aggiungi_numero([15])) # output = [15,17]
print(aggiungi_numero([15])) # output = [15,17]

# ARGOMENTI POSIZIONALI E ARGOMENTI PER NOME
    # Una funzione può avere un numero x di argomenti indefinito, e questi possono essere posizionali o per nome:

def stampa_argomenti(*posizionali, **per_nome):
    print(posizionali)
    print(per_nome)
    
stampa_argomenti(1,2,3,4,5,c=6)# output = (1, 2, 3, 4, 5) # output = {'c': 6}
    # questo succede perchè 

  

# FUNCTIONAL PROGRAMMING 
    # FILTER ()
    # In Python esistono delle funzioni built-in che possono aiutarci nella costruzione del codice, e 
    # solitamente diminuiscono l'utilizzo della memoria.
    # Un esempio è la funzione filter(predicato, listaInput) che dandogli un predicato (ovvero un'operazione che
    # restituisce true o false), ed una lista input, filtra la listaInput per i valori che rispettano il predicato
def divisibile_per_5(numero):
    return numero % 5==0 

listaFiltrata = filter(divisibile_per_5, [5,10,12,20]) # output = [5,10,20] 


    # FUNZIONI ANINIME  (Lambda)
        # esse sono funzioni che permettono di eseguire una sola operazione ed ammettono 1 o più parametri
da_num_a_stringa = lambda numero: str(numero)
        # questo è uguale a scrivere:
def da_num_a_stringa_2(numero):
    return str(numero)
        # questa tipologia di funzioni è comoda se ad esempio vogliamo diminuire il codice scritto, come nel caso del filter()
listaFiltrata_lambda = filter(lambda x: x%5==0, [5,10,12,20]) # output = [5,10,20]

    # Min() e Max()
        # Min() e Max() sono due funzioni built-in che permettono di trovare il minimo o il massimo
        # valore all'interno di una lista data come parametro, e può contenere un altro parametro che
        # ci permette di specificare la "chiave" con cui eseguire questa valutazione:
        
lista_numeri = [1,2,6,8,]
print(max(lista_numeri)) #output = 8
        # mettiamo il caso che voglia trovare il rettangolo con l'area maggiore e quello con l'area minore
lista_rettangoli = [(2,4), (7,8), (2,30), (3,1)]
massimo_rettangolo_senza_key = max(lista_rettangoli) # output = (7,8) --> SBAGLIATO
minimo_rettangolo_senza_key = min(lista_rettangoli) # output = (2,4) --> SBAGLIATO
        # la funzione max() riconosce il primo valore ed esegue la funzione solo su di esso,
        # ma tramite la funzione lambda specifichiamo il tipo di calcolo che deve essere eseguito
        # per poter effettuare una valutazione sull'elemento maggiore (o minore) della lista
massimo_rettangolo_with_key = max(lista_rettangoli, key=lambda lato: lato[0]*lato[1]) # output = (2,30) --> CORRETTO
minimo_rettangolo_with_key = min(lista_rettangoli, key=lambda lato: lato[0]*lato[1]) # output = (3,1) --> CORRETTO

    # Map()
        # la funzione built-in map() permette di iterare all'interno di una o più liste passate come (secondo) parametro,
        # un'operazione definita nel (primo) parametro:
trova_il_doppio = lambda x: x*2
lista_esempio = [1,3,5]
lista_output = list( map(trova_il_doppio, lista_esempio) ) # output = [2,6,10]
        # e' possibile anche specificare più di una lista, e svolgere operazioni tra due liste contemporaneamente:
lista_esempio_2 = [9,7,5]
somma_liste = list(map(lambda x,y : x+y, lista_esempio, lista_esempio_2)) #output = [10,10,10]
        # nell'esempio "somma_liste", x corrisponde all'elemento[n] della prima lista passata come parametro (lista_esempio),
        # mentre y corrisponde all'elemento[n] della seconda lista passata (lista_esempio_2)
        
    # all()
        # all() permette di avere una lista di risultati booleani come parametro, e stampare TRUE se tutti gli elementi
        # sono True, altrimenti FALSE. Ovviamente, la lista di booleani è una lista ottenuta da una serie di calcoli fatta
        # tra due o più liste, con lo scopo di verificare il risultato dell'operazione passata come primo parametro:
lista_maggiore = [8,9,10,]
lista_minore = [4,3,5,]
all(map(lambda x,y: x>y, lista_maggiore, lista_minore)) #output = True
all(map(lambda x,y: x<y, lista_maggiore, lista_minore)) #output = False


    # any()
        # any() funziona come un "or", quindi passata una lista di booleani come in "all()", ritorna True se esiste almeno
        # valore True, altrimenti false
lista_numeri = [2,3,5,7,]
pari = list(map(lambda x:x%2==0, lista_numeri)) #output = [True, False, False, False]
print(any(pari)) # output = True


# ITERATION
    # Noi sappiamo che nel ciclo for, ogni elemento di una lista viene iterato, ma esattamente cosa succede?
    # Possiamo capirlo con il seguente esempio: supponiamo che vogliamo stampare ogni elemento di una lista
    # innanzitutto, definiamo la lista:
lista_da_iterare = ["uno", "due", "tre", "quattro"]
    # ora, invece di usare il for, creamo una variabile iteration tramite iter():
a = iter(lista_da_iterare)
    # bene, ora la memoria se che, nella variabile a, è sempre presente un elemento, poichè l'elemento successivo
    # viene visualizzato solo dopo che il primo viene chiamato, questo tramite la funzione next():
print(next(a)) # output = "uno"
print(next(a)) # output = "due"
print(next(a)) # output = "tre"
print(next(a)) # output = "quattro"
print(next(a)) # output = "Error : StopIteration"
    # quando un iteratore termina gli elementi di una lista, viene lanciata l'eccezione StopIteration che, in casi
    # come nel ciclo for, viene gestita "uscendo" dal ciclo.
    
    # In alcuni casi l'iteration è un'ottima soluzione per il risparmio di memoria, vediamo un esempio pratico.
    # Importiamo il modulo sys che ci servirà per calcolare la memoria utilizzata di una variabile
import sys
    # Impostiamo due Variabili, una contenente una lista di elementi calcolata con la list comprehension,
    # ed un'altra contenente un generatore di elementi:
lista_elementi = [x*3 for x in range(100)]
generatore_elementi = (x*3 for x in range(100))
print(sys.getsizeof(lista_elementi)) # output = 918
print(sys.getsizeof(generatore_elementi)) #output = 88
    # come possiamo notare, la variabile "generatore_elementi" calcola un elemento per volta, e quindi la memoria
    # utilizzata per ogni elemento, in questo caso, è 88 bytes. Mentre per lista_elementi, la memoria è utilizzata per
    # prendere in considerazione già tutti gli elementi della lista, quindi 918 bytes
    
# YIELD
    # yield() è una parola chiave usata nelle funzioni per costruire un generatore, per risparmiare memoria in un'iterazione.
    # Essa restituisce un oggetto generatore senza eseguire il corpo della funzione.
    # ogni volta che il generatore viene iterato, l'esecuzione riprende dall'ultimo punto in cui 
    # si era interrotta durante l'ultima chiamata, fino a quando non raggiunge una nuova istruzione "yield", o
    # finisce l'esecuzione della funzione. Esempio: 
def generatore_esempio():
    yield 1
    yield 2
    yield 3
    # Creazione di un generatore
gen = generatore_esempio()
    # Iterazione attraverso il generatore
print(next(gen))  # Stampa: 1
print(next(gen))  # Stampa: 2
print(next(gen))  # Stampa: 3
    # Dopo aver raggiunto l'ultimo yield, se si prova a chiamare next() di nuovo, verrà sollevata un'eccezione StopIteration
    # print(next(gen))  # Solleva l'eccezione StopIteration

    

# INPUT
name = input("inserisci il tuo nome ")
print(name)

# IF STATEMENT
is_hot = True
caldo = 5
if is_hot:
    print("fa caldo")
elif caldo == 5:
    print("fa freddo")
elif caldo == 5 and is_hot == True:
    print("fammocc a mammt")
elif caldo == 4 or caldo == 6:
    print("a quant n ti")
elif not caldo == 5:
    print("caldo non vale 5")
    
# IF EXPRESSION
    # Per scrivere una condizione if, se essa conterrà solo un'espressione, possiamo utilizzare la if expression:
print("Fa caldo" if is_hot else False) # output = "Fa caldo"

# WHILE LOOPS
i = 1
while i < 5:
    print(f"loop numero: {i}")
    i += 1
    break
print("done")  # basta uscire dall'identazione per uscire dal loop, oppure usare break

# in python, é stato aggiunto la condizione else, sia nel ciclo while che nel ciclo for
# questa istruzione serve ad eseguire una certa porzione di codice che verrá eseguita  SE
# E SOLO SE l' intero cicli for termina correttamente (quindi, questa porzione di codice
# non verrebbe eseguita in caso di errore oppure se viene lanciato un BREAK)

# in questo esempio, creo un codice che stampa "finito se l'array é stato completamente
# analizzato, altrimenti non stampa nulla"

lista_else_while = [0, 1, 2, 3, 4, 5]
i = 5
while i != 3:
    print("siamo al numero = " + str(i))
else:
    print("finito!")


# FOOR LOOPS
for i in "python":
    print(i)  # output: "p" + "y" + "t" + "h" + "o" + "n"

for i in range(10):
    print(i)

for i in range(2, 10):
    print(i)  # il 10 é escluso

for i in range(0, 10, 2):
    print(i)  # output: 0,2,4,6,8,

#

# ARRAY (o Liste)
numeri = ["uno", "due", "3", "4"]
print(0)  # output = 'uno'
print(
    numeri[0:2]
)  # output= '["uno", "due"]' , il numero indice destro non viene contato

matrice = [
    1,
    ["due", "tre"],
    4,
]  # esempio matrice, quindi una lista con al sui interno liste
print(matrice[1][0])  # output: "due"

numeri = [1, 2, 3, 4]
numeri.append(5)
print(numeri)  # output: '[1,2,3,4,5]'

# per poter "appendere" altri valori ad una lista esistente, possiamo utilizzare
# anche l'operatore "+":

print((numeri + 6))  # output = [1,2,3,4,5,6]

# l'operatore "*" permette, come per le stringhe, di poter ripetere gli elementi
# contenuti nella lista più volte:

unoDueTre = [1, 2, 3]
print(unoDueTre * 3)  # output = [1,2,3,1,2,3,1,2,3]

# se volessi stamparmi l'ultimo elemento della lista senza conoscere la posizione,
# posso utilizzare l'indice negativo:

print(unoDueTre[-1])  # output = 3

numeri.insert(2, 10)  # mi inserisce il numero "10" nella posizione 2 della lista
print(numeri)  # output: '[1,2,10,3,4,5]'

numeri.remove(10)  # toglie il numero 10
print(numeri)  # output: '[1,2,3,4,5]'

numeri.clear()  # svuota la lista
numeri = [1, 2, 3, 4]

numeri.pop()  # elimina l'ultimo elemento

numeri.index(1)  # output: '0', trova l'indice del valore messo nelle parentesi

numeri.append(3)
numeri.count(
    3
)  # output: 2, conta quante volte é presente nella lista il valore specificato nelle parentesi

# per ordinare una lista, abbiamo due opzioni: metodo DISTRUTTIVO e  metodo NON DISTRUTTIVO
sorted(
    numeri
)  # non distruttivo, l'indirizzo di memoria della lista rimane identico poichè la lista non viene eliminata
numeri.sort()  # DISTRUTTIVO, l'indirizzo di memoria della lista è cambiato poichè la lista è stata eliminata e poi ricreata


numeri.reverse  # li ordina in ordine decrescente

numeri2 = numeri.copy()


# TUPLE
# Le tuple sono un insieme di elementi ordinati, non modificabili e con la possibilitá di presenza di duplicati
# per creare una tupla, possiamo inserire i valori tra parentesi tonde
esempioTupla = (1, 2, 3)
# oppure, di default, python intende una sequenza di elementi separati da virgola ¨,¨ come tupla:
esempioTupla2 = 3, 4, 5, 6
print(type(esempioTupla2))  # output = tuple
print(esempioTupla[0])  # output: '1'

esempioTupla[0] = 10  # errore, non si possono modificare le tuple
esempioTupla.append(4)  # errore, non posso aggiungere elementi alla tupla

# SEQUENCE UNPACKING (si puó fare anche con un altro tipo di sequenza, come una lista, o una stringa ecc...)
# le tuple sono comode per poter assegnare ad una sequenza in riga di variabili, ogni valore di una tupla:
tuplaDaAssegnare = 1, 2, 3, 4
a, b, c, d = tuplaDaAssegnare
print(a)  # output = 1
# OPPURE, POSSIAMO EFFETTUARLO COSÍ
esempioTupla = (1, 2, 3)
(
    x,
    y,
    z,
) = esempioTupla  # abbiamo spacchettato la tupla assegnando i seguenti valori:
# x= 1
# y= 2
# z= 3

#  volendo, posso estrarre una lista contenente i valori di una tupla, attraverso il casting list():
daTuplaALista = list(esempioTupla)
#  o viceversa
daListaATupla = tuple(daTuplaALista)

# per confermare quanto detto precedentemente sulla modifica delle tuple, facciamo un esempio
# (con le liste e poi con le tuple):
# supponendo di avere unalista ¨listaOrginale¨, a cui verranno aggiunti gli elementi, possiamo
# farlo o in maniera distruttiva oppure no:
# MANIERA NON DISTRUTTIVA
listaOriginale = [
    3,
    4,
    5,
]  # id = 12345678123
listaOriginale += [
    6,
    7,
    8,
]  # id = 12345678123

# MANIERA DISTRUTTIVA
listaOriginale2 = [
    3,
    4,
    5,
]  # id = 12345678123
listaOriginale2 = listaOriginale2 + [
    6,
    7,
    8,
]  # id = 56812911872

# facciamo la stessa cosa con una tupla:
tuplaOriginale = [
    3,
    4,
    5,
]  # id = 65847382625
tuplaOriginale += [
    6,
    7,
    8,
]  # id = 52315122351
# quindi, possiamo notare che nelle tuple, l'indirizzo di memoria cambia a prescindere,
# questo perché, essendo la tupla NON MODIFICABILE, non puó mantenere lo stesso indirizzo di memoria

# ASSEGNAZIONE ESTESA
    # L'assegnazione estesa in python ci permette di assegnare in un'unica variabile una parte variabile di una sequenza:
a,b,*c = "abcdef"
print(a) # output = "a"
print(b) # output = "b"
print(c) # output = "cdef"
    # in questo modo, abbiamo assegnato alla variabile c la rimanenza degli elementi presenti nella stringa "abcdef"
    # Questo tipo di assegnazione può risultare molto utile anche se vogliamo "togliere" da una lista di elementi,
    # alcune parti da assegnare ad altre variabili ad esempio:
lista_assegnazione = [1,2,3,4,5,]
primo, secondo, *lista_assegnazione = lista_assegnazione 
print(primo) # output = 1
print(secondo) # output = 2
print(lista_assegnazione) # output = [3,4,5]


# LIST COMPREHENSION
# in Python, é stata introdotta la List Comprehension, ovvero la possibilitá di
# poter effettuare un ciclo for "in linea", che permette la semplificazione del codice.

# Ci sono 3 possibili costrutti della List COmprehension:

# [<calcolo_da_eseguire> for x in <sequenza>]
# [<calcolo_da_eseguire> for x in <sequenza> if <condizione_su_x>]
# [<calcolo_da_eseguire> for x in <sequenza> if <condizione_su_x> else <in_caso_la_condizione_sia_falsa>]

# adesso faremo degli esempi per tutte e 3 le casistiche

# stampa 10 volte il valore attuale della i
[print(f"la i vale = {i}") for i in range(0, 10)]

# stampa 9 volte il valore attuale della i poiché salto la i quando vale 3
[print(f"la i vale = {i}") for i in range(0, 10) if i != 3]

# stampa 10 volte il valore attuale della i , e quando vale 3 stampa "ciao" invece
[print(f"la i vale = {i}") if i != 3 else print("ciao") for i in range(10)]


# DICTIONARIES
customer = {"name": "John", "last_name": "Smith"}
print(customer.get("last_name"))  # output: 'Smith'
print(customer["name"])  # output: John
customer["name"] = "Jack"  # nome cambiato in 'Jack

# DICTIONARIES(esempio pratico)
# numero in input:
numbers = 12345
# creo un dictionary
digits_mapping = {
    "1": "One ",
    "2": "Two ",
    "3": "Three ",
    "4": "Four ",
    "5": "Five ",
}
# dichiarazione stringa di output vuota
outputString = ""
# per ogni carattere nella variabile numeri
for ch in numbers:
    # somma la stringa output con il seguente pezzo di stringa
    # ricavato da dictionary.get(nomeAttributoDictionary, valore sostitutivo)
    outputString += digits_mapping.get(ch, "!")
# stampa
print(outputString)

# DICTIONARIES(filter)
messageInput = "i am so stupid"
# divide il messaggio in un array di parole ogni volta che incontra uno spazio vuoto' '
wordsArray = messageInput.split(" ")
dictionaryFilter = {"stupid": "******", "fuck": "****", "idiot": "*****"}
outputMessage = ""
for word in wordsArray:
    outputMessage += dictionaryFilter.get(word, word) + " "
print(outputMessage)


# DICTIONARIES (SCRITTO BENE)
# Un dizionario é un insieme di coppie chiave-valore che puó contenere solo chiavi diverse.
# infatti, una chiave non puó cambiare di valore proprio per evitare di avere 2 chiavi con
# stesso valore:

dictVuoto = {}

dictDueChiavi = {"nome": "Alessandro", "cognome": "Cupaiolo"}

# come chiave posso inserire anche una tupla, facciamo il seguente esempio con una chiave che
# corrisponde ad una tupla di due numeri, e come valore la loro somma:

dictTuple = {(3, 3): 6, (1, 5): 6}

# Se volessi iterare nelle coppie chiave-valore nel dizionario, ho 2 strade:

# strada scomoda
for x in dictDueChiavi:
    print(x, dictDueChiavi[x])

    # strada comoda e pulita
for x, y in dictDueChiavi.items():
    print(x, y)

    # RICORDA !!!!!!!!!!!!!!!!!!
    # In python, é buona usanza, in fase di creazione di un qualsiasi tipo di insieme (lista, tupla, dictionaries...)
    # mettere la ¨,¨ anche dopo l'ultimo elemento (SOLO IN PYTHON).
    # Questa disponibilitá é usata per i vari copia/incolla che vengono eseguiti in python che negli altri
    # linguaggi generano errore, mentre in python no

    # INSIEME SET
    # Il set fa parte dei 4 tipi di dato "di collezione", insieme alle liste, tuple e dictionaries.
    # Il set non é ordinato, non ha indici (quindi gli elementi sono "disordinati") e non cambiabile (quindi gli elementi al suo interno non possono cambiare}
    # Inoltre, a differenza delle liste, non possono esserci duplicati alll'interno del set

    # Dichiarazione
    setEsempio = {
        "a",
        "b",
        "c",
        "d",
        "e",
    }
    # É possibile anche convertire un tipo di dato "di collezione " in un set, attraverso la funzione built-in ¨set()¨
    set([1], [2, 3, 4], 5)


# OPERATORI Set
primoInsieme = {1, 2, 3, 4}
secondoInsieme = {4, 5, 6, 7}

# Unione = unisce tutti gli elementi non in comune dal secondo insieme al primo
print(primoInsieme | secondoInsieme)  # output = {1,2,3,4,5,6,7}

# Differenza = stampa solo gli elementi che il secondo insieme non ha nel primo insieme
print(primoInsieme - secondoInsieme)  # output = {1,2,3}

# Intersezione = stampa solo gli elementi in comune
print(primoInsieme & secondoInsieme)  # output = {4}

# Differenza simmetrica = stampa tutti gli elementi che appartengono solo al primoInsieme
# e non al secondoInsieme o viceversa (in pratica esclude gli elementi in comune)
print(primoInsieme ^ secondoInsieme)  # output = {1,2,3,5,6,7}


# MATRICI
# Una matrice corrisponde banalmente ad una lista contenente liste al suo interno
matrice = [
    [
        1,
        2,
    ],
    [
        3,
        4,
    ],
]

# possiamo considerare il primo elemento di una sottolista come una "riga":
print(matrice[0])  # stampa la prima riga
# output = [0,1]

for riga in matrice:
    for elemento in riga:
        print(elemento, end="\t")
    print()
    # output = 0  1
    #          2  3


# Esempio Matrice con un'immagine
# un immagine può essere rappresentata come una matrice due matrici, contenenti tuple, essendo che ogni pixel è un mix di 3 tonalità
# di colori, ovvero rosso, verde e blue (RGB)
imgEsempio_1 = [
    [(255, 0, 0), (0, 255, 0)],
    [(0, 0, 255), (255, 128, 0)],
]  # esempio immagine 2 x 2


# FUNCTIONS
def greet_user():
    print("hello")


# quando creamo una funzione, bisogna lasciare 2 spazi vuoti dopo, per convenzione


def greet_user_return_statement():
    return "return String"


greet_user()
print(greet_user_return_statement())

    # SCOPE
    # In python, a differenza di altri linguaggi, non c'è uno scope all'interno delle funzioni:
def ritorna_x(lista_parametro):
    for x in lista_parametro:
        print(x)
    return x # sono fuori dal for qui, teoricamente dovrebbe lanciare un'eccezione in altri linguaggi
             # invece ritornerà l'ultimo valore di x, poichè python non è un linguaggio compilato ma
             # interpretato (ciò significa che la macchina non si occuperà di tradurre il codice in 
             # linguaggio macchina, poichè python lo farà autonomamente in tempo reale durante
             # l'esecuzione del programma), e perciò, sarebbe troppo oneroso mantenere gli scope in
             # termini di memoria.
             
    # Sempre per lo scope, se volessi cambiare il valore di una variabile globale ad esempio, all'interno
    # di una funzione, non basta semplicemente assegnarle un nuovo valore, ma dichiararla all'interno della
    # funzione come variabile globale:
a = 4
def cambia_a(x):
    global a # si dichiara prima di cambiargli il valore
    a = x    # ora il valore a all'esterno della funzione "cambia_a()" risulta cambiato con il valore "x"
    pass
    
    # Funzioni nidificate
    # Posso creare funzioni nelle funzioni, e le più interne hanno accesso a variabili e parametri di quelle
    # più esterne:
    
def divisibile_per (lista_numeri, divisore):
    def verifica(numero): # ho accesso alla variabile divisore, quindi è inutile riscriverlo come parametro
       return numero % divisore == 0 # ritorno della variabile nidificata
    output = [verifica(numero) for numero in lista_numeri]
    return output
    

             


# CLASSI
class Numbers:
    # constructor ( si fa con __init__(self) )
    # self sta per 'this', quindi si riferisce all'oggetto corrente
    # quindi, quando noi creamo un'istanza, il numero di parametri sarà n+1:
    # esempio: p = Numbers(1,2) # esso contiene 3 parametri, anche se noi ne vediamo 2, e sono (self,1,2)
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # infatti, quando creamo un'istanza dell'oggetto Numbers, essa avrà un id.
    # lo stesso id, lo potremmo stampare se creassimo una funzione ad-hoc
    def print_id(self):
        id(self)

    def move(self):
        print("move")

    def draw(self):
        print("draw")
        
    # SPECIAL METHODS (Magic methods o Dunder methods)
        # le funzioni speciali (o magiche o dunder) sono funzioni che vengono utilizzate in automatico con 
        # particolari operazioni, come ad esempio la somma.
        # Per dichiararle, contengono il double underscrore "__" all'inizio ed alla fine del nome del metodo
    def __add__(self):
        return(self.x + self.y)
    
    # CONVENZIONE
        # A differenza di altri linguaggi, in python non c'è nessun controllo per quanto riguarda l'utilizzo
        # delle variabili all'interno o all'esterno della classe, quindi per indicare che una variabile o metodo
        # è utilizzato solo all'interno della classe in cui è dichiarato, il nome di tale variabile/metodo è 
        # preceduto da underscore "_"
    _variabile_interna = x+1
    
    # per esempio (Numbers(1,2)+(Numbers(1,2))) output = Numbers(2,4)


# creazione istanza
number = Numbers()
email.draw()


#ERRORS
    # In python è possibile gestire gli errori, customizzarli o crearli:
    # > con try noi proviamo ad eseguire il codice
    # > con except gestiamo l'errore , e possiamo anche specificafre la classe di Errore specifica
    # > con else viene eseguita una porzione di codice SOLO se NON scatta nessun errore
    # > con finally, eseguiamo una porzione di codice a prescindere dal fatto che sia andato in errore o meno
variabile = 5
try:
    print("questa variabile vale = " + variabile)
except TypeError:
    print("la variabile da stampare non è di tipo stringa")
except :
    print(" un altro tipo di errore, non saprei")
else: # l'else si scrive dopo tutti gli except
    print(" non ha generato errori")
finally:# finally si scrive alla fine
    print(" sono arrivato fino a qui")
    
# ASSERTION
    # In python esiste l'asserzione, ovvero sia un modo per verificare una certa condizione data, e in 
    # caso di differenza, lancia un errore di tipo AssertionError e stampa un messaggio che noi diamo
    # in inputn alla funzione assert().
    
variabile = 5
assert(isinstance(variabile, (int, float)),'la variabile non è di tipo int/float') 
print("questa variabile vale = " + variabile)# output = Assertion Error : 'la variabile non è di tipo int/float'

#RICORSIONE
    # La ricorsione è un concetto della programmazione che si riferisce al fatto che una funzione può richiamare se stessa.
    # in pratica viene identificato un problema, e viene spezzettato in altri sotto-problemi simili, risolti con la
    # medesima funzione utilizzata per risolvere il problema "padre", ma con parametri diversi
    # Da ricordare che la ricorsione permette una maggiore eleganza del codice, utilizzando però maggiore memoria.

def permutazioni(numeri):
    # Caso base: se la lista è vuota, restituisci una lista che contiene una lista vuota
    if not numeri:
        return [numeri]

    # Inizializza una lista per le permutazioni
    lista_permutazioni = []

    # Itera su ogni indice della lista numeri
    for i in range(len(numeri)):
        # Seleziona un elemento x all'indice i
        x = numeri[i]
        # Crea una lista dei numeri rimasti senza l'elemento x
        numeri_rimasti = numeri[:i] + numeri[i+1:]
        # Chiamata ricorsiva per ottenere le permutazioni dei numeri rimasti
        permutazioni_rimaste = permutazioni(numeri_rimasti)

        # Componi le permutazioni aggiungendo l'elemento x all'inizio
        for permutazione in permutazioni_rimaste:
            lista_permutazioni.append([x] + permutazione)

    # Ritorna la lista completa di permutazioni
    return lista_permutazioni

# Esempio di utilizzo
lista_valori = [1, 2, 3]
risultato = trova_permutazioni(lista_valori)

print(risultato)
"""
------------------- Starting recursion -------------------

entering       permutazioni([1, 2, 3],)
|-- entering    permutazioni([2, 3],)
|--|-- entering permutazioni([3],)
|--|-- exiting  permutazioni([3],)      returns [[3]]
|--|-- entering permutazioni([2],)
|--|-- exiting  permutazioni([2],)      returns [[2]]
|-- exiting     permutazioni([2, 3],)   returns [[2, 3], [3, 2]]
|-- entering    permutazioni([1, 3],)
|--|-- entering permutazioni([3],)
|--|-- exiting  permutazioni([3],)      returns [[3]]
|--|-- entering permutazioni([1],)
|--|-- exiting  permutazioni([1],)      returns [[1]]
|-- exiting     permutazioni([1, 3],)   returns [[1, 3], [3, 1]]
|-- entering    permutazioni([1, 2],)
|--|-- entering permutazioni([2],)
|--|-- exiting  permutazioni([2],)      returns [[2]]
|--|-- entering permutazioni([1],)
|--|-- exiting  permutazioni([1],)      returns [[1]]
|-- exiting     permutazioni([1, 2],)   returns [[1, 2], [2, 1]]
 exiting        permutazioni([1, 2, 3],)        returns [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
-------------------- Ending recursion --------------------"""

# MODULI
# il modulo é un file python, contenente classi, funzioni e variabili
# l'import dei moduli va messo incima a tutto il codice

import app  # importa l'intero modulo app
from app import prova1  # importa la funzione (prova) da app

prova1()  # chiama la funzione


# PACKAGES
import nomepacchetto.nomemodulo


# utile
# 1) shift+f6 = rinomina l'elemento selezionato

# FILES AND DIRECTORIES

# Partiamo con il dire, che in python ci sono vari modi per accedere ai file, il
# piú "gettonato" é utilizzando la libreria "io"

import io

# Prima di fare qualsiasi cosa con un file, bisogna ottenere un oggetto di tipo file
# attraverso la funzione built-in "open()"
# come parametri della funzione obbligatori, c'é solo il primo, che é il path del
# file da apire, poi c'é come secondo parametro(di tipo stringa), i permessi di apertura, che
# si dividono in:
# 'r' = read, permessi di lettura
# 'w' = write, permessi di scrittura
# 'a' = append, scrittura alla fine del file, in aggiunta a ció che giá c'era

fileAperto = open("fileEsempio.txt", mode="r")

# una volta aperto il file, dobbiamo chiuderlo se vogliamo eseguire altre istruzioni
# al di fuori del file dopo

fileAperto.close()

# esiste una maniera piú pulita per fare quanto detto prima in Python, senza che
# dobbiamo ogni volta ricordarci di chiudere il file, ma semplicemente utilizzando
# "l'identazione" tramite lo strumento "with" (chiamato il contesto)

with open("fileEsempio.txt", mode="r") as fileAperto:
    # ...
    print("vuoto")
    #  possiamo dire che esistono due tipi di files:
    #    1) file di testo
    #    3) file in bit
    #  questo perché in python ci sono due trattamenti diversi delle informazioni
    #  contenute a seconda del tipo di file che stiamo trattando

# FILE DI TESTO

# per quanto riguarda i file di testo, in python dobbiamo ricordare alcune funzioni


# LETTURA

with open("fileDiTesto.txt", mode="r") as fileAperto:
    # una funzione é readlines([NumeroOpzionale]) serve a leggere tutte le
    # righe del file, solo che visualizza anche "/n"
    contenuto = fileAperto.readlines()

    # read([numeroOpzionale]) é una funzione che ci permette di trasformare l'intero contenuto di un file
    # di testo in una stringa, fedele alle spaziature ed agli endline (senza visualizzare "/n")
    # da ricordare che il parametro ¨numeroOpzionale¨, se maggiore delle righe presenti nel file,
    # non rileverá piú stringhe dopo la chiamata corrispondente all'ultima riga presente nel file.
    contenuto = fileAperto.read()

    # readline() ci permette di trasformare la riga corrente in una stringa
    # ogni volta che viene chiamata, si sposta di riga (quindi, se la chiamo 3 volte, il
    # terzo valore sará anche l'ultimo se consideriamo il file "prova.txt", le chiamate
    # successive risulteranno stringhe vuote poiché le righe del file sono terminate)
    print(fileAperto.readline())  # output = ¨ciao¨
    print(fileAperto.readline())  # output = ¨sono¨
    print(fileAperto.readline())  # output = ¨una prova¨
    print(fileAperto.readline())  # output = ¨¨
    print(fileAperto.readline())  # output = ¨¨

    # seek(numPosizione) ci permette di spostarci nella posizione da noi scelta del file
    fileAperto.seek(7)
    print(fileAperto.read())  # output = no
    #          una prova

    # É possibile specificare  l'encoding del file che andremo a leggere, per una corretta traduzione:
    with open("file_da_leggere.txt", encoding="utf-8"):
        # ...
        pass

    # SCRITTURA

    with open("fileDiTesto.txt", mode="w") as fileDaScrivere:
        # per scrivere in output si usa write(contenutoDaScrivere)
        fileDaScrivere.write("prova")  # output = ¨prova¨
        fileDaScrivere.write("prova")  # output = ¨provaprova¨
        # anche in write mode é possibile usare la funzione seek, che ci permette di
        # poter scrivere dalla posizione passata come parametro integer
        fileDaScrivere.seek(0)
        fileDaScrivere.write("provola")  # output = ¨provolaova¨

        fileDaScrivere.writelines(
            "riga1", "riga2", "riga3"
        )  # per ogni stringa parametro
        #   passata, viene scritta una riga (quindi, alla fine di una stringa parametro
        #   viene inserito il carattere /n o \n)

    # la modalitá di apertura ¨a¨ serve ad APPENDERE il contenuto di un file,
    # e quindi a non sostituirlo
    with open("fileDiTesto.txt", mode="a") as f:
        f.write("aggiunta")

    # APERTURA E SCRITTURA

    with open("fileDiTesto.txt", mode="r") as fileAperto:
        with open("outputest.txt", "w") as fileDaScrivere:
            for line in fileAperto:
                fileDaScrivere.write(
                    line
                )  # crea una copia del file ¨fileDiTesto.txt¨ nel
                # file da scrivere ¨outputest.txt¨

    # FILE NON DI TESTO (IN Byte)
    # Per aprire un file che NON é di tipo testo, bisogna utilizzare l'aggiunta di "b" al
    # parametro "mode", che ci permetterá di NON interpretare gli accapi come ¨/n¨ ma in
    # altro modo:
    with open("fileImmagine", mode="rb"):
        # .....
        pass

    # Leggere un file dal web

    # Per poter leggere un file dal web, possiamo usufruire del modulo ¨requests¨, che ci permette
    # di leggere un file specificando il suo URL "Uniform Resource Locator":
    import requests

    pagina = requests.get("https://www.google.it")

    #   ENUMERATE
    # la funzione enumerate() permette di iterare sulle coppie indice-valore

    # Files JSON
    # per lavorare con i files json, c'� bisogno di utilizzare il modulo json

from pathlib import Path

# Absolute path
# c:/ProgramFiles/ecc...(Windows)
# /usr/local/bin/ecc...(Linux

path = Path("app.py")  # prende il path della directory corrente
print(path.exists())
path_new = Path("newDirectory")
path_new.mkdir()  # crea la cartella "newDirectory" nella directory corrente
path_new.rmdir()  # rimuove la cartella
path_new.mkdir()
for file in path_new.glob(
    "*"
):  # glob é un metodo che serve a cercare i file o le directory specificate
    print(
        file
    )  # stampa il nome di ogni file e directory nella directory, nella console

# se volessimo visualizzare solo i file e non le directory:
for file in path_new.glob("*.*"):
    print(file)

# PiP
# Python Package Index, sono cartelle dove puoi trovare centinaia di
# pacchetti per fare molte cose, create dalla community, per esempio,
# ci sono progetti o pacchetti per inviare sms, usare il bluetooth ecc...
# per installare i pypi, bisogna andare su pypi.org e cercare il pypi desiderato
# per fare un esempio, se volessimo installare 'openpyxl', dovremmo andare nel terminale di pyCharm o nel cmd
# e scrivere 'pip install openpyxl'
# i pip installati possono essere visualizzati andando su 'Project'
# in alto a sinistra, poi 'External Libraries', e 'site-packages


# Relative path
