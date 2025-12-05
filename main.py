from fasthtml.common import *

app, rt = fast_app(
    hdrs=( 
        Link(rel="stylesheet", href="https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/dark.min.css"),
        Style("""
            body {margin:0; min-height:100dvh; display:grid; place-items:center; background:#000;}
            .quote {font-size: 2.2rem; font-weight: 800; max-width: 90%; line-height: 1.4;}
            @media (max-width: 600px) { .quote {font-size: 1.6rem;} }
        """)
    )
)

quote = """The problem is almost certainly
unescaped quotes inside the string.
Look at this part of your text:

“These principles have not been
attended to. An instance has
been mentioned already where
they have been in some degree
violated.”"""

@rt("/")
def get():
    return Div(
        Div(quote, cls="quote"),
        style="text-align:center; color:white;"
    )

serve()
