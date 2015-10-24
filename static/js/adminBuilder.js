var topicCounter = 2
var subtopicCounter = 2


$( 'body' ).click(function(event) {

	var element = $(event.target);

	if (element.attr("id") == "remove-subtopic") {
        var subtopicRow = $( event.target ).parents("#subtopic-row");
        var hr = subtopicRow.next()
		subtopicRow.remove();
		hr.remove();

    } else if (element.attr("id") == "remove-topic") {
    	var topicRow = $( event.target ).parents("#topic-row");
		var hr = topicRow.next()
		topicRow.remove();
		hr.remove();

    } else if (element.attr("id") == "topic") {
    	var previous = $( event.target )
		var topic = HTMLTopicRow.replace(/(%subtopicdata%)/g, subtopicCounter);
		var newTopic = $(topic.replace(/(%topicdata%)/g, topicCounter));

		topicCounter ++;
		subtopicCounter ++;
		event.preventDefault();
		newTopic.insertBefore(previous);

    } else if (element.attr("id") == "subtopic") {
    	var previous = $( event.target )
		var newSubtopic = $(HTMLSubtopicRow.replace(/(%subtopicdata%)/g, subtopicCounter));
		subtopicCounter ++;
		event.preventDefault();
		newSubtopic.insertBefore(previous);

    } ;
  //   else if (element.attr("id") == "submit-new-course") {
		// var form = $("#new-course")
		// var courseJSON = form.serializeObject();    	
		// console.log(courseJSON)
		// event.preventDefault();
  //   }
    // ; 

});

$.fn.serializeObject = function()
{
    var o = {};
    var a = this.serializeArray();
    $.each(a, function() {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        } else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};

$(function() {
    $('form').submit(function() {
        $('#result').text(JSON.stringify($('form').serializeObject()));
        return false;
    });
});


$('.required').blur(function() { //whenever you click off an input element
    if( !$(this).val() ) {                      //if it is blank. 
         console.log("empty");
         // $(this).append('i cannot be empty');    
         alert("Please Fill All Required Field");
    }
});







