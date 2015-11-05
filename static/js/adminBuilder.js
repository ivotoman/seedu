function clearErrors () {
    console.log("cleaning up")
    $('.input-group').each(function() {
        if ($(this).hasClass("has-error")) {
            $(this).removeClass("has-error");
        }
    });
    $('#order-error').hide();
};

function putCourse () {
    console.log("putting courses")
    // event.preventDefault(); //change return to false together with event.preventDefault(); in order to prevent submit
    var content = JSON.stringify($('form').serializeObject());
    $('#result').text(content);
    console.log(content)
    var pathname = window.location.pathname
    $.ajax({
        type : "PUT",
        url : pathname,
        data: JSON.stringify(content, null, '\t'),
        contentType: 'application/json;charset=UTF-8'
    });
    return true; //change return to false together with event.preventDefault(); in order to prevent submit
    // return false; //change return to false together with event.preventDefault(); in order to prevent submit
};


function checkOrder (schoolCurriculum) {
    clearErrors();
    event.preventDefault();
    var allGood = true
    console.log("starting anew. allGood = " + allGood)
    $('input').each(function() {
        
        console.log("")
        console.log("")
        console.log("")
        var $current = $(this);
        var current_topic_id = $(this).parents(".topic-row:first").find(".topic-order:first").attr('id');
        if ($(this).hasClass("topic-order")) {
            $('.topic-order').each(function() {
                if ($(this).val() == $current.val() && $(this).attr('id') != $current.attr('id') && $(this).attr('class') == $current.attr('class')) {
                    console.log("error: topic-order")
                    if (!$current.parent().hasClass("has-error")) {
                        $current.parent().addClass("has-error");
                    }
                    if (!$(this).parent().hasClass("has-error")) {
                        $current.parent().addClass("has-error");
                    }
                    allGood = false;
                } else {
                    // console.log("changing topic-order: value, or class didn't match or ids matched")
                    console.log("")
                }
            })
        } else if ($(this).hasClass("subtopic-order")) {
            $('.subtopic-order').each(function() {
                var this_topic_id = $(this).parents(".topic-row:first").find(".topic-order:first").attr('id');
                var $current_year = $current.parent().parent().parent().parent().parent().find(".subtopic-year")
                if ($(this).val() == $current.val() && $(this).attr('id') != $current.attr('id') && $(this).attr('class') == $current.attr('class')) {
                    var subtopic_year = $(this).parent().parent().parent().parent().parent().find(".subtopic-year")
                    var this_topic_id = $(this).parents(".topic-row").find(".topic-order:first").attr('id'); 
                    if ($(subtopic_year).val() == $current_year.val() && this_topic_id == current_topic_id) {
                        console.log("error: subtopic-order")
                        $current.parent().addClass("has-error");    
                        $(this).parent().addClass("has-error");
                        $current_year.parent().addClass("has-error");  
                        $(subtopic_year).parent().addClass("has-error"); 
                        allGood = false;
                    } else {
                        // console.log("this and current belong to different topics eventually the the subtopics have different ids")
                        console.log("")
                    }

                    
                } else {
                    // console.log("changing subtopic-order: value, or class didn't match or ids matched")                
                    console.log("")
                }
            })
        }  else {
            // console.log("else of event listener to inputs")
            console.log("")   
        } 
    })
    
    console.log("finished the function. allGood = " + allGood)

    if (allGood == true) {
        if (schoolCurriculum) {
            console.log("returning true to checkOrderAndPutNewCurriculum")   
            return true
        } else {
            putCourse();
        };
        
    } else if (allGood == false) {
        console.log("there are errors!")
        $('#order-error').show() 
        return false
    };    
    
};



////////////////////////////////////////////////
////////////////////////////////////////////////
/////////////new standard curricula/////////////
////////////////////////////////////////////////
////////////////////////////////////////////////


$(function() {
    $('#submit-new-standard-curricula').click(function(event) {
        var checkedCount = $('input[class="courses"]:checked').length
        if (checkedCount == 0) {
            event.preventDefault(); //change return to false together with event.preventDefault(); in order to prevent submit    
            $('#no-checkbox').show();
            return false; //change return to false together with event.preventDefault(); in order to prevent submit
        } else {
            $('#no-checkbox').hide();
        };
        return true; //change return to false together with event.preventDefault(); in order to prevent submit
    });
});

////////////////////////////////////////////////
////////////////////////////////////////////////
//////////////new school curricula//////////////
////////////////////////////////////////////////
////////////////////////////////////////////////
function hideCoursesNewCurriculum () {
    var courses = $('.available-courses')
    var selected = $("#select-standard-curriculum").val()
    for (var i = courses.length - 1; i >= 0; i--) {
        if ($(courses[i]).hasClass(selected)) {    
            $(courses[i]).show()
                $(courses[i]).find('input').prop('checked', true); // Checks it    
        } else {
            $(courses[i]).hide()
            $(courses[i]).find('input').prop('checked', false); // Unchecks it
        };
    }
};




function checkOrderAndPutNewCurriculum () {
    var allGood = checkOrder(true);
    if (allGood == true) {
        console.log("I am ready to puNewCurriculum:  allGood = " + allGood)
        putNewCurriculum();
        // info on js redirect http://stackoverflow.com/questions/503093/how-can-i-make-a-redirect-page-using-jquery
        window.location.href = '/admin/schools';
        return true;
    } else {
        console.log("ERROR: allGood = " + allGood)
        return false;
    };
    console.log("this should not be HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
}


function putNewCurriculum () {
    // event.preventDefault(); //change return to false together with event.preventDefault(); in order to prevent submit
    var content = JSON.stringify($('form').serializeObject());
    $('#result').text(content);
    console.log(content)
    var pathname = window.location.pathname
    $.ajax({
        type : "PUT",
        url : pathname,
        data: JSON.stringify(content, null, '\t'),
        contentType: 'application/json;charset=UTF-8'
    });
    return true; //change return to false together with event.preventDefault(); in order to prevent submit
};



////////////////////////////////////////////////
////////////////////////////////////////////////
////////////////////courses/////////////////////
////////////////////////////////////////////////
////////////////////////////////////////////////

// i am not sure if these counters could interfere with topic and subtopic IDs
var topicCounter = 1
var subtopicCounter = 1

function addTopic (element) {
    var topic = HTMLTopicRow.replace(/(%subtopicdata%)/g, subtopicCounter);
    var newTopic = $(topic.replace(/(%topicdata%)/g, topicCounter));
    topicCounter ++;
    subtopicCounter ++;
    newTopic.insertBefore(element);
};

function addSubtopic (element) {
    var topic_id = element.parent().parent().parent().attr("id");
    var topic = HTMLSubtopicRow.replace(/(%topicdata%)/g, topic_id);
    var newSubtopic = $(topic.replace(/(%subtopicdata%)/g, subtopicCounter));
    subtopicCounter ++;
    newSubtopic.insertBefore(element);
};

function hideCoursesEdit () {
    var courses = $('.available-courses')
    var selected = $("#select-grade").val()
    for (var i = courses.length - 1; i >= 0; i--) {
        if ($(courses[i]).hasClass(selected)) {    
            $(courses[i]).show()
            if ($(courses[i]).hasClass("jinja")) {
                $(courses[i]).find('input').prop('checked', true); // Checks it    
            };
                
        } else {
            $(courses[i]).hide()
            $(courses[i]).find('input').prop('checked', false); // Unchecks it
        };
    }
};

function hideCoursesNew () {
    console.log("hide courses called")
    var courses = $('.available-courses')
    var selected = $("#select-grade").val()
    var standardCurriculum = $("#select-grade").val()
    for (var i = courses.length - 1; i >= 0; i--) {
        if ($(courses[i]).hasClass(selected)) {    
            $(courses[i]).show()
                $(courses[i]).find('input').prop('checked', true); // Checks it    
        } else {
            $(courses[i]).hide()
            $(courses[i]).find('input').prop('checked', false); // Unchecks it
        };
    }
};


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
        addTopic(element);
    } else if (element.attr("id") == "subtopic") {
        addSubtopic(element);

  //   } else if (element.attr("id") == "submit-edit-course") {
  //   	// event.preventDefault(); //change return to false together with event.preventDefault(); in order to prevent submit
  //       var content = JSON.stringify($('form').serializeObject());
  //       $('#result').text(content);
  //       var pathname = window.location.pathname
  //       $.ajax({
		//     type : "POST",
		//     url : pathname,
		//     data: JSON.stringify(content, null, '\t'),
		//     contentType: 'application/json;charset=UTF-8'
		// });
    } else if (element.attr("id") == "submit-new-course") {
        // event.preventDefault(); //change return to false together with event.preventDefault(); in order to prevent submit
        var content = JSON.stringify($('form').serializeObject());
        $('#result').text(content);
        console.log(content)
        $.ajax({
            type : "PUT",
            url : '/admin/courses/new'  ,
            data: JSON.stringify(content, null, '\t'),
            contentType: 'application/json;charset=UTF-8'
        });
        return true; //change return to false together with event.preventDefault(); in order to prevent submit
        // return false; //change return to false together with event.preventDefault(); in order to prevent submit
    // } else if (element.attr("id") == "submit-customized-courses") {
    //     putNewCurriculum();
        // // event.preventDefault(); //change return to false together with event.preventDefault(); in order to prevent submit
        // var content = JSON.stringify($('form').serializeObject());
        // $('#result').text(content);
        // console.log(content)
        // $.ajax({
        //     type : "PUT",
        //     url : '/admin/courses/new'  ,
        //     data: JSON.stringify(content, null, '\t'),
        //     contentType: 'application/json;charset=UTF-8'
        // });
        // return true; //change return to false together with event.preventDefault(); in order to prevent submit
        // return false; //change return to false together with event.preventDefault(); in order to prevent submit
    }; 
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

// function submitNewCourse () {
//     console.log("submitNewCourse")
//     // event.preventDefault(); //change return to false together with event.preventDefault(); in order to prevent submit
//     var content = JSON.stringify($('form').serializeObject());
//     $('#result').text(content);
//     console.log(content)
//     $.ajax({
//         type : "PUT",
//         url : '/admin/courses/new'  ,
//         data: JSON.stringify(content, null, '\t'),
//         contentType: 'application/json;charset=UTF-8'
//     });
//     return true; //change return to false together with event.preventDefault(); in order to prevent submit
// };



// $(function() {
//     $('submit-new-course').submit(function(event) {
//         // event.preventDefault(); //change return to false together with event.preventDefault(); in order to prevent submit
//         var content = JSON.stringify($('form').serializeObject());
//         $('#result').text(content);

//         $.ajax({
// 		    type : "PUT",
// 		    url : '/admin/courses/new'	,
// 		    data: JSON.stringify(content, null, '\t'),
// 		    contentType: 'application/json;charset=UTF-8'
// 		});
//         return true; //change return to false together with event.preventDefault(); in order to prevent submit
//     });
// });


function confirmAction(){
      var confirmed = confirm("Are you sure? This will remove this entry forever.");
      return confirmed;
}





