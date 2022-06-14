import imp
from application import app
from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly.express as px

@app.route("/")
def index():
    # Graph One
    # df = px.data.medals_wide()
    dfCon = "/Users/France/Desktop/JUPYTER NOTEBOOK/Data-Visualization-using-Python/Weather_Data_Visualize/Test.csv"
    dfTest = pd.read_csv(dfCon)
    # fig1 = px.bar(df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")
    fig1 = px.histogram(dfTest, y="humidity", x="temperature", title="Wide-Form Input")
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph two
    df = px.data.iris()
    fig2 = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species',  title="Iris Dataset")
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

    # Graph three
    df = px.data.gapminder().query("continent=='Oceania'")
    fig3 = px.line(df, x="year", y="lifeExp", color='country',  title="Life Expectancy")
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    
    df = px.data.medals_wide()
    fig4 = px.bar(df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")
    graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('index.html', graph1JSON=graph1JSON, graph2JSON=graph2JSON, graph3JSON=graph3JSON, graph4JSON=graph4JSON)