## 变换

第一种方法
```python
text1=TextMobject("文本1")
text2=TextMobject("文本2")
text3=TextMobject("文本3")
self.play(Write(text1))
self.play(Transform(text1,text2))
self.play(Transform(text1,text3))
```

第二种方法
```python
text1=TextMobject("文本1")
text2=TextMobject("文本2")
text3=TextMobject("文本3")
self.play(Write(text1))
self.play(ReplacementTransform(text1,text2))
self.play(ReplacementTransform(text1,text3))
```

## 制作拷贝并变换
```python
self.play(
  ReplacementTransform(formula[2].copy(),formula[8]),
  ReplacementTransform(formula[3].copy(),formula[9])
)
```

## 改变颜色等其他属性
```python
self.play(text.set_color,YELLOW,run_time=2)
```
或
```python
self.play(ApplyMethod(text.set_color,YELLOW),run_time=2)
```
或
```python
text.generate_target()
text.target.set_color(RED)
self.play(MoveToTarget(text),run_time=2)
```

## 注意
如果不是数组，要用text[:]的方法
