var topicCounter = 2
var subtopicCounter = 2


$( 'body' ).click(function(event) {

	var element = $(event.target);

	if (element.attr("id") == "remove-subtopic") {
        var subtopicRow = $( event.target ).parent().parent().parent().parent().parent();
        var hr = subtopicRow.next()
		subtopicRow.remove();
		hr.remove();

    } else if (element.attr("id") == "remove-topic") {
    	var topicRow = $( event.target ).parent().parent().parent().parent();
		var hr = topicRow.next()
		topicRow.remove();
		hr.remove();

    } else if (element.attr("id") == "topic") {
		var topic = HTMLTopicRow.replace(/(%subtopicdata%)/g, subtopicCounter);
		var newTopic = $(topic.replace(/(%topicdata%)/g, topicCounter));
		topicCounter ++;
		subtopicCounter ++;
		event.preventDefault();
		newTopic.insertBefore(element);

    } else if (element.attr("id") == "subtopic") {
		var topic_id = element.parent().parent().parent().attr("id");
		console.log(topic_id);
		var topic = HTMLSubtopicRow.replace(/(%topicdata%)/g, topic_id);
		var newSubtopic = $(topic.replace(/(%subtopicdata%)/g, subtopicCounter));
		subtopicCounter ++;
		event.preventDefault();
		newSubtopic.insertBefore(element);
    } ; 
});



(function($){
    $.fn.serializeObject = function(){

        var self = this,
            json = {},
            push_counters = {},
            patterns = {
                "validate": /^[a-zA-Z][a-zA-Z0-9_]*(?:\[(?:\d*|[a-zA-Z0-9_]+)\])*$/,
                "key":      /[a-zA-Z0-9_]+|(?=\[\])/g,
                "push":     /^$/,
                "fixed":    /^\d+$/,
                "named":    /^[a-zA-Z0-9_]+$/
            };


        this.build = function(base, key, value){
            base[key] = value;
            return base;
        };

        this.push_counter = function(key){
            if(push_counters[key] === undefined){
                push_counters[key] = 0;
            }
            return push_counters[key]++;
        };

        $.each($(this).serializeArray(), function(){

            // skip invalid keys
            if(!patterns.validate.test(this.name)){
                return;
            }

            var k,
                keys = this.name.match(patterns.key),
                merge = this.value,
                reverse_key = this.name;

            while((k = keys.pop()) !== undefined){

                // adjust reverse_key
                reverse_key = reverse_key.replace(new RegExp("\\[" + k + "\\]$"), '');

                // push
                if(k.match(patterns.push)){
                    merge = self.build([], self.push_counter(reverse_key), merge);
                }

                // fixed
                else if(k.match(patterns.fixed)){
                    merge = self.build([], k, merge);
                }

                // named
                else if(k.match(patterns.named)){
                    merge = self.build({}, k, merge);
                }
            }

            json = $.extend(true, json, merge);
        });

        return json;
    };
})(jQuery);

$(function() {
    $('form').submit(function(event) {
        // event.preventDefault();
        var content = JSON.stringify($('form').serializeObject());
        $('#result').text(content);

        $.ajax({
		    type : "PUT",
		    url : '/admin/courses/new'	,
		    data: JSON.stringify(content, null, '\t'),
		    contentType: 'application/json;charset=UTF-8'
		});
        return true;
    });
});






