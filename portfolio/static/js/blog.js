$(document).ready(function () {
	checkBlogViews();
    addLikeButtonListener();
    updateSocialUrl();
});

function checkBlogViews() {
	let blogName = getBlogName();
	if (blogName != ''){
		getPageViews(blogName);
		incrementPageViews(blogName);
	}
};

function getBlogName() {
	let url = location.href.split("/").slice(-3);
	if (url[0] == "blog") {
		return url[1];
	}
	return '';
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

let pageAlreadyLiked = false;
function incrementClaps() {
	// Increment local count
	if (pageAlreadyLiked == true){
		return;
	}
	pageAlreadyLiked = true;
	pageLikes = $('#page-likes').html();
	$('#page-likes').html(parseInt(pageLikes, 10) + 1);

	// Increment remote data
	let blogName = getBlogName();
	$.post('/api/v1/incrementclaps', { 'blog_name': blogName });
};

function addLikeButtonListener() {
        let btnlike = document.querySelector('#likebutton')
        btnlike.addEventListener('click',() => btnlike.style.color='#1d2124')
};

function updateSocialUrl(){
    let socialShare = [".fa-linkedin", ".fa-twitter", ".fa-facebook", ".fa-reddit-alien"]
    socialShare.forEach(function(item){
        $(item).attr('href',$(item).attr('href') + window.location.href);
    });
};
