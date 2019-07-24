$(document).ready(function() {
	// Variable to get the shuffle button
    var shuffle = document.getElementById('shuffle');

    // Variable to get the div contained in the ticker row
   	var stocks = $(".ticker-row div");

   	// Used to store the randomly genrated index's
   	var randPos1, randPos2;

   	// This function loops through the number of items in stocks
   	// and generates a random index between 1 and 3 and then using
   	// the eq method the items are swapped.
	shuffle.onclick = function() {
		for(var i = 0, length = stocks.length; i < length; i++) {
			randPos1 = Math.floor(Math.random() * length-1) + 1;
			randPos2 = Math.floor(Math.random() * length-1) + 1;
			stocks.eq(randPos1).before(stocks.eq(randPos2));
		}
	}
});
 
