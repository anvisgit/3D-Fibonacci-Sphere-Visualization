import numpy as np
import streamlit as st
import plotly.graph_objects as go

st.sidebar.header("Fibonacci Sphere Controls")
samples = st.sidebar.slider("Number of points", 100, 5000, 1000, 100)
size = st.sidebar.slider("Marker size", 1, 10, 4, 1)
color = st.sidebar.color_picker("Marker color", "#1f77b4")

i = np.arange(0, samples, dtype=float) + 0.5
phi = (1 + np.sqrt(5)) / 2
theta = 2 * np.pi * i / phi
z = 1 - (2 * i / samples)
radius = np.sqrt(1 - z * z)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(size=size, color=color)
)])

fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ),
    title=f"3D Fibonacci Sphere with {samples} points",
    margin=dict(l=0, r=0, b=0, t=30)
)

st.plotly_chart(fig, use_container_width=True)
