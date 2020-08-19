const options = {
    includeScore: true,
    keys: ['name', 'labels']
}

const fuse = new Fuse(items, options)

// creates and returns an item container to the box for search return.
function createItemContainer(item) {
    let item_container = 	$(`<div class='course-container'>
								<h3>${item['name']}</h3>
								<ul></ul>
                            </div>`);

	labelList = item['labels'].toString();

	var newLabels = labelList.replace(/,/g, ' - ');

    let newItem = 	$(`<li>
								<table class="section_table">
									<tr>
										<td><a href=${item['product']}> Product Link </a></td>
										<td>Tags:<br>${newLabels}</td>
										<td><img src=\"${item['image']}\" alt="" border=3 height=100 width=100></img></td>
									</tr>
								</table>
                            </li>`);
                            
    let ul = item_container.find('ul');
    ul.append(newItem);

    // return no html if no sections pass the filter
	if (ul.children().length == 0) {
		return null;
	} else {
		return item_container;
	}
}

// perform search using user input in the search bar, display results
function executeSearch() {
	let user_input = $('#search-box').val().toUpperCase();
		
	// clears search results
	$('#search-return').empty();

	// display search hint when input box is empty
	// if (user_input == ""){
		// $('#search-return').append(emptySearchFieldInfo());
    // }
    
    var results = fuse.search(user_input)
	
	for (result of results) {
        console.log(result)
		if (result['score'] < 0.3) {
            $('#search-return').append(createItemContainer(result.item));
        }
		
	}
	
	// display a message if no results is returned
	if ($('#search-return').children().length == 0) {
		$('#search-return').append(`<li style='border: 3px solid black;'>
										<h3>Sorry, we couldn't find what you were looking for.</h3>
									</li>`)
	}
}

// wait until html elements are ready and execute code within
$(document).ready(function () {	
	
	// create behavior for when text is entered in the input box
	$('#search-box').on('input', executeSearch);

})