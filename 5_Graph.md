## 定义使用全局变量
```python
class ConfigExample(Scene):
  CONFIG={
    "text_1":"Text_1",
    "text_2":"Text_2"
  }
  
  def construct(self):
    self.custom_method()
    
  def custom_method(self):
    t1=TextMobject(self.text_1)
    self.play(Write(t1))
```

## 更改场景和相机设定
```python
CONFIG={
  "camera_config"={"background_color":RED}
}
```
详见manimlib/scene/scene.py
manimlib/scene/graph_scene.py
manimlib/camera/camera.py
manimlib/mobject/number_line.py

## 二维坐标
```python
class 2d(GraphScene):
  def construct(self):
    self.setup_axes(animate=True)
```

## 三维坐标
在manimlib/mobject/coordinate_systems.py中添加
```python
def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
```

```python
class 3d(ThreeDScene):
  def construct(self):
    axes = ThreeDAxes()
    self.set_camera_orientation(phi=80 * DEGREES,theta=45*DEGREES,distance=6,gamma=30*DEGREES)
    self.move_camera(phi=30*DEGREES,theta=-45*DEGREES,run_time=3) #设定相机角度
    self.begin_ambient_camera_rotation(rate=0.1) #旋转相机
    self.wait(5)
    self.stop_ambient_camera_rotation() #停止旋转相机
```

## 定义曲线
```python
curve1=ParametricFunction(
      lambda u : np.array([
      1.2*np.cos(u),
      1.2*np.sin(u),
      u/2
  ]),color=RED,t_min=-TAU,t_max=TAU,
  )
```

## 定义曲面
```python
paraboloid = ParametricSurface(
  lambda u, v: np.array([
      np.cos(v)*u,
      np.sin(v)*u,
      u**2
  ]),v_max=TAU,
  checkerboard_colors=[PURPLE_D, PURPLE_E],
  resolution=(10, 32)).scale(2)
  ```
