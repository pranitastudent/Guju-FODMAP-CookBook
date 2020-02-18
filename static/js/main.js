// Year-  Code Taken from Brad Traversy's Course Python Django to Dev (Nov 2018)
const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// End of Code taken

// Fade Out JS for Alerts

setTimeout(function(){
    $('#message').fadeOut('fast');
}, 2000);

// Back To The Top Button- adapted from  Traversy Media you tube video project :'myTunes Site'

$(document).ready(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 400) {
            $('#topBtn').fadeIn();
        }
        else {
            $("#topBtn").fadeOut();
        }
    });
    // scroll body to 0px on click
    $('#topBtn').click(function() {
        $('body,html').animate({
                scrollTop: 0
            },
            100
        );
        return false;
    });
});