import pandas as pd
import pathlib
from dash import Dash,html, dcc, Input, Output, State, ClientsideFunction, callback
import plotly.express as px 
from app_support import make_graphs, load_data

app = Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
)

app.title ="DashBoard"
server = app.server # kina garya ? 

df= load_data()



effluent_graphs=["CCT_pH","CCT_BOD","CCT_COD","CCT_TSS","CCT_TColi","CCT_FColi","CCT_com_OG","CCT_com_N","CCT_FRC"]
figures=make_graphs(df,effluent_graphs)

# App layout

app.layout = html.Div(
    [
         dcc.Store(id="aggregate_data"),
        # empty Div to trigger javascript file for graph resizing
        html.Div(id="output-clientside"),
        html.H3("Guheswori Waste Water Treatment Plant",style={"margin-bottom": "50px",
                                                               "display": "flex" ,  
                                                               "justify-content": "center"}),
                 
                
        dcc.Tabs(id='tab_list', value='landing', children=[
            dcc.Tab(label='landing', value='landing'),
            dcc.Tab(label='Effluent Characteristics', value='effluent'),
        ]),
        html.Div(id='tab_output'),
        
        
       
           
    ]
)


#tabs callback
@callback(
    Output('tab_output', 'children'),
    Input('tab_list', 'value')
)

def print_tab(selected):
    if selected == "landing":
        return html.Div(
            [
                html.Div([
                    dcc.Dropdown(
                            id="parameter_select",
                            options=effluent_graphs,
                            multi=False,
                            value = effluent_graphs[1],
                            className="dcc_control",
                        ),
                    html.Div(
                        [ 
                         # "CCT_pH","CCT_BOD","CCT_COD","CCT_TSS","CCT_TColi","CCT_FColi","CCT_com_OG","CCT_com_N","CCT_FRC"
                            html.Div(
                                    [
                                        html.Div([
                                            html.H6(id="CCT_pH"),
                                            html.H6("%"),
                                            html.P("Compliance")],
                                                 className="row flex-display"                                                 
                                        ),
                                        html.P("pH")
                                    
                                  ],
                                    
                                    id="wells",
                                    className="mini_container two columns",
                                ),
                            html.Div(
                                    [html.H6(id="CCT_BOD"), html.P("No. of Wells")],
                                    id="wells",
                                    className="mini_container two columns",
                                ),
                            html.Div(
                                    [html.H6(id="well_text"), html.P("No. of Wells")],
                                    id="wells",
                                    className="mini_container two columns",
                                ),
                        ],
                        className="row container-display",
                    )
                ],
                         className='pretty_container six columns',
                         ),
                
                html.Div([
                    dcc.Graph(
                        id='landing_graph',
                    )
                ],
                         className='pretty_container six columns')
            ], 
            className="row flex-display",
        )
            
        
    
       
    if selected =="effluent":
        return html.Div([         
        # 9 ota effluent ko FG
        # figures ko acutal name nalekhera index gareko bhaye yei use garne hunthyo 
        html.Div(
    [
        html.Div(
            [dcc.Graph(figure = figures['CCT_pH'])],
            className ="pretty_container four columns",                    
        ),
        
        html.Div(
            [dcc.Graph(figure = figures["CCT_BOD"])],
            className ="pretty_container four columns",                    
        ),
        
        html.Div(
            [dcc.Graph(figure = figures["CCT_TSS"])],
            className ="pretty_container four columns",                    
        ),
        
                                    
    
    ],
    className="row flex-display",
),        
        html.Div(
            [
                html.Div(
                    [dcc.Graph(figure = figures["CCT_COD"])],
                    className ="pretty_container four columns",                    
                ),
                
                html.Div(
                    [dcc.Graph(figure = figures["CCT_TColi"] )],
                    className ="pretty_container four columns",                    
                ),
                
                html.Div(
                    [dcc.Graph(figure = figures["CCT_FColi"])],
                    className ="pretty_container four columns",                    
                ),
                
                                        
            
            ],
            className="row flex-display",
        ),   
        html.Div(
    [
        html.Div(
            [dcc.Graph(figure =figures["CCT_FRC"] )],
            className ="pretty_container four columns",                    
        ),
        
        html.Div(
            [dcc.Graph(figure = figures["CCT_com_OG"])],
            className ="pretty_container four columns",                    
        ),
        
        html.Div(
            [dcc.Graph(figure =figures["CCT_com_N"] )],
            className ="pretty_container four columns",                    
        ),             
    ],
    className="row flex-display",
)
        ])

#callback for landing page 
@callback(
    Output("landing_graph","figure"),
    [
        Input('parameter_select','value'),
    ]
)

def landing_graph_fig(selection):
    selected_fig=figures[selection]
    selected_fig.update_layout(height=450)
    
    return figures[selection]


# Main
app.config.suppress_callback_exceptions=True
app.run_server(debug=True)


