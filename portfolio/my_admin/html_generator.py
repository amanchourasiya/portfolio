def create_html(title,blocks):
    fileobj=open("my_admin/templates/blog/"+title+".html","a")
    message='''<html>
         '''+blocks[1]['data']+'''  
    </html>
    '''
    fileobj.write(message)
    fileobj.close()
