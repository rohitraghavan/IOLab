$(document).ready(  
    $(function() {
    $("#list-todo").sortable();
    $("#list-completed").sortable();
  })
);

$("#new-item").on('click', function() {
    inputVal = $("#input-val").val();
    listItemHTMLStart = "<li class=\"list-group-item\">\
    					<span class=\"glyphicon glyphicon-sort\" aria-hidden=\"true\"></span>"
    listItemHTMLEnd = "</li>";
    listToDo = $("#list-todo");
    if(inputVal != "") {
    	listItem = listItemHTMLStart + inputVal + listItemHTMLEnd;
    	$('#input-val').val('');
        $(listItem).hide().prependTo(listToDo).slideDown("slow");
    }
})


$("#list-todo").on('click', "li", function() {
        listCompleted = $("#list-completed");
        $(this).hide().prependTo(listCompleted).slideDown("slow")
});

$("#list-completed").on('click', "li", function() {
        listToDo = $("#list-todo");
        $(this).hide().prependTo(listToDo).slideDown("slow")
});
