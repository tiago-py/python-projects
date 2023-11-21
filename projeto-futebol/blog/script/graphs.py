import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

# Carregar os dados do arquivo CSV
goals_data = pd.read_csv('csvs/goals.csv')
stats_data = pd.read_csv('csvs/stats.csv')
results_data = pd.read_csv('csvs/results.csv')
cards_data = pd.read_csv('csvs/cards.csv')

# Função para criar um gráfico de gols por equipe
def graph_goals_per_club(data=goals_data):
    # Contar o número de gols marcados por cada equipe
    gols_por_equipe = data['clube'].value_counts().reset_index()
    gols_por_equipe.columns = ['Equipe', 'Gols']

    fig = px.bar(
        gols_por_equipe, 
        x="Equipe",
        y="Gols",
        labels={"value": "", "variable": ""},
        text="Gols",
        height=420
    )
    fig.update_layout(
        plot_bgcolor='#B8D8D8',
        paper_bgcolor='rgba(44, 146, 213, 0.06)',
        xaxis_title='',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5
        ),
        margin=dict(l=10, r=10, t=10, b=0)  # Define as margens do gráfico
    )
    return html.Div(
        className="graph-goals-per-club",
        children=[
            dcc.Graph(
                id="graph-goals-per-club",
                figure=fig
            )
        ]
    )

# Função para criar um gráfico de chutes por equipe
def graph_shoots_per_club(data=stats_data):
    # Contar o número de chutes por cada equipe
    chutes_por_equipe = data.groupby('clube')['chutes'].sum().reset_index()
    chutes_por_equipe.columns = ['Equipe', 'Chutes']

    # Ordenar o DataFrame em ordem decrescente pela coluna 'Chutes'
    chutes_por_equipe = chutes_por_equipe.sort_values(by='Chutes', ascending=False)

    fig = px.bar(
        chutes_por_equipe, 
        x="Equipe",
        y="Chutes",
        labels={"value": "", "variable": ""},
        text="Chutes",
        height=420
    )
    fig.update_layout(
        plot_bgcolor='#B8D8D8',
        paper_bgcolor='rgba(44, 146, 213, 0.06)',
        xaxis_title='',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5
        ),
        margin=dict(l=10, r=10, t=10, b=0)  # Define as margens do gráfico
    )
    return html.Div(
        className="graph-shoots_per_club",
        children=[
            dcc.Graph(
                id="graph-shoots-per-club",
                figure=fig
            )
        ]
    )

# Função para criar um gráfico de vitórias do Internacional
def graph_victories_inter(data=results_data):
    # Filtrar os dados para partidas em que o Internacional foi o mandante
    mandante_inter = data[data['mandante'] == 'Internacional']

    # Filtrar os dados para partidas em que o Internacional foi o visitante
    visitante_inter = data[data['visitante'] == 'Internacional']

    # Contar o número de vitórias do Internacional como mandante
    vitorias_mandante_inter = mandante_inter[mandante_inter['vencedor'] == 'Internacional'].shape[0]

    # Contar o número de vitórias do Internacional como visitante
    vitorias_visitante_inter = visitante_inter[visitante_inter['vencedor'] == 'Internacional'].shape[0]

    # Calcular a porcentagem de vitórias como mandante e visitante
    total_jogos_mandante = mandante_inter.shape[0]
    total_jogos_visitante = visitante_inter.shape[0]

    porcentagem_vitorias_mandante = (vitorias_mandante_inter / total_jogos_mandante) * 100
    porcentagem_vitorias_visitante = (vitorias_visitante_inter / total_jogos_visitante) * 100

    df_inter = pd.DataFrame({
        'local': ['Mandante', 'Visitante'],
        'vitórias': [vitorias_mandante_inter, vitorias_visitante_inter],
        'porcentagem_vitórias': [porcentagem_vitorias_mandante, porcentagem_vitorias_visitante]
    })

    fig = px.bar(
        df_inter, 
        x="local",
        y="vitórias",
        text="porcentagem_vitórias",  # Mostrar a porcentagem de vitórias como texto
        text_auto='.2s',
        labels={"value": "", "variable": ""},
        height=420
    )

    fig.update_layout(
        plot_bgcolor='#B8D8D8',
        paper_bgcolor='rgba(44, 146, 213, 0.06)',
        xaxis_title='',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5
        ),
        margin=dict(l=10, r=10, t=10, b=0)  # Define as margens do gráfico
    )

    return html.Div(
        className="graph-victories-inter",
        children=[
            dcc.Graph(
                id="graph-victories-inter",
                figure=fig
            )
        ]
    )

# Função para criar um gráfico de cartões por equipe
def graph_cards_per_team(data=cards_data):
    # Filtrar os dados para cartões amarelos e vermelhos
    cartoes_amarelos = data[data['cartao'] == 'Amarelo']
    cartoes_vermelhos = data[data['cartao'] == 'Vermelho']

    # Contar o número de cartões amarelos e vermelhos por equipe
    cartoes_amarelos_por_equipe = cartoes_amarelos['clube'].value_counts().reset_index()
    cartoes_amarelos_por_equipe.columns = ['Equipe', 'Cartões Amarelos']

    cartoes_vermelhos_por_equipe = cartoes_vermelhos['clube'].value_counts().reset_index()
    cartoes_vermelhos_por_equipe.columns = ['Equipe', 'Cartões Vermelhos']

    # Fazer o merge dos DataFrames e preencher com 0 caso haja valores faltantes
    cartoes_por_equipe = pd.merge(cartoes_amarelos_por_equipe, cartoes_vermelhos_por_equipe, on='Equipe', how='outer')
    cartoes_por_equipe.fillna(0, inplace=True)

    fig = px.bar(
        cartoes_por_equipe,
        x="Equipe",
        y=["Cartões Amarelos", "Cartões Vermelhos"],
        barmode="stack",  # Para empilhar as barras
        labels={"value": "", "Equipe": "Equipe"},
        height=420
    )

    fig.update_layout(
        plot_bgcolor='#B8D8D8',
        paper_bgcolor='rgba(44, 146, 213, 0.06)',
        xaxis_title='',
        yaxis_title='Quantidade de Cartões',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5
        ),
        margin=dict(l=10, r=10, t=10, b=0)  # Define as margens do gráfico
    )

    return html.Div(
        className="graph-cards-per-team",
        children=[
            dcc.Graph(
                id="graph-cards-per-team",
                figure=fig
            )
        ]
    )

# Função para criar um gráfico de melhores artilheiros
def graph_best_goal_scorers(data=goals_data):
    # Contar o número de gols marcados por cada jogador
    artilheiros = data['atleta'].value_counts().reset_index()
    artilheiros.columns = ['Atleta', 'Gols']
    artilheiros = artilheiros[artilheiros['Gols'] > 50]

    fig = px.bar(
        artilheiros,
        x="Atleta",
        y="Gols",
        labels={"value": "", "Atleta": "Atleta"},
        height=420
    )

    fig.update_layout(
        plot_bgcolor='#B8D8D8',
        paper_bgcolor='rgba(44, 146, 213, 0.06)',
        xaxis_title='',
        yaxis_title='Gols',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5
        ),
        margin=dict(l=10, r=10, t=10, b=0)  # Define as margens do gráfico
    )

    return html.Div(
        className="graph-goal-scorers",
        children=[
            dcc.Graph(
                id="graph-goal-scorers",
                figure=fig
            )
        ]
    )

# Função para criar um gráfico de resultados por equipe
def graph_results_per_team(time="Internacional"):
    # Filtrar os dados para partidas em que o time selecionado foi o mandante
    jogos_em_casa = results_data[results_data['mandante'] == time]

    # Contar o número de vitórias, empates e derrotas EM CASA
    vitorias_casa = jogos_em_casa[jogos_em_casa['vencedor'] == time].shape[0]
    empates_casa = jogos_em_casa[jogos_em_casa['vencedor'] == '-'].shape[0]
    derrotas_casa = jogos_em_casa[(jogos_em_casa['vencedor'] != time) & (jogos_em_casa['vencedor'] != '-')].shape[0]

    # Filtrar os dados para partidas em que o time selecionado foi o visitante
    jogos_fora = results_data[results_data['visitante'] == time]

    # Contar o número de vitórias, empates e derrotas FORA DE CASA
    vitorias_fora = jogos_fora[jogos_fora['vencedor'] == time].shape[0]
    empates_fora = jogos_fora[jogos_fora['vencedor'] == '-'].shape[0]
    derrotas_fora = jogos_fora[(jogos_fora['vencedor'] != time) & (jogos_fora['vencedor'] != '-')].shape[0]

    # Criar um dicionário com os resultados
    resultados = {
        'Local': ['Casa', 'Fora'],
        'Vitórias': [vitorias_casa, vitorias_fora],
        'Empates': [empates_casa, empates_fora],
        'Derrotas': [derrotas_casa, derrotas_fora]
    }

    # Criar um DataFrame com os resultados
    df_resultados = pd.DataFrame(resultados)

    fig = px.bar(
        df_resultados,
        x="Local",
        y=["Vitórias", "Empates", "Derrotas"],
        barmode="stack",  # Para empilhar as barras
        labels={"value": "", "Equipe": "Equipe"},
        height=420
    )

    fig.update_layout(
        plot_bgcolor='#B8D8D8',
        paper_bgcolor='rgba(44, 146, 213, 0.06)',
        xaxis_title='',
        yaxis_title='Quantidade de Cartões',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5
        ),
        margin=dict(l=10, r=10, t=10, b=0)  # Define as margens do gráfico
    )

    return html.Div(
        id="results-graph",
        className="graph-results-team",
        children=[
            dcc.Graph(
                id="graph-results-team",
                figure=fig
            )
        ]
    )

# Função para criar um gráfico de gols por equipe
def graph_goals_per_team(time="Internacional"):
    # Filtrar os dados para partidas em que o time selecionado foi o mandante
    jogos_mandantes = results_data[results_data['mandante'] == time]

    gols_mandante = jogos_mandantes['mandante_Placar'].sum()

    gols_sofridos_mandante = jogos_mandantes['visitante_Placar'].sum()

    # Filtrar os dados para partidas em que o time selecionado foi o visitante
    jogos_visitantes = results_data[results_data['visitante'] == time]

    gols_visitante = jogos_visitantes['visitante_Placar'].sum()

    gols_sofridos_visitante = jogos_visitantes['mandante_Placar'].sum()

    # Criar um dicionário com os resultados
    resultados = {
        'Local': ['Mandante', 'Visitante'],
        'Jogos': [jogos_mandantes.shape[0], jogos_visitantes.shape[0]],
        'Gols Marcados': [gols_mandante, gols_visitante],
        'Gols Sofridos': [gols_sofridos_mandante, gols_sofridos_visitante]
    }

    # Criar um DataFrame com os resultados
    df_resultados = pd.DataFrame(resultados)

    fig = px.bar(
        df_resultados,
        x="Local",
        y=["Gols Marcados", "Gols Sofridos"],
        barmode="group",  # Para colocar lado a lado
        labels={"value": "Gols", "Local": "Local"},
        height=420
    )

    fig.update_layout(
        plot_bgcolor='#B8D8D8',
        paper_bgcolor='rgba(44, 146, 213, 0.06)',
        xaxis_title='',
        yaxis_title='Quantidade de Gols',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5
        ),
        margin=dict(l=10, r=10, t=10, b=0)  # Define as margens do gráfico
    )

    return html.Div(
        id="goals-graph",
        className="graph-goals-per-team",
        children=[
            dcc.Graph(
                id="graph-goals-per-team",
                figure=fig
            )
        ]
    )

# Função para criar um gráfico de distribuição de gols por equipe
def goals(data=goals_data, team1=None, team2=None):
    # Se os valores dos dropdowns não forem fornecidos, use os valores padrão
    if team1 is None:
        team1 = "team-dropdown-01"
    if team2 is None:
        team2 = "team-dropdown-02"

    # Filtrar os dados para incluir apenas os gols feitos pelos dois times
    filtered_data = data[(data['clube'] == team1) | (data['clube'] == team2)]

    # Contar o número de gols marcados por cada equipe
    gols_equipe = filtered_data['clube'].value_counts().reset_index()
    gols_equipe.columns = ['Equipe', 'Gols']

    # O restante do código permanece inalterado
    # ...
    # Contar o número de gols marcados por cada equipe
    gols_equipe = data['clube'].value_counts().reset_index()
    gols_equipe.columns = ['Equipe', 'Gols']

    fig = px.scatter_matrix(
        gols_equipe, 
        names="Equipe",
        values="Gols",
        dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"], 
        color="species"

    )

    fig.update_layout(
        plot_bgcolor='#B8D8D8',
        paper_bgcolor='rgba(44, 146, 213, 0.06)',
        xaxis_title='',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.25,
            xanchor="center",
            x=0.5
        ),
        margin=dict(l=10, r=10, t=10, b=0)  # Define as margens do gráfico
    )

    return html.Div(
        className="goals",
        children=[
            dcc.Graph(
                id="goals",
                figure=fig
            )
        ]
    )
