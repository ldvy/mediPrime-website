$(document).ready(function(){
	$('.reagent-prev').on('click', function(){
		if(
			window.matchMedia("(max-width: 750px)").matches ||
			window.matchMedia("(max-device-aspect-ratio: 9/16)").matches ||
			window.matchMedia("(max-device-aspect-ratio: 9/18)").matches ||
			window.matchMedia("(max-device-aspect-ratio: 2/3)").matches
		){
			let height = $(this).height();

			$('.desc-active').css('top', 0);
			$('.desc-active').parent().css('margin-bottom', '1.5vw');
			$('.desc-active').removeClass('desc-active');

			$(this).parent().children('.reagent-desc').addClass('desc-active');
			$(this).parent().css('margin-bottom', height);
			$(this).parent().children('.reagent-desc').css('top', height);
		}else{
			let width = $(this).width();

			$('.desc-active').css('left', 0);
			$('.desc-active').parent().css('margin-right', '1.5vw');
			$('.desc-active').removeClass('desc-active');

			$(this).parent().children('.reagent-desc').addClass('desc-active');
			$(this).parent().css('margin-right', width);
			$(this).parent().children('.reagent-desc').css('left', width);
		}
	});

	$('.close-desc').on('click', function(){
		if(
			window.matchMedia("(max-width: 750px)").matches ||
			window.matchMedia("(max-device-aspect-ratio: 9/16)").matches ||
			window.matchMedia("(max-device-aspect-ratio: 9/18)").matches ||
			window.matchMedia("(max-device-aspect-ratio: 2/3)").matches
		){
			$(this).parent().css('top', 0);
			$(this).parent().parent().css('margin-bottom', '1.5vw');
		}else {
			$(this).parent().css('left', 0);
			$(this).parent().parent().css('margin-right', '1.5vw');
		}
	});
});