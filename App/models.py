###########################################################################
# importar librerias generales de dash
###########################################################################

import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_bootstrap_components as dbc
import dash_table as dte
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate

###########################################################################
# referenciamos py externos
###########################################################################
from lib import filtros, textos , graficas, mapas , tablas
from app import app

###########################################################################
# crear contenido html
###########################################################################
page_2_layout = html.Section([
    #######################################################################
    # cabecera
    #######################################################################
    html.Header ([
        html.Div ([
            html.Div ([],className='fa fa-bars tooltips')
        ],className='sidebar-toggle-box')
        ,html.A ([
            html.B ([
                html.Img(src='assets/usuario.jpg', className='img-circle logo')
                ,'CNC'
                ,html.Span (' ECAR')
            ])
        ],href='',className='logo')
        ,html.Div ([
            html.Ul ([
                html.Li (
                    html.A ([
                        dcc.Link('DASHBOARD', href='/')
                    ],className='logout')
                )
            ],className='nav pull-right top-menu')
        ],className='top-menu')
        ,html.Div ([
            html.Ul ([
                html.Li (
                    html.A ([
                        dcc.Link('ACERCA TEAM76', href='/page-1')
                    ],className='logout')
                )
            ],className='nav pull-right top-menu')
        ],className='top-menu')
        ,html.Div ([
            html.Ul ([
                html.Li (
                    html.A ([
                        dcc.Link('INFORMACIÓN', href='/page-3')
                    ],className='logout')
                )
            ],className='nav pull-right top-menu')
        ],className='top-menu')
    ],className='header black-bg')
    #######################################################################
    # sidebar
    #######################################################################
    ,html.Aside ([
        html.Div ([
            html.Ul ([
                html.Li([
                    html.A ([
                        html.I(className='fa fa-th')
                        ,html.Span('MODELS')
                    ], href='', className='active')
                ], className='mt')
                ###########################################################
                # filtros
                ###########################################################
                ,filtros.filtro_03
                ,filtros.filtro_05   
            ],id='nav-accordion', className='sidebar-menu')
        ],id='sidebar', className='nav-collapse ')
    ])
    ,html.Section ([
        html.Section ([
            ###############################################################
            # contenido
            ###############################################################
            html.Div ([
                html.Div ([
                    html.Div ([
                        html.H3('IMPORTANCIA DE LAS COVARIABLES')
                    ],className='border-head')
                    #######################################################
                    # 'IMPORTANCIA DE LAS COVARIABLES'
                    #######################################################
                    ,graficas.grafica_04
                ],className='col-md-6 main-chart')
                ,html.Div ([
                    html.Div ([
                        html.H3('EFECTIVIDAD vs. TIEMPOS POR CLUSTER')
                    ],className='border-head')
                    #######################################################
                    # 'EFECTIVIDAD vs. TIEMPOS POR CLUSTER'
                    #######################################################
                    ,graficas.grafica_05
                ],className='col-md-6 main-chart')
            ],className='row')
            ,html.Div ([
                html.Div ([
                    html.Div ([
                        html.H3('RADAR DE EDUCACIÓN FORMAL')
                    ],className='border-head')
                    #######################################################
                    # 'RADAR DE EDUCACIÓN FORMAL'
                    #######################################################
                    ,graficas.grafica_06
                ],className='col-md-6 main-chart')
                ,html.Div ([
                    html.Div ([
                        html.H3('BOXPLOT DE EFECTIVIDAD POR CLUSTER')
                    ],className='border-head')
                    #######################################################
                    # BOXPLOT DE EFECTIVIDAD POR CLUSTER
                    #######################################################
                    ,graficas.grafica_07
                ],className='col-md-6 main-chart')
            ],className='row')
        ],className='wrapper')
        ###################################################################
        # pie de pagina
        ###################################################################
        ,html.Footer ([
            html.Div ([
                html.P ([
                    'Copyright 2020'
                    ,html.Strong(' CNC ')
                    ,'Todos los derechos reservados'
                ])
                ,html.A ([
                    html.I ([
                    ],className='fa fa-angle-up')
                ],href='index.py#', className='go-top')
            ],className='text-center')
        ],className='site-footer')
    ],id='main-content')
],id='container')