ck_config = {
    'awesome_ckeditor': {
        'toolbar': 'Basic',
    }
};

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
	var self = this;
	$.post(
	    '/home/save_post',
	    get_form_values(self),
	    function(data,status,xhr){
		
		console.log(data);
	    });
    });
})();
