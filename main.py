import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Voce gostaria de gerar um novo valor para o dado?\n"

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == "sim" or resposta == "s":
                self.GerarValorDoDado()
            elif resposta == "nao" or resposta == "n" or resposta == "não" or resposta == "nao":
                print("Agradecemos a sua participação")
        except:
            print("Ocorreu um erro ao receber sua resposta")

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
        print("Voce gostaria de jogar de novo?")
        segundaResposta = input()
        if segundaResposta == "sim" or segundaResposta == "s":
            self.GerarValorDoDado()
        else:
            print("Obrigado por participar.")

simulador = SimuladorDeDado()
simulador.Iniciar()