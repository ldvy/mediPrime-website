$(document).ready(function(){
	//animating infographic counters 
	let info_nums = []; 
	let counter_dur = 1500;
	$('.info-graph-counter').each(function(){
		info_nums.push(parseInt($(this).html()));
		$(this).html("0+");
	});

	let counters = $('.info-graph-counter');

	function launchCounter(elem, interval, max_count){
		let cur_int = setInterval(function(){
			let cur = parseInt($(elem).html()) + 1;
			if(cur == max_count) clearInterval(cur_int);
			$(elem).html(`${cur}+`);
		}, interval);
	}


	let counter_eng = false;
	$(document).on('scroll', function(){
		s_top = $(document).scrollTop();
		if(s_top > $('.info-graph-sec').offset().top/1.5 && !counter_eng){
			counter_eng = true;
			for(let i = 0; i < counters.length; i++){
				launchCounter(counters[i], counter_dur/info_nums[i], info_nums[i]);
			}
		}
	});

	//brand slider 
	let slide_width = $('.brand-slide').outerWidth(true);
	let slider_width = slide_width * $('.brand-slide').length;
	$('.brand-slides').css('width', `${slider_width}px`);

	let max_margin = Math.round($('.brand-slider-window').width() - $('.brand-slides').width()) + 1;
	console.log(slide_width, max_margin);

	let brand_margin = 0;
	function nextSlideBrand(prev = false){
		if(prev && brand_margin == 0){
			brand_margin = 0;
		}else if(brand_margin > max_margin){
			brand_margin = prev ? brand_margin + slide_width : brand_margin - slide_width;
		}else {
			brand_margin = 0;
		}
		$('.brand-slides').css('margin-left', `${brand_margin}px`);
	}

	let brand_interval = setInterval(nextSlideBrand, 1900);

	$('.brand-slider-sec').hover(function(){
		clearInterval(brand_interval);
	}, function(){
		brand_interval = setInterval(nextSlideBrand, 1900);
	});

	$('.left').on('click', function(){nextSlideBrand(true);});
	$('.right').on('click', function(){nextSlideBrand(false);});

	//main slider
	let main_slides = $('.slide-wrap');	
	let slide_btns = $('.slider-btns li');
	let cur_slide = main_slides[0];
	let next_index = 1;

	function nextSlideMain(){
		$(cur_slide).fadeOut(800);
		$('.active').attr('class', '');
		if(next_index < main_slides.length){
			$(main_slides[next_index]).fadeIn(500);
			$(slide_btns[next_index]).addClass('active');
			cur_slide = main_slides[next_index];
			next_index += 1;
		}else {
			$(main_slides[0]).fadeIn(500);
			$(slide_btns[0]).addClass('active');
			cur_slide = main_slides[0];
			next_index = 1;
		}
	}

	let main_slide_interval = setInterval(nextSlideMain, 6000);

	$('.slider-btns').hover(function(){
		clearInterval(main_slide_interval);
	}, function(){
		main_slide_interval = setInterval(nextSlideMain, 6000);
	});

	$('.slider-btns li').on('click', function(){
		let id = parseInt($(this).attr('id').slice(-1,));
		$('.active').attr('class', '');
		$(this).addClass('active');
		$(cur_slide).fadeOut();
		$(`#sl${id}`).fadeIn();
		cur_slide = $(`#sl${id}`);
	});
});