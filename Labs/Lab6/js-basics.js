function increment_counter(counter_name){
	var counter = document.getElementById(counter_name).value;
	counter++;
	document.getElementById(counter_name).value = counter;
}