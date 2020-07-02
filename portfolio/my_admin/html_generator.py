def create_html(title,blocks):
    flag=0
    fileobj=open("blog/templates/blog/"+title+".html","a")
    navbar='''

         {% extends "base.html" %}
     {% load static%} 
     {% block page_content %}
    '''

    fileobj.write(navbar)
 
    for block in blocks:
        if block['type']=='header':
               header='''
                     
                     
                        <div container-fluid class="blog" >                       
                        <h1 class="text-center head-blog" style="margin-top:70px;">'''+block['data']['text']+'''</h1>
                    
                     
                   
                       
 
                      '''
               fileobj.write(header)
              
        elif block['type']=='paragraph':
            if flag==0:               
                paragraph='''
                    <div class="para-desc-blog">
                    <p ><span class="blog-first-char">'''+block['data']['text'][0]+'''</span>'''+block['data']['text'][1:-1]+'''</p>
                    </div>
                    
            '''
            else:
                paragraph='''
                    <div class="para-desc-blog">
                    <p >'''+block['data']['text']+'''</p>
                    </div>
                    
            '''
            flag=flag+1
            fileobj.write(paragraph)
        elif block['type']=='list':
               if block['data']['style']=='ordered':
                   o_l='''<ol class="para-desc-blog">'''
                   fileobj.write(o_l)
                   for items in block['data']['items']:
                         list_data='''<li>'''+items+'''</li>'''
                         fileobj.write(list_data)
                   fileobj.write("</ol>")
               else:
                   u_l='''<ul class="para-desc-blog">'''
                   fileobj.write(u_l)
                   for items in block['data']['items']:
                         list_data='''<li>'''+items+'''</li>'''
                         fileobj.write(list_data)
                   fileobj.write("</ul>")
                   
        elif block['type']=='quote':
               pass
        elif block['type']=='code':
               
               code='''<div style="text-align:center;"> <textarea  style=" width:100%;
    font-size: 0.9rem;" rows="7"  disabled>'''+block['data']['code']+ '''</textarea></div> '''
               fileobj.write(code)
        elif block['type']=='warning':
             pass
        elif block['type']=='image':
              image='''<div class="text-center">
                     <figure class="figure">
                     <img src='''+block['data']['file']['url']+''' class="figure-img img-fluid img-thumbnail " style="width:100%;height:70%;"> 
                     <figcaption class="figure-caption text-center">'''+block['data']['caption']+'''</figcaption>
                     </figure>
                     </div>
                     
                     '''
              fileobj.write(image)
        elif block['type']=='delimiter':
             hr='''<hr style="height:2px;border-width:0;color:gray;background-color:gray">'''
             fileobj.write(hr)
    fileobj.write("</div>")
        
    footer='''

              {% endblock %}

           '''
    fileobj.write(footer)   
    fileobj.close()
