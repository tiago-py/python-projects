import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from graphs import (graph_goals_per_club, graph_shoots_per_club, graph_victories_inter, 
                    graph_cards_per_team, graph_best_goal_scorers, graph_results_per_team,
                    graph_goals_per_team, goals)

template_theme1 = "spacelab"
template_theme2 = "darkly"
url_theme1 = dbc.themes.SPACELAB
url_theme2 = dbc.themes.DARKLY
tab_card = {'height': '100%'}
goals_data = pd.read_csv('csvs/goals.csv')
stats_data = pd.read_csv('csvs/stats.csv')
results_data = pd.read_csv('csvs/results.csv')
cards_data = pd.read_csv('csvs/cards.csv')
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
FONT_AWESOME = ["https://use.fontawesome.com/releases/v5.10.2/css/all.css"]

# Inicializando o aplicativo Dash
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = dbc.Container(children=[
    # LAYOUT
    # ROW
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.Legend("Análise Histórica Futebol")
                        ], sm=8),
                        dbc.Col([
                            html.I(className='fa fa-futbol', style={'font-size': '300%'})
                        ], sm=4, align="center")
                    ]),
                    dbc.Row([
                        dbc.Col([
                            ThemeSwitchAIO(aio_id='theme', themes=[
                                url_theme1, url_theme2]),
                        ])
                    ], style={'margin-top': '10px'}),
                    dbc.Row([
                        dbc.Col(
                            dbc.Button(
                                ["Visite  ", html.I(className="fab fa-github",  style={'font-size': '100%'})],
                                href="https://github.com/tiago-py", target="_blank",
                                className="m-1",
                            ),
                        )
                    ], style={'margin-top': '10px'}),
                    
                ])
            ], style=tab_card)
        ], sm=4, lg=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H6('Gols por time'),
                            goals(),
                        ])
                    ], style={'margin-top': '10px'})
                ]),
            ], style=tab_card)
        ]),
    dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H6('Chutes por Clube'),
                            graph_shoots_per_club(),
                        ], sm=6)
                    ]),     
                ])
            ], style=tab_card)
        ], sm=20, lg=10)
    ], className='g-2 my-auto'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
        dbc.CardBody([
            dbc.Row([
            dbc.Col([
                html.H6('Vitórias por Time'),
                dcc.Dropdown(
                    id='team-dropdown',
                    options=[{'label': time, 'value': time} for time in sorted(results_data['mandante'].unique())],
                    value=results_data['mandante'].unique()[0],  # Valor inicial do dropdown
                ),
                
                graph_victories_inter()
            ], sm=12, md=6),
            dbc.Col([
                html.H6('Cartões por time'),
                graph_cards_per_team(),
            ], sm=12, md=6)
    ], style={'column-gap': '0px'}),
        ]),
    ], style=tab_card),   
    
    ],style={'margin-top':'10px'}),
    ]),
    # ROW 2
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H3('Maiores Artilheiros'),
                    dbc.Row([
                        dbc.Col([
                            graph_best_goal_scorers()
                        ], sm=10),
                    ]),
                ])
            ], style=tab_card)
        ], sm=12, md=6, lg=5),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6('Resultados de cada time'),
                    dcc.Dropdown(
                        id='team-dropdown2',
                        options=[{'label': time, 'value': time} for time in sorted(results_data['mandante'].unique())],
                        value=results_data['mandante'].unique()[0],  # Valor inicial do dropdown
                    ),
                ]),
                dbc.Col([
                    graph_results_per_team()
                ], style=tab_card)
            ])
        ], sm=12, md=6, lg=4),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            graph_goals_per_team(),
                        ])
                    ], style=tab_card)
                ])
            ], justify='center', style={'padding-bottom': '7px', 'height': '50%'}),
        ], sm=12, lg=3, style={'height': '100%'})
    ], className='g-2 my-auto'),
], fluid=True, style={'height': '100%'})

# Callback para atualizar o gráfico de vitórias com base no time selecionado
@app.callback(
    Output('graph-victories-inter', 'figure'),
    [Input('team-dropdown', 'value')]
)
def update_victories_graph(selected_team):
    # Filtrar os dados para partidas em que o time selecionado foi o mandante
    mandante_selected_team = results_data[results_data['mandante'] == selected_team]

    # Filtrar os dados para partidas em que o time selecionado foi o visitante
    visitante_selected_team = results_data[results_data['visitante'] == selected_team]

    # Contar o número de vitórias do time selecionado como mandante
    vitorias_mandante_selected_team = mandante_selected_team[mandante_selected_team['vencedor'] == selected_team].shape[0]

    # Contar o número de vitórias do time selecionado como visitante
    vitorias_visitante_selected_team = visitante_selected_team[visitante_selected_team['vencedor'] == selected_team].shape[0]

    # Calcular a porcentagem de vitórias como mandante e visitante
    total_jogos_mandante = mandante_selected_team.shape[0]
    total_jogos_visitante = visitante_selected_team.shape[0]

    porcentagem_vitorias_mandante = (vitorias_mandante_selected_team / total_jogos_mandante) * 100
    porcentagem_vitorias_visitante = (vitorias_visitante_selected_team / total_jogos_visitante) * 100

    df_inter = pd.DataFrame({
        'local': ['Mandante', 'Visitante'],
        'vitórias': [vitorias_mandante_selected_team, vitorias_visitante_selected_team],
        'porcentagem_vitórias': [porcentagem_vitorias_mandante, porcentagem_vitorias_visitante]
    })

    fig = px.bar(
        df_inter, 
        x="local",
        y="vitórias",
        text="porcentagem_vitórias",  # Mostrar a porcentagem de vitórias como texto
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
        margin=dict(l=10, r=10, t=10, b=0),  # Define as margens do gráfico
    )

    return fig

# Callback para atualizar o gráfico de resultados e de gols quando um novo time for selecionado
@app.callback(
    [Output('results-graph', 'children'),
     Output('goals-graph', 'children')],
    [Input('team-dropdown2', 'value')]
)
def update_graphs(selected_team):
    graph_results = graph_results_per_team(selected_team)
    graph_goals = graph_goals_per_team(selected_team)
    graph_goals02 = goals(selected_team)
    graph_goals03 = goals(selected_team)
    return graph_results, graph_goals, graph_goals02, graph_goals03

# Executar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
