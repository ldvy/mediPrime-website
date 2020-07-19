$(document).ready(function(){

	//toggling text-blocks in description
	$('.model-info:first-child').fadeIn();

	$('.prop-btn').on('click', function(){
		$('.active').removeClass('active');
		$(this).addClass('active');
		let block_to_open = $(this).attr('id');
		$('.cur-block').fadeOut(0);
		$('.cur-block').removeClass('.cur-block');
		$(`.${block_to_open}`).fadeIn();
		$(`.${block_to_open}`).addClass('cur-block');
	});


	//model slider

	let slide_height = $('.model-slide').outerHeight(true); 
	let tape_height = slide_height * $('.model-slide').length;
	let max_margin = Math.round($('.model-slider-window').height() - tape_height) + 1;

	let tape_margin = 0;

	function nextImgModel(prev = false){
		if(prev && tape_margin == 0){
			tape_margin = 0;
		}else if(tape_margin > max_margin){
			tape_margin = prev ? tape_margin + slide_height : tape_margin - slide_height;
		}else {
			tape_margin = 0;
		}
		$('.model-slider-tape').css('margin-top', `${tape_margin}px`);
	}

	$('.prev').on('click', function(){nextImgModel(true);});
	$('.next').on('click', function(){nextImgModel();});

	$('.model-slide').on('click', function(){
		$('.cur-slide').removeClass('cur-slide');
		$(this).addClass('cur-slide');
		let img = $(this).css('background-image');
		$('.slider-prev').css('background-image', img);
	});
});