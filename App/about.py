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

page_1_layout = html.Section([
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
                        dcc.Link('INFORMACIÓN', href='/page-3')
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
                    html.Img(src='assets/background.jpg', className='background_img')
            ],className='centered')
            ,html.Div ([
                html.Div (className='col-md-1')
                ###########################################################
                # Andres
                ##########################################################
                ,html.Div ([
                    html.Img(src='assets/andres.jpg', className='team_img grayscale')
                    ,html.H3('Andres Lopez', className='centered')
                    ,html.P ([
                        'Engineer'
                    ],className='opacity')
                    ,textos.about_01
                    ,html.Div([
                        html.A ([
                            html.I(className='fa fa-envelope')
                            ,html.Span('CONTACT')
                        ], href='mailto:andresap.lopez@gmail.com', className='contact')
                    ], className='centered')
                ],className='col-md-2 about')
                ###########################################################
                # Angelica
                ##########################################################
                ,html.Div ([
                    html.Img(src='assets/angelica.jpg', className='team_img grayscale')
                    ,html.H3('Angelica Castillo', className='centered')
                    ,html.P ([
                        'Statistician'
                    ],className='opacity')
                    ,textos.about_02
                    ,html.Div([
                        html.A ([
                            html.I(className='fa fa-envelope')
                            ,html.Span('CONTACT')
                        ], href='mailto:macastilloh@unal.edu.co', className='contact')
                    ], className='centered')
                ],className='col-md-2 about')
                ###########################################################
                # Yesica
                ##########################################################
                ,html.Div ([
                    html.Img(src='assets/yesica.jpg', className='team_img grayscale')
                    ,html.H3('Yesica Salas', className='centered')
                    ,html.P ([
                        'Mathematician'
                    ],className='opacity')
                    ,textos.about_03
                    ,html.Div([
                        html.A ([
                            html.I(className='fa fa-envelope')
                            ,html.Span('CONTACT')
                        ], href='mailto:yasalasc@unal.edu.co', className='contact')
                    ], className='centered')
                ],className='col-md-2 about')
                ###########################################################
                # Mildreck
                ##########################################################
                ,html.Div ([
                    html.Img(src='assets/mildreck.jpg', className='team_img grayscale')
                    ,html.H3('Mildreck Cubillos', className='centered')
                    ,html.P ([
                        'Economist'
                    ],className='opacity')
                    ,textos.about_04
                    ,html.Div([
                        html.A ([
                            html.I(className='fa fa-envelope')
                            ,html.Span('CONTACT')
                        ], href='mailto:mildreck.cubillos@hotmail.com', className='contact')
                    ], className='centered')
                ],className='col-md-2 about')
                ###########################################################
                # Camilo
                ##########################################################
                ,html.Div ([
                    html.Img(src='assets/camilo.jpg', className='team_img grayscale')
                    ,html.H3('Camilo Amezquita', className='centered')
                    ,html.P ([
                        'Engineer'
                    ],className='opacity')
                    ,textos.about_05
                    ,html.Div([
                        html.A ([
                            html.I(className='fa fa-envelope')
                            ,html.Span('CONTACT')
                        ], href='mailto:johan.camilo.amezquita@outlook.com', className='contact')
                    ], className='centered')
                ],className='col-md-2 about')
                ,html.Div (className='col-md-1')
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
        ],className='site-footer2')
    ],id='main-content2')
],id='container')
