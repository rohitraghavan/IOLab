$($("#submit").on('click', function() {
	
	search = $("#search").val();
	
	//Call SoundCloud API and pass search term
	callAPI(search);
}))

function display_songs(data) {
	
	//Clear previous search results, if any
	$("#search-results").empty();
	
	//Get position of search results insertion
	searchResults = $("#search-results");
	
	//HTML template code for a song entry
	htmlTR = "<tr>\
				<td><button type='button'class='play btn btn-default' playUrl='playLink'><span class='glyphicon glyphicon-play' aria-hidden='true'></span></button></td>\
				<td rowspan='2'><img data-src='holder.js/200x200' class='img-thumbnail' src='url'></td>\
				<td class='tit'>title</td>\
			</tr>\
			<tr>\
				<td><button type='button' class='add-playlist btn btn-default'><span class='glyphicon glyphicon-list' aria-hidden='true'></span></button></td>\
				<td class='art'>artist</td>\
			</tr>";
	
	//Restrict results to first 20 songs
	if (data.length > 20)
		maxLoop = 20;
	else
		maxLoop = data.length;
	
	//Display the first 20 songs in the Search Results panel
	for (var i=0; i < maxLoop; i++) {
		
		// Replace HTML template code with actual song details
		tableRow = htmlTR;
		albumArt = data[i].artwork_url;
		artist = data[i].user.username;
		title = data[i].title;
		playUrl = data[i].permalink_url;
		if (albumArt == null)
			albumArt = "no_album_artwork.jpg";
		tableRow = tableRow.replace("url", albumArt);
		tableRow = tableRow.replace("title", title);
		tableRow = tableRow.replace("artist", artist);
		tableRow = tableRow.replace("playLink", playUrl);
		//Append to Search Results panel
		searchResults.append(tableRow);
	}

	//Associate play button click to play in the stratus player
	$(".play").off('click');
	$(".play").on('click', function() {
		playUrl = $(this).attr("playUrl");
		if (playUrl != null) {
			changeTrack(playUrl);
		}
	});

	//Associate add-playlist button click to add song to the playlist panel
	$(".add-playlist").off('click');
	$(".add-playlist").on('click', function() {

		//Get parent of parent of add-playlist button i.e <tr>
		main_tr = $(this).parent().parent().clone();
		//Get previous sibling of parent of parent of button i.e prev <tr>
		sib_tr = $(this).parent().parent().prev().clone();

		//Search if the track already exists in the playlist, if so, dont add.
		playUrlOfTrack = $(this).parent().parent().prev().children().find(".play").attr("playUrl");
		existingInPlaylist = $("#playlist").find("[playUrl='"+playUrlOfTrack+"']");
		if (existingInPlaylist.length != 0)
			return;
		
		//Insert at playlist position
		$("#playlist").prepend(main_tr);
		$("#playlist").prepend(sib_tr);

		//Associate play button click to play in the stratus player
		$(".play").off('click');
		$(".play").on('click', function() {
			playUrl = $(this).attr("playUrl");
			if (playUrl != null) {
				changeTrack(playUrl);
			}
		});

		//Add move up and move down buttons
		$("#playlist .add-playlist").parent().parent().prepend("<td><button type='button' class='movedown-playlist btn btn-default'><span class='glyphicon glyphicon-chevron-down' aria-hidden='true'></span></button></td>");
		$("#playlist .add-playlist").parent().parent().prev().prepend("<td><button type='button' class='moveup-playlist btn btn-default'><span class='glyphicon glyphicon-chevron-up' aria-hidden='true'></span></button></td>");
		
		//Associate move up and move down button clicks to move tracks up or down in the playlist
		$(".movedown-playlist").off('click');
		$(".movedown-playlist").on('click', function() {
			
			main_tr = $(this).parent().parent();
			sib_tr = $(this).parent().parent().prev();
			if (main_tr.next().length != 0) {
				next = main_tr.next().next();
				sib_tr.insertAfter(next);
				main_tr.insertAfter(sib_tr);
			}
		});
		$(".moveup-playlist").off('click');
		$(".moveup-playlist").on('click', function() {
			
			main_tr = $(this).parent().parent();
			sib_tr = $(this).parent().parent().next();
			if (main_tr.prev().length != 0) {
				prev = main_tr.prev().prev();
				sib_tr.insertBefore(prev);
				main_tr.insertBefore(sib_tr);
			}
		});

		//Replace playlist button with remove button.
		$("#playlist .add-playlist").replaceWith("<button type='button' class='remove-playlist btn btn-default'><span class='glyphicon glyphicon-remove' aria-hidden='true'></span></button>");
		//Associate remove-playlist button click to remove songs from playlist panel
		$(".remove-playlist").off('click');
		$(".remove-playlist").on('click', function() {
			
			$(this).parent().parent().prev().remove();
			$(this).parent().parent().remove();
		});
	});
}

// Event hander for calling the SoundCloud API using the user's search query
function callAPI(query) {
	$.get("https://api.soundcloud.com/tracks?client_id=b3179c0738764e846066975c2571aebb",
		{'q': query,
		'limit': '200'},
		function(data) {
			// PUT IN YOUR CODE HERE TO PROCESS THE SOUNDCLOUD API'S RESPONSE OBJECT
			// HINT: CREATE A SEPARATE FUNCTION AND CALL IT HERE
			//Display songs in Search Results panel
			display_songs(data);
		},'json'
	);
}

// 'Play' button event handler - play the track in the Stratus player
function changeTrack(url) {
	// Remove any existing instances of the Stratus player
	$('#stratus').remove();

	// Create a new Stratus player using the clicked song's permalink URL
	$.stratus({
      key: "b3179c0738764e846066975c2571aebb",
      auto_play: true,
      align: "bottom",
      links: url
    });
}


