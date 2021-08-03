function onClickMenu(){
	document.getElementById("menu").classList.toggle("change");
	document.getElementById("nav").classList.toggle("change");
	document.getElementById("social").classList.toggle("change");
	document.getElementById("menu-bg").classList.toggle("change-bg");
}

/*carousel*/
$(document).ready(function(){
	

	$(".slider").slick({
	infinite: true,
	arrows: false,
	dots: false,
	autoplay: false,
	speed: 800,
	slidesToShow: 1,
	slidesToScroll: 1,
	});

	//ticking machine
	var percentTime;
	var tick;
	var time = 1;
	var progressBarIndex = 0;

	$('.progressBarContainer .progressBar').each(function(index) {
	    var progress = "<div class='inProgress inProgress" + index + "'></div>";
	    $(this).html(progress);
	});

	function startProgressbar() {
	    resetProgressbar();
	    percentTime = 0;
	    tick = setInterval(interval, 10);
	}

	function interval() {
	    if (($('.slider .slick-track div[data-slick-index="' + progressBarIndex + '"]').attr("aria-hidden")) === "true") {
	        progressBarIndex = $('.slider .slick-track div[aria-hidden="false"]').data("slickIndex");
	        startProgressbar();
	    } else {
	        percentTime += 1 / (time + 5);
	        $('.inProgress' + progressBarIndex).css({
	            height: percentTime + "%"
	        });
	        if (percentTime >= 100) {
	            $('.single-item').slick('slickNext');
	            progressBarIndex++;
	            if (progressBarIndex > 2) {
	                progressBarIndex = 0;
	            }
	            startProgressbar();
	        }
	    }
	}

	function resetProgressbar() {
	    $('.inProgress').css({
	        height: 0 + '%'
	    });
	    clearInterval(tick);
	}
	startProgressbar();
	// End ticking machine

	$('.progressBarContainer div').click(function () {
		clearInterval(tick);
		var goToThisIndex = $(this).find("span").data("slickIndex");
		$('.single-item').slick('slickGoTo', goToThisIndex, false);
		startProgressbar();
	});
	
		
});


