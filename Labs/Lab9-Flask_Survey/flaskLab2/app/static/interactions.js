$('#submit-survey').on('click', function submitSurvey() {
	var favClass = $("input[name=fav-class]").val();
	var assignments = $("input[name=assignments]").val();
	var professor = $("input[name=professor]").val();
	var feBefore = $("input[name=front-end-before]").val();
	var feAfter = $("input[name=front-end-after]").val();
	$.post("submit-survey", 
		{favClass: favClass,
		assignments: assignments,
		professor: professor,
		feBefore: feBefore,
		feAfter: feAfter},
		function(data){
			$("html").html(data);
		}
	)
});

$("#results-email-container").on('click', '#email-results-button', function emailResults() {
	console.log($(this));
});

$("#site-title-wrapper").on('click', function goHome() {
	window.location.href = '/';
});

$(document).ready(function applySliderLabels() {
	var currentValue = $("#fe-before").val();
	$("#fe-before").next().html(currentValue);

	currentValue = $("#fe-after").val();
	$("#fe-after").next().html(currentValue);
});


$("input[type='range']").on('change', function updateLabel() {
	var currentValue = $(this).val();
	$(this).next().html(currentValue);
});