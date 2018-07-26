import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import data

markdown_text = '''
Esta aplicación [Dash](https://dash.plot.ly/) se ha desarrollado como proyecto final de la 1ª Edición 
del Curso de Especialista [CIDAEN](http://www.cidaen.es/) de la [Universidad de Castilla-La Mancha](https://www.uclm.es/).
'''


def bar_graph(segment):
    return go.Bar(x=data.categ_by_segment(segment),
                  y=data.casos_by_segment(segment),
                  name=segment)

def salida_bar_graph(segment):
    return {'data': [bar_graph(seg) for seg in segment],
            'layout': go.Layout(
                title='Gráfico Barras',
                showlegend=True,
                xaxis={'title': 'Categoria'},
                yaxis={'title': 'Nº Casos'})
            }


def line_graph(segment):
    return go.Scatter(x=data.fecha_by_segment(segment),
                      y=data.label_by_segment(segment),
                      name=segment)

def salida_line_graph(segment):
    return {'data': [line_graph(seg) for seg in segment],
            'layout': go.Layout(
                title='Serie Temporal',
                xaxis=dict(
                    rangeslider=dict(visible=True),
                    type='date'))
            }


def box_graph(data, segment):
    return go.Box(y=data,
                  name=segment,
                  jitter=0.3,
                  pointpos=-1.8,
                  boxpoints='all')


def salida_box_graph(data, segment):
    return {
        'data': [box_graph(data, segment)],
        'layout': go.Layout(
            hovermode='closest',
            title='Box Plot')
    }


app = dash.Dash()


app.layout = html.Div([
    html.Div([
        html.H2("Visualización de Series Temporales")
    ], className='banner'),

    html.Div([
        dcc.Markdown(children=markdown_text)
    ], className='texto'),

    html.Div([
        html.Div([
            html.H4("Evolución temporal")
        ]),
        dcc.Graph(id='serie-temporal')
    ], className='info-serie-temporal'),

    html.Div([
        html.Div([
            html.H4("Análisis descriptivo")
        ]),

        html.Div([

            html.Div([
                html.H5("Diagrama de Cajas y Bigotes"),
                html.H6("Seleccione el segmento que desee analizar:"),
                html.Div([
                    dcc.Dropdown(
                        id='segmento_select',
                        options=[{'label': i, 'value': i} for i in data.segmento],
                        value='segmento1'
                    )
                ]),
                dcc.Graph(id='box-graphic')
            ], className='info-box-plot'),

            html.Div([
                html.H5("Distribución de categorias en función del segmento"),
                dcc.Graph(id='grafico-barras')
            ], className='info-barras')

        ], style={'columnCount': 2})
    ], className='analisis-descriptivo'),

], style={'padding': '0px 10px 15px 10px',
          'marginLeft': 'auto', 'marginRight': 'auto', "width": "900px",
          'boxShadow': '0px 0px 5px 5px rgba(204,204,204,0.4)'}
)


@app.callback(
    dash.dependencies.Output('box-graphic', 'figure'),
    [dash.dependencies.Input('segmento_select', 'value')])
def update_box_graph(segmento_select):
    view = data.label_by_segment(segmento_select)
    return salida_box_graph(view, segmento_select)


@app.callback(
    dash.dependencies.Output('grafico-barras', 'figure'),
    [dash.dependencies.Input('segmento_select', 'value')])
def update_bar_graph(segmento_select):
    return salida_bar_graph(data.segmento)



@app.callback(
    dash.dependencies.Output('serie-temporal', 'figure'),
    [dash.dependencies.Input('segmento_select', 'value')])
def update_line_graph(segmento_select):
    return salida_line_graph(data.segmento)


app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
