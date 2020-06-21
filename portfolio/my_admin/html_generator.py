def create_html(title,blocks):
    flag=0
    fileobj=open("blog/templates/blog/"+title+".html","a")
    navbar='''

 {% load static%}    
<head>
  
   <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <script src='https://kit.fontawesome.com/a076d05399.js'></script>
  <link rel="stylesheet" href="{%static 'css/style.css'%}">
    </head>
	
<body>	

<nav class="navbar navbar-expand-md bg-dark navbar-dark fixed-top">
  <a class="navbar-brand" href="#">Aman</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
    <ul class="navbar-nav ml-auto">
      <li class="nav-item">
        <a class="nav-link" href="/"><i class="fa fa-fw fa-home"></i>Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#"><i class="fab fa-blogger-b"></i>log</a>
      </li>
      <li class="nav-item">
        <a  href={%url 'port'%} class="nav-link" > <i class="fa fa-user"></i>Portfolio</a>
      </li>    
	   <li class="nav-item" >
        <a   class="nav-link" href="#"><i class="fa fa-pencil-square-o"></i>Post</a>
      </li> 
	 {% block navbar %}
	  {% endblock %}
    </ul>
  </div>  
</nav>
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

           <footer class="page-footer font-small text-white50 bg-dark">

  <!-- Footer Elements -->
  <div class="container">

    <!-- Grid row-->
    <div class="row text-center">

      <!-- Grid column -->
      <div class="col-md-12 pt-5 pb-0">
        <div class="mb-5 flex-center">
 <!--Linkedin -->
          <a class="li-ic" href="https://in.linkedin.com/in/aman-chourasiya">
            <i class="fab fa-linkedin-in fa-lg white-text mr-md-5 mr-3 fa-2x"style="color:white"> </i>
          </a>
          <!-- Facebook -->
          <a class="fb-ic" href="https://www.fb.com/aman.chourasia.35">
            <i class="fab fa-facebook-f fa-lg  mr-md-5 mr-3 fa-2x" style="color:white"> </i>
          </a>
          <!-- Twitter -->
          <a class="tw-ic" href="https://twitter.com/techieaman">
            <i class="fab fa-twitter fa-lg white-text mr-md-5 mr-3 fa-2x"style="color:white"> </i>
          </a>
          <!-- Google +-->
          <a class="gplus-ic" href="">
            <i class="fab fa-google-plus-g fa-lg black-text mr-md-5 mr-3 fa-2x"style="color:white"> </i>
          </a>
        
          <!--Instagram-->
          <a class="ins-ic" href="https://www.instagram.com/techie_aman/">
            <i class="fab fa-instagram fa-lg white-text mr-md-5 mr-3 fa-2x"style="color:white"> </i>
          </a>
          <!--Pinterest-->
          
        </div>
      </div>
      <!-- Grid column -->

    </div>
    <!-- Grid row-->

  </div>
  <!-- Footer Elements -->

  <!-- Copyright -->
  <p class="text-center " style="color:white">Team of AC Brothers.Be ready to be Hacked!!!!</p>
  <div class="footer-copyright text-center pt-1" style="color:white">2020 Copyright:
    <a href="https://mdbootstrap.com/"> Chourasiya Brothers</a>
  </div>
  <!-- Copyright -->

</footer>

           '''
    fileobj.write(footer)   
    fileobj.close()
