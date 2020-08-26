import datetime


def create_html(title, blocks, path='blog/templates/blog/'):
    blog_default_date = datetime.date.today()
    blog_default_date = blog_default_date.strftime("%d %B %Y")
    flag = 0

    header_flag = 0
    fileobj = open(path + title + ".html", "w+")
    header='''

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="google-site-verification" content="UWZvQZ1V61UOV7vRiEO4B6fw5zSG564goDnTUq5j450" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>'''+blocks[0]['data']['text']+'''</title>
<meta property="og:site_name" content="Aman Chourasiya" />
<meta property="og:title" content="'''+blocks[0]['data']['text']+'''" />
<meta property="og:type" content="article" />
<meta property="og:description" content="'''+blocks[2]['data']['text']+'''" />
<meta property="og:url" content="https://www.amanchourasiya.com/blog/'''+title+'''/" />
<meta property="og:image" content="'''+blocks[1]['data']['file']['url']+'''" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="675" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="'''+blocks[0]['data']['text']+'''" />
<meta name="twitter:description" content="'''+blocks[2]['data']['text']+'''" />
<meta name="twitter:url" content="https://www.amanchourasiya.com/blog/'''+title+'''/" />
<meta name="twitter:image" content="'''+blocks[1]['data']['file']['url']+'''" />
<meta name="twitter:label1" content="Written by" />
<meta name="twitter:data1" content="'''+blocks[0]['data']['text']+'''" />
<meta name="twitter:label2" content="Filed under" />
<meta name="twitter:data2" content="Blog" />
<meta name="twitter:site" content="@techieaman" />
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
<script src='https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.2.2/lazysizes.min.js' async></script>
<script src='https://kit.fontawesome.com/a076d05399.js'></script>
<link rel="stylesheet" href="/static/css/owl.carousel.min.css">
<link rel="stylesheet" href="/static/css/owl.theme.default.min.css">
<link rel="stylesheet" href="/static/css/animate.css">
<link rel="stylesheet" href="/static/css/style.css">
<link rel="icon" href="https://ik.imagekit.io/portfolio/logo_yJ88tl3MK.png" type="image/icon">
</head>
<body>
<nav class="navbar navbar-expand-md navbar-dark fixed-top " style="    background-color: #000000fc;">
<a class="navbar-brand" href="/"><img class="img-fluid" src="https://ik.imagekit.io/portfolio/logo_yJ88tl3MK.png" alt="logo" width="60;" height="20;"></a>
<button class="navbar-toggler " style="outline:none;" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
<span class="navbar-toggler-icon"></span>
</button>
<div class="collapse navbar-collapse" id="collapsibleNavbar">
<ul class="navbar-nav ml-auto">
<li class="nav-item">
<a class="nav-link " href="/"><i class="fa fa-fw fa-home"></i>Home</a>
</li>
<li class="nav-item ">
<a href=/blog/ class="nav-link"><i class="fab fa-blogger-b"></i>log</a>
</li>
<li class="nav-item">
<a href=/port/ class="nav-link"> <i class="fa fa-user"></i>Portfolio</a>
</li>

</ul>
</div>
</nav>
    '''

    fileobj.write(header)
    blog_structure = '''<div class="blog" >'''
    fileobj.write(blog_structure)
    for block in blocks:
        if block['type'] == 'header':
            if header_flag == 0:

                header = '''
                
                      <h1 id="blog-title" class="text-center head-blog" style="margin-top:70px;">'''+block['data']['text']+'''</h1>
                      <div class="post-socialIcons">
                         <ul>
                           <li class="socialIcons-links socialIcons-links-linkedin">
                            <a id="linkedinId" class="fa fa-linkedin" href="https://www.linkedin.com/sharing/share-offsite/?url=" target="_blank"></a>
                            
                           </li>
                           <li class="socialIcons-links socialIcons-links-twitter">
                           <a id="twitterId" class="fa fa-twitter" href="https://twitter.com/share?url=" target="_blank"></a>
                           
                           </li>
                           <li class="socialIcons-links socialIcons-links-facebook">
                           <a id="fbId" class="fa fa-facebook" href="https://www.facebook.com/sharer/sharer.php?u=" target="_blank"></a>
                           
                           </li>
                            <li class="socialIcons-links socialIcons-links-reddit">
                           <a id="redditId" class="fa fa-reddit-alien" href="https://reddit.com/submit?url=" target="_blank"></a>
                           
                           </li>
                           <li id="page-views" class="fa fa-eye " style="float: right;margin-top: 10px;">0</li>
                          
                          
                         </ul>
                      </div>
                      <h6 class="text-center" style="margin-right:10px;">'''+block.get('date', blog_default_date)+'''</h6><br>
                     '''

            else:
                if block['data']['level'] == 2:
                    header = '''
                      <h1 class="head-blog" style=" margin-top:40px;">'''+block['data']['text']+'''</h1>
                     '''
                elif block['data']['level'] == 3:
                    header = '''
                      <h2 class="head-blog" style="font-size: 26px; margin-top:40px;">'''+block['data']['text']+'''</h2>
                     '''
                elif block['data']['level'] == 4:
                    header = '''
                      <h3 class="head-blog" style=" font-size: 22px; margin-top:40px;">'''+block['data']['text']+'''</h3>
                     '''
            header_flag += 1
            fileobj.write(header)
        elif block['type'] == 'paragraph':
            if flag == 0:
                paragraph = '''
                    <div class="para-desc-blog">
                    <p id="blog-description"><span class="blog-first-char">'''+block['data']['text'][0]+'''</span>'''+block['data']['text'][1:]+'''</p>
                    </div>
                    
            '''
            else:
                paragraph = '''
                    <div class="para-desc-blog">
                    <p >'''+block['data']['text']+'''</p>
                    </div>
                    
            '''
            flag = flag+1
            fileobj.write(paragraph)
        elif block['type'] == 'list':
            if block['data']['style'] == 'ordered':
                o_l = '''<ol class="para-desc-blog">'''
                fileobj.write(o_l)
                for items in block['data']['items']:
                    list_data = '''<li>'''+items+'''</li>'''
                    fileobj.write(list_data)
                fileobj.write("</ol>")
            else:
                u_l = '''<ul class="para-desc-blog">'''
                fileobj.write(u_l)
                for items in block['data']['items']:
                    list_data = '''<li>'''+items+'''</li>'''
                    fileobj.write(list_data)
                fileobj.write("</ul>")

        elif block['type'] == 'quote':
            pass

        elif block['type'] == 'embed':
            youtube = '''  <iframe height="345" src="''' + \
                block['data']['embed']+'''" style="align:center;width:70%;"></iframe>'''
            fileobj.write(youtube)

        elif block['type'] == 'code':

            code = '''<div style="text-align:center;"> <textarea  style=" width:100%;
    font-size: 0.9rem;" rows="7"  disabled>'''+block['data']['code'] + '''</textarea></div> '''
            fileobj.write(code)
        elif block['type'] == 'warning':
            pass
        elif block['type'] == 'image':
            image = '''<div class="text-center">
                     <figure class="figure">
                     <img data-src='''+block['data']['file']['url']+''' class="figure-img img-fluid img-thumbnail lazyload" style="width:100%;"> 
                     <figcaption class="figure-caption text-center">'''+block['data']['caption']+'''</figcaption>
                     </figure>
                     </div>
                     
                     '''
            fileobj.write(image)
        elif block['type'] == 'delimiter':
            hr = '''<hr style="height:2px;border-width:0;color:gray;background-color:gray">'''
            fileobj.write(hr)
            
    like_ann_sharing_icon=''' 
                             <div class="post-socialIcons" style="">
                         <ul class="list-unstyled">
                           <li class="socialIcons-links socialIcons-links-like" style="display: inline-table;float: left;">
                           <button  onclick="incrementClaps()" id="likebutton" class="fa fa-thumbs-up like-button" ></button>
                           
                           </li>
                           
                           
                           <li id="page-likes"   style="float: left;margin-top: 4px;">100</li>
                         
                           <li class="socialIcons-links socialIcons-links-linkedin">
                           <a id="linkedinId" class="fa fa-linkedin" href="https://www.linkedin.com/sharing/share-offsite/?url=" target="_blank"></a>
                           </li>
                           <li class="socialIcons-links socialIcons-links-twitter">
                           <a id="twitterId" class="fa fa-twitter" href="https://twitter.com/share?url=" target="_blank"></a>
                           
                           </li>
                           <li class="socialIcons-links socialIcons-links-facebook">
                           <a id="fbId" class="fa fa-facebook" href="https://www.facebook.com/sharer/sharer.php?u=" target="_blank"></a>
                           
                           </li>
                            <li class="socialIcons-links socialIcons-links-reddit">
                           <a id="redditId" class="fa fa-reddit-alien" href="https://reddit.com/submit?url=" target="_blank"></a>
                           
                           </li>
                           
                          
                          
                          
                         </ul>
                      </div>
                               
                          '''
    fileobj.write(like_ann_sharing_icon)
    fileobj.write("</div>")

    footer = '''

                  </body>

            <footer class="page-footer font-small text-white " style="background-color: #000000fc;">


<div class="text-center">

<div class="col-md-12 pt-5 pb-0">
<div class="mb-4 flex-center">

<a class="li-ic" href="https://in.linkedin.com/in/aman-chourasiya">
<i class="fab fa-linkedin-in fa-lg white-text mr-md-5 mr-3 fa-2x" style="color:white"> </i>
</a>

<a class="fb-ic" href="https://www.fb.com/aman.chourasia.35">
<i class="fab fa-facebook-f fa-lg  mr-md-5 mr-3 fa-2x" style="color:white"> </i>
</a>

<a class="tw-ic" href="https://twitter.com/techieaman">
<i class="fab fa-twitter fa-lg white-text mr-md-5 mr-3 fa-2x" style="color:white"> </i>
</a>


<a class="ins-ic" href="https://www.instagram.com/techie_aman/">
<i class="fab fa-instagram fa-lg white-text mr-md-5 mr-3 fa-2x" style="color:white"> </i>
</a>

</div>
</div>

</div>


<p class="text-center " style="color:white">Contact me for any queries</p>
<div class="footer-copyright text-center pt-1" style="color:white">2020 Copyright:
<a href="https://mdbootstrap.com/"> Chourasiya Brothers</a>
</div>

</footer>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="/static/js/blog.js"></script>
<script src="/static/js/owl.carousel.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>
</html>

           '''
    fileobj.write(footer)
    fileobj.close()
