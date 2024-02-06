"""
Ce module contient les importations nécessaires pour le script.
"""
# Module pour interagir avec les bases de données SQLite.
import sqlite3

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

# Composant de boîte de dialogue pour afficher des messages dans Tkinter.
from tkinter import messagebox

# Objet de figure utilisé pour créer des graphiques avec Matplotlib.
from matplotlib.figure import Figure

# Utilisé pour intégrer des graphiques Matplotlib dans une interface Tkinter.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Module pour interagir avec le système d'exploitation.
import os

import csv