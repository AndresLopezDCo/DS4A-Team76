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

from app import app
from lib import textos

###########################################################################
# crear contenido html
###########################################################################

page_3_layout = html.Section([
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
                        dcc.Link('MODEL', href='/page-2')
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
    ],className='header black-bg')
    #######################################################################
    # sidebar
    #######################################################################
    ,html.Section ([
        html.Section ([
            ###############################################################
            # contenido
            ###############################################################
            html.Div ([
                    #######################################################
                    # background
                    #######################################################
                    html.Img(src='assets/background2.jpg', className='background_img')
            ],className='centered')
            ,html.Div ([
                html.Br ()
                ,html.Div ([
                    'HEADER - CABECERA'
                ],className='col-12 centered titulo')
                ,html.Div ([
                    html.Img(src='assets/info/header.jpg', className='centered info ancho')
                ],className='col-12 centered')
                ,html.Div ([
                    html.Img(src='assets/info/logo.jpg', className='centered info')
                ],className='col-4 centered')
                ,html.Div ([
                    textos.informacion_01
                ],className='col-8 centered')
                ,html.Div ([
                    html.Img(src='assets/info/modulos.jpg', className='centered info')
                ],className='col-4 centered')
                ,html.Div ([
                    textos.informacion_02
                ],className='col-8 centered')
            ],className='row')
            ,html.Div ([
                html.Br ()
                ,html.Div ([
                    'KPI - INDICADORES'
                ],className='col-12 centered titulo')
                ,html.Div ([
                    html.Img(src='assets/info/kpi.jpg', className='centered info ancho')
                ],className='col-12 centered')
                ,html.Div ([
                    textos.informacion_13
                ],className='col-12 centered')
            ],className='row')
            ,html.Div ([
                html.Br ()
                ,html.Div ([
                    'SIDERBAR - MENU DE FILTROS'
                ],className='col-12 centered titulo')
                ,html.Div ([
                    html.Img(src='assets/info/siderbar.jpg', className='centered info ancho')
                ],className='col-12 centered')
                ,html.Div ([
                    html.Img(src='assets/info/f_mapa.jpg', className='centered info')
                ],className='col-4 centered')
                ,html.Div ([
                    textos.informacion_03
                ],className='col-8 centered')
                ,html.Div ([
                    html.Img(src='assets/info/f_variable.jpg', className='centered info')
                ],className='col-4 centered')
                ,html.Div ([
                    textos.informacion_04
                ],className='col-8 centered')
                ,html.Div ([
                    html.Img(src='assets/info/f_marcador.jpg', className='centered info')
                ],className='col-4 centered')
                ,html.Div ([
                    textos.informacion_05
                ],className='col-8 centered')
                ,html.Div ([
                    html.Img(src='assets/info/f_year.jpg', className='centered info')
                ],className='col-4 centered')
                ,html.Div ([
                    textos.informacion_06
                ],className='col-8 centered')
            ],className='row')
            ,html.Div ([
                html.Br ()
                ,html.Div ([
                    'CONTENT - CONTENIDO'
                ],className='col-12 centered titulo')
                ,html.Div ([
                    html.Img(src='assets/info/content.jpg', className='centered info ancho')
                ],className='col-12 centered')
                ,html.Div ([
                    html.Img(src='assets/info/mapa.jpg', className='centered info')
                ],className='col-4 centered')
                ,html.Div ([
                    textos.informacion_03
                ],className='col-8 centered')
                ,html.Div ([
                    html.Img(src='assets/info/efectividad.jpg', className='centered info')
                ],className='col-4 centered')
                ,html.Div ([
                    textos.informacion_04
                ],className='col-8 centered')
                ,html.Div ([
                    html.Img(src='assets/info/encuestadores.jpg', className='centered info')
                ],className='col-4 centered')
                ,html.Div ([
                    textos.informacion_05
                ],className='col-8 centered')
                ,html.Div ([
                    html.Img(src='assets/info/tabla.jpg', className='centered info')
                ],className='col-4 centered')
                ,html.Div ([
                    textos.informacion_06
                ],className='col-8 centered')
            ],className='row')
            ,html.Div ([
                html.Br ()
                ,html.Div ([
                    'DETAILS - DETALLES'
                ],className='col-12 centered titulo')
                ,html.Div ([
                    html.Img(src='assets/info/tarjetas.jpg', className='centered info ancho')
                ],className='col-12 centered')
                ,html.Div ([
                    textos.informacion_14
                ],className='col-12 centered')
            ],className='row')
            ,html.Br ()
        ],className='wrapper information')
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
                ],href='/page-3', className='go-top')
            ],className='text-center')
        ],className='site-footer2')
    ],id='main-content2 ')
],id='container')

