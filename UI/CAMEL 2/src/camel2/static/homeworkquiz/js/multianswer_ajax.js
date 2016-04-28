$(document).ready( function(){
	$('#btn_save').click( function( event ){
		event.preventDefault();

		// error handling
        if(!check_answer()){
            alert("Error - No answer is selected");
            return;
        }

		save_answer();
	});


});

$('#btn_submit').click( function( event ){
    if(!check_answer()){
        alert("Error - No answer is selected");
        event.preventDefault();
        return;
    }
});

function check_answer(){
     var n = $( "input:checked" ).length;
     if (n > 0){
        return true;
     }
     return false;
}

function save_answer(){
    /* function to make ajax request to save function.*/
	var node = $('#node').val();
    var book = $('#book').val();
    var chapter = $('#chapter').val();
    var module = $('#module').val();

    // get answers and add them to an array
    // array then is passed to python view
    var user_answers = [];
    $('input[type=checkbox]:checked').each(function () {
        user_answers.push($(this).val());
    });

	$.ajax({
        url : "/module/" + module + "/book/" + book + "/chapter/" +  chapter +"/save-multi/" + node + "/", //endpoint
        type : "POST", // http method
        data : { 
        	user :$('#user').val(),
        	multiplechoice : user_answers,
        }, // data sent with the post request
        
        //get the csrf_token
        beforeSend: function(xhr, settings) {
        	//console.log("Before Send");
        	$.ajaxSettings.beforeSend(xhr, settings);
    	},

        // handle a successful response
        success : function(json) {
            // console.log(json); // log the returned json to the console
            // console.log("success");
            update_screen();
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.responseText);
        }
    });
}

function update_screen(){
    // alert user to indicate it has been saved
	alert("Answer saved.");
}