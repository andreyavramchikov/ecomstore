function prepareDocument(){
	$("#submit_review").click(addProductReview);
	$("#review_form").addClass('hidden');
	$("#add_review").click(slideToggleReviewForm);
	$("#add_review").addClass('visible');
	$("#cancel_review").click(slideToggleReviewForm);

}


function slideToggleReviewForm(){
	$("#review_form").slideToggle();
	$("#add_review").slideToggle();
}

function addProductReview(){
	var review = {
		title: $("#id_title").val(),
		content: $("#id_content").val(),
		rating: $("#id_rating").val(),
		slug: $("#id_slug").val() 
	};
	// make request, process response
	$.post("/review/product/add/", review,
	function(response){
		$("#review_errors").empty();
		if(response.success == "True"){
			$("#submit_review").attr('disabled','disabled');
			
			
			$("#no_reviews").empty();
			
			$("#reviews").prepend(response.html).slideDown();
			
			new_review = $("#reviews").children(":first");
			new_review.addClass('new_review');

			$("#review_form").slideToggle();
		}
		else{
			// add the error text to the review_errors div
			$("#review_errors").append(response.html);
		}
	}, "json");
}


$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = $.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});



$(document).ready(prepareDocument);