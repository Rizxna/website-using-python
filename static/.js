// C$(function() {
    $('#side-menu').metisMenu();


//Loads the correct sidebar on window load,
//collapses the sidebar on window resize.
// Sets the min-height of #page-wrapper to window size
$(function() {
    $(window).bind("load resize", function() {
        var topOffset = 50;
        var width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
        if (width < 768) {
            $('div.navbar-collapse').addClass('collapse');
            topOffset = 100; // 2-row-menu
        } else {
            $('div.navbar-collapse').removeClass('collapse');
        }

        var height = ((this.window.innerHeight > 0) ? this.window.innerHeight : this.screen.height) - 1;
        height = height - topOffset;
        if (height < 1) height = 1;
        if (height > topOffset) {
            $("#page-wrapper").css("min-height", (height) + "px");
        }
    });

    var url = window.location;
    // var element = $('ul.nav a').filter(function() {
    //     return this.href == url;
    // }).addClass('active').parent().parent().addClass('in').parent();
    var element = $('ul.nav a').filter(function() {
        return this.href == url;
    }).addClass('active').parent();

    while (true) {
        if (element.is('li')) {
            element = element.parent().addClass('in').parent();
        } else {
            break;
        }
    }
});


// Sample function for handling user login
function handleLogin() {
    // Your login logic here
    // For example, you can show a login modal or redirect to the login page
    console.log('User clicked on login button');
}

// Sample function for handling user signup
function handleSignup() {
    // Your signup logic here
    // For example, you can show a signup modal or redirect to the signup page
    console.log('User clicked on signup button');
}

// Sample function for handling project submission
function submitProject() {
    // Your project submission logic here
    // For example, you can validate the project details and send them to the server
    console.log('User submitted a project');
}

// Sample function for displaying live stream updates
function showLiveStream() {
    // Your live stream update logic here
    // For example, you can fetch live stream data from the server and display it
    console.log('Fetching and displaying live stream updates');
}

// Sample function for sharing on social media
function shareOnSocialMedia(platform) {
    // Your social sharing logic here
    // For example, you can use a JavaScript library to handle social sharing
    console.log(`User clicked on share to ${platform}`);
}

// Sample function for supporting a project
function supportProject() {
    // Your project support logic here
    // For example, you can display a support modal or redirect to the project support page
    console.log('User clicked on support button');
}

// Add event listeners for buttons and elements
document.addEventListener('DOMContentLoaded', function () {
    const loginButton = document.getElementById('login-button');
    const signupButton = document.getElementById('signup-button');
    const submitButton = document.getElementById('submit-button');
    const liveStreamButton = document.getElementById('live-stream-button');
    const facebookShareButton = document.getElementById('facebook-share');
    const instagramShareButton = document.getElementById('instagram-share');
    const twitterShareButton = document.getElementById('twitter-share');
    const redditShareButton = document.getElementById('reddit-share');
    const linkedinShareButton = document.getElementById('linkedin-share');
    const supportButton = document.getElementById('support-button');

    loginButton.addEventListener('click', handleLogin);
    signupButton.addEventListener('click', handleSignup);
    submitButton.addEventListener('click', submitProject);
    liveStreamButton.addEventListener('click', showLiveStream);
    facebookShareButton.addEventListener('click', () => shareOnSocialMedia('Facebook'));
    instagramShareButton.addEventListener('click', () => shareOnSocialMedia('Instagram'));
    twitterShareButton.addEventListener('click', () => shareOnSocialMedia('Twitter'));
    redditShareButton.addEventListener('click', () => shareOnSocialMedia('Reddit'));
    linkedinShareButton.addEventListener('click', () => shareOnSocialMedia('LinkedIn'));
    supportButton.addEventListener('click', supportProject);
});
