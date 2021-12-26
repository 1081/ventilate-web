import time
from math import pi
from random import random
from time import sleep

import numpy as np
import pandas as pd
import streamlit as st
from streamlit import _DeltaGenerator

options = st.sidebar.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)

st.write("You selected:", options)
