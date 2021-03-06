
/*
These are HTML strings. Use JavaScript functions to replace the %data% placeholder text.
*/
var HTMLSubtopicRow = 
                  '<div class="row subtopic-row"> <!-- subtopic row -->' +
                    '<div class="col-xs-12">' +
                        '<div class="row"> <!-- subtopic name + grade row -->' +
                            '<div class="col-xs-12"> <!-- subtopic name + grade column -->' +
                                '<div class="col-xs-8">' +
                                    '<div class="input-group">' +
                                        '<span class="input-group-addon control-label required">Subtopic name:</span>' +
                                        '<input type="text" class="form-control required" placeholder="Please enter the subtopic name" name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_name]" required>' +
                                    '</div> ' +
                                '</div>' +

                                '<div class="col-xs-3">' +
                                    '<div class="input-group">' +
                                        '<span class="input-group-addon control-label">Order:</span>' +
                                        '<input type="number" class="form-control subtopic-order required" placeholder="Subtopic order" name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_order]" id="new_%subtopicdata%" required>' +
                                    '</div>' +
                                    
                                '</div>' +
                                '<div class="col-xs-1">' +
                                    '<span class="glyphicon glyphicon-remove" id="remove-subtopic" aria-hidden="true"></span>' +
                                '</div>' +


                            '</div> <!-- /subtopic name + grade column -->' +
                        '</div><!-- /subtopic name + grade row -->' +
                        '<br>' +
                        '<div class="row"> <!-- subtopic year + # hours row -->' +
                            '<div class="col-xs-12"> <!-- subtopic year + # hours column -->' +
                                '<div class="col-xs-6">' +
                                    '<div class="input-group">' +
                                        '<span class="input-group-addon control-label">Year:</span>' +
                                        '<input type="number" class="form-control subtopic-year required" placeholder="Year/grade when it will be taught" name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_year]" id="new_%subtopicdata%" required>' +
                                    '</div> ' +
                                '</div>' +

                                '<div class="col-xs-5">' +
                                    '<div class="input-group">' +
                                        '<span class="input-group-addon control-label"># hours:</span>' +
                                        '<input type="number" class="form-control required" placeholder="Hours spent on it" name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_hours]">' +
                                    '</div>  ' +
                                '</div>' +
                                '<div class="col-xs-1">' +
                                '</div>' +
                            '</div> <!-- /subtopic year + # hours column -->' +
                        '</div><!-- /subtopic year + # hours row -->' +
                        '<br>' +

                        '<div class="row"> <!-- subtopic description row -->' +
                            '<div class="col-xs-12"> <!-- subtopic descripton column -->' +
                                '<div class="col-xs-2">' +
                                '<label class="control-label" for="subtopic_description">Subtopic description:</label>' +
                                '</div>' +
                                '<div class="col-xs-10">' +
                                    '<div class="form-group">' +

                                        '<textarea rows="3" class="form-control required" name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_description]" placeholder="Please write a bried description of the subtopic here"></textarea>' +
                                    '</div> ' +
                                '</div> ' +
                            '</div> <!-- /subtopic description column -->' +
                        '</div><!-- /subtopic description row -->' +
                    '</div>' +
                  '</div> <!-- /subtopic row -->' +
                  '<hr>';


var HTMLTopicRow = 
'<div class="row topic-row" id="newtopic_%topicdata%"> <!-- topic row -->' +
        '<div class="col-xs-4"> <!-- topic panel -->' +
            '<div class="row"> <!-- topic name row -->' +
                '<div class="col-xs-1">' +
                    '<span class="glyphicon glyphicon-remove" id="remove-topic" aria-hidden="true"></span>' +
                '</div>' +
                '<div class="col-xs-11">' +
                    '<div class="input-group">' +
                        '<span class="input-group-addon control-label">Topic name:</span>' +
                        '<input type="text" class="form-control required" placeholder="Please enter the topic name" name="course[topic_%topicdata%][topic_name]" required>' +
                    '</div>' +
                '</div>' +
            '</div> <!-- /row topic name row -->' +
            '<br>' +
            '<div class="row"> <!-- topic order row -->' +
                '<div class="col-xs-1">' +
                '</div>' +  
                '<div class="col-xs-11">' +
                    '<div class="input-group">' +
                        '<span class="input-group-addon control-label">Order:</span>' +
                        '<input type="number" class="form-control topic-order required" placeholder="Topic order" name="course[topic_%topicdata%][topic_order]" id="newtopic_%topicdata%" required>' +
                    '</div>' +
                '</div>' +
            '</div>' +
            '<br>' +
            '<div class="row"> <!-- topic description row -->' +
                '<div class="col-xs-1">' +
                '</div>' +
                '<div class="col-xs-11">' +
                    '<div class="form-group">' +
                        '<label class="control-label" for="topic_description">Topic description:</label>' +
                        '<textarea rows="4" class="form-control required" name="course[topic_%topicdata%][topic_description]" placeholder="Please write a bried description of the topic here">' +
                        '</textarea>' +
                    '</div> ' +
                '</div>' +
            '</div>' +

        '</div> <!-- /topic panel -->' +


        '<div class="col-xs-8"> <!-- subtopic panel -->' +
            '<div class="col-xs-1">' +
            '</div>' +

            '<div class="col-xs-11"> <!-- effective subtopic panel -->' +
                '<div class="row subtopic-row"> <!-- subtopic row -->' +
                    '<div class="col-xs-12">' +
                        '<div class="row"> <!-- subtopic name + grade row -->' +
                            '<div class="col-xs-12"> <!-- subtopic name + grade column -->' +
                                '<div class="col-xs-8">' +
                                    '<div class="input-group">' +
                                        '<span class="input-group-addon control-label required">Subtopic name:</span>' +
                                        '<input type="text" class="form-control required" placeholder="Please enter the subtopic name" name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_name]" required>' +
                                    '</div> ' +
                                '</div>' +

                                '<div class="col-xs-3">' +
                                    '<div class="input-group">' +
                                        '<span class="input-group-addon control-label">Order:</span>' +
                                        '<input type="number" class="form-control subtopic-order required" placeholder="Subtopic order" name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_order]" id="newsubtopic_%subtopicdata%" required>' +
                                    '</div>' +
                                    
                                '</div>' +
                                '<div class="col-xs-1">' +
                                    '<span class="glyphicon glyphicon-remove" id="remove-subtopic" aria-hidden="true"></span>' +
                                '</div>' +


                            '</div> <!-- /subtopic name + grade column -->' +
                        '</div><!-- /subtopic name + grade row -->' +
                        '<br>' +
                        '<div class="row"> <!-- subtopic year + # hours row -->' +
                            '<div class="col-xs-12"> <!-- subtopic year + # hours column -->' +
                                '<div class="col-xs-6">' +
                                    '<div class="input-group">' +
                                        '<span class="input-group-addon control-label">Year:</span>' +
                                        '<input type="number" class="form-control subtopic-year required" placeholder="Year/grade when it will be taught" name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_year]" id="newsubtopic_%subtopicdata%" required>' +
                                    '</div> ' +
                                '</div>' +

                                '<div class="col-xs-5">' +
                                    '<div class="input-group">' +
                                        '<span class="input-group-addon control-label"># hours:</span>' +
                                        '<input type="number" class="form-control required" placeholder="Hours spent on it" name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_hours]">' +
                                    '</div>  ' +
                                '</div>' +
                                '<div class="col-xs-1">' +
                                '</div>' +
                            '</div> <!-- /subtopic year + # hours column -->' +
                        '</div><!-- /subtopic year + # hours row -->' +
                        '<br>' +

                        '<div class="row"> <!-- subtopic description row -->' +
                            '<div class="col-xs-12"> <!-- subtopic descripton column -->' +
                                '<div class="col-xs-2">' +
                                '<label class="control-label" for="subtopic_description">Subtopic description:</label>' +
                                '</div>' +
                                '<div class="col-xs-10">' +
                                    '<div class="form-group">' +

                                        '<textarea rows="3" class="form-control required" name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_description]" placeholder="Please write a bried description of the subtopic here"></textarea>' +
                                    '</div> ' +
                                '</div> ' +
                            '</div> <!-- /subtopic description column -->' +
                        '</div><!-- /subtopic description row -->' +
                    '</div>' +
                  '</div> <!-- /subtopic row -->' +
                  '<hr>' +
                '<a class="subtopic btn btn-success pull-right" role="button" id="subtopic">Add a subtopic</a>' +
            '<div id="end-of-subtopic" style="display: none;"></div>' +
            '</div><!-- /effective subtopic panel -->' +

        '</div> <!-- /subtopic panel -->' +

    '</div> <!-- /topic row -->' +
    '<hr>' ;
