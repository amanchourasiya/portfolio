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
		loop: true,
		autoplay: true,
		autoplayTimeout: 2500,
		responsive: responsive,
	});
	checkBlogViews();
	addLikeButtonListener();
});

function checkBlogViews() {
	let url = location.href.split("/").slice(-3);
	if (url[0] == "blog") {
		getPageViews(url[1]);
		incrementPageViews(url[1]);
	}
};

function getPageViews(blogName) {
	let pageViews;
	let pageClaps;
	$.get('/api/v1/getviews/' + blogName, function (data, status) {
		console.log(data);
		pageViews = data["blog_views"];
		pageClaps = data["blog_claps"];
		console.log(pageViews);
		console.log(pageClaps);
		$('#page-views').html(pageViews);
		$('#page-likes').html(pageClaps);
		
	});
};

function incrementPageViews(blogName) {
	$.post('/api/v1/incrementviews', { 'blog_name': blogName });
};

function incrementClaps(blogName) {
	$.post('/api/v1/incrementclaps', { 'blog_name': blogName });
};

function addLikeButtonListener() {
        let btnlike = document.querySelector('#likebutton')
        btnlike.addEventListener('click',() => btnlike.style.color='#1d2124')
};
