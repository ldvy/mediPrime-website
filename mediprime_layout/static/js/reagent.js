$(document).ready(function(){
	$('.reagent-prev').on('click', function(){
		let width = $(this).width();

		$('.desc-active').css('left', 0);
		$('.desc-active').parent().css('margin-right', '1.5vw');
		$('.desc-active').removeClass('desc-active');

		$(this).parent().children('.reagent-desc').addClass('desc-active');
		$(this).parent().css('margin-right', width);
		$(this).parent().children('.reagent-desc').css('left', width);
	});

	$('.close-desc').on('click', function(){
		$(this).parent().css('left', 0);
		$(this).parent().parent().css('margin-right', '1.5vw');
	});
});