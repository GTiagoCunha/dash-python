from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_excel("Vendas.xlsx")

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append("Todas as Lojas")

app.layout = html.Div(children=[
    html.H1(children='FATURAMENTO DAS LOJAS'),
    html.H2(children='Grafico dos faturamentos de Todas as lojas'),
    html.Div(children='''
        Esse grafico mostra aquantidade de items vendidos.
    '''),

    dcc.Dropdown(opcoes, value='Todas as Lojas',  id='Lista_Lojas'),

    dcc.Graph(
        id='Grafico_quantidade_de_vendas',
        figure=fig
    )
])

@app.callback(
    Output('Grafico_quantidade_de_vendas', 'figure'),
    Input('Lista_Lojas', 'value')
)
def update_output(value):
    if value == "Todas as Lojas":
        fig=px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada =df.loc[df['ID Loja']== value,:]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
