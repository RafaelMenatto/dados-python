import streamlit as st            # Importa o Streamlit (framework usado para criar o dashboard web)
import pandas as pd               # Importa o Pandas (biblioteca para manipular dados em tabelas/DataFrames)
import plotly.express as px       # Importa o Plotly Express (biblioteca para criar gráficos interativos)

# --- Configuração da Página ---
# Define o título da página, o ícone e o layout para ocupar a largura inteira.
st.set_page_config(               # Chama a função que configura a página do Streamlit
    page_title="Dashboard de Salários na Área de Dados",  # Título que aparece na aba do navegador
    page_icon="📊",                # Ícone/emoji exibido ao lado do título na aba
    layout="wide",                # Layout de largura total (aproveita toda a tela)
)

# --- Carregamento dos dados ---
df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")  # Baixa o CSV da internet e carrega em um DataFrame chamado 'df'

# --- Barra Lateral (Filtros) ---
st.sidebar.header("🔍 Filtros")   # Adiciona um cabeçalho "Filtros" na barra lateral do dashboard

# Filtro de Ano
anos_disponiveis = sorted(df['ano'].unique())            # Pega os anos únicos do DataFrame e ordena em uma lista
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis)  # Cria caixa de seleção múltipla de anos, já marcando todos por padrão

# Filtro de Senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())          # Lista os níveis de senioridade únicos e ordenados
senioridades_selecionadas = st.sidebar.multiselect("Senioridade", senioridades_disponiveis, default=senioridades_disponiveis)  # Caixa de seleção múltipla de senioridades (todos marcados)

# Filtro por Tipo de Contrato
contratos_disponiveis = sorted(df['contrato'].unique())                # Lista os tipos de contrato únicos e ordenados
contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis)  # Caixa de seleção múltipla de contratos (todos marcados)

# Filtro por Tamanho da Empresa
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())          # Lista os tamanhos de empresa únicos e ordenados
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)  # Caixa de seleção múltipla de tamanhos (todos marcados)

# --- Filtragem do DataFrame ---
# O dataframe principal é filtrado com base nas seleções feitas na barra lateral.
df_filtrado = df[                # Cria um novo DataFrame 'df_filtrado' apenas com as linhas que atendem a todos os filtros
    (df['ano'].isin(anos_selecionados)) &              # Mantém linhas cujo ano está na lista selecionada
    (df['senioridade'].isin(senioridades_selecionadas)) &  # E cuja senioridade está na lista selecionada
    (df['contrato'].isin(contratos_selecionados)) &    # E cujo tipo de contrato está na lista selecionada
    (df['tamanho_empresa'].isin(tamanhos_selecionados))    # E cujo tamanho da empresa está na lista selecionada
]

# --- Conteúdo Principal ---
st.title("🎲 Dashboard de Análise de Salários na Área de Dados")   # Título principal exibido no topo da página
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")  # Texto de introdução/descrição do dashboard

# --- Métricas Principais (KPIs) ---
st.subheader("Métricas gerais (Salário anual em USD)")   # Subtítulo da seção de métricas

if not df_filtrado.empty:                                # Se o DataFrame filtrado não estiver vazio (há dados para mostrar)
    salario_medio = df_filtrado['usd'].mean()            # Calcula a média da coluna 'usd' (salário médio anual)
    salario_maximo = df_filtrado['usd'].max()            # Obtém o maior salário da coluna 'usd'
    total_registros = df_filtrado.shape[0]               # Conta o número de linhas (registros) do DataFrame filtrado
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]  # Pega o cargo que mais aparece (moda) na coluna 'cargo'
else:                                                    # Se o DataFrame estiver vazio (nenhum dado)
    salario_medio, salario_mediano, salario_maximo, total_registros, cargo_mais_comum = 0, 0, 0, ""  # Define valores zerados para as métricas evitarem erro (obs: variável 'cargo_mais_frequente' não é definida aqui)

col1, col2, col3, col4 = st.columns(4)                   # Divide a largura da página em 4 colunas para exibir as métricas lado a lado
col1.metric("Salário médio", f"${salario_medio:,.0f}")   # Mostra na 1ª coluna o salário médio formatado com cifrão e milhar
col2.metric("Salário máximo", f"${salario_maximo:,.0f}") # Mostra na 2ª coluna o salário máximo formatado
col3.metric("Total de registros", f"{total_registros:,}")  # Mostra na 3ª coluna o total de registros com separador de milhar
col4.metric("Cargo mais frequente", cargo_mais_frequente)  # Mostra na 4ª coluna o cargo mais frequente

st.markdown("---")                                       # Insere uma linha divisória horizontal na página

# --- Análises Visuais com Plotly ---
st.subheader("Gráficos")                                 # Subtítulo da seção de gráficos

col_graf1, col_graf2 = st.columns(2)                     # Cria 2 colunas lado a lado para os dois primeiros gráficos

with col_graf1:                                          # Bloco que define o conteúdo da 1ª coluna
    if not df_filtrado.empty:                            # Só desenha o gráfico se houver dados
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()  # Agrupa por cargo, calcula a média salarial, pega os 10 maiores e ordena do menor para o maior
        grafico_cargos = px.bar(                         # Cria um gráfico de barras com o Plotly
            top_cargos,                                  # DataFrame de origem dos dados
            x='usd',                                     # Eixo X = salário médio (média em USD)
            y='cargo',                                   # Eixo Y = nome do cargo
            orientation='h',                             # Barras na horizontal
            title="Top 10 cargos por salário médio",     # Título do gráfico
            labels={'usd': 'Média salarial anual (USD)', 'cargo': ''}  # Renomeia os rótulos dos eixos
        )
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})  # Ajusta posição do título e ordena os cargos do maior para o menor salário
        st.plotly_chart(grafico_cargos, use_container_width=True)  # Exibe o gráfico interativo ocupando toda a largura da coluna
    else:                                                # Se não houver dados:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")  # Exibe um aviso na tela

with col_graf2:                                          # Bloco que define o conteúdo da 2ª coluna
    if not df_filtrado.empty:                            # Só desenha o gráfico se houver dados
        grafico_hist = px.histogram(                     # Cria um histograma (distribuição de frequência)
            df_filtrado,                                 # DataFrame de origem dos dados
            x='usd',                                     # Eixo X = valores de salário em USD
            nbins=30,                                    # Divide os dados em 30 intervalos (barras)
            title="Distribuição de salários anuais",     # Título do gráfico
            labels={'usd': 'Faixa salarial (USD)', 'count': ''}  # Renomeia os rótulos dos eixos
        )
        grafico_hist.update_layout(title_x=0.1)          # Ajusta a posição do título (um pouco para a direita)
        st.plotly_chart(grafico_hist, use_container_width=True)  # Exibe o histograma ocupando toda a largura da coluna
    else:                                                # Se não houver dados:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")  # Exibe um aviso na tela

col_graf3, col_graf4 = st.columns(2)                     # Cria mais 2 colunas lado a lado para os dois últimos gráficos

with col_graf3:                                          # Bloco que define o conteúdo da 3ª coluna
    if not df_filtrado.empty:                            # Só desenha o gráfico se houver dados
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()  # Conta quantas vezes cada tipo de trabalho aparece e transforma em DataFrame
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']  # Renomeia as colunas do DataFrame de contagem
        grafico_remoto = px.pie(                         # Cria um gráfico de pizza/rosca
            remoto_contagem,                             # DataFrame com os dados da contagem
            names='tipo_trabalho',                       # Coluna que define os rótulos das fatias (tipos de trabalho)
            values='quantidade',                         # Coluna que define o tamanho de cada fatia
            title='Proporção dos tipos de trabalho',     # Título do gráfico
            hole=0.5                                     # Tamanho do "buraco" central (0.5 = rosca)
        )
        grafico_remoto.update_traces(textinfo='percent+label')  # Mostra porcentagem e rótulo dentro de cada fatia
        grafico_remoto.update_layout(title_x=0.1)        # Ajusta a posição do título
        st.plotly_chart(grafico_remoto, use_container_width=True)  # Exibe o gráfico de rosca ocupando toda a coluna
    else:                                                # Se não houver dados:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")  # Exibe um aviso na tela

with col_graf4:                                          # Bloco que define o conteúdo da 4ª coluna
    if not df_filtrado.empty:                            # Só desenha o gráfico se houver dados
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']  # Filtra apenas as linhas onde o cargo é "Data Scientist"
        media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()  # Agrupa por país (código ISO) e calcula o salário médio de cada país
        grafico_paises = px.choropleth(media_ds_pais,    # Cria um mapa-múndi colorido (choropleth)
            locations='residencia_iso3',                 # Coluna com os códigos de país que o mapa usa para localizar
            color='usd',                                 # Coluna usada para colorir cada país (salário médio)
            color_continuous_scale='rdylgn',             # Escala de cores: vermelho (baixo) → amarelo → verde (alto)
            title='Salário médio de Cientista de Dados por país',  # Título do gráfico
            labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'})  # Renomeia os rótulos
        grafico_paises.update_layout(title_x=0.1)        # Ajusta a posição do título
        st.plotly_chart(grafico_paises, use_container_width=True)  # Exibe o mapa ocupando toda a coluna
    else:                                                # Se não houver dados:
        st.warning("Nenhum dado para exibir no gráfico de países.")   # Exibe um aviso na tela

# --- Tabela de Dados Detalhados ---
st.subheader("Dados Detalhados")                         # Subtítulo da seção da tabela
st.dataframe(df_filtrado)                                # Exibe o DataFrame filtrado em uma tabela interativa e rolável
