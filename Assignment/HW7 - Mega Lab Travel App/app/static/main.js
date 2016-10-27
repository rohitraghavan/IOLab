$(document).ready(function() {
    $('select').material_select();
});

$(".delete-row").click(function() {
    var tripName = $(this).closest('tr').children()[0].innerHTML
    var trRemove = $(this).closest('tr')
    $.ajax({
			type: "POST",
			url: "/delete_trip",
			data: JSON.stringify({ "tripName" : tripName }),
			contentType: "application/json",
			success: function(response){
				console.log(response)
				$(this).closest('tr').remove()
				trRemove.fadeOut(1000,function(){ 
                            trRemove.remove();                    
                });
			}
	});
});