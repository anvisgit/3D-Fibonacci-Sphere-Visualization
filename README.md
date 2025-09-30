# Interactive 3D Fibonacci Sphere

An interactive Streamlit app that generates a 3D Fibonacci Sphere, distributing points evenly on a sphere using the golden angle. Allows real-time parameter adjustments

---

## Features

- interactive 3D visualization using Plotly.
- Sidebar controls for:
  - Number of points 
  - Marker size
  - Marker color
- updates on parameter change.
- Supports zoom, rotation, and hover info for points.


---

## Math

The Fibonacci Sphere uses a Fibonacci lattice for uniform point distribution:

1. **Golden Angle**  
\[
\theta_i = \frac{2\pi i}{\phi}, \quad i = 0,1,...,n-1
\]  
where φ = (1 + √5)/2.

2. **Z-coordinate (height)**  
\[
z_i = 1 - \frac{2i}{n}
\]

3. **Radius at height z**  
\[
r_i = \sqrt{1 - z_i^2}
\]

4. **Cartesian coordinates**  
\[
x_i = r_i \cos(\theta_i), \quad y_i = r_i \sin(\theta_i)
\]

---

