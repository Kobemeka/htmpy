class Tag:
    def __init__(self,tag_name,id_name='',class_name='',inner='',href='',style=''):
        self.tag_name =tag_name
        self.id_name = id_name
        self.class_name = class_name
        self.inner = inner
        self.href = href
        self.style = style
        
        if tag_name=='a':
            self.tag = '<{} style="{}" href="{}" class={} id={}>{}</{}>'.format(self.tag_name,self.style,self.href,self.class_name,self.id_name,self.inner,self.tag_name)
        else:
            self.tag = '<{} style="{}" class={} id={}>{}\n</{}>'.format(self.tag_name,self.style,self.class_name,self.id_name,self.inner,self.tag_name)
            
        
class Html:
    def __init__(self,head,body):
        self.head=head
        self.body=body
        self.html = '<html>\n{}\n{}\n</html>'.format(self.head.head,self.body.body)

class Head:
    def __init__(self,title,inner=''):
        self.title = title
        self.inner = inner
        self.head = '<head>\n<title>{}</title>{}\n</head>'.format(self.title,self.inner)

class Body:
    def __init__(self,inner):
        self.inner = inner 
        self.body = '<body>\n{}\n</body>'.format(self.inner)

def html_run(html_,file_name):
    text_file = open('{}.html'.format(file_name),'w')
    text_file.write(html_.html)
    text_file.close()