from filterpy.common import Q_discrete_white_noise
from filterpy.kalman import ExtendedKalmanFilter
import control

rk = ExtendedKalmanFilter(dim_x=3, dim_z=1)
lqr_control = control.lqr(sys, Q, R)
#Input: Initial belief state, b
#Output: Vector of control actions, u1:T

while b != goal_state:
    for t in range(T):
        u_t = lqr_control(b, u_bar[t], b_bar[t])
        b_tp1 = rk(b, u_t, z_t)
        if m_tp1 > theta:
            break
    b = b_tp1

    

