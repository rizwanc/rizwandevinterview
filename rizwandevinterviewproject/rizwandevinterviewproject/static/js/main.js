$(document).ready(function() {
    var shuffle = document.getElementById('shuffle');
   	var stocks = $(".ticker-row div");
   	var randPos1, randPos2;
   	var addComment = document.getElementById('addCommentButton');

	shuffle.onclick = function() {
		for(var i = 0, length = stocks.length; i < length; i++) {
			randPos1 = Math.floor(Math.random() * length-1) + 1;
			randPos2 = Math.floor(Math.random() * length-1) + 1;
			stocks.eq(randPos1).before(stocks.eq(randPos2));
		}
	}
});
 
