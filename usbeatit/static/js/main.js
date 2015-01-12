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
		
		if(data.success)
		    window.location.reload();
		console.log(data);
	    });
    });

    $('.delete_post_form').on('submit', function(e){
	e.preventDefault();
	$.post(
	    '/home/delete_post',
	    get_form_values(this),
	    function(data,status,xhr){
		
		if(data.success)
		    window.location.reload();
	    })});

    $('.update_user_form').on('submit', function(e){
	e.preventDefault();
	$.post(
	    '/home/user_update',
	    get_form_values(this),
	    function(data,status,xhr){
		
		if(data.success)
		    window.location.reload();
	    })});

})();
