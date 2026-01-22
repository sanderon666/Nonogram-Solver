# Resolvedor de Nonogramas com SAT Solver

Este projeto implementa um **resolvedor automático de Nonogramas (Picross)** utilizando **Programação Booleana (SAT)** por meio da biblioteca **PySAT (Glucose4)**, com visualização gráfica feita em **Tkinter**.

O sistema gera e resolve diferentes nonogramas a partir de regras de linhas e colunas, exibindo o resultado tanto no terminal quanto em janelas gráficas interativas.

---

## Funcionalidades

- ✔️ Resolução automática de Nonogramas usando SAT Solver  
- ✔️ Suporte a múltiplos puzzles com tamanhos variados  
- ✔️ Visualização gráfica com interface Tkinter  
- ✔️ Exibição das regras de linhas e colunas  
- ✔️ Medição de tempo de resolução  
- ✔️ Estatísticas de desempenho  
- ✔️ Impressão da solução no terminal em formato visual  

---

## Nonogramas Disponíveis

Atualmente, o projeto inclui os seguintes puzzles:

- Creeper (Minecraft)
- Coração
- Super Mario
- Hollow Knight
- Toad (cujo foi uma adição póstuma da apresentação do trabalho)

Cada nonograma possui:
- Tamanho personalizado (linhas × colunas)
- Regras específicas de linhas e colunas
- Cor própria para exibição gráfica

---

## Tecnologias Utilizadas

- **Python 3**
- **PySAT** (`Glucose4`)
- **Tkinter** (interface gráfica)
- **Lógica Proposicional / SAT**

---

## Dependências

Antes de executar o projeto, instale as dependências:

```bash
pip install python-sat[pblib,aiger]
```
Como Executar
Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
Execute o programa:
```bash
python trabalhodelogica.py
```

# Contexto Acadêmico

Este projeto foi desenvolvido com fins acadêmicos, envolvendo conceitos de:

Lógica Matemática

Satisfatibilidade Booleana (SAT)

Modelagem de problemas com restrições

Interface gráfica em Python

# Autor

Desenvolvido por Alecsander Ribeiro
Projeto acadêmico – Lógica para Computação

E um obrigado a meus monitores e professor da disciplina.

# Licença
Este projeto é de uso educacional.
Sinta-se à vontade para estudar, modificar e melhorar o código.
