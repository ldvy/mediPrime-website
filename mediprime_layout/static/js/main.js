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

	//novation slider
	let nov_slide_width = $('.nov-slide').outerWidth(true);
	let nov_sl_num = $('.nov-slide').length;
	let nov_slider_width = nov_slide_width * nov_sl_num;
	$('.nov-slides-list').css('width', `${nov_slider_width}px`); 
	let nov_max_margin = Math.round($('.nov-slider-window').width() - $('.nov-slides-list').width()) + 1;

	let nov_margin = 0;
	let nov_cur_slide = 0;
	let nov_texts = $('.nov-text-wrap');
	setTimeout(function(){$(nov_texts[nov_cur_slide]).fadeIn();}, 600);

	function nextSlideNov(prev = false){
		$(nov_texts[nov_cur_slide]).fadeOut();
		if(prev && nov_margin == 0){
			nov_margin = 0;
			nov_cur_slide = 0;
		}else if(nov_margin > nov_max_margin){
			nov_margin = prev ? nov_margin + nov_slide_width : nov_margin - nov_slide_width;
			nov_cur_slide = prev ? nov_cur_slide - 1 : nov_cur_slide + 1;
		}else {
			nov_margin = 0;
			nov_cur_slide = 0;
		}
		setTimeout(function(){$('.nov-slides-list').css('margin-left', `${nov_margin}px`);}, 400);
		setTimeout(function(){$(nov_texts[nov_cur_slide]).fadeIn();}, 1000);
	}

	// let nov_interval = setInterval(nextSlideNov, 4000);

	// $('.nov-slider-window').hover(function(){
	// 	clearInterval(nov_interval);
	// }, function(){
	// 	nov_interval = setInterval(nextSlideNov, 4000);
	// });

	// $('.nov-sl-btn').hover(function(){
	// 	clearInterval(nov_interval);
	// }, function(){
	// 	nov_interval = setInterval(nextSlideNov, 4000);
	// });

	$('.nov-left').on('click', function(){nextSlideNov(true);});
	$('.nov-right').on('click', function(){nextSlideNov(false);});

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