import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import matplotlib

# 设置字体为SimHei（黑体），防止中文显示乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 定义系统参数
m = 1.0  # 质量
c = 0.2  # 阻尼系数
k = 1.0  # 弹簧常数

# 定义二阶方程的右侧
def mass_spring_damper(t, y):
    x, v = y
    dxdt = v
    dvdt = -(c/m) * v - (k/m) * x
    return [dxdt, dvdt]

# 初始条件
x0 = 1.0  # 初始位移
v0 = 0.0  # 初始速度

# 定义时间范围
t_span = [0, 10]  # 模拟的时间范围
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # 定义时间点

# 求解微分方程
sol = solve_ivp(mass_spring_damper, t_span, [x0, v0], t_eval=t_eval)

# 绘制结果
plt.plot(sol.t, sol.y[0], label='位移 $x(t)$')
plt.plot(sol.t, sol.y[1], label='速度 $v(t)$')
plt.title('质量-弹簧-阻尼系统的响应')
plt.xlabel('时间 $t$')
plt.ylabel('响应')
plt.legend()
plt.grid()
plt.show()
