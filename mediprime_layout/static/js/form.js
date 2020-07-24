$(document).ready(function(){
	$('#send').on('click', function(event){
		if(
			$('#name').val() == '' ||
			$('#topic').val() == '' ||
			$('#email').val() == '' ||
			$('#phone').val() == '' ||
			$('#message').val() == '' 
		){
			alert("Заполните все поля формы перед отпрвкой!");
		}else {
			jQuery(this).attr('type', 'submit');
		}
	});
});