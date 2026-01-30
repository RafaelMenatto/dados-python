https://dados-python-ngrgtffqptdt8v6zqp9sbr.streamlit.app/

Este código cria um Dashboard Interativo utilizando a biblioteca Streamlit para analisar dados de salários na área de dados (Data Science, Data Analytics, Data Engineering, etc.).

Aqui está uma descrição detalhada da estrutura e funcionalidade do script app.py:



1. Bibliotecas e Configuração Inicial

Bibliotecas: O código importa streamlit (para a interface web), pandas (para manipulação de dados) e plotly.express (para gráficos interativos).

Configuração da Página: Define o título da aba do navegador, o ícone ("📊") e ajusta o layout para "wide" (tela cheia), permitindo melhor visualização dos gráficos.

2. Carregamento de Dados

O script carrega um arquivo CSV hospedado no GitHub (dados-imersao-final.csv) diretamente para um DataFrame do Pandas. Este conjunto de dados contém informações sobre salários, cargos, experiência, etc..

3. Barra Lateral de Filtros

Na barra lateral (st.sidebar), o usuário pode filtrar os dados dinamicamente. Os filtros disponíveis são baseados nos valores únicos encontrados no dataset:



Ano: Seleção de anos específicos.

Senioridade: Nível de experiência (ex: Junior, Senior).

Tipo de Contrato: Ex: Full-time, Contractor.

Tamanho da Empresa: Pequena, Média ou Grande.

O DataFrame principal (df) é então filtrado com base nessas escolhas, criando o df_filtrado, que alimenta todo o restante do dashboard.



4. Métricas Principais (KPIs)

No topo do painel principal, são exibidos quatro cartões de métricas (KPIs) calculados sobre os dados filtrados:



Salário Médio: A média da coluna usd.

Salário Máximo: O maior valor encontrado na coluna usd.

Total de Registros: Quantidade de linhas filtradas.

Cargo mais frequente: A moda estatística da coluna cargo.

O código inclui uma verificação (if not df_filtrado.empty) para evitar erros caso os filtros retornem um resultado vazio.



5. Visualizações Gráficas

O dashboard apresenta quatro gráficos divididos em duas linhas:



Gráfico de Barras (Top 10 Cargos): Mostra os 10 cargos com a maior média salarial anual em USD. As barras são orientadas horizontalmente.

Histograma (Distribuição Salarial): Exibe a frequência dos salários, permitindo ver em qual faixa salarial a maioria dos profissionais se concentra.

Gráfico de Pizza/Rosca (Trabalho Remoto): Mostra a proporção entre os diferentes tipos de modalidade de trabalho (Presencial, Remoto, Híbrido).

Mapa Coroplético (Múndi): Este gráfico é específico: ele filtra apenas o cargo de 'Data Scientist' e colore os países baseados na média salarial, usando códigos ISO3 (residencia_iso3) para geolocalização.

6. Dados Detalhados

Ao final da página, o código exibe a tabela completa dos dados filtrados (st.dataframe), permitindo que o usuário explore as linhas individuais que compõem os gráficos acima.
<img width="1408" height="768" alt="Gemini_Generated_Image_wpcvgewpcvgewpcv" src="https://github.com/user-attachments/assets/ded14176-2cfe-4249-947f-28484ad6e4cf" />

