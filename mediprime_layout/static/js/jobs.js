$(document).ready(function(){
	let jobs_height = [];
	$('.job-item-info').each(function(){
		jobs_height.push($(this).outerHeight(true) + 16*5);
		$(this).css('height', '0');
		$(this).css('padding', '0');
	});

	$('.job-item-thumbnail').on('click', function(){
		closeJob($('.job-active'));
		openJob(this);
	});

	function openJob(elem){
		let index = parseInt($(elem).parent().attr('id').slice(-1,)) - 1;
		$(elem).parent().children('.job-item-info').animate({'height': `${jobs_height[index]}px`}, 300);
		$(elem).parent().children('.job-item-info').addClass('job-active');
		$(elem).children('i').removeClass('fa-folder');
		$(elem).children('i').addClass('fa-folder-open');
	}

	function closeJob(elem){
		$(elem).parent().children('.job-item-info').animate({'height': '0px'}, 300);
		$(elem).parent().children('.job-item-info').removeClass('job-active');
		$(elem).parent().children('.job-item-thumbnail').children('i').removeClass('fa-folder-open');
		$(elem).parent().children('.job-item-thumbnail').children('i').addClass('fa-folder');
	}
});