
/*
These are HTML strings. Use JavaScript functions to replace the %data% placeholder text.
*/
var HTMLSubtopicRow = 
                  '<div class="row"> <!-- subtopic row -->' +
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
                                        '<input type="number" class="form-control required" placeholder="Subtopic order" name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_order]" required>' +
                                    '</div>' +
                                    
                                '</div>' +
                                '<div class="col-xs-1">' +
                                    '<span class="glyphicon glyphicon-remove" id="remove-subtopic" aria-hidden="true"></span>' +
                                '</div>' +


                            '</div> <!-- /subtopic name + grade column -->' +
                        '</div><!-- /subtopic name + grade row -->' +
                        '<br>' +

                        '<div class="row"> <!-- subtopic description row -->' +
                            '<div class="col-xs-12"> <!-- subtopic descripton column -->' +
                                '<div class="col-xs-2">' +
                                '</div>' +
                                '<div class="col-xs-10">' +
                                    '<div class="form-group">' +
                                        '<label class="control-label" for="subtopic_description">Subtopic description:</label>' +
                                        '<textarea rows="3" class="form-control required" name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_description]" placeholder="Please write a bried description of the subtopic here"></textarea>' +
                                    '</div> ' +
                                '</div> ' +
                            '</div> <!-- /subtopic name + grade column -->' +
                        '</div><!-- /subtopic name + grade row -->' +
                    '</div>' +
                  '</div> <!-- /subtopic row -->' +
                  '<hr>';


var HTMLTopicRow = 
'<div class="row topic-row" id="%topicdata%"> <!-- topic row -->' +
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
                        '<input type="number" class="form-control required" placeholder="Topic order" name="course[topic_%topicdata%][topic_order]" required>' +
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
                '<div class="row"> <!-- subtopic row -->' +
                    '<div class="col-xs-12">' +
                        '<div class="row"> <!-- subtopic name + grade row -->' +
                            '<div class="col-xs-12"> <!-- subtopic name + grade column -->' +
                                '<div class="col-xs-8">' +
                                    '<div class="input-group">' +
                                        '<span class="input-group-addon control-label">Subtopic name:</span>' +
                                        '<input type="text" class="form-control required" placeholder="Please enter the subtopic name" name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_name]" required>' +
                                    '</div> ' +
                                '</div>' +

                                '<div class="col-xs-3">' +
                                    '<div class="input-group">' +
                                        '<span class="input-group-addon control-label">Order:</span>' +
                                        '<input type="number" class="form-control required" placeholder="Subtopic order" name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_order]" required>' +
                                    '</div>' +
                                    
                                '</div>' +
                                '<div class="col-xs-1">' +
                                    '<span class="glyphicon glyphicon-remove" id="remove-subtopic" aria-hidden="true"></span>' +
                                '</div>' +


                            '</div> <!-- /subtopic name + grade column -->' +
                        '</div><!-- /subtopic name + grade row -->' +
                        '<br>' +

                        '<div class="row"> <!-- subtopic description row -->' +
                            '<div class="col-xs-12"> <!-- subtopic descripton column -->' +
                                '<div class="col-xs-2">' +
                                '</div>' +
                                '<div class="col-xs-10">' +
                                    '<div class="form-group">' +
                                        '<label class="control-label" for="subtopic_description">Subtopic description:</label>' +
                                        '<textarea rows="3" class="form-control required" name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_description]" placeholder="Please write a bried description of the subtopic here">' +
                                        '</textarea>' +
                                    '</div> ' +
                                '</div> ' +
                            '</div> <!-- /subtopic name + grade column -->' +
                        '</div><!-- /subtopic name + grade row -->' +
                    '</div>' +
                '</div> <!-- /subtopic row -->' +
                '<hr>' +
                '<button class="btn btn-success pull-right subtopic" id="subtopic">Add a subtopic</button>' +

            '</div><!-- /effective subtopic panel -->' +

        '</div> <!-- /subtopic panel -->' +

    '</div> <!-- /topic row -->' +
    '<hr>' ;
