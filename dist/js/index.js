$(document).ready(function(){
    $('#adalt').click(function(){
		$('body, html').animate({
			scrollTop: '0px'
		}, 300);
	});
	
	$('#YES').click(function(){
	var usuari=$(this).closest('.item').data('usuari');
	alert(usuari);
	});
	
})