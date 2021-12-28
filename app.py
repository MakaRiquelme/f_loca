import os
import json
import base64

from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

#import pubchempy as pcp
#from dash_bio_utils.chem_structure_reader import read_structure
#import dash_bio

import pandas as pd
import io
import dash_table

from layout_helper import run_standalone_app


DATAPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


def header_colors():
    return {
        'bg_color': '#015BB0',
        'font_color': '#FFFFFF',
        'light_logo': True
    }


def layout():
    return html.Div(
        id='mol2d-body',
        className='app-body',
        children=[
            html.Div(
                id='mol2d-control-tabs',
                className='control-tabs',
                children=[
                    dcc.Tabs(id='mol2d-tabs', value='what-is', children=[
                        dcc.Tab(
                            label='Load Data',
                            value='what-is',
#Upload Locations Data
                            children=html.Div(className='control-tab', children=[
                                html.Div(className='fullwidth-app-controls-name',
                                                 children='Locations'),
                                html.Div([
                                    dcc.Upload(
                                        id='upload-data-locations',
                                        children=html.Div([
                                            'Drag and Drop or ',
                                            html.A('Select Files')
                                        ]),
                                        style={
                                            'width': '100%',
                                            'height': '60px',
                                            'lineHeight': '60px',
                                            'borderWidth': '1px',
                                            'borderStyle': 'dashed',
                                            'borderRadius': '5px',
                                            'textAlign': 'center',
                                            'margin': '10px'
                                        },
                                        # Allow multiple files to be uploaded
                                        multiple=True
                                    ),
                                    #html.Div(id='output-data-upload-locations'),
                                ]),
#Upload Candidate Stations Data
                                html.Div(className='fullwidth-app-controls-name',
                                                 children='Stations'),
                                html.Div([
                                    dcc.Upload(
                                        id='upload-data-stations',
                                        children=html.Div([
                                            'Drag and Drop or ',
                                            html.A('Select Files')
                                        ]),
                                        style={
                                            'width': '100%',
                                            'height': '60px',
                                            'lineHeight': '60px',
                                            'borderWidth': '1px',
                                            'borderStyle': 'dashed',
                                            'borderRadius': '5px',
                                            'textAlign': 'center',
                                            'margin': '10px'
                                        },
                                        # Allow multiple files to be uploaded
                                        multiple=True
                                    ),
                                    html.Div(id='output-data-upload-stations'),
                                ]),
#Upload Lanes Data
                                html.Div(className='fullwidth-app-controls-name',
                                                 children='Lanes'),
                                html.Div([
                                    dcc.Upload(
                                        id='upload-data-lanes',
                                        children=html.Div([
                                            'Drag and Drop or ',
                                            html.A('Select Files')
                                        ]),
                                        style={
                                            'width': '100%',
                                            'height': '60px',
                                            'lineHeight': '60px',
                                            'borderWidth': '1px',
                                            'borderStyle': 'dashed',
                                            'borderRadius': '5px',
                                            'textAlign': 'center',
                                            'margin': '10px'
                                        },
                                        # Allow multiple files to be uploaded
                                        multiple=True
                                    ),
                                    html.Div(id='output-data-upload-lanes'),
                                ]),
#Upload Demand Data
                                html.Div(className='fullwidth-app-controls-name',
                                                 children='Demand'),
                                html.Div([
                                    dcc.Upload(
                                        id='upload-data-demand',
                                        children=html.Div([
                                            'Drag and Drop or ',
                                            html.A('Select Files')
                                        ]),
                                        style={
                                            'width': '100%',
                                            'height': '60px',
                                            'lineHeight': '60px',
                                            'borderWidth': '1px',
                                            'borderStyle': 'dashed',
                                            'borderRadius': '5px',
                                            'textAlign': 'center',
                                            'margin': '10px'
                                        },
                                        # Allow multiple files to be uploaded
                                        multiple=True
                                    ),
                                    html.Div(id='output-data-upload-demand'),
                                ]),
                                html.A(
                                    html.A(
                                        "Download sample",
                                        id="mol3d-download-sample-data",
                                        className='control-download'
                                    ),
                                    # html.A('Download Template'),
                                    
                                    href=os.path.join('data', 'data_loc_template.csv'),
                                    download='data_loc_template.csv'
                                ),
                            ]
                            )
                        ),
                        
                        dcc.Tab(
                            label='View',
                            children=html.Div(className='control-tab', children=[
                                html.Div(
                                    title='Search for a molecule to view',
                                    className='app-controls-block',
                                    children=[
                                        html.Div(className='fullwidth-app-controls-name',
                                                 children='Search for molecule by name'),
                                       
                                        # dcc.Input(
                                        #     id='mol2d-search',
                                        #     placeholder='molecule name',
                                        #     type='text',
                                        #     value='buckminsterfullerene',
                                        #     n_submit=1
                                        # )
                                    ]
                                ),
                                # html.Div(
                                #     title='Change the bond length multiplier',
                                #     className='app-controls-block',
                                #     children=[
                                #         html.Div(className='app-controls-name',
                                #                  children='Bond length multiplier'),
                                #         dcc.Slider(
                                #             id='mol2d-bond-length',
                                #             min=1,
                                #             max=100,
                                #             value=1
                                #         ),
                                #         html.Div(
                                #             className='app-controls-desc',
                                #             children='Increase bond lengths linearly from their ' +
                                #             'values at equilibrium. This visualization will be ' +
                                #             'reminiscent of chemical bond stretching.'
                                #         )
                                #     ]
                                # ),
                                # html.Div(
                                #     id='mol2d-search-results-wrapper', children=[
                                #         dcc.Dropdown(id='mol2d-search-results')
                                #     ]
                                # ),
                                # html.Hr(),
                                # html.Div(id='error-wrapper'),
                                # html.Div(id='mol2d-sel-atoms-output'),
                            ])
                        )
                    ])
                ]
            ),
            # html.Div(id='mol2d-container', children=[
            #     dash_bio.Molecule2dViewer(
            #         id='mol2d',
            #         height=700,
            #         width=700
            #     )
            # ]),
            # dcc.Store(id='mol2d-search-results-store'),
            # dcc.Store(id='mol2d-compound-options-store')
            html.Div(id='output-data-upload-locations'),
        ]
    )


def callbacks(_app):
##################################################################################################    
#Locations
##################################################################################################  
    def parse_contents_locations(contents, filename, date):
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                # Assume that the user uploaded a CSV file
                df = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')))
            elif 'xls' in filename:
                # Assume that the user uploaded an excel file
                df = pd.read_excel(io.BytesIO(decoded))
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])

        return html.Div([
            html.H5(filename),
            #html.H6(datetime.datetime.fromtimestamp(date)),

            dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df.columns]
            ),

            html.Hr(),  # horizontal line

            # For debugging, display the raw contents provided by the web browser
            # html.Div('Raw Content'),
            # html.Pre(contents[0:200] + '...', style={
            #     'whiteSpace': 'pre-wrap',
            #     'wordBreak': 'break-all'
            # })
        ])

    @_app.callback(Output('output-data-upload-locations', 'children'),
                Input('upload-data-locations', 'contents'),
                State('upload-data-locations', 'filename'),
                State('upload-data-locations', 'last_modified'))
    
    def update_output(list_of_contents, list_of_names, list_of_dates):
        if list_of_contents is not None:
            children = [
                parse_contents_locations(c, n, d) for c, n, d in
                zip(list_of_contents, list_of_names, list_of_dates)]
            return children

##################################################################################################    
#Stations
##################################################################################################  
    def parse_contents_stations(contents, filename, date):
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                # Assume that the user uploaded a CSV file
                df = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')))
            elif 'xls' in filename:
                # Assume that the user uploaded an excel file
                df = pd.read_excel(io.BytesIO(decoded))
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])

        return html.Div([
            html.H5(filename),
            #html.H6(datetime.datetime.fromtimestamp(date)),

            dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df.columns]
            ),

            html.Hr(),  # horizontal line

            # For debugging, display the raw contents provided by the web browser
            # html.Div('Raw Content'),
            # html.Pre(contents[0:200] + '...', style={
            #     'whiteSpace': 'pre-wrap',
            #     'wordBreak': 'break-all'
            # })
        ])

    @_app.callback(Output('output-data-upload-stations', 'children'),
                Input('upload-data-stations', 'contents'),
                State('upload-data-stations', 'filename'),
                State('upload-data-stations', 'last_modified'))
    
    def update_output(list_of_contents, list_of_names, list_of_dates):
        if list_of_contents is not None:
            children = [
                parse_contents_stations(c, n, d) for c, n, d in
                zip(list_of_contents, list_of_names, list_of_dates)]
            return children

##################################################################################################    
#Lanes
##################################################################################################  
    def parse_contents_lanes(contents, filename, date):
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                # Assume that the user uploaded a CSV file
                df = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')))
            elif 'xls' in filename:
                # Assume that the user uploaded an excel file
                df = pd.read_excel(io.BytesIO(decoded))
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])

        return html.Div([
            html.H5(filename),
            #html.H6(datetime.datetime.fromtimestamp(date)),

            dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df.columns]
            ),

            html.Hr(),  # horizontal line

            # For debugging, display the raw contents provided by the web browser
            # html.Div('Raw Content'),
            # html.Pre(contents[0:200] + '...', style={
            #     'whiteSpace': 'pre-wrap',
            #     'wordBreak': 'break-all'
            # })
        ])

    @_app.callback(Output('output-data-upload-lanes', 'children'),
                Input('upload-data-lanes', 'contents'),
                State('upload-data-lanes', 'filename'),
                State('upload-data-lanes', 'last_modified'))
    
    def update_output(list_of_contents, list_of_names, list_of_dates):
        if list_of_contents is not None:
            children = [
                parse_contents_lanes(c, n, d) for c, n, d in
                zip(list_of_contents, list_of_names, list_of_dates)]
            return children

##################################################################################################    
#Demand
##################################################################################################  
    def parse_contents_demand(contents, filename, date):
        content_type, content_string = contents.split(',')

        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                # Assume that the user uploaded a CSV file
                df = pd.read_csv(
                    io.StringIO(decoded.decode('utf-8')))
            elif 'xls' in filename:
                # Assume that the user uploaded an excel file
                df = pd.read_excel(io.BytesIO(decoded))
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])

        return html.Div([
            html.H5(filename),
            #html.H6(datetime.datetime.fromtimestamp(date)),

            dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df.columns]
            ),

            html.Hr(),  # horizontal line

            # For debugging, display the raw contents provided by the web browser
            # html.Div('Raw Content'),
            # html.Pre(contents[0:200] + '...', style={
            #     'whiteSpace': 'pre-wrap',
            #     'wordBreak': 'break-all'
            # })
        ])

    @_app.callback(Output('output-data-upload-demand', 'children'),
                Input('upload-data-demand', 'contents'),
                State('upload-data-demand', 'filename'),
                State('upload-data-demand', 'last_modified'))
    
    def update_output(list_of_contents, list_of_names, list_of_dates):
        if list_of_contents is not None:
            children = [
                parse_contents_demand(c, n, d) for c, n, d in
                zip(list_of_contents, list_of_names, list_of_dates)]
            return children
    


app = run_standalone_app(layout, callbacks, header_colors, __file__)
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)