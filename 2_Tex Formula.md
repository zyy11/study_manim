##新建Tex公式对象

```python
formula=TexMobject(r"公式代码")
formula=TextMobject("文本$\\displaystyle公式代码$") #需要转义
formula=TexMobject("公式1","公式2","公式3") #推荐\over代替\frac
formula=TexMobject("""多行公式""")
```

##对象缩放

```python
formula.scale(系数)
```

##引入latex包
把包拷贝到manimlib/tex_template.tex
