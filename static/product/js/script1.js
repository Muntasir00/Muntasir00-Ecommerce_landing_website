window.addEventListener('scroll',function(){
	var header = document.querySelector('.header');
	header.classList.toggle('sticky',window.scrollY > 0);
})

// custom menu
var menu = document.querySelector('#menu');
var menu_btn = document.querySelector('#menu_btn');
var menu_img = document.querySelector('#menu_img');

menu.style.right = '-250px';

menu_btn.onclick = function(){
	if(menu.style.right == '-250px'){
		menu.style.right = '0';
		menu_img.src = 'images/close.png';
		
	}else{
		menu.style.right = '-250px';
		menu_img.src = 'images/menu.png';
	}
}
// custom menu

// header start
$(document).ready(function(){
	$('#search').click(function(){
		$('.menu-item').addClass('hide-item')
		$('.search-form').addClass('active')
		$('.close').addClass('active')
		$('#search').hide()
	})
	$('.close').click(function(){
		$('.menu-item').removeClass('hide-item')
		$('.search-form').removeClass('active')
		$('.close').removeClass('active')
		$('#search').show()
	})

	$('#small_search').click(function(){
		$('.small_logo').addClass('hide-item')
		$('.small_search-form').addClass('active')
		$('.small_close').addClass('active')
		$('#small_search').hide()
	})
	$('.small_close').click(function(){
		$('.small_logo').removeClass('hide-item')
		$('.small_search-form').removeClass('active')
		$('.small_close').removeClass('active')
		$('#small_search').show()
	})

})
// header end
// map start
// function initMap(){
// 	var location = {lat:23.684994, lng:90.356331};
// 	var map = new google.maps.Map(document.querySelector('#main_map'),{
// 		zoom: 4,
// 		center: location
// 	});
// }
// map end
// 23.684994
// 90.356331
// -25.363
// 131.044