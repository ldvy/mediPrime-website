$(document).ready(function(){
	$('.brand-block').on('click', function(){
		let grids;
		if(
			window.matchMedia('(max-width: 800px)').matches ||
			window.matchMedia("(max-device-aspect-ratio: 9/16)").matches ||
			window.matchMedia("(max-device-aspect-ratio: 9/18)").matches ||
			window.matchMedia("(max-device-aspect-ratio: 2/3)").matches
		){
			grids = 1;
		}else if(window.matchMedia('(max-width: 1160px)').matches){
			grids = 2;
		} else {
			grids = 3;
		}
		let offset_diff = $('.brands-sec').offset().top;
		let brand_height = $('.brand-block').not('.brand-active').outerHeight();
		let brand_width = $('.brand-block').not('.brand-active').outerWidth(true);
		if(grids == 1){
			$(this).css('height', `${brand_height}px`);

			closeBrand();

			let row = parseInt($(this).attr('id').slice(-1,));

			$(this).children('.brand-thumbnail').css('height', '25%');
			$(this).children('.brand-desc').css('height', '75%');
			$(this).css('grid-row', `${row}/${row+2}`);
			$(this).addClass('brand-active');
			$(this).css('height', `${brand_height * 2}px`);
			$(this).children('.brand-desc').children('.more-bullets').css('display', 'none');
			$(this).children('.brand-desc').css('overflow-y', 'scroll');
			$(this).children('.close-brand').fadeIn();
		}else {
			$(this).css('width', `${brand_width}px`);

			closeBrand();

			let row = Math.round(($(this).offset().top - offset_diff) / brand_height + 1);

			$(this).children('.brand-desc').css('width', '90%');
			$(this).css('grid-row', `${row}/${row+1}`);
			$(this).addClass('brand-active');
			$(this).css('width', `${brand_width * grids}px`);
			$(this).children('.brand-desc').children('.more-bullets').css('display', 'none');
			$(this).children('.brand-desc').css('overflow-y', 'scroll');
			$(this).children('.close-brand').fadeIn();
		}
	});

	$('.close-brand').on('click', function(event){
		event.stopPropagation();
		closeBrand();
	});

	function closeBrand(){
		let grids;
		let elem = $('.brand-active');
		let brand_width = $('.brand-block').not('.brand-active').outerWidth(true);
		let brand_height = $('.brand-block').not('.brand-active').outerHeight();
		if(
			window.matchMedia('(max-width: 800px)').matches ||
			window.matchMedia("(max-device-aspect-ratio: 9/16)").matches ||
			window.matchMedia("(max-device-aspect-ratio: 9/18)").matches ||
			window.matchMedia("(max-device-aspect-ratio: 2/3)").matches
		){
			grids = 1;
		} else {
			grids = 3;
		}
		if(grids == 1){
			$('.brand-active').css('height', `${brand_height}px`);
			$('.brand-active').css('grid-row', 'auto');
			$('.brand-active').children('.close-brand').fadeOut();
			$('.brand-active').children('.brand-thumbnail').css('height', '50%');
			$('.brand-active').children('.brand-desc').css('height', '45%');
			$('.brand-active').children('.brand-desc').children('.more-bullets').css('display', 'flex');
			$('.brand-active').children('.brand-desc').css('overflow', 'hidden');
			$('.brand-active').removeClass('brand-active');
		}else {
			$('.brand-active').css('width', `${brand_width}px`);
			setTimeout(function(){
				$(elem).css('width', 'auto');
			}, 500);
			$('.brand-active').css('grid-row', 'auto');
			$('.brand-active').children('.close-brand').fadeOut();
			$('.brand-active').children('.brand-desc').css('width', '75%');
			$('.brand-active').children('.brand-desc').children('.more-bullets').css('display', 'flex');
			$('.brand-active').children('.brand-desc').css('overflow', 'hidden');
			$('.brand-active').removeClass('brand-active');
		}
	}
});