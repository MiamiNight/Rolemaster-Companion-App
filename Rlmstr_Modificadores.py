from tkinter import *
from tkinter.ttk import *
import random

class Modificadores:
    def __init__(self, name):
        self.name = name
        self.d100 = 0
        self.skillBonus = 0
        self.itemBonus = 0
        self.porcentagemExc = 0
        self.penalidadePeso = 0
        self.mMP = 0
        self.exauMod = 0
        self.valorDado = 0
        self.hpMod = 0
        self.modFer = 0
        self.iluminacaoVant = 0
        self.tipoIluminacao = 0
        self.situacaoCombate = 0
        self.atordoado = 0
        self.modIlumi = 0
        self.dificuldade = 0
        self.selfDiscipline = 0
        self.modDif = 0
        self.danoPorRound = 0
        self.valorSoma = 0
        self.resultadoFinal = ''
        self.resultadoFinalInt = 0

    
    # Função do D100, configurando o dado para abrir no acerto, ou erro crítico
    def dadoAberto(self): 

        ldado = Label(janela, text='')
        ldado.grid(column=4, row=24)

        self.d100 = random.randint(1, 100)
        
        self.valorDado = self.d100
        rolagem = '''

        
        O valor do dado foi:  ''' +str(self.d100)
        ldado.config(text=rolagem, font=('Arial Bold', 12))
        
        # Abertura do Acerto
        if self.valorDado > 95:
            for loop in range(10):
                ldado.config(text=rolagem, font=('Arial Bold', 12))
                self.d100 = 0
                self.d100 = random.randint(1, 100)
                self.valorDado += self.d100
                rolagem = '''
                O DADO ABRIU!!!
                ACERTO CRÍTICO!!!
                O resultado foi: ''' +str(self.valorDado)
                ldado.config(text=rolagem)
                                
                if self.d100 <= 95:
                    break

        # Abertura do Erro
        elif self.valorDado < 6:
            for loop in range(10):
                self.d100 = 0
                self.d100 = random.randint(1, 100)
                self.valorDado -= self.d100
                rolagem = '''
                O DADO ABRIIU!!!
                ERRO CRÍTICO!!!
                O resultado foi: ''' +str(self.valorDado)
                ldado.config(text=rolagem)

                
                if self.d100 <= 95:
                    break


    #Função para calcular os mods que correlacionam HP e dano sofrido
    def modDanoSofrido(self):
        hpTotal = int(eHpTotal.get())
        hpCorrente = int(eHpCorrente.get())

        soma = hpTotal - hpCorrente
        
        
        if soma <= hpTotal / 4:
            self.hpMod = 0
        elif soma > hpTotal / 4 and soma <= hpTotal / 2:
            self.hpMod = -10
        elif soma > hpTotal / 2 and soma <= hpTotal / 1.33:
           self.hpMod = -20
        else:
            self.hpMod = -30

        print('hp mod = ' +str(self.hpMod))

    #Função dos Modificadores de Combate e outros tipos de ferimento
    def modCondicionais(self):
        self.modFer = 0

        sD = int(self.selfDiscipline.get())
     
        if self.atordoado.get() == 1:
            self.modFer = (sD * 3) + -50

        if self.situacaoCombate.get() == 1:
            self.modFer -= 30
        elif self.situacaoCombate.get() == 2: #alvejado por porjeteis
            self.modFer -= 10
        
        print('modFer = ' +str(self.modFer))
    
    #Função que confere a iluminação do ambiente, quando desvantajosa, e aplica os modificadores corretos  
    def modIIluminacao(self):
        if self.iluminacaoVant.get() == 1:
            if self.tipoIluminacao.get() == 1:
                self.modIlumi = -30
            elif self.tipoIluminacao.get() == 2:
                self.modIlumi = -20
            elif self.tipoIluminacao.get() == 3:
                self.modIlumi = 0
            elif self.tipoIluminacao.get() == 4:
                self.modIlumi = +10
            elif self.tipoIluminacao.get() == 5:
                self.modIlumi = +30
            else:
                self.modIlumi = +40
        
        else:
            if self.tipoIluminacao.get() == 1:
                self.modIlumi = +10
            elif self.tipoIluminacao.get() == 2:
                self.modIlumi = +5
            elif self.tipoIluminacao.get() == 3:
                self.modIlumi = 0
            elif self.tipoIluminacao.get() == 4:
                self.modIlumi = -10
            elif self.tipoIluminacao.get() == 5:
                self.modIlumi = -25
            elif self.tipoIluminacao.get() == 6:
                self.modIlumi = -40 
       
        print('self.modIlumi = ' +str(self.modIlumi))        

    #Função que aplica o modificador relacionado a dificuldade
    def modDificuldade(self):
        
        if self.dificuldade.get() == 1:
            self.modDif = +30
        elif self.dificuldade.get() == 2:
            self.modDif = +20
        elif self.dificuldade.get() == 3:
            self.modDif = +10
        elif self.dificuldade.get() == 4:
            self.modDif = +0
        elif self.dificuldade.get() == 5:
            self.modDif = -10
        elif self.dificuldade.get() == 6:
            self.modDif = -20    
        elif self.dificuldade.get() == 7:
            self.modDif = -30
        elif self.dificuldade.get() == 8:
            self.modDif = -50
        else:
            self.modDif = -70

        print('self.modDif = ' +str(self.modDif))

    #Função sobre Pontos de Exasutão
    def modCalculoExaustao(self):       
        exaustaoTotal = int(eExausTotal.get())
        exaustaoCorrente = int(eExausCorrente.get())

        somaExau = exaustaoTotal - exaustaoCorrente

        if somaExau <= exaustaoTotal / 4:
            self.exauMod = 0
        elif somaExau > exaustaoTotal / 4 and somaExau <= exaustaoTotal / 2:
            self.exauMod = -5       
        elif somaExau > exaustaoTotal / 2 and somaExau <= exaustaoTotal / 1.33:
            self.exauMod = -15
        elif somaExau > exaustaoTotal / 1.33 and somaExau <= exaustaoTotal / 1.11:
            self.exauMod = -30
        elif somaExau > exaustaoTotal / 1.11 and somaExau <= exaustaoTotal / 1.01:
            self.exauMod = -60
        else:
            self.exauMod = -100
        
        print('self.exauMod ' +str(self.exauMod))

    #Função que mostra o resultado
    def resultadoManEstatica(self):
        if self.valorSoma < -25:
            self.resultadoFinal = '''
~~~~~~~~~ Falha Espetacular ~~~~~~~~
Você fez uma confusão da bulbônica.
Você se esqueceu até dos principios
mais básicos dessa manobra.
Você tem -20 nas suas 
duas próximas ações
enquanto se recupera da falha.
SHAME!!!'''
        elif (self.valorSoma > -24 and self.valorSoma < 5):
            self.resultadoFinal = '''
~~~~~~~~~~ Falha Absoluta ~~~~~~~~~~
Sua falha memorável marca 
você ao ridiculo
Espero que seus pais 
não estejam olhando...'''
        elif (self.valorSoma == 66):
            self.resultadoFinal = '''
~~~~~~~~~~ EVENTO INCOMUM ~~~~~~~~~~
O resultado final da sua tarefa
foi algo inesperadmente embasbacante'''
        elif (self.valorSoma > 4 and self.valorSoma < 76):
            self.resultadoFinal = '''
~~~~~~~~~~~~~~~ Falha ~~~~~~~~~~~~~~'''
        elif (self.valorSoma > 75 and self.valorSoma < 91):
            self.resultadoFinal = '''
~~~~~~~~~~ Sucesso Parcial ~~~~~~~~~
Você executou 20% da tarefa'''
        elif (self.valorSoma > 90 and self.valorSoma < 111):
            self.resultadoFinal = '''
~~~~~~~~~~~~ Quase Sucesso ~~~~~~~~~
Você executou 80% da tarefa'''
        elif (self.valorSoma == 100):
            self.resultadoFinal = '''
~~~~~~~~~~ Sucesso Incomum ~~~~~~~~~
Você executou a sua tarefa
de forma explendorosa'''
        elif (self.valorSoma > 110 and self.valorSoma < 176):
            self.resultadoFinal = '''
~~~~~~~~~~~~~~ Sucesso ~~~~~~~~~~~~~'''
        elif (self.valorSoma > 175):
            self.resultadoFinal = '''
~~~~~~~~~ Sucesso Absoluto ~~~~~~~~~
Você opera com essa skill daqui
 em diante com +10, até que você
tire uma Falha Absoluta,
ou Falha Espetacular'''

        lRolagem.config(text=obj.valorSoma)      
        lResultadoFinal.config(text=obj.resultadoFinal)

    #Iteração que define a dificuldade e mods relacionados a isso
    def resultManMovimento(self):

        self.resultadoFinal = ''
        self.resultadoFinalInt = 0

        if (self.dificuldade.get() == 1): #Dificuldade Routine
            if (self.valorSoma < -200):
                self.resultadoFinal = '''Voce caiu.
+2 Hits.
Voce esta fora por dois rounds.'''
            elif (self.valorSoma > -201 and self.valorSoma < -150):            
                self.resultadoFinal ='''Você falhou em agir.'''            
            elif (self.valorSoma > -151 and self.valorSoma < -100):            
                self.resultadoFinalInt = 10           
            elif (self.valorSoma > -101 and self.valorSoma < -50):        
                self.resultadoFinalInt = 30            
            elif (self.valorSoma > -51 and self.valorSoma < -25):
                self.resultadoFinalInt = 50
            elif (self.valorSoma > -26 and self.valorSoma < 1):
                self.resultadoFinalInt = 70
            elif (self.valorSoma > 0 and self.valorSoma < 21):
                self.resultadoFinalInt = 80           
            elif (self.valorSoma > 20 and self.valorSoma < 41):            
                self.resultadoFinalInt = 90            
            elif (self.valorSoma > 40 and self.valorSoma < 56):            
               self.resultadoFinalInt = 100          
            elif (self.valorSoma > 55 and self.valorSoma < 96):           
                self.resultadoFinalInt = 100          
            elif (self.valorSoma > 95 and self.valorSoma < 116):            
                self.resultadoFinalInt = 110           
            elif (self.valorSoma > 115 and self.valorSoma < 136):            
                self.resultadoFinalInt = 120           
            elif (self.valorSoma > 137 and self.valorSoma < 156):           
                self.resultadoFinalInt = 130            
            elif (self.valorSoma > 155 and self.valorSoma < 186):           
                self.resultadoFinalInt = 140            
            elif (self.valorSoma > 185 and self.valorSoma < 276):            
                self.resultadoFinalInt = 150           
            else:            
                self.resultadoFinal ='''Movimentaçao incrivel,
você se sente bem. 
Recupera 3 hits.'''
            
            
        elif (self.dificuldade.get() == 2): # Dificuldade Easy
            
            if (self.valorSoma < -200):
                self.resultadoFinal ='''Caiu. 
Desmaiou.
Voce esta fora por 12 rounds. +2 hits'''          
            elif (self.valorSoma > -201 and self.valorSoma < -150):
                self.resultadoFinal ='''Caiu no chao. 
Perdera 2 rounds. 
+2 hits'''
            elif (self.valorSoma > -151 and self.valorSoma < -100):            
                self.resultadoFinal ="Falhou em agir"          
            elif (self.valorSoma > -101 and self.valorSoma < -50):
                self.resultadoFinalInt = 10
            elif (self.valorSoma > -51 and self.valorSoma < -25):
                self.resultadoFinalInt = 30
            elif (self.valorSoma > -26 and self.valorSoma < 1):
                self.resultadoFinalInt = 50
            elif (self.valorSoma > 0 and self.valorSoma < 21):
                self.resultadoFinalInt = 60
            elif (self.valorSoma > 20 and self.valorSoma < 41):
                self.resultadoFinalInt = 70
            elif (self.valorSoma > 40 and self.valorSoma < 56):
                self.resultadoFinalInt = 80
            elif (self.valorSoma > 55 and self.valorSoma < 66):
                self.resultadoFinalInt = 90
            elif (self.valorSoma > 65 and self.valorSoma < 106):
                self.resultadoFinal ="100"
            elif (self.valorSoma > 107 and self.valorSoma < 126):
                self.resultadoFinal ="110"
            elif (self.valorSoma > 125 and self.valorSoma < 146):
                self.resultadoFinal ="120"
            elif (self.valorSoma > 145 and self.valorSoma < 166):
                self.resultadoFinal ="130"
            elif (self.valorSoma > 167 and self.valorSoma < 226):
                self.resultadoFinal ="140"
            elif (self.valorSoma > 227 and self.valorSoma < 276):
                self.resultadoFinal ='''Movimentaçao incrivel,
voce se sente bem.
Recupera 3 hits.'''
            else:
                self.resultadoFinal ='''Seu movimento brilhante inspira a todos.
Seu aliados tem +10 por 2 rounds.'''
            
            
        elif (self.dificuldade.get() == 3): # Dificuldade Light
            
            if (self.valorSoma < -200):            
                self.resultadoFinal ='''Caiu.
Quebrou os braços.
Você esta fora por 6 rounds. +10 hits.'''        
            elif (self.valorSoma > -201 and self.valorSoma < -150):
                self.resultadoFinal ='''Caiu no chao.
Você esta fora por 4 rounds. +3 hits.'''        
            elif (self.valorSoma > -151 and self.valorSoma < -100):            
                self.resultadoFinal ='''Caiu no chao.
Você esta fora por 2 rounds. +2 hits.'''         
            elif (self.valorSoma > -101 and self.valorSoma < -50):            
                self.resultadoFinal ="Falhou em agir."
            elif (self.valorSoma > -51 and self.valorSoma < -25):            
                self.resultadoFinalInt = 10
            elif (self.valorSoma > -26 and self.valorSoma < 1):
                self.resultadoFinalInt = 30
            elif (self.valorSoma > 0 and self.valorSoma < 21):
                self.resultadoFinalInt = 50 
            elif (self.valorSoma > 20 and self.valorSoma < 41):
                self.resultadoFinalInt = 60 
            elif (self.valorSoma > 40 and self.valorSoma < 56):
                self.resultadoFinalInt = 70 
            elif (self.valorSoma > 55 and self.valorSoma < 66):
                self.resultadoFinalInt = 80 
            elif (self.valorSoma > 65 and self.valorSoma < 76):
                self.resultadoFinalInt = 90 
            elif (self.valorSoma > 75 and self.valorSoma < 116):
                self.resultadoFinalIInt = 100
            elif (self.valorSoma > 115 and self.valorSoma < 136):
                self.resultadoFinalInt = 110
            elif (self.valorSoma > 135 and self.valorSoma < 166):
                self.resultadoFinalInt = 120
            elif (self.valorSoma > 167 and self.valorSoma < 186):
                self.resultadoFinalInt = 130
            elif (self.valorSoma > 185 and self.valorSoma < 226):
                self.resultadoFinal ='''Movimentaçao incrivel,
você se sente bem. 
Cura 4 hits.'''
            elif (self.valorSoma > 225 and self.valorSoma < 276):
                self.resultadoFinal ='''Seu movimento brilhante inspira a todos.
Seu aliados tem +10 nos por 2 rounds.'''
            else:
                self.resultadoFinal ='''Seu movimento brilhante inspira a todos.
Seu aliados tem +20 nos por 3 rounds.'''
            
            
        elif (self.dificuldade.get() == 4): #Dificuldade Medium
            if (self.valorSoma < -200):                
                self.resultadoFinal ='''Caiu. 
Quebrou um braço.
Você esta fora por 9 rounds. +15 hits.'''
            elif (self.valorSoma > -201 and self.valorSoma < -150):
                self.resultadoFinal ='''Caiu. 
Quebrou o punho.
Você esta fora por 6 rounds. +10 hits.'''
            elif (self.valorSoma > -151 and self.valorSoma < -100):                
                self.resultadoFinal ='''Caiu no chao. 
Tornoselo torcido.
Você esta com -25. +5 hits.'''             
            elif (self.valorSoma > -101 and self.valorSoma < -50):                
                self.resultadoFinal ='''Caiu no chao. 
Pedera 2 rounds.
+3 hits.'''              
            elif (self.valorSoma > -51 and self.valorSoma < -25):                
                self.resultadoFinal ="Falha em agir."   
            elif (self.valorSoma > -26 and self.valorSoma < 1):                
                self.resultadoFinalInt = 5 
            elif (self.valorSoma > 0 and self.valorSoma < 21):                
                self.resultadoFinalInt = 10          
            elif (self.valorSoma > 20 and self.valorSoma < 41):                
                self.resultadoFinalInt = 20              
            elif (self.valorSoma > 40 and self.valorSoma < 56):                
                self.resultadoFinalInt = 30               
            elif (self.valorSoma > 55 and self.valorSoma < 66):                
                self.resultadoFinalInt = 40             
            elif (self.valorSoma > 65 and self.valorSoma < 76):               
                self.resultadoFinalInt = 50            
            elif (self.valorSoma > 75 and self.valorSoma < 86):                
                self.resultadoFinalInt = 60              
            elif (self.valorSoma > 85 and self.valorSoma < 96):                
                self.resultadoFinalInt = 70              
            elif (self.valorSoma > 95 and self.valorSoma < 106):                
                self.resultadoFinalInt = 80              
            elif (self.valorSoma > 105 and self.valorSoma < 116):                
                self.resultadoFinalInt = 90             
            elif (self.valorSoma > 115 and self.valorSoma < 136):               
                self.resultadoFinalInt = 100            
            elif (self.valorSoma > 135 and self.valorSoma < 146):               
                self.resultadoFinalInt = 110           
            elif (self.valorSoma > 145 and self.valorSoma < 166):                
                self.resultadoFinalInt = 120             
            elif (self.valorSoma > 165 and self.valorSoma < 186):               
                self.resultadoFinal ='''Super movimento.
Voce se sente bem. 
Cura 3 hits.'''              
            elif (self.valorSoma > 185 and self.valorSoma < 226):               
                self.resultadoFinal ='''O movimento inspira a todos.
Você não está mais atordoado. 
Aliados estão a +10 por 2 rounds.'''              
            elif (self.valorSoma > 225 and self.valorSoma < 276):               
                self.resultadoFinal ='''Seu movimento inspira a todos. 
Seus aliados tem +20 por 3 rounds.'''               
            else:                
                self.resultadoFinal ='''Seu movimento inspira a todos. 
Seus aliados tem +25 por 3 rounds.'''
            
         
        elif (self.dificuldade.get() == 5): #Dificuldade Hard            
            if (self.valorSoma < -200):            
                self.resultadoFinal ='''Caiu. 
Quebrou um braço. 
Voce esta fora por 18 rounds. 
+20 hits.'''           
            elif (self.valorSoma > -201 and self.valorSoma < -150):           
                self.resultadoFinal ='''Caiu. 
Quebrou a perna. 
Voce esta fora por 9 rounds. 
+15 hits.'''           
            elif (self.valorSoma > -151 and self.valorSoma < -100):            
                self.resultadoFinal ='''Caiu no chao. 
Quebrou o braço. 
Você esta fora por 6 rounds. 
+10 hits.'''            
            elif (self.valorSoma > -101 and self.valorSoma < -50):            
                self.resultadoFinal ='''Caiu no chao. 
Torceu o tornozelo. 
Você esta com -25. 
+5 hits.'''           
            elif (self.valorSoma > -51 and self.valorSoma < -25):            
                self.resultadoFinal ='''Caiu no chao. 
Você esta fora por 3 rounds.
+5 hits.'''            
            elif (self.valorSoma > -26 and self.valorSoma < 1):            
                self.resultadoFinal ="Falha em agir."
            elif (self.valorSoma > 0 and self.valorSoma < 21):            
                self.resultadoFinalInt = 5
            elif (self.valorSoma > 20 and self.valorSoma < 41):            
                self.resultadoFinalInt = 10         
            elif (self.valorSoma > 40 and self.valorSoma < 56):            
                self.resultadoFinalInt = 20            
            elif (self.valorSoma > 55 and self.valorSoma < 66):            
                self.resultadoFinalInt = 30            
            elif (self.valorSoma > 65 and self.valorSoma < 76):            
                self.resultadoFinalInt = 40            
            elif (self.valorSoma > 75 and self.valorSoma < 86):           
                self.resultadoFinalInt = 50            
            elif (self.valorSoma > 85 and self.valorSoma < 96):            
                self.resultadoFinalInt = 60          
            elif (self.valorSoma > 95 and self.valorSoma < 106):            
                self.resultadoFinalInt = 70           
            elif (self.valorSoma > 105 and self.valorSoma < 116):            
                self.resultadoFinalInt = 80           
            elif (self.valorSoma > 115 and self.valorSoma < 126):            
               self.resultadoFinalInt = 90          
            elif (self.valorSoma > 125 and self.valorSoma < 146):            
                self.resultadoFinalInt = 100           
            elif (self.valorSoma > 145 and self.valorSoma < 156):            
                self.resultadoFinalInt = 110            
            elif (self.valorSoma > 155 and self.valorSoma < 166):            
                self.resultadoFinalInt = 120            
            elif (self.valorSoma > 165 and self.valorSoma < 186):            
                self.resultadoFinal ='''Escelente movimento. 
Você não está mais atordoado. 
Aliados estão a +10 por 2 rounds.'''           
            elif (self.valorSoma > 185 and self.valorSoma < 226):           
                self.resultadoFinal ='''Seu movimento inspira a seus companheiros. 
Seus aliados tem +20 por 3 rounds.'''          
            elif (self.valorSoma > 225 and self.valorSoma < 276):           
                self.resultadoFinal ='''Seu movimento inspira a seus companheiros. 
Seus aliados tem +25 por 3 rounds.'''
            else:            
                self.resultadoFinal ='''Seu movimento inspira a todos. 
Seus aliados tem +30 por 3 rounds.'''
        
    
        elif (self.dificuldade.get() == 6): #Dificuldade Very Hard    
            if (self.valorSoma < -200):            
                self.resultadoFinal ='''Caiu. 
Quebrou os braços e o pescoço.
Voce esta fora por 60 rounds. 
+30 hits.'''           
            elif (self.valorSoma > -201 and self.valorSoma < -150):            
                self.resultadoFinal ='''Caiu. 
Braços quebrados. 
Seus braços são inuteis. 
Voce esta fora por 18 rounds. 
+20 hits.'''            
            elif (self.valorSoma > -151 and self.valorSoma < -100):            
                self.resultadoFinal ='''Caiu. 
Quebrou a perna. 
Voce esta fora por 6 rounds. 
+15 hits.'''          
            elif (self.valorSoma > -101 and self.valorSoma < -50):            
                self.resultadoFinal ='''Caiu. 
Quebrou o punho. 
Você esta fora por 6 rounds. 
+10 hits. 
Não muito suave.'''            
            elif (self.valorSoma > -51 and self.valorSoma < -25):            
                self.resultadoFinal ='''Caiu no chao. 
Torceu o tornozelo e rompeu o ligamento. 
Você esta com -30. 
+15 hits.'''         
            elif (self.valorSoma > -26 and self.valorSoma < 1):            
                self.resultadoFinal ='''Caiu no chao.
Você esta fora por 3 rounds. 
+5 hits.'''            
            elif (self.valorSoma > 0 and self.valorSoma < 21):           
                self.resultadoFinal ="Falha em agir."
            elif (self.valorSoma > 20 and self.valorSoma < 41):            
                self.resultadoFinalInt = 5
            elif (self.valorSoma > 40 and self.valorSoma < 56):            
                self.resultadoFinalInt = 10
            elif (self.valorSoma > 55 and self.valorSoma < 66):            
                self.resultadoFinalInt = 20      
            elif (self.valorSoma > 65 and self.valorSoma < 76):            
                self.resultadoFinalInt = 30         
            elif (self.valorSoma > 75 and self.valorSoma < 86):            
                self.resultadoFinalInt = 40          
            elif (self.valorSoma > 85 and self.valorSoma < 96):            
                self.resultadoFinalInt = 50         
            elif (self.valorSoma > 95 and self.valorSoma < 106):           
                self.resultadoFinalInt = 60          
            elif (self.valorSoma > 105 and self.valorSoma < 116):            
                self.resultadoFinalInt = 70           
            elif (self.valorSoma > 115 and self.valorSoma < 126):            
                self.resultadoFinalInt = 80           
            elif (self.valorSoma > 125 and self.valorSoma < 136):            
                self.resultadoFinalInt = 90           
            elif (self.valorSoma > 135 and self.valorSoma < 156):            
                self.resultadoFinalInt = 100           
            elif (self.valorSoma > 155 and self.valorSoma < 166):            
                self.resultadoFinalInt = 110            
            elif (self.valorSoma > 165 and self.valorSoma < 186):            
                self.resultadoFinalInt = 120           
            elif (self.valorSoma > 185 and self.valorSoma < 226):           
                self.resultadoFinal ='''Seu movimento inspira a seus companheiros. 
Seus aliados tem +30 por 2 rounds.'''          
            elif (self.valorSoma > 225 and self.valorSoma < 276):            
                self.resultadoFinal ='''Seu movimento inspira a seus companheiros. 
Seus aliados tem +30 por 3 rounds.'''       
            else:           
                self.resultadoFinal ='''Seu movimento inspira a todos. 
Seus aliados tem +30 por 4 rounds.'''
            
          
        elif (self.dificuldade.get() == 7): #Dificuldade Extremely Hard           
            if (self.valorSoma < -200):            
                self.resultadoFinal ='''A queda o envia para um coma de três anos. 
Espinha quebrada. 
+30 hits.'''          
            elif (self.valorSoma > -201 and self.valorSoma < -150):            
                self.resultadoFinal ='''Caiu. 
Quebrou a coluna e as pernas. 
Paralisia da parte inferior do corpo. 
+25 hits.'''                           
            elif (self.valorSoma > -151 and self.valorSoma < -100):            
                self.resultadoFinal ='''Caiu. 
Esmigalhou o joelho.
Voce esta a -80, fora por 6 rounds. 
+30 hits.'''           
            elif (self.valorSoma > -101 and self.valorSoma < -50):            
                self.resultadoFinal ='''Caiu. Quebrou o braço. 
Você esta fora por 6 rounds. 
+12 hits.'''          
            elif (self.valorSoma > -51 and self.valorSoma < -25):            
                self.resultadoFinal ='''Caiu. 
Desmaiado por 18 rounds. 
+10 hits. 
Você perdeu parceiro.'''            
            elif (self.valorSoma > -26 and self.valorSoma < 1):            
                self.resultadoFinal ='''Caiu. 
Torceu o tornozelo e rompeu o ligamento. 
Você esta a -30. 
+10 hits.'''           
            elif (self.valorSoma > 0 and self.valorSoma < 21):            
                self.resultadoFinal ='''Caiu no chao. 
Você está fora por 3 rounds. 
+5 hits.'''     
            elif (self.valorSoma > 20 and self.valorSoma < 41):            
                self.resultadoFinal ='''Falha em agir.'''
            elif (self.valorSoma > 40 and self.valorSoma < 56):            
                self.resultadoFinalInt = 5     
            elif (self.valorSoma > 55 and self.valorSoma < 66):           
                self.resultadoFinalInt = 10        
            elif (self.valorSoma > 65 and self.valorSoma < 76):            
                self.resultadoFinalInt = 20           
            elif (self.valorSoma > 75 and self.valorSoma < 86):            
                self.resultadoFinalInt = 30           
            elif (self.valorSoma > 85 and self.valorSoma < 96):            
                self.resultadoFinalInt = 40           
            elif (self.valorSoma > 95 and self.valorSoma < 106):            
                self.resultadoFinalInt = 50          
            elif (self.valorSoma > 105 and self.valorSoma < 116):            
                self.resultadoFinalInt = 60          
            elif (self.valorSoma > 115 and self.valorSoma < 126):            
                self.resultadoFinalInt = 70           
            elif (self.valorSoma > 125 and self.valorSoma < 136):            
                self.resultadoFinalInt = 80           
            elif (self.valorSoma > 135 and self.valorSoma < 146):            
                self.resultadoFinalInt = 90           
            elif (self.valorSoma > 145 and self.valorSoma < 166):            
                self.resultadoFinalInt = 100            
            elif (self.valorSoma > 165 and self.valorSoma < 186):            
                self.resultadoFinalInt = 110            
            elif (self.valorSoma > 185 and self.valorSoma < 226):            
                self.resultadoFinalInt = 120            
            elif (self.valorSoma > 225 and self.valorSoma < 276):            
                self.resultadoFinal ="Você tem metade do round para agir."           
            else:            
                self.resultadoFinal ='''Seu movimento inspira seus aliados. 
+30 para seus companheiros.'''
            
           
        elif (self.dificuldade.get() == 8): #Dificuldade Sheer Folly    
            if (self.valorSoma < -200):            
                self.resultadoFinal ='''A queda quebra seu pescoço.
Voce morre em 3 rounds.'''          
            elif (self.valorSoma > -201 and self.valorSoma < -150):            
                self.resultadoFinal ='''Caiu. 
Voce arrebenta sua coluna
e esta em coma por 1 ano.'''         
            elif (self.valorSoma > -151 and self.valorSoma < -100):            
                self.resultadoFinal ='''Caiu. 
Quebrou os dois braços e o pescoço. 
Voce esta a -80, fora por 6 rounds. +30 hits.'''           
            elif (self.valorSoma > -101 and self.valorSoma < -50):            
                self.resultadoFinal ='''Caiu. 
Esmigalhou o joelho. 
Você esta a -80, por 9 rounds. +30 hits.'''           
            elif (self.valorSoma > -51 and self.valorSoma < -25):            
                self.resultadoFinal ='''Caiu. 
Quebrou o braço. 
Voce esta fora por 6 rounds. +12 hits.'''         
            elif (self.valorSoma > -26 and self.valorSoma < 1):            
                self.resultadoFinal ='''Caiu.
Quebrou o punho. 
Você esta fora por 2 rounds. 
+20 hits. Não muito suave.'''          
            elif (self.valorSoma > 0 and self.valorSoma < 21):            
                self.resultadoFinal ='''Caiu. 
Destendeu um musculo da perna. 
Voce está a -25, fora por 2 rounds.
+5 hits.'''          
            elif (self.valorSoma > 20 and self.valorSoma < 41):            
                self.resultadoFinal ='''Caiu no chao. 
Voce toma 3 hits por round, esta fora por 2 rounds. 
+7 hits.'''           
            elif (self.valorSoma > 40 and self.valorSoma < 56):            
                self.resultadoFinal ='''Caiu no chao. 
Voce esta fora por 3 rounds. 
+5 hits.'''      
            elif (self.valorSoma > 55 and self.valorSoma < 66):            
                self.resultadoFinal ="Falha em agir."
            elif (self.valorSoma > 65 and self.valorSoma < 76):           
                self.resultadoFinalInt = 5
            elif (self.valorSoma > 75 and self.valorSoma < 86):            
                self.resultadoFinalInt = 10
            elif (self.valorSoma > 85 and self.valorSoma < 96):
                self.resultadoFinalInt = 20
            elif (self.valorSoma > 95 and self.valorSoma < 106):            
                self.resultadoFinalInt = 30
            elif (self.valorSoma > 105 and self.valorSoma < 116):           
                self.resultadoFinalInt = 40       
            elif (self.valorSoma > 115 and self.valorSoma < 126):            
                self.resultadoFinalInt = 50 
            elif (self.valorSoma > 125 and self.valorSoma < 136):            
                self.resultadoFinalInt = 60  
            elif (self.valorSoma > 135 and self.valorSoma < 146):            
                self.resultadoFinalInt = 70    
            elif (self.valorSoma > 145 and self.valorSoma < 166):            
                self.resultadoFinalInt = 80     
            elif (self.valorSoma > 165 and self.valorSoma < 186):            
                self.resultadoFinalInt = 90    
            elif (self.valorSoma > 185 and self.valorSoma < 276):            
                self.resultadoFinalInt = 100      
            else:            
                self.resultadoFinal ='''Seu movimento atordoa seus inimigos
dentro de 30' por 1 round. 
Você e seus companheiros estao +15.'''
            
           
        elif (self.dificuldade.get() == 9):  #Dificuldade Absurd            
            if (self.valorSoma < -200):            
                self.resultadoFinal ="A queda quebra seu cranio."            
            elif (self.valorSoma > -201 and self.valorSoma < -150):            
                self.resultadoFinal ="A quedo o paraliza do pescoço para baixo."           
            elif (self.valorSoma > -151 and self.valorSoma < -100):            
                self.resultadoFinal ='''Caiu. 
Voce esbagaçou sua coluna 
e esta em coma por 1 ano.'''          
            elif (self.valorSoma > -101 and self.valorSoma < -50):           
                self.resultadoFinal ='''Caiu. 
Quebrou a coluna e as pernas. 
Paralesia da parte de baixo do corpo. 
+25 hits.'''           
            elif (self.valorSoma > -51 and self.valorSoma < -25):            
                self.resultadoFinal ='''Caiu. 
Quebrou os braços. 
Voce esta fora por 18 rounds. 
+25 hits.'''            
            elif (self.valorSoma > -26 and self.valorSoma < 1):            
                self.resultadoFinal ='''Caiu. 
Quebrou a perna. 
Voce esta a -75, fora por 6 rounds. 
+10 hits.'''            
            elif (self.valorSoma > 0 and self.valorSoma < 21):            
                self.resultadoFinal ='''Caiu. 
Quebrou o braço. 
Voce está fora por 6 rounds. 
+15 hits.'''           
            elif (self.valorSoma > 20 and self.valorSoma < 41):            
                self.resultadoFinal ='''Caiu. 
Desmaiou. 
Você esta fora por 3 rounds. 
+10 hits.'''            
            elif (self.valorSoma > 40 and self.valorSoma < 56):            
               self.resultadoFinal ='''Caiu. 
Torceu o tornozelo. 
Voce esta a -30. 
+15 hits.'''        
            elif (self.valorSoma > 55 and self.valorSoma < 66):            
                self.resultadoFinal ='''Caiu. 
3 hits por round, 
fora por 2 rounds. 
7 hits.'''      
            elif (self.valorSoma > 65 and self.valorSoma < 76):            
                self.resultadoFinal ="Congelado por 2 rounds."
            elif (self.valorSoma > 75 and self.valorSoma < 86):            
                self.resultadoFinal ="Falha em agir."
            elif (self.valorSoma > 85 and self.valorSoma < 96):            
                self.resultadoFinalInt = 5
            elif (self.valorSoma > 95 and self.valorSoma < 106):            
                self.resultadoFinal = 10
            elif (self.valorSoma > 105 and self.valorSoma < 116):            
                self.resultadoFinalInt = 20
            elif (self.valorSoma > 115 and self.valorSoma < 126):            
                self.resultadoFinalInt = 30            
            elif (self.valorSoma > 125 and self.valorSoma < 136):            
                self.resultadoFinalInt = 40            
            elif (self.valorSoma > 135 and self.valorSoma < 146):            
                self.resultadoFinalInt = 50           
            elif (self.valorSoma > 145 and self.valorSoma < 156):           
                self.resultadoFinalInt = 60          
            elif (self.valorSoma > 155 and self.valorSoma < 166):            
                self.resultadoFinalInt = 70           
            elif (self.valorSoma > 165 and self.valorSoma < 185):            
                self.resultadoFinalInt = 80           
            elif (self.valorSoma > 185 and self.valorSoma < 226):            
                self.resultadoFinalInt = 90           
            elif (self.valorSoma > 225 and self.valorSoma < 276):            
                self.resultadoFinalInt = 100            
            else:            
                self.resultadoFinal ='''Seu movimento atordoa seus inimigos
dentro de 50', por 1 round. 
Você e seus companheiros estao +15.'''

        if self.resultadoFinal == '' and self.resultadoFinalInt != 0:
            
            d100 = random.randint(1, 100)
            posManobra = self.resultadoFinalInt - 100

            if d100 > self.resultadoFinalInt:
                self.resultadoFinal = '''(1)Você completou ''' +str(self.resultadoFinalInt)+ '''% da tarefa.
(2)Você falhou em realizar a tarefa.
(3)Você completou a manobra e no próximo turno tem ''' +str(posManobra)+ ''' como bônus/ônus.'''
            else :
                self.resultadoFinal = '''(1)Você completou ''' +str(self.resultadoFinalInt)+ '''% da tarefa.
(2)Você conseguiu realizar a tarefa.
(3)Você completou a manobra e no próximo turno tem ''' +str(posManobra)+ ''' como bônus/ônus.'''    
            lResultadoFinal.config(text=obj.resultadoFinal)
            print(self.resultadoFinal)
        else:      
            lResultadoFinal.config(text=obj.resultadoFinal)
            print(self.resultadoFinal)
            
                  

    def execResult(self):
        obj.resultado()
        

        

    #Função Botão
    def resultado(self):
        tipo = tipoTeste.get()

        self.dadoAberto()
        self.modCalculoExaustao()
        self.modDificuldade()
        self.modIIluminacao()
        self.modCondicionais()
        self.modDanoSofrido()

        print('self.skillBonus = ' +str(self.skillBonus.get()))
        print('self.itemBonus = ' +str(self.itemBonus.get()))
        print('vmodPorcentagem = ' +str(self.porcentagemExc.get()))
        print('self.danoPorRound = ' +str(self.danoPorRound.get()))
        print('vmodPenalidadePeso = ' +str(self.penalidadePeso.get()))
        print('vmodMMP = ' +str(self.mMP.get()))

        if (tipo == 'Manobra Estática'):
            self.valorSoma = int(self.skillBonus.get()) + int(self.itemBonus.get()) - int(self.porcentagemExc.get()) - int(self.danoPorRound.get()) - int(self.penalidadePeso.get()) - int(self.mMP.get())
            self.valorSoma += self.exauMod + self.modDif + self.modIlumi + self.modFer + self.hpMod + self.valorDado
            lResultadoSoma.config(text='O valor total foi: ' +str(self.valorSoma))

            self.resultadoManEstatica()
        else:          
            self.valorSoma = int(self.skillBonus.get()) + int(self.itemBonus.get()) - int(self.porcentagemExc.get()) - int(self.danoPorRound.get()) - int(self.penalidadePeso.get()) - int(self.mMP.get())
            self.valorSoma += self.exauMod + self.modDif + self.modIlumi + self.modFer + self.hpMod + self.valorDado
            lResultadoSoma.config(text='O valor total foi: ' +str(self.valorSoma))

            self.resultManMovimento()


obj = Modificadores("obj")    

#Janela
janela = Tk()
janela.title("Rolemaster")
janela.geometry("1450x900")




#Rolagem
lRolagem = Label(janela, text='', font=('Arial Bold', 15))
lRolagem.grid(column=4, row=25)




#Resultado
lResultadoFinal = Label(janela, text='', font=('Arial Bold', 10))
lResultadoFinal.grid(column=4, row=26)

lResultadoSoma =  Label(janela, text='', font=('Arial Bold', 10))
lResultadoSoma.grid(column=4, row=25)



#logo
logo = PhotoImage(file='logo.png')
lLogo = Label(janela, image=logo)
lLogo.grid(column=4, row=0)




#Botão Rolar
botaoRolar = Button(janela, text="Rolar", command=obj.execResult)
botaoRolar.grid(column=4, row=23)




#Tipo de teste
lEspacamento2 = Label(janela, text='', font=('Arial Bold', 10))
lEspacamento2.grid(column=0, row=23)

tipoTeste = Combobox(janela)
tipoTeste['values']= ('Manobra Estática', 'Manobra de Movimento')
tipoTeste.grid(column=4, row=1)
tipoTeste.current(0)




#Skill Bônus
lSkillBonus = Label(janela, text="Skill Bônus", font=("Arial Bold", 10))
lSkillBonus.grid(column=0, row=4)

eSkillBonus = IntVar()
eSkillBonus = Entry(janela, width=5)
eSkillBonus.grid(column=1, row=4)
obj.skillBonus = eSkillBonus

#Item Bônus
lItenBonus = Label(janela, text="Item Bônus", font=("Arial Bold", 10))
lItenBonus.grid(column=0, row=5)

eItemBonus = IntVar()
eItemBonus = Entry(janela, width=5)
eItemBonus.grid(column=1, row=5)
obj.itemBonus = eItemBonus

#HP
lHpTotal = Label(janela, text="HP Total", font=("Arial Bold", 10))
lHpTotal.grid(column=0, row=6)

lHpCorrente = Label(janela, text="HP Corrente", font=("Arial Bold", 10))
lHpCorrente.grid(column=0, row=7)

eHpTotal = Entry(janela, width=5)
eHpTotal.grid(column=1, row=6)

eHpCorrente = Entry(janela, width=5)
eHpCorrente.grid(column=1, row=7)

#Porcentagem Excedente de Atividade de Turno
lPorcentagemExc = Label(janela, text="Porcentagem Excedente", font=("Arial Bold", 10))
lPorcentagemExc.grid(column=4,row=4)

ePorcentagemExc = IntVar()
ePorcentagemExc = Entry(janela, width=5)
ePorcentagemExc.grid(column=5, row=4)
obj.porcentagemExc = ePorcentagemExc

#Pontos de Exaustão 
lExausTotal = Label(janela, text='Pontos de Exaustão Totais', font=("Arial Bold", 10))
lExausTotal.grid(column=4, row=5)

eExausTotal = Entry(janela, width=5)
eExausTotal.grid(column=5, row=5)

lExausCorrente = Label(janela, text='Pontos de Exaustão Corrente', font=('Arial Bold', 10))
lExausCorrente.grid(column=4, row=6)

eExausCorrente = Entry(janela, width=5)
eExausCorrente.grid(column=5, row=6)

#Dano Por Round
lDanoPorRound = Label(janela, text='Dano Sofrido por Round', font=('Arial Bold', 10))
lDanoPorRound.grid(column=4, row=7)

eDanoPorRound = IntVar()
eDanoPorRound = Entry(janela, width=5)
eDanoPorRound.grid(column=5, row=7)
obj.danoPorRound = eDanoPorRound



#Penalidade Por Peso
lPenalidadePeso = Label(janela, text='Penalidade por Peso', font=('Arial Bold', 10))
lPenalidadePeso.grid(column=9, row=4)

ePenalidadePeso = IntVar()
ePenalidadePeso = Entry(janela, width=5)
ePenalidadePeso.grid(column=10, row=4)
obj.penalidadePeso = ePenalidadePeso

#Moving Maneuver Penalty
lMMP = Label(janela, text='Penalidade por Manobra de Movimento', font=('Arial Bold', 10))
lMMP.grid(column=9, row=5)

eMMP = IntVar()
eMMP = Entry(janela, width=5)
eMMP.grid(column=10, row=5)
obj.mMP = eMMP 

#Modificador de Self Dicipline
lModSD = Label(janela, text='Modificador de Self Discipline', font=('Arial Bold', 10))
lModSD.grid(column=9, row=6)

eModSD = IntVar()
eModSD = Entry(janela, width=5)
eModSD.grid(column=10, row=6)

obj.selfDiscipline = eModSD

#Espaçamentos

lEspacamento = Label(janela, text='', font=('Arial Bold', 10))
lEspacamento.grid(column=0, row=3)

lEspacamento2 = Label(janela, text='', font=('Arial Bold', 10))
lEspacamento2.grid(column=2, row=20)

lEspacamento3 = Label(janela, text='                                                  ', font=('Arial Bold', 10))
lEspacamento3.grid(column=7, row=5)

lEspacamento3 = Label(janela, text='                                                       ', font=('Arial Bold', 10))
lEspacamento3.grid(column=2, row=5)

lEspacamento4 = Label(janela, text='', font=('Arial Bold', 10))
lEspacamento4.grid(column=0, row=12)

lEspacamento1 = Label(janela, text='', font=('Arial Bold', 10))
lEspacamento1.grid(column=2, row=17)

#### Check Boxes ####

#Radiobuttons

#Dificuldade
lDificuldade = Label(janela, text='           Dificuldade           ', font=('Arial Bold', 10))
lDificuldade.grid(column=0, row=13)

dificuldade = IntVar()

rRotina = Radiobutton(janela, text="Rotina", var=dificuldade, value=1)
rRotina.grid(column=0, row=14)

rFacil = Radiobutton(janela, text="Fácil", var=dificuldade, value=2)
rFacil.grid(column=0, row=15)

rBaixa = Radiobutton(janela, text="Baixa", var=dificuldade, value=3)
rBaixa.grid(column=0, row=16)

rMedia = Radiobutton(janela, text="Media", var=dificuldade, value=4)
rMedia.grid(column=0, row=17)

rDificil = Radiobutton(janela, text="Difícil", var=dificuldade, value=5)
rDificil.grid(column=0, row=18)

rMDificil = Radiobutton(janela, text="Muito Difícil", var=dificuldade, value=6)
rMDificil.grid(column=0, row=19)

rEDificil = Radiobutton(janela, text="Extremamente Difícil", var=dificuldade, value=7)
rEDificil.grid(column=0, row=20)

rPuraLoucura = Radiobutton(janela, text="Pura Loucura", var=dificuldade, value=8)
rPuraLoucura.grid(column=0, row=21)

rAbsurdo = Radiobutton(janela, text="Absurdo", var=dificuldade, value=9)
rAbsurdo.grid(column=0, row=22)

obj.dificuldade = dificuldade



#Iluminação do Ambiente (colocar o checkbox se vantajosa ou desvantajosa)
lIluminacao = Label(janela, text='Iluminação', font=('Arial Bold', 10))
lIluminacao.grid(column=9, row=13)

iluminacaoVant = IntVar()
cIlumVant = Checkbutton(janela, text='Vantajosa', var=iluminacaoVant, onvalue=1)
cIlumVant.grid(column=9, row=14)

obj.iluminacaoVant = iluminacaoVant

tipoIluminacao = IntVar()
rSSombras = Radiobutton(janela, text='Sem Sombras', var=tipoIluminacao, value=1)
rSSombras.grid(column=9, row=16)

rPSombras = Radiobutton(janela, text='Poucas Sombras', var=tipoIluminacao, value=2)
rPSombras.grid(column=9, row=17)

rSoturno = Radiobutton(janela, text='Soturno', var=tipoIluminacao, value=3)
rSoturno.grid(column=9, row=18)

rMSombras= Radiobutton(janela, text='Muitas Sombras', var=tipoIluminacao, value=4)
rMSombras.grid(column=9, row=19)

rEscuro = Radiobutton(janela, text='Escuro', var=tipoIluminacao, value=5)
rEscuro.grid(column=9, row=20)

rETotal = Radiobutton(janela, text='Escuridão Total', var=tipoIluminacao, value=6)
rETotal.grid(column=9, row=21)

obj.tipoIluminacao = tipoIluminacao



#Checkbuttons

#Condições
lCondicoes = Label(janela, text='Condições', font=('Arial Bold', 10))
lCondicoes.grid(column=4, row=15)

#Atordoado
atordoado = IntVar()
cAtordoado = Checkbutton(janela, text="Atordoado", var=atordoado, onvalue=1)
cAtordoado.grid(column=4, row=16)

obj.atordoado = atordoado

#Situação de Combate
situacaoCombate = IntVar()
rAmbienteComb = Radiobutton(janela, text='Em Combate corpo-a-corpo', var=situacaoCombate, value=1)
rAmbienteComb.grid(column=4, row=17)

rAlvoDeProjeteis = Radiobutton(janela, text='Alvejado por Projeteis', var=situacaoCombate, value=2)
rAlvoDeProjeteis.grid(column=4, row=18)

obj.situacaoCombate = situacaoCombate




















janela.mainloop()

                 


