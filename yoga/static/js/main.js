

// Search for yoga
$( "#search" ).on('keypress', searchingYoga);

function searchingYoga(e){
	var $container = $('#contenedor').isotope({
    	itemSelector: '.grid-25',
    	getSortData: {
      		name: '[data-name]'
      	}
    });

	var searchValue = $(this).val();
	if(e.which == 13){
		//searchValue = filterFns[ filterValue ] || filterValue;
		$container.isotope({ filter: searchValue });
	}
}
