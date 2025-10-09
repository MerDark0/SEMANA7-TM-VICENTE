import dash
from dash import html

dash.register_page(__name__, path='/', name='Inicio')

layout = html.Div(className='cv-container', children=[
    html.Div(className='cv-header', children=[
        html.Img(src='/assets/images/me.png', className='cv-photo'),
        html.Div(className='cv-header-text', children=[
            html.H3("Hola :D yo soy...", className='cv-subtitle'),
            html.H1("Melanie Vicente Fajardo", className='cv-title'),
            html.Div(className='cv-tags', children=[
                html.Span("Software Developer", className='cv-tag'),
                html.Span("Web Designer", className='cv-tag')
            ])
        ])
    ]),

    html.Div(className='cv-grid', children=[
        html.Div(className='cv-box', children=[
            html.H2("EDUCATION", className='cv-section-title'),
            html.Div(className='cv-item', children=[
                html.H4("Computación Científica", className='cv-item-title'), 
                html.P("UNMSM", className='cv-item-subtitle'),
                html.P("2023 - Actualidad", className='cv-item-date')
            ]),
            html.Div(className='cv-item', children=[
                html.H4("Desarrollo de Sistemas de Información", className='cv-item-title'),
                html.P("IDAT", className='cv-item-subtitle'),
                html.P("2021 - 2023 y 2025", className='cv-item-date')
            ]),
            html.H2("INTERESTS", className='cv-section-title'),
            html.Div(className='cv-tags', children=[
                html.Span("Ciencia de Datos", className='cv-tag'),
                html.Span("IA", className='cv-tag'),
                html.Span("Desarrollo FullStack", className='cv-tag')
            ])
        ]),

        html.Div(className='cv-box', children=[
            html.H2("EXPERIENCE", className='cv-section-title'),
            html.Div(className='cv-item', children=[
                html.H4("A restaurant Website", className='cv-item-title'),
                html.P("2025", className='cv-item-subtitle')
            ]),
            html.Div(className='cv-item', children=[
                html.H4("Mobile App - Delicias Food", className='cv-item-title'),
                html.P("2025", className='cv-item-subtitle')
            ]),
            html.Div(className='cv-item', children=[
                html.H4("Veterinary clinic desktop system", className='cv-item-title'),
                html.P("2022", className='cv-item-subtitle')
            ]),
            html.Div(className='cv-item', children=[
                html.H4("Santa Natura's system", className='cv-item-title'),
                html.P("2023", className='cv-item-subtitle')
            ])
        ]),

        html.Div(className='cv-box', children=[
            html.H2("CONTACT", className='cv-section-title'),
            html.P("Lima, Perú"),
            html.P("+51 926 184 955"), 
            html.P("melanie.vicente@unmsm.edu.pe"),

            html.H2("TECNOLOGIES I USE:", className='cv-section-title'),
            html.Div(className='cv-tags', children=[
                html.Span("Python", className='cv-tag'),
                html.Span("Java", className='cv-tag'),
                html.Span("C#", className='cv-tag'),
                html.Span("HTML & CSS & JS", className='cv-tag'),
                html.Span("PHP", className='cv-tag'),
                html.Span("SQL", className='cv-tag')
            ])
        ])
    ])
])