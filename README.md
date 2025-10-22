# 🧩 Projeto de Controle de Sistemas Dinâmicos

## 🎯 Objetivo

Este projeto tem como objetivo o projeto e análise de controladores PID aplicados a diferentes sistemas dinâmicos com e sem atraso de transporte, utilizando métodos clássicos de sintonia e projeto de controladores (LGR, Síntese Direta, entre outros).
A avaliação enfatiza a análise crítica dos resultados obtidos, considerando tanto o desempenho em regime transitório quanto em regime permanente, além de aspectos de robustez e rejeição a distúrbios.

As plantas analisadas são:

`Planta A:`  

![G(s)](https://latex.codecogs.com/svg.image?\color{white}G(s)%20=%20\frac{0.20e^{-5s}}{20s%20+%201})

`Planta B:`  

![G(s)](https://latex.codecogs.com/svg.image?\color{white}G(s)%20=%20=%20\frac{100e^{-7s}}{(14s%20+%201)(21s%20+%201)})

`Planta C:`  

![G(s)](https://latex.codecogs.com/svg.image?\color{white}G(s)%20=%20\frac{-8}{s^2%20+%201.5s%20-%201})


Cada uma é estudada sob diferentes critérios de projeto e métodos de controle, com ênfase em resposta temporal, resposta em frequência e análise de erro estacionário.

---

## ⚙️ Como clonar e executar

- Clonar o repositório:

```bash
git clone https://github.com/Regi2409/Trabalho-1---Sistemas-de-Controle.git
cd Trabalho-1---Sistemas-de-Controle
```

- Executar os códigos de simulação:

```bash
python src/nome-do-arquivo.py
```
---

## 👥 Autores
```
Pedro Otávio Gaspar de Freitas
Curso: Engenharia Mecatrônica — CEFET-MG Campus V (Divinópolis)
Contato: pedro.freitas@aluno.cefetmg.br
```

```
Regiane Aparecida Pereira
Curso: Engenharia Mecatrônica — CEFET-MG Campus V (Divinópolis)
Contato: regiane@aluno.cefetmg.br
```