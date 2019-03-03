(function($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });


  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#sideNav'
  });

  // $(function () {
  //   $('[data-toggle="tooltip"]').tooltip()
  // })

  // $(document).ready(function() {
  //   // executes when HTML-Document is loaded and DOM is ready
  //  console.log("document is ready");
  //   $( ".card" ).hover(function() {
  //     $(this).addClass('shadow-lg').css('cursor', 'pointer');
  //   }, function() {
  //     $(this).removeClass('shadow-lg');
  //   }
  // );
  // });

  // $(document).ready(function() {
  //   // executes when HTML-Document is loaded and DOM is ready
  //  console.log("document is ready");
  //   $( ".a" ).hover(function() {
  //     $(this).addClass('shadow-lg').css('cursor', 'pointer');
  //   }, function() {
  //     $(this).removeClass('shadow-lg');
  //   }
  // );
  // });

  // $(window).scroll(function() {
  //   if ($(this).scrollTop() >= 50) {        // If page is scrolled more than 50px
  //       $('#return-to-top').fadeIn(200);    // Fade in the arrow
  //   } else {
  //       $('#return-to-top').fadeOut(200);   // Else fade out the arrow
  //   }
  //   });
  //   $('#return-to-top').click(function() {      // When arrow is clicked
  //   $('body,html').animate({
  //       scrollTop : 0                       // Scroll to top of body
  //   }, 500);
  // });




})(jQuery); // End of use strict
