import init as hpy

a = hpy.Tag('a','d','https://www.google.com')

p = hpy.Tag('p',inner='paragraph'+a.tag,style='color: red')
pp = hpy.Tag('p',inner='slm',style='color: blue')

d = hpy.Tag('div',inner=p.tag,style='border:5pt #000 solid')
dd = hpy.Tag('div',inner=pp.tag,style='border:1pt red solid')

head = hpy.Head('Python Html Class',inner='')
body = hpy.Body(d.tag+dd.tag)
html = hpy.Html(head,body)

hpy.html_run(html,'index')