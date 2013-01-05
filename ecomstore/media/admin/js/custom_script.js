function prepareDocument(){
	jQuery("#submit_review").click(addProductReview);
	jQuery("#review_form").addClass('hidden');
	jQuery("#add_review").click(slideToggleReviewForm);
	jQuery("#add_review").addClass('visible');
	jQuery("#cancel_review").click(slideToggleReviewForm);

}

// toggles visibility of "write review" link
// and the review form.
function slideToggleReviewForm(){
jQuery("#review_form").slideToggle();
jQuery("#add_review").slideToggle();
}

function addProductReview(){
// build an object of review data to submit
var review = {
title: jQuery("#id_title").val(),
content: jQuery("#id_content").val(),
rating: jQuery("#id_rating").val(),
slug: jQuery("#id_slug").val() };
// make request, process response
jQuery.post("/review/product/add/", review,
function(response){
jQuery("#review_errors").empty();
// evaluate the "success" parameter
if(response.success == "True"){
// disable the submit button to prevent duplicates
jQuery("#submit_review").attr('disabled','disabled');
// if this is first review, get rid of "no reviews" text
jQuery("#no_reviews").empty();
// add the new review to the reviews section
jQuery("#reviews").prepend(response.html).slideDown();
// get the newly added review and style it with color
new_review = jQuery("#reviews").children(":first");
new_review.addClass('new_review');
// hide the review form
jQuery("#review_form").slideToggle();
}
else{
// add the error text to the review_errors div
jQuery("#review_errors").append(response.html);
}
}, "json");
}


$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
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



jQuery(document).ready(prepareDocument);