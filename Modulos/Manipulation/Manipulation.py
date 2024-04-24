# IMPORT LIB
import json
# CLASSE MANIPULADORA DAS INFORMAÇÕES
class Analise:
    def __init__(self) -> None:
        pass
    
    def Calc_analise(self, peso_vazio: float,bitola_aeronave: float, C: float , C2: float, largura_ppd_aeroporto: float, acostamento: float, faixa_de_pista: float,envergadura_aeronave: float, X: float, Z: float):
        '''
        FUNÇÃO PARA CALCULAR EXECUTAR OS CALCULOS DA ANALISE.
        return MTOW, largura_ppd, segurança1, D1, D2
        '''
        #MTOW
        self.MTOW = peso_vazio
        #Largura da pista de pouso e decolagem para a aeronave
        self.largura_ppd = bitola_aeronave + 2 *C
        #largura da pista de táxi
        self.largura_pt = bitola_aeronave + 2 *C2
        #Análise do acostamento da pista de pouso e decolagem
        self.segurança1 = largura_ppd_aeroporto + acostamento
        #Análise de separação - pista de táxi e de pouso e decolagem
        ## distância entre eixos de pistas de táxi e de pista depouso e decolagem
        self.D1 = 0.5 * (faixa_de_pista + envergadura_aeronave)
        ## distância ente o eixo da pista de táxi de acesso ao estacionamentoe um objeto
        self.D2 = 0.5 * envergadura_aeronave + X + Z
        
    def ConstructorJSON(self, aeroporto: str):
        '''
        FUNÇÃO CONSTRUTORA DO JSON COM INFORMAÇÕES FINAIS
        '''
        info ={}
        data = self.OpenDados()
        largura_ppd_aeroporto = data[aeroporto]["largura_ppd_aeroporto"]
        largura_pt_aeroporto = data[aeroporto]["largura_pt_aeroporto"]
        mtow_aeroporto = data[aeroporto]["mtow_aeroporto"]
        # CONDIÇÕES
        if self.largura_ppd > largura_ppd_aeroporto:
            # A AERONAVE NÂO É COMPATIVEL COM A PISTA DE POUSO E DECOLAGEM
            info[aeroporto][f"A aeronave nâo é compativel com a Pista de pouso e decolagem {aeroporto}"]
            info[aeroporto]["Largura necessaria" :self.largura_ppd]
            info[aeroporto][f"A aeronave nâo é compativel com a Pista de pouso e decolagem {aeroporto}"]
            info[aeroporto][f"Largura da pista do aeroporto {aeroporto}":largura_ppd_aeroporto]
        else:
        # A AERONAVE É COMPATIVEL COM A PISTA DE POUSO E DECOLAGEM
            info[aeroporto][f"A aeronave é compativel com a Pista de pouso e decolagem {aeroporto}"]
            info[aeroporto]["Largura necessaria":self.largura_ppd]
            info[aeroporto][f"A aeronave é compativel com a Pista de pouso e decolagem {aeroporto}"]
            info[aeroporto][f"Largura da pista do aeroporto {aeroporto}": largura_ppd_aeroporto]
        # COMPATIBILIDADE DA TAXIWAY    
        if self.largura_pt > largura_pt_aeroporto:
            info[aeroporto]["táxiway"] = "A aeronave não é compativel com a táxiway"
        else:
            info[aeroporto]["táxiway"] = "A aeronave é compativel com a táxiway"
        #  INCOMPATIBILIDADE DA TAXIWAY 
        if self.MTOW > mtow_aeroporto:
            info[aeroporto]["Peso de decolagem"] = "Peso de decolagem incompativel"
        else:
            info[aeroporto]["Peso de decolagem"] = "Peso de decolagem compativel"
        # SALVANDO DADOS EM JSON 
        with open("Resultado_analise.json", "w") as file:
            json.dumps([info], file)
    
    def Constructor_infoJSON(self,aeroporto: str, largura_ppd_aeroporto: float,largura_pt_aeroporto: float,mtow_aeroporto: float):
        '''
        FUNÇÃO CONSTRUTORA DO JSON 
        return Info_aeroporto.json
        '''
        info = self.OpenDados()
        info[aeroporto]["largura_ppd_aeroporto"] = [largura_ppd_aeroporto]
        info[aeroporto]["largura_pt_aeroporto"] = [largura_pt_aeroporto]
        info[aeroporto]["mtow_aeroporto"] = [mtow_aeroporto]
        # SALVANDO JSON 
        with open("Info_aeroporto.json", "w") as file:
            json.dumps([info], file)
    
    def OpenDados(self):
        '''
        FUNÃO PARA LER DADOS DO JSON
        '''
        with open("Info_aeroporto.json", "r") as file:
            dados = json.load(file)
            return dados