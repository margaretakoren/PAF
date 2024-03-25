import numpy as np
import particle as cp
import plotly.graph_objects as go

B = np.array((0, 0, 1))
E = np.array((0, 0, 0))

q_ele, q_pos = -1, +1
m_ele, m_pos = 1, 1
v_ele, v_pos = np.array([0.1] * 3), np.array([0.1] * 3)

ele = cp.ChargedParticle(q_ele, m_ele, v_ele, E, B, 0.01)
poz = cp.ChargedParticle(q_pos, m_pos, v_pos, E, B, 0.01)

x_ele, y_ele, z_ele = ele.calculate_trajectory(20, 'rk')
x_poz, y_poz, z_poz = poz.calculate_trajectory(20, 'rk')

fig = go.Figure()
fig.add_trace(go.Scatter3d(x=x_ele, y=y_ele, z=z_ele, mode='lines', name='Electron', line=dict(color='lime', width=5)))
fig.add_trace(go.Scatter3d(x=x_poz, y=y_poz, z=z_poz, mode='lines', name='Positron', line=dict(color='magenta', width=5)))

fig.update_layout(
    scene=dict(
        xaxis=dict(title='X', titlefont=dict(color='lime'), tickfont=dict(color='lime')),
        yaxis=dict(title='Y', titlefont=dict(color='lime'), tickfont=dict(color='lime')),
        zaxis=dict(title='Z', titlefont=dict(color='lime'), tickfont=dict(color='lime')),
        bgcolor='black'
    )
)

fig.write_html("ele_poz.html", auto_open=True)

# Euler & Runge-Kutta
q_e = -1
q_rk = -1
m_e = 1
m_rk = 1
v_e = np.array((0.1, 0.1, 0.1))
v_rk = np.array((0.1, 0.1, 0.1))

e = cp.ChargedParticle(q_e, m_e, v_e, E, B, 0.01)
rk = cp.ChargedParticle(q_rk, m_rk, v_rk, E, B, 0.01)

x_e, y_e, z_e = e.calculate_trajectory(20, 'euler')
x_rk, y_rk, z_rk = rk.calculate_trajectory(20, 'rk')

fig = go.Figure()
fig.add_trace(go.Scatter3d(x=x_e, y=y_e, z=z_e, mode='lines', name='Euler', line=dict(color='lime', width=5)))
fig.add_trace(go.Scatter3d(x=x_rk, y=y_rk, z=z_rk, mode='lines', name='Runge-Kutta', line=dict(color='magenta', dash='dash', width=5)))

fig.update_layout(
    scene=dict(
        xaxis=dict(title='X', titlefont=dict(color='lime'), tickfont=dict(color='lime')),
        yaxis=dict(title='Y', titlefont=dict(color='lime'), tickfont=dict(color='lime')),
        zaxis=dict(title='Z', titlefont=dict(color='lime'), tickfont=dict(color='lime')),
        bgcolor='black'
    )
)

fig.write_html("ele_euler_rk.html", auto_open=True)
