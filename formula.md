# 迭代公式

## verlet公式

$$ r_{t+1}=2r{t}-r_{t-1}+a_{t}^2 $$

## 速度表示的verlet公式

$$ x_{n+1}=x_n+v_n\Delta t+1/2a_n \Delta t^2 $$
$$ v_{n+1}=v_n+1/2(a_n+a_{n+1})\Delta t $$
