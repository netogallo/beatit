(function(){

    function get_form_values(form){

	var data = {};
	$(form).find('input, textarea, select').each(
	    function(i, field) {
		data[field.name] = field.value;
	});

	return data;
    };

    $('.save_post_form').on('submit', function(e){
        e.preventDefault();
	console.log(get_form_values(this));
    });
})();
