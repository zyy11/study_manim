## 在manim文件夹下进行引用

```python
from manimlib.imports import *
```

## 编写场景

```python
class NameOftheScene(Scene):
  def construct(self):
    #Animation process
```

## 生成视频

```cmd
python -m manim 文件名.py 场景名 -选项
```
-ps:导出最后一帧图片
-pl:低质量(480p,15fps)
-pm:中等质量（720p,30fps）
-p:高质量（1440p,60fps）

所有场景
-as:导出最后一帧图片
-al:低质量(480p,15fps)
-am:中等质量（720p,30fps）
-a:高质量（1440p,60fps）

r HEIGHT：定义高度
r HEIGHT,WIDTH：定义高度和宽度

t:有透明度

-n START：渲染START之后的动画
-n START,END+1：渲染START和END之间的动画

-o OUTPUT_NAME：输出文件名

--leave_progress_bars：保留进度条




## 定义文字对象并在屏幕上显示

```python
    text=TextMobject("text")
    self.add(text)  #在屏幕上显示text对象（无动画效果）
    self.wait(3) #等待3秒
```
## 进入动画

```python
    self.play(Write(text))
```

参见manimlib/mobject/creation.py
manimlib/mobject/fading.py
manimlib/mobject/growing.py

进入动画
- 出现
  * self.add(对象)：出现
- 创建
  * self.play(Write(对象),[run_time=时间])：打字机
- 淡入
  * self.play(FadeIn(对象),[run_time=时间])：淡入
  * self.play(FadeInFrom(对象,[direction=方向]),[run_time=时间])：从某个方向淡入
  * self.play(FadeInFromLarge(对象,[scale_factor=比例因子]),[run_time=时间])：缩放并淡入
  * self.play(FadeInFromPoint(对象,np.array([x,y,z]),[run_time=时间])：从某个点淡入
- 生成
  * self.play(GrowFromCenter(对象),[run_time=时间])：从中心缩放

退出动画
- 消失
  * self.remove(对象)：消失
- 淡出
  * self.play(FadeOut(对象))：淡出
  * self.play(FadeOutAndShift(对象,[direction=方向]),[run_time=时间])：向某个方向淡出

## 图形对象
参见manimlib/mobject/geometry.py
- 文字：TextMobject("文字")
- 点：Dot([arc_center=位置])
- 小点：SmallDot([arc_center=位置])
- 矩形：Rectangle([height=高, width=宽])
- 正方形：Square([side_length=边长])
- 圆：Circle([radius=半径,arc_center=圆心])
- 椭圆：Ellipse([height=横轴, width=纵轴,arc_center=中心])
- 弧：Arc([radius=半径,arc_center=原点,start_angle=始边,angle=圆心角]) #弧度制，可用PI表示圆周率
- 过两点的弧：ArcBetweenPoints(起点,终点,[圆心角])
- 过两点的弯箭头：CurvedArrow(起点,终点,[angle=圆心角])
- 过两点的双向弯箭头：CurvedDoubleArrow(起点,终点,[angle=圆心角])
- 直线：Line([start=起点, end=终点])
- 虚线：DashedLine
- 箭头：Arrow,Vector
- 双向箭头：DoubleArrow
- 多边形：Polygon(端点,端点,...)
- 扇形：Sector
- 圆环：Annulus
- 圆环扇：AnnularSector


## 图形对象的参数
- 边框颜色：color=PURPLE_A
- 填充颜色：fill_color
- 填充透明度：fill_opacity

## 移动位置

- 绝对位置 
  - .to_edge(方向,buff=缓冲区大小) #UP,DOWN,LEFT,RIGHT
  - .to_corner(方向,buff=缓冲区大小) #UR,UL,DR,DL
```python
    object=Dot()
    object.to_edge(UP)
```
- 相对位置
  - .move_to(向量)
  - .move_to(对象.get_center()+向量)
  - .next_to(对象,方向,[buff=缓冲])
  - .shift(方向)
- 旋转
  - .rotate(角度,[about_point=旋转中心]) #可用PI、TAU、DEGREES
- 翻转
  - .flip(方向) #方向为翻转轴
