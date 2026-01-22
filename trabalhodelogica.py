from pysat.solvers import Glucose4
import tkinter as tk
from tkinter import Canvas, Tk
import time

SETTINGS = {
    "creeper": {
        "name": "Creeper",
        "size": {"row": 9, "column": 8},
        "rules": {
            "rows": {
                1: [8],
                2: [8],
                3: [1, 2, 1],
                4: [1, 2, 1],
                5: [3, 3],
                6: [2, 2],
                7: [2, 2],
                8: [2, 2, 2],
                9: [8],
            },
            "columns": {
                1: [9],
                2: [2, 5],
                3: [2, 1, 1],
                4: [4, 2],
                5: [4, 2],
                6: [2, 1, 1],
                7: [2, 5],
                8: [9],
            },
        },
        "color": "#00ff66"
    },
    "heart": {
        "name": "Coração",
        "size": {"row": 10, "column": 12},
        "rules": {
            "rows": {
                1: [2, 2],
                2: [4, 4],
                3: [12],
                4: [12],
                5: [12],
                6: [10],
                7: [8],
                8: [6],
                9: [4],
                10: [2],
            },
            "columns": {
                1: [3],
                2: [5],
                3: [7],
                4: [8],
                5: [8],
                6: [8],
                7: [8],
                8: [8],
                9: [8],
                10: [7],
                11: [5],
                12: [3],
            },
        },
        "color": "#FF0000"
    },
    "mario": {
        "name": "Super Mario",
        "size": {"row": 14, "column": 14},
        "rules": {
            "rows": {
                1: [4],
                2: [2, 2],
                3: [1, 1],
                4: [1, 5],
                5: [1, 8],
                6: [4, 1],
                7: [4, 1, 1, 1],
                8: [1, 2, 1, 1, 1],
                9: [1, 3, 1],
                10: [1, 1, 1, 1],
                11: [1, 4, 2],
                12: [2, 5],
                13: [3, 1],
                14: [5],
            },
            "columns": {
                1: [2],
                2: [2, 1],
                3: [3, 1],
                4: [1, 4, 2],
                5: [1, 5, 1],
                6: [1, 1, 1, 1],
                7: [1, 1, 1, 1],
                8: [1, 1, 2, 1],
                9: [1, 2, 2, 2, 1],
                10: [1, 2, 2, 1],
                11: [2, 2, 2, 1, 1],
                12: [4, 2],
                13: [5, 2],
                14: [1, 3],
            },
        },
        "color": "#E52521"
    },
    "hollow_knight": {
        "name": "Hollow Knight",
        "size": {"row": 19, "column": 20},
        "rules": {
            "rows": {
                1: [20],
                2: [3, 10, 3],
                3: [2, 2, 8, 2, 2],
                4: [2, 2, 8, 2, 2],
                5: [1, 2, 10, 2, 1],
                6: [1, 2, 10, 2, 1],
                7: [1, 3, 8, 3, 1],
                8: [2, 3, 4, 3, 2],
                9: [2, 5, 5, 2],
                10: [2, 14, 2],
                11: [3, 2, 4, 2, 3],
                12: [3, 1, 2, 1, 3],
                13: [3, 1, 2, 1, 3],
                14: [3, 1, 2, 1, 3],
                15: [4, 1, 4, 1, 4],
                16: [4, 10, 4],
                17: [5, 6, 5],
                18: [7, 7],
                19: [20],
            },
            "columns": {
                1: [19],
                2: [4, 12],
                3: [2, 3, 9],
                4: [1, 8, 5],
                5: [1, 2, 8, 3],
                6: [2, 2, 4, 2, 2],
                7: [7, 2, 1, 2],
                8: [7, 2, 2, 1],
                9: [8, 2, 3, 1],
                10: [8, 8, 1],
                11: [8, 8, 1],
                12: [8, 2, 3, 1],
                13: [7, 2, 2, 1],
                14: [7, 2, 1, 2],
                15: [2, 2, 4, 2, 2],
                16: [1, 2, 8, 3],
                17: [1, 8, 5],
                18: [2, 3, 9],
                19: [4, 12],
                20: [19],
            },
        },
        "color": "#4A4A8C"
    },
        "Toad": {
        "name": "Toad",
        "size": {"row": 20, "column": 20},
        "rules": {
            "rows": {
                1: [6],
                2: [4, 4],
                3: [5, 5],
                4: [6, 6],
                5: [6, 6],
                6: [6, 6],
                7: [5, 5],
                8: [3, 3],
                9: [1, 8, 1],
                10: [1, 1, 1, 1],
                11: [1, 1, 1, 1, 1, 1],
                12: [2, 1, 1, 1, 1, 2],
                13: [3, 3],
                14: [1, 2, 1],
                15: [1, 1],
                16: [10],
                17: [2, 2, 2, 2],
                18: [1, 3, 3, 1],
                19: [1, 3, 3, 1],
                20: [1, 4, 4, 1],
            },
            "columns": {
                1: [0],
                2: [0],
                3: [8],
                4: [5, 2, 2],
                5: [6, 1, 2],
                6: [6, 5, 2, 1],
                7: [6, 1, 2, 3],
                8: [6, 1, 5],
                9: [4, 1, 2, 5],
                10: [1, 1, 1, 1],
                11: [1, 1, 1, 1],
                12: [4, 1, 2, 5],
                13: [6, 1, 5],
                14: [6, 1, 2, 3],
                15: [6, 5, 2, 1],
                16: [6, 1, 2],
                17: [5, 2, 2],
                18: [8],
                19: [0],
                20: [0],
            }
        },
        "color": "#000000"
    },
}

def gerar_sequencias(n, blocos):
    if not blocos or blocos == [0]:
        return [[0] * n]
    
    k = len(blocos)
    total = sum(blocos)
    
    if total + k - 1 > n:
        return []
    
    sequencias = []
    
    def gerar(posicao, indice_bloco, sequencia):
        if indice_bloco == k:
            if len(sequencia) < n:
                sequencia.extend([0] * (n - len(sequencia)))
            sequencias.append(sequencia.copy())
            return
        
        bloco_atual = blocos[indice_bloco]
        
        if indice_bloco == k - 1:
            max_inicio = n - bloco_atual
        else:
            blocos_restantes = sum(blocos[indice_bloco+1:])
            espacos_necessarios = k - indice_bloco - 1
            max_inicio = n - (blocos_restantes + espacos_necessarios + bloco_atual)
        
        for inicio in range(posicao, max_inicio + 1):
            nova_seq = sequencia.copy()
            
            while len(nova_seq) < inicio:
                nova_seq.append(0)
            
            nova_seq.extend([1] * bloco_atual)
            
            if indice_bloco < k - 1:
                nova_seq.append(0)
                gerar(inicio + bloco_atual + 1, indice_bloco + 1, nova_seq)
            else:
                gerar(inicio + bloco_atual, indice_bloco + 1, nova_seq)
    
    gerar(0, 0, [])
    return sequencias

def resolver_nonogram(config):
    linhas = config['size']['row']
    colunas = config['size']['column']
    
    regras_linhas = config['rules']['rows']
    regras_colunas = config['rules']['columns']
    
    for i in range(1, linhas + 1):
        if i not in regras_linhas:
            regras_linhas[i] = [0]
    
    for j in range(1, colunas + 1):
        if j not in regras_colunas:
            regras_colunas[j] = [0]
    
    sequencias_linhas = []
    for i in range(1, linhas + 1):
        seq = gerar_sequencias(colunas, regras_linhas[i])
        if not seq:
            return None, None, None
        sequencias_linhas.append(seq)
    
    sequencias_colunas = []
    for j in range(1, colunas + 1):
        seq = gerar_sequencias(linhas, regras_colunas[j])
        if not seq:
            return None, None, None
        sequencias_colunas.append(seq)
    
    solver = Glucose4()
    
    var_celula = {}
    contador = 1
    for i in range(linhas):
        for j in range(colunas):
            var_celula[(i, j)] = contador
            contador += 1
    
    var_linha_seq = {}
    for i, seqs in enumerate(sequencias_linhas):
        var_linha_seq[i] = []
        for _ in seqs:
            var_linha_seq[i].append(contador)
            contador += 1
    
    var_coluna_seq = {}
    for j, seqs in enumerate(sequencias_colunas):
        var_coluna_seq[j] = []
        for _ in seqs:
            var_coluna_seq[j].append(contador)
            contador += 1
    
    for i, vars_seq in var_linha_seq.items():
        solver.add_clause(vars_seq.copy())
        
        for a in range(len(vars_seq)):
            for b in range(a+1, len(vars_seq)):
                solver.add_clause([-vars_seq[a], -vars_seq[b]])
        
        for var_seq, seq in zip(vars_seq, sequencias_linhas[i]):
            for j, valor in enumerate(seq):
                var_cel = var_celula[(i, j)]
                if valor == 1:
                    solver.add_clause([-var_seq, var_cel])
                else:
                    solver.add_clause([-var_seq, -var_cel])
    
    for j, vars_seq in var_coluna_seq.items():
        solver.add_clause(vars_seq.copy())
        
        for a in range(len(vars_seq)):
            for b in range(a+1, len(vars_seq)):
                solver.add_clause([-vars_seq[a], -vars_seq[b]])
        
        for var_seq, seq in zip(vars_seq, sequencias_colunas[j]):
            for i, valor in enumerate(seq):
                var_cel = var_celula[(i, j)]
                if valor == 1:
                    solver.add_clause([-var_seq, var_cel])
                else:
                    solver.add_clause([-var_seq, -var_cel])
    
    if solver.solve():
        modelo = solver.get_model()
        
        grade = [[0] * colunas for _ in range(linhas)]
        
        verdadeiras = set()
        for var in modelo:
            if var > 0:
                verdadeiras.add(var)
        
        for (i, j), var in var_celula.items():
            if var in verdadeiras:
                grade[i][j] = 1
        return grade, regras_linhas, regras_colunas
    else:
        return None, None, None

def exibir_grade_com_numeros(grade, regras_linhas, regras_colunas):
    linhas = len(grade)
    colunas = len(grade[0])
    
    max_blocos_linhas = max(len(regras_linhas[i]) for i in range(1, linhas + 1))
    max_blocos_colunas = max(len(regras_colunas[j]) for j in range(1, colunas + 1))
    
    for i in range(max_blocos_colunas):
        print("   " * max_blocos_linhas, end="")
        for j in range(1, colunas + 1):
            if i < len(regras_colunas[j]):
                print(f"{regras_colunas[j][i]:2} ", end="")
            else:
                print("   ", end="")
        print()
    
    for i in range(linhas):
        for k in range(max_blocos_linhas):
            if k < len(regras_linhas[i+1]):
                print(f"{regras_linhas[i+1][k]:2} ", end="")
            else:
                print("   ", end="")
        
        for j in range(colunas):
            if grade[i][j] == 1:
                print('██', end='')
            else:
                print('░░', end='')
        print()

def criar_janela_nonograma(grade, regras_linhas, regras_colunas, nome="Nonograma", color="#000000", tempo=0.0):
    janela = Tk()
    janela.title(f"Nonograma resolvido: {nome} (Tempo: {tempo:.2f}s)")
    
    linhas = len(grade)
    colunas = len(grade[0])
    
    if linhas * colunas > 200:
        tamanho_celula = 20
        tamanho_fonte = 8
    else:
        tamanho_celula = 30
        tamanho_fonte = 10
    
    margem = 40
    
    max_blocos_linhas = max(len(regras_linhas[i]) for i in range(1, linhas + 1))
    max_blocos_colunas = max(len(regras_colunas[j]) for j in range(1, colunas + 1))
    
    largura = margem * 2 + max_blocos_linhas * (tamanho_fonte * 3) + colunas * tamanho_celula
    altura = margem * 2 + max_blocos_colunas * (tamanho_fonte * 3) + linhas * tamanho_celula + 30
    canvas = Canvas(janela, width=largura, height=altura, bg='white')
    canvas.pack()
    
    for j in range(colunas):
        blocos = regras_colunas[j+1]
        x = margem + max_blocos_linhas * (tamanho_fonte * 3) + j * tamanho_celula + tamanho_celula//2
        for k, bloco in enumerate(blocos):
            y = margem + (max_blocos_colunas - len(blocos) + k) * (tamanho_fonte + 5)
            canvas.create_text(x, y, text=str(bloco), font=('Arial', tamanho_fonte))
    
    for i in range(linhas):
        blocos = regras_linhas[i+1]
        y = margem + max_blocos_colunas * (tamanho_fonte * 3) + i * tamanho_celula + tamanho_celula//2
        for k, bloco in enumerate(blocos):
            x = margem + (max_blocos_linhas - len(blocos) + k) * (tamanho_fonte + 5)
            canvas.create_text(x, y, text=str(bloco), font=('Arial', tamanho_fonte))
    
    for i in range(linhas):
        for j in range(colunas):
            x1 = margem + max_blocos_linhas * (tamanho_fonte * 3) + j * tamanho_celula
            y1 = margem + max_blocos_colunas * (tamanho_fonte * 3) + i * tamanho_celula
            x2 = x1 + tamanho_celula
            y2 = y1 + tamanho_celula
            
            if grade[i][j] == 1:
                canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='black')
    
    for i in range(linhas + 1):
        y = margem + max_blocos_colunas * (tamanho_fonte * 3) + i * tamanho_celula
        canvas.create_line(
            margem + max_blocos_linhas * (tamanho_fonte * 3), 
            y, 
            margem + max_blocos_linhas * (tamanho_fonte * 3) + colunas * tamanho_celula, 
            y, 
            width=2
        )
    
    for j in range(colunas + 1):
        x = margem + max_blocos_linhas * (tamanho_fonte * 3) + j * tamanho_celula
        canvas.create_line(
            x, 
            margem + max_blocos_colunas * (tamanho_fonte * 3), 
            x, 
            margem + max_blocos_colunas * (tamanho_fonte * 3) + linhas * tamanho_celula, 
            width=2
        )
    
    info_text = f"{nome} - {linhas}x{colunas} - Tempo de resolução: {tempo:.3f} segundos"
    canvas.create_text(largura//2, altura-15, text=info_text, font=('Arial', 10))
    
    janela.mainloop()

if __name__ == "__main__":
    print("="*60)
    print("RESOLUÇÃO DE NONOGRAMAS")
    print("="*60)
    
    resultados = []
    tempos = []
    
    print(f"Número de nonogramas para resolver: {len(SETTINGS)}")
    
    for chave, config in SETTINGS.items():
        nome = config['name']
        cor = config.get('color', '#000000')
        
        print(f"\n[{chave}] Resolvendo: {nome}")
        print(f"Tamanho: {config['size']['row']}x{config['size']['column']}")
        
        inicio = time.time()
        grade, regras_linhas, regras_colunas = resolver_nonogram(config)
        fim = time.time()
        
        tempo_resolucao = fim - inicio
        tempos.append((nome, tempo_resolucao))
        
        if grade:
            resultados.append((grade, regras_linhas, regras_colunas, nome, cor, tempo_resolucao))
            
            total_celulas = len(grade) * len(grade[0])
            celulas_pintadas = sum(sum(linha) for linha in grade)
            
            print(f"✓ Solução encontrada!")
            print(f"  Tempo de resolução: {tempo_resolucao:.3f} segundos")
            print(f"  Células pintadas: {celulas_pintadas}/{total_celulas} ({celulas_pintadas/total_celulas*100:.1f}%)")
        else:
            print(f"✗ Não foi possível resolver")
            print(f"  Tempo de resolução: {tempo_resolucao:.3f} segundos")
    
    print(f"\n{'='*60}")
    print(f"TOTAL: {len(resultados)} de {len(SETTINGS)} nonogramas resolvidos")
    
    if tempos:
        print("\nESTATÍSTICAS DE TEMPO:")
        print("-" * 40)
        
        tempos_sucesso = [t for n, t in tempos if any(r[3] == n for r in resultados)]
        tempos_falha = [t for n, t in tempos if not any(r[3] == n for r in resultados)]
        
        if tempos_sucesso:
            print(f"Tempo médio (sucesso): {sum(tempos_sucesso)/len(tempos_sucesso):.3f} segundos")
            print(f"Tempo máximo (sucesso): {max(tempos_sucesso):.3f} segundos")
            print(f"Tempo mínimo (sucesso): {min(tempos_sucesso):.3f} segundos")
        
        if tempos_falha:
            print(f"\nTempo médio (falha): {sum(tempos_falha)/len(tempos_falha):.3f} segundos")
        
        print(f"\nTempo total: {sum([t for _, t in tempos]):.3f} segundos")
    
    print(f"\n{'='*60}")
    
    if resultados:
        print(f"Abrindo {len(resultados)} janelas...")
        for grade, regras_linhas, regras_colunas, nome, cor, tempo_resolucao in resultados:
            criar_janela_nonograma(grade, regras_linhas, regras_colunas, nome, cor, tempo_resolucao)
    else:
        print("Nenhuma solução encontrada para abrir janelas.")
