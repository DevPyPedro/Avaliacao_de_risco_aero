import json

class Analise:
    def __init__(self) -> None:
        pass
    
    def Calc_analise(self, peso_vazio: float, bitola_aeronave: float, C: float, C2: float, largura_ppd_aeroporto: float, acostamento: float, faixa_de_pista: float, envergadura_aeronave: float, X: float, Z: float):
        self.MTOW = peso_vazio
        self.largura_ppd = bitola_aeronave + (2 * C)
        self.largura_pt = bitola_aeronave + (2 * C2)
        self.seguranca1 = largura_ppd_aeroporto + acostamento
        self.D1 = 5 * (faixa_de_pista + envergadura_aeronave)
        self.D2 = 5 * envergadura_aeronave + X + Z
        
    def ConstructorJSON(self, aeroporto: str):
        info = {}  # Inicialize info corretamente
        data = self.OpenDados()
        largura_ppd_aeroporto = data.get(aeroporto, {}).get("largura_ppd_aeroporto", 0)
        largura_pt_aeroporto = data.get(aeroporto, {}).get("largura_pt_aeroporto", 0)
        mtow_aeroporto = data.get(aeroporto, {}).get("mtow_aeroporto", 0)

        if self.largura_ppd > largura_ppd_aeroporto:
            info[aeroporto] = {
                "compatibilidade_ppd": "A aeronave não é compativel com a Pista de pouso e decolagem",
                "largura_necessaria": self.largura_ppd,
                "largura_aeroporto": largura_ppd_aeroporto
            }
        else:
            info[aeroporto] = {
                "compatibilidade_ppd": "A aeronave é compativel com a Pista de pouso e decolagem",
                "largura_necessaria": self.largura_ppd,
                "largura_aeroporto": largura_ppd_aeroporto
            }

        info[aeroporto]["compatibilidade_taxiway"] = "A aeronave não é compativel com a táxiway" if self.largura_pt > largura_pt_aeroporto else "A aeronave é compativel com a táxiwa"
        info[aeroporto]["compatibilidade_mtow"] = "Peso de decolagem incompativel" if self.MTOW > mtow_aeroporto else "Peso de decolagem compativel"

        with open("Resultado_analise.json", "w") as file:
            json.dump(info, file)
    
    def Constructor_infoJSON(self, aeroporto: str, largura_ppd_aeroporto: float, largura_pt_aeroporto: float, mtow_aeroporto: float):
        try:
            info = self.OpenDados()  # Carrega os dados do arquivo JSON
            if aeroporto not in info:
                info[aeroporto] = {}  # Cria um novo dicionário vazio se a chave não existir
            info[aeroporto] = {
                "largura_ppd_aeroporto": largura_ppd_aeroporto,
                "largura_pt_aeroporto": largura_pt_aeroporto,
                "mtow_aeroporto": mtow_aeroporto
            }
            # Salva os dados atualizados no arquivo JSON
            with open("Info_aeroporto.json", "w") as file:
                json.dump(info, file)
        except Exception as e:
            print(f"Erro ao atualizar os dados do aeroporto {aeroporto}: {e}")

    
    def OpenDados(self):
        try:
            with open("Info_aeroporto.json", "r") as file:
                dados = json.load(file)
                return dados
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"Erro ao abrir o arquivo: {e}")
            return {}
