"use strict";
$(document).ready(function(){

	//mobile menu
	$('.mobile-menu-btn').on('click', function(){
		$('.main-menu').toggleClass('main-menu-active');
		$('.mobile-menu-btn i').toggleClass('fa-bars');
		$('.mobile-menu-btn i').toggleClass('fa-times');
	});

	//drop windows for language and phone
	$('.sec-icon').on('click', function(){
		$(this).parent().children('div').toggleClass('drop-show');
	});
	$('.phone-num .sec-icon').on('click', function(){
		$('.lang-menu div').removeClass('drop-show');
	});
	$('.lang-menu .sec-icon').on('click', function(){
		$('.phone-num div').removeClass('drop-show');
	});


	// phone animation
	let animInterval;
	$('.drop-number a').on('mouseover', function(){
		let elem = $('.phone-num .sec-icon');
		animInterval = setInterval(function(){
			elem.css('transform', 'rotateZ(10deg)');
			setTimeout(function(){
			elem.css('transform', 'rotateZ(-10deg)');
			}, 400);
		}, 1000);
	});
	$('.drop-number a').on('mouseleave', function(){
		$('.phone-num .sec-icon').css('transform', 'rotateZ(0deg)');
		clearInterval(animInterval);
	});

	// animating product menu
	let height_p = (3.3 + 1.5 * $('#products').children('.main-cat').children('li').length) * 1.1 + 1;
	$('#prod-men').on('click', function(){
		closeBigMenu($('#company'));
		menu_c_shown = false;
		openBigMenu($('#products'), height_p, menu_p_shown);	
		menu_p_shown = !menu_p_shown ? true : false;
	});
	$('#close-prod').on('click', function(){
		menu_p_shown = false;
		closeBigMenu($('#products'));
	});

	$('.main-cat li').on('click', function(){
		let cat_id = parseInt($(this).attr('id').slice(-1,));
		$('.sub-cat').css('display', 'none');
		$(`#sub-cat-${cat_id}`).css('display', 'flex');
	});
	
	// animating company menu
	let height_c = (3.3 + 1.5 * $('#company').children('.main-cat').children('a').length) * 1.1 + 1;
	$('#company-men').on('click', function(){
		closeBigMenu($('#products'));
		menu_p_shown = false;
		openBigMenu($('#company'), height_c, menu_c_shown);
		menu_c_shown = !menu_c_shown ? true : false;
	});
	$('#close-comp').on('click', function(){
		menu_c_shown = false;
		closeBigMenu($('#company'));
	});

	let menu_p_shown = false;
	let menu_c_shown = false;

	function openBigMenu(el, height, flag){
		if(!flag){
			$(el).children('.main-cat').animate({'height': `${height}em`}, 200);
			$(el).css('padding', '2em 3em 2em 3em');
			$(el).children('.bottom-line').css('display', 'flex');
			setTimeout(function(){
				$(el).children('.main-cat').css('height', 'auto');
				$('.transparent-layer').fadeIn();
			}, 200);
		}else {
			$('.transparent-layer').fadeOut();
			$('.sub-cat').css('display', 'none');
			$(el).children('.main-cat').animate({'height': '0px'}, 200);
			$(el).children('.bottom-line').css('display', 'none');
			setTimeout(function(){$(el).css('padding', '0px');}, 200);
		}
	}

	function closeBigMenu(el){
		$('.transparent-layer').fadeOut();
		$('.sub-cat').css('display', 'none');
		$(el).children('.main-cat').animate({'height': '0px'}, 200);
		$('.bottom-line').css('display', 'none');
		setTimeout(function(){$(el).css('padding', '0px');}, 200);
	}

	jQuery(document).on('scroll', function(){
		let s_top = jQuery(document).scrollTop();
		if(s_top > 50){
			jQuery('.nav-sec').addClass('nav-sec-scroll');
		}else {
			jQuery('.nav-sec').removeClass('nav-sec-scroll');
		}
	});
});