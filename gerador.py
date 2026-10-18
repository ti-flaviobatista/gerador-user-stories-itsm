import random
import tkinter as tk
from tkinter import messagebox

ATORES = [
    "Como um Analista de Suporte Júnior",
    "Como um Gerente de Incidentes (ITIL)",
    "Como um Cliente do Service Desk",
    "Como um Administrador de Banco de Dados"
]

ACOES = [
    "quero um relatório automatizado que calcule o MTTR (Tempo Médio de Atendimento)",
    "quero um sistema de alertas que identifique chamados prestes a estourar o SLA",
    "quero uma ferramenta que classifique automaticamente o impacto e a urgência de um incidente",
    "quero um script que identifique chamados duplicados abertos pelo mesmo usuário em menos de 1 hora"
]

BENEFICIOS = [
    "para que a equipe possa focar nos gargalos de atendimento e melhorar a eficiência.",
    "para evitar penalidades contratuais e garantir a satisfação do cliente.",
    "para que a triagem inicial seja feita sem intervenção humana manual.",
    "para evitar o retrabalho dos técnicos e manter a base de dados limpa."
]

REGRAS_DE_NEGOCIO = [
    [
        "Regra 1: O cálculo do tempo deve desconsiderar horários fora do expediente (finais de semana e feriados).",
        "Regra 2: O resultado final deve ser exportado em formato JSON ou CSV.",
        "Regra 3: Se o MTTR estiver acima de 4 horas, o relatório deve destacar o indicador em vermelho."
    ],
    [
        "Regra 1: O alerta deve ser gerado quando o chamado atingir 80% do tempo limite do SLA.",
        "Regra 2: Chamados de prioridade Crítica devem disparar o alerta imediatamente se não forem atribuídos em 15 minutos.",
        "Regra 3: O log de alertas deve registrar a data, hora e o ID do chamado afetado."
    ],
    [
        "Regra 1: A matriz de prioridade deve cruzar Impacto (Alto/Médio/Baixo) e Urgência (Alta/Média/Baixa) conforme o padrão ITIL.",
        "Regra 2: Se o ator for da diretoria da empresa, o impacto deve ser automaticamente elevado para Alto."
    ]
]

def gerar_user_story():
    indice_acao = random.randint(0, len(ACOES) - 1)
    ator = random.choice(ATORES)
    acao = ACOES[indice_acao]
    beneficio = random.choice(BENEFICIOS)
    
    regras_idx = min(indice_acao, len(REGRAS_DE_NEGOCIO) - 1)
    regras = REGRAS_DE_NEGOCIO[regras_idx]
    
    texto_story = f"{ator}\n{acao}\n{beneficio}\n\nCritérios de Aceite / Regras de Negócio:\n"
    for regra in regras:
        texto_story += f"- {regra}\n"
        
    txt_resultado.delete("1.0", tk.END)
    txt_resultado.insert(tk.END, texto_story)

def copiar_texto():
    conteudo = txt_resultado.get("1.0", tk.END).strip()
    if conteudo:
        janela.clipboard_clear()
        janela.clipboard_append(conteudo)
        messagebox.showinfo("Sucesso", "História de Usuário copiada!")
    else:
        messagebox.showwarning("Aviso", "Gere uma história antes de copiar.")

janela = tk.Tk()
janela.title("Gerador de User Stories - ITSM")
janela.geometry("600x450")
janela.configure(padx=15, pady=15)

lbl_titulo = tk.Label(janela, text="Gerador Randômico de User Stories", font=("Helvetica", 14, "bold"))
lbl_titulo.pack(pady=(0, 15))

txt_resultado = tk.Text(janela, wrap=tk.WORD, font=("Consolas", 11), height=14)
txt_resultado.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

frame_botoes = tk.Frame(janela)
frame_botoes.pack()

btn_gerar = tk.Button(frame_botoes, text="Gerar Nova Story", font=("Helvetica", 11, "bold"), bg="#2ecc71", fg="white", padx=10, pady=5, command=gerar_user_story)
btn_gerar.pack(side=tk.LEFT, padx=10)

btn_copiar = tk.Button(frame_botoes, text="Copiar Texto", font=("Helvetica", 11), bg="#3498db", fg="white", padx=10, pady=5, command=copiar_texto)
btn_copiar.pack(side=tk.LEFT, padx=10)

janela.mainloop()
