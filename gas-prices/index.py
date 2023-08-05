import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash_bootstrap_templates import ThemeSwitchAIO


# ========= App ============== #
FONT_AWESOME = ["https://use.fontawesome.com/releases/v5.10.2/css/all.css"]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY, dbc_css])
app.scripts.config.serve_locally = True
server = app.server

# ========== Styles ============ #

template_theme1 = "flatly"
template_theme2 = "vapor"
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.VAPOR


# ===== Reading n cleaning File ====== #
df_main = pd.read_csv("data_gas.csv")

df_main['DATA INICIAL'] = pd.to_datetime(df_main['DATA INICIAL'])
df_main['DATA FINAL'] = pd.to_datetime(df_main['DATA FINAL'])

df_main['DATA MEDIA'] = ((df_main['DATA FINAL']-df_main['DATA INICIAL'])/2)+df_main['DATA INICIAL']

df_main = df_main.sort_values(by='DATA MEDIA', ascending = True)
df_main.rename(columns = {'DATA MEDIA' : 'DATA'}, inplace = True)
df_main.rename(columns = {'PREÇO MÉDIO REVENDA ' : 'PRECO REVENDA (R$/L)'}, inplace = True)

df_main["ANO"] = df_main["DATA"].apply(lambda x: str(x.year))
df_main = df_main[df_main.PRODUTO == 'GASOLINA COMUM']





df_main = df_main.reset_index()


df_main.drop(['UNIDADE DE MEDIDA','UNIDADE DE MEDIDA','COEF DE VARIAÇÃO DISTRIBUIÇÃO','NÚMERO DE POSTOS PESQUISADOS','DATA FINAL',
'DATA INICIAL','PREÇO MÁXIMO DISTRIBUIÇÃO','PREÇO MÍNIMO DISTRIBUIÇÃO','MARGEM MÉDIA REVENDA','PREÇO MÁXIMO REVENDA','PREÇO MÍNIMO REVENDA'
,'PRODUTO', 'PREÇO MÉDIO DISTRIBUIÇÃO' ], inplace = True, axis=1)

df_main.info()
df_store = df_main.to_dict()
# =========  Layout  =========== #
app.layout = dbc.Container(children=[
    #armazenando o dataset
    dcc.Store(id='dataset', data=df_store),
    dcc.Store(id='dataset_fixed', data=df_store),

    #layout
    #row 1 
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                           html.Legend("Gas Prices Analysis") 
                        ],sm=8),
                        dbc.Col([
                            html.I(className='fa fa-filer', style={'font-size':'300%'})
                        ],sm=4, align="center")
                    
                    ]),
                    dbc.Row([
                        dbc.Col([
                            ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2]),
                            html.Legend("Tiago Braga-Dev")
                        ],)
                    ],style={'margin-top':'10px'}),
                             
                ])
            ])
        ])
    ])
], fluid=True, style={'height': '100%'})


# ======== Callbacks ========== #


# Run server
if __name__ == '__main__':
    app.run_server(debug=True)
