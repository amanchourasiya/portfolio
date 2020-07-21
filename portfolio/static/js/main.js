const responsive = {
	0: {
		items: 1
	},
	320: {
		items: 1
	},
	560: {
		items: 2
	},
	960: {
		items: 3
	}
}
$(document).ready(function () {
	$(".owl-carousel").owlCarousel({
		loop:true,
		autoplay:true,
		autoplayTimeout:2500,
		responsive:responsive,
		});
		checkBlogViews();	
		//updateMetaTags();
});

function checkBlogViews(){
	let url = location.href.split("/").slice(-3);
	if (url[0] == "blog"){
		getPageViews(url[1]);
		incrementPageViews(url[1]);
	}
};

function getPageViews(blogName){   
	let pageViews; 
    $.get('/api/v1/getviews/'+ blogName , function(data, status){
		console.log(data);
		pageViews = data["blog_views"];
		console.log(pageViews);
		$('#page-views').html(pageViews);
	});
	// Change page views
	//window.alert(pageViews);
	
};

function incrementPageViews(blogName){
	$.post('/api/v1/incrementviews', {'blog_name': blogName});
};

function updateMetaTags(){
	// Updating og tags
	$('meta[property="og:title"]').attr('content' ,$('#blog-title').text());
	$('meta[property="og:description"]').attr('content', $('#blog-description').text());
	$('meta[property="og:url"]').attr('content', window.location.href);

	// updating twitter tags
	$('meta[name="twitter:title"]').attr('content', $('#blog-title').text());
	$('meta[name="twitter:description"]').attr('content' ,$('#blog-description').text());
	$('meta[name="twitter:url"]').attr('content',window.location.href);
};
