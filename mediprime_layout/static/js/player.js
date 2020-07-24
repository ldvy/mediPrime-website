let video = document.querySelector('.video');
let timeBar = document.querySelector('.time_bar');
let timeFill = document.querySelector('.bar_fill');
let btn = document.querySelector('#play_pause');
let bigBtn = document.querySelector('#play');
let pausedBg = document.querySelector('.paused_bg');


video.onclick = function(){
	playPause();
}

bigBtn.onclick = function(){
	playPause();
}

btn.onclick = function(){
	playPause();
}

timeBar.addEventListener('click', function(event){
	timeBarSkip(event);
});

video.addEventListener('timeupdate', function(){
	let fillWidth = video.currentTime / video.duration;
	timeFill.style.width = `${fillWidth * 100}%`;
});

function playPause(){
	if(video.paused){
		btn.children[0].className = 'fa fa-pause';
		pausedBg.style.display = 'none';
		video.play()
	} else {
		btn.children[0].className = 'fa fa-play';
		pausedBg.style.display = 'flex';
		video.pause();
	}
}

function timeBarSkip(click){
	let cord = click.clientX;
	let offsetDiff = (document.body.clientWidth - timeBar.offsetWidth)/2 + 4;
	let newTime = (cord - offsetDiff) / timeBar.offsetWidth;
	timeFill.style.width = `${newTime * 100}%`;
	console.log(video.duration);
	video.currentTime = video.duration * newTime;
}