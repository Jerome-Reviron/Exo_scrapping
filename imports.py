"""
Ce module contient les importations nécessaires pour le script.
"""
# Module pour interagir avec les bases de données SQLite.
import sqlite3

# Module pour interagir avec la base de données Oracle.
import cx_Oracle

# Utilisé pour ouvrir des URL et récupérer les données.
from urllib.request import urlopen, urlretrieve, Request

# Parseur HTML pour extraire des informations à partir de pages web.
from bs4 import BeautifulSoup

# Bibliothèque de traitement et d'analyse de données.
import pandas as pd

# Module pour travailler avec les dates et heures.
from datetime import datetime

# Module pour mesurer le temps d'exécution.
import timeit

# Framework de test pour Python.
import pytest

# Utilisés pour créer des objets simulés (mock objects) dans les tests.
from unittest.mock import patch, Mock

# Bibliothèque graphique pour créer des interfaces utilisateur.
import tkinter as tk
from tkinter import ttk, messagebox  

# Objet de figure utilisé pour créer des graphiques avec Matplotlib.
from matplotlib.figure import Figure

# Utilisé pour intégrer des graphiques Matplotlib dans une interface Tkinter.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Importation de matplotlib.pyplot
import matplotlib.pyplot as plt
from io import BytesIO  

# Importation de la classe Image depuis le module PIL
from PIL import Image

# Importation de ImageTk depuis le module PIL
from PIL import ImageTk

# Module pour interagir avec le système d'exploitation.
import os

# Module pour manipuler des fichiers CSV.
import csv
