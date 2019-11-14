# Machine Learning

This readme files contains information with all datascience and machine learning resources.

## TOC

- [Machine Learning](#machine-learning)
  - [TOC](#toc)
  - [Course](#course)
  - [Libraries links](#libraries-links)
  - [Datasets](#datasets)
  - [Example code](#example-code)
  - [Visualization libraries](#visualization-libraries)

## Course

- [Python for Data Science](https://www.edx.org/course/python-for-data-science-3)

## Libraries links

- [numpy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [Natural Language Toolkit¶](https://www.nltk.org/)

## Datasets

Main ones:
- [kaggle](https://www.kaggle.com/)
- [movielens](https://grouplens.org/datasets/movielens/)
- [kaggle - World development indicators](https://www.kaggle.com/worldbank/world-development-indicators)
- [minute_weather.csv](https://drive.google.com/file/d/0B8iiZ7pSaSFZb3ItQ1l4LWRMTjg/view)
- [Iris Species](https://www.kaggle.com/uciml/iris/download)

Others:
- [KDnuggets Dataset](https://www.kdnuggets.com/datasets/index.html)
- [US Government Data](https://www.data.gov/) 
- [US Government Data](https://data.gov.uk/)
- [World Health Organization](https://www.who.int/gho/en/)

## Example code
- [edx Soccer](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/51bc9c62d2a4c9a03140fe521b069753/asset-v1:UCSanDiegoX+DSE200x+3T2019+type@asset+block/Week-1-Intro-new.zip)
- [numpy satellite](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/fd97cfcb5daf0402e3332ea4b2bf69c2/asset-v1:UCSanDiegoX+DSE200x+3T2019+type@asset+block/numpy_satellite.zip)
- [pandas](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/86226f41b3024393240da79c79bea504/asset-v1:UCSanDiegoX+DSE200x+3T2019+type@asset+block/Week-4-Pandas.zip)
- [Data visualization](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/07fdbcdcf18fa306bdbb042f64132f09/asset-v1:UCSanDiegoX+DSE200x+3T2019+type@asset+block/Week5-Visualization.zip)
- [Machine learning](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/67715bdd21eebbb26a95b1b3cc4a6684/asset-v1:UCSanDiegoX+DSE200x+3T2019+type@asset+block/Week-7-MachineLearning.zip)
- [Text and Databases](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/4f283f7388ded41911aeafa06fc6afa6/asset-v1:UCSanDiegoX+DSE200x+3T2019+type@asset+block/Week-8-NLP-Databases.zip)
- [Natural Language Processing - Databases](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/4f283f7388ded41911aeafa06fc6afa6/asset-v1:UCSanDiegoX+DSE200x+3T2019+type@asset+block/Week-8-NLP-Databases.zip)
- [Python 4 datascience - Example notebook](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/9be6813917bd9292d1523b31d2f2b47e/asset-v1:UCSanDiegoX+DSE200x+3T2019+type@asset+block/Week-9-ExampleNotebooks.zip)

## Visualization libraries

The following list provides a few plotting libraries for you to get started based on their use case(s).  This list is focused on providing a few solid options for each case rather than overwhelming you with the variety of options available.

The foundation: Matplotlib, most used plotting library, best for two-dimensional non-interactive plots. A possible replacement is pygal, it provides similar functionality but generates vector graphics SVG output and has a more user-friendly interface.

Specific use cases:

- Specialized statistical plots, like automatically fitting a linear regression with confidence interval or like scatter plots color-coded by category.

  - seaborn: it builds on top of Matplotlib and it can also be used as a replacement for matplotlib just for an easier way to specify color palettes and plotting aestetics
  
- Grammar of graphics plotting, if you find the interface of Matplotlib too verbose, Python provides packages based on a different paradigm of plot syntax based on R's ggplot2

    - ggplot: it provides similar functionality to Matplotlib and is also based on Matplotlib but provides a different interface.
    - altair: it has a simpler interface compared to ggplot and generates Javascript based plots easily embeddable into the Jupyter Notebook or exported as PNG.
  
- Interactive plots, i.e. pan, zoom that work in the Jupyter Notebooks but also can be exported as Javascript to work standalone on a webpage.

    - bokeh: maintained by Continuum Analytics, the company behind Anaconda
    - plotly: is both a library and a cloud service where you can store and share your visualizations (it has free/paid accounts)

Interactive map visualization

    *folium: Creates HTML pages that include the Leaflet.js javascript plotting library to display data on top of maps. *plotly: it supports color-coded country/world maps embedded in the Jupyter Notebook.

- Realtime plots that update with streaming data, even integrated in a dashboard with user interaction.

    - bokeh plot server: it is part of Bokeh but requires to launch a separate Python process that takes care of responding to events from User Interface or from streaming data updates.

- 3D plots are not easy to interpret, it is worth first consider if a combination of 2D plots could provide a better insight into the data

    - mplot3d: Matplotlib tookit for 3D visualization