$(document).ready(function(){
	let offset_diff = $('.brands-sec').offset().top;
	let brand_height = $('.brand-block').outerHeight();
	let brand_width = $('.brand-block').outerWidth(true);
	$('.brand-block').on('click', function(){
		$(this).css('width', `${brand_width}px`);

		$('.brand-active').css('width', `${brand_width}px`);
		$('.brand-active').css('grid-row', 'auto');
		$('.brand-active').children('.close-brand').fadeOut();
		$('.brand-active').children('.brand-desc').css('width', '75%');
		$('.brand-active').children('.brand-desc').children('.more-bullets').css('display', 'flex');
		$('.brand-active').removeClass('brand-active');

		let row = Math.round(($(this).offset().top - offset_diff) / brand_height + 1);

		$(this).children('.brand-desc').css('width', '90%');
		$(this).css('grid-row', `${row}/${row+1}`);
		$(this).addClass('brand-active');
		$(this).css('width', `${brand_width * 3}px`);
		$(this).children('.brand-desc').children('.more-bullets').css('display', 'none');
		$(this).children('.close-brand').fadeIn();
	});

	$('.close-brand').on('click', function(event){
		event.stopPropagation();
		$('.brand-active').css('width', `${brand_width}px`);
		$('.brand-active').css('grid-row', 'auto');
		$('.brand-active').children('.close-brand').fadeOut();
		$('.brand-active').children('.brand-desc').css('width', '75%');
		$('.brand-active').children('.brand-desc').children('.more-bullets').css('display', 'flex');
		$('.brand-active').removeClass('brand-active');
	});
});