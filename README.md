


## 📌 Sobre o Projeto

O objetivo deste dashboard é fornecer uma visão analítica e dinâmica sobre o panorama salarial, modalidades de trabalho e níveis de experiência dos profissionais de dados. 

Os dados são carregados dinamicamente a partir de um conjunto de dados hospedado no GitHub (`dados-imersao-final.csv`), permitindo que o usuário aplique filtros personalizados em tempo real e visualize KPIs e gráficos interativos.

---

## 🎯 Principais Funcionalidades

### 🎛️ Barra Lateral de Filtros Dinâmicos
Filtre todo o painel de acordo com parâmetros específicos:
- **Ano:** Seleção por anos específicos da base.
- **Senioridade:** Filtragem por nível de experiência (*Junior*, *Pleno*, *Senior*, etc.).
- **Tipo de Contrato:** *Tempo Integral*, *Contractor / Empreiteiro*, entre outros.
- **Tamanho da Empresa:** Pequena (*S*), Média (*M*) ou Grande (*L*).

### 📈 Indicadores Chave de Desempenho (KPIs)
Resumo em tempo real dos dados filtrados:
- 💵 **Salário Médio:** Média salarial anual em USD.
- 🚀 **Salário Máximo:** Maior salário encontrado na seleção atual.
- 📋 **Total de Registros:** Contagem total de linhas analisadas.
- 💼 **Cargo Mais Frequente:** Moda estatística da coluna de cargos.

---

## 📊 Visualizações Gráficas

O painel é composto por 4 gráficos interativos gerados com **Plotly Express**:

| Gráfico | Tipo | Descrição |
| :--- | :--- | :--- |
| **Top 10 Cargos** | Barras Horizontais | Exibe os 10 cargos com maior salário médio anual em USD. |
| **Distribuição Salarial** | Histograma | Exibe a frequência e concentração dos salários por faixa. |
| **Modalidade de Trabalho** | Pizza / Rosca | Mostra a proporção entre trabalho Presencial, Remoto e Híbrido. |
| **Mapa Global de Salários** | Coroplético (Múndi) | Distribuição geográfica do salário médio para o cargo de *Data Scientist* por país (códigos ISO3). |

---
O código exibe a tabela completa dos dados filtrados (st.dataframe), permitindo que o usuário explore as linhas individuais que compõem os gráficos acima.
<img width="1408" height="768" alt="Gemini_Generated_Image_wpcvgewpcvgewpcv" src="https://github.com/user-attachments/assets/ded14176-2cfe-4249-947f-28484ad6e4cf" />
## 💻 Estrutura do Projeto

```text
dados-python/
│
├── app.py                   # Script principal com a aplicação Streamlit
├── dados-imersao-final.csv  # Base de dados utilizada no projeto
├── requirements.txt         # Bibliotecas e dependências do projeto
└── README.md                # Documentação do repositório

---
