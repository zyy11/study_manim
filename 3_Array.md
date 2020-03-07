## 颜色代码

详见manimlib/constants.py

## 数组
```python
text=TextMobject("A","B","C","D","E")
text[0].set_color(RED)
text[1].set_color("#DC28E2")
```
注意\\sqrt自占2个位置
有时公式最后一个字母显示不出来，可以加一个"\\tiny ."
有上有下的时候，先上后下

## 循环设置颜色
```python
for i in [1,2,3,4]:
  text[i].set_color(RED)
for i in range(1,5):
  text[i].set_color(RED)
for i,color in [(2,RED),(5,BLUE)]:
  text[i].set_color(color)
```
