// $(document).on('change', 'input', function() {
//    console.log("")
//    console.log("")
//    console.log("")
//    var $current = $(this);
//    var current_topic_id = $(this).parents(".topic-row:first").find(".topic-order:first").attr('id');
//    if ($(this).hasClass("topic-order")) {
//         $('.topic-order').each(function() {
//             if ($(this).val() == $current.val() && $(this).attr('id') != $current.attr('id') && $(this).attr('class') == $current.attr('class')) {
//                 $current.parent().addClass("has-error");    
//                 $(this).parent().toggleClass("has-error");
//             } else {
//                 console.log("changing topic-order: value, or class didn't match or ids matched")
//             }
//         })
//     } else if ($(this).hasClass("subtopic-order")) {
//         $('.subtopic-order').each(function() {
//             var this_topic_id = $(this).parents(".topic-row:first").find(".topic-order:first").attr('id');
//             var $current_year = $current.parent().parent().parent().parent().parent().find(".subtopic-year")
//             if ($(this).val() == $current.val() && $(this).attr('id') != $current.attr('id') && $(this).attr('class') == $current.attr('class')) {
//                 var subtopic_year = $(this).parent().parent().parent().parent().parent().find(".subtopic-year")
//                 var this_topic_id = $(this).parents(".topic-row").find(".topic-order:first").attr('id'); 
//                 if ($(subtopic_year).val() == $current_year.val() && this_topic_id == current_topic_id) {
//                     $current.parent().addClass("has-error");    
//                     $(this).parent().toggleClass("has-error");
//                     $current_year.parent().toggleClass("has-error");  
//                     $(subtopic_year).parent().toggleClass("has-error"); 
//                 } else {
//                     console.log("this and current belong to different topics eventually the the subtopics have different ids")
//                 }

                
//             } else {
//                 console.log("changing subtopic-order: value, or class didn't match or ids matched")                
//             }
//         })
//     } else if ($(this).hasClass("subtopic-year")) {
//         var $subtopic_order = $(this).parent().parent().parent().parent().parent().find(".subtopic-order");
//         var current_year = $current.parent().parent().parent().parent().parent().find(".subtopic-year")
//         var this_topic_id = $(this).parents(".topic-row:first").find(".topic-order:first").attr('id');
        
//         $('.subtopic-order').each(function() {
//             if ($(this).val() == $subtopic_order.val() && $(this).attr('id') != $subtopic_order.attr('id') && $(this).attr('class') == $subtopic_order.attr('class')) {
//                 var subtopic_year = $(this).parent().parent().parent().parent().parent().find(".subtopic-year")
//                 if ($(subtopic_year).val() == $(current_year).val()) {
//                     $current.parent().addClass("has-error");    
//                     $subtopic_order.parent().toggleClass("has-error");  
//                     $(this).parent().toggleClass("has-error");
//                     $(subtopic_year).parent().toggleClass("has-error"); 
//                     return;
//                 } else {
//                     console.log('different subtopic');
//                 };

                
//             } else {
//                 console.log('changed year, but no match of values, ' + $(this).val());
                
//             }
//         })
//     } else {
//         console.log("else of event listener to inputs")
        
//     }
// });


// $(document).on('change', 'input', function() {
//    console.log("")
//    console.log("")
//    console.log("")
//    // console.log("form has changed")
//    var $current = $(this);
//    var current_topic_id = $(this).parents(".topic-row:first").find(".topic-order:first").attr('id');
//    if ($(this).hasClass("topic-order")) {
//         $('.topic-order').each(function() {
//             if ($(this).val() == $current.val() && $(this).attr('id') != $current.attr('id') && $(this).attr('class') == $current.attr('class')) {
//                 $current.parent().addClass("has-error");    
//                 $(this).parent().toggleClass("has-error");
//             } else {
//                 console.log("changing topic-order: value, or class didn't match or ids matched")
//             }
//         })
//     } else if ($(this).hasClass("subtopic-order")) {
//         $('.subtopic-order').each(function() {
//             var this_topic_id = $(this).parents(".topic-row:first").find(".topic-order:first").attr('id');
//             var $current_year = $current.parent().parent().parent().parent().parent().find(".subtopic-year")
//             if ($(this).val() == $current.val() && $(this).attr('id') != $current.attr('id') && $(this).attr('class') == $current.attr('class')) {
//                 var subtopic_year = $(this).parent().parent().parent().parent().parent().find(".subtopic-year")
//                 var this_topic_id = $(this).parents(".topic-row").find(".topic-order:first").attr('id'); 
//                 if ($(subtopic_year).val() == $current_year.val() && this_topic_id == current_topic_id) {
//                     $current.parent().addClass("has-error");    
//                     $(this).parent().toggleClass("has-error");
//                     $current_year.parent().toggleClass("has-error");  
//                     $(subtopic_year).parent().toggleClass("has-error"); 
//                 } else {
//                     console.log("this and current belong to different topics eventually the the subtopics have different ids")
//                 }

                
//             } else {
//                 console.log("changing subtopic-order: value, or class didn't match or ids matched")                
//             }
//         })
//     } else if ($(this).hasClass("subtopic-year")) {
//         var $subtopic_order = $(this).parent().parent().parent().parent().parent().find(".subtopic-order");
//         var current_year = $current.parent().parent().parent().parent().parent().find(".subtopic-year")
//         var this_topic_id = $(this).parents(".topic-row:first").find(".topic-order:first").attr('id');
        
//         $('.subtopic-order').each(function() {
//             if ($(this).val() == $subtopic_order.val() && $(this).attr('id') != $subtopic_order.attr('id') && $(this).attr('class') == $subtopic_order.attr('class')) {
//                 var subtopic_year = $(this).parent().parent().parent().parent().parent().find(".subtopic-year")
//                 if ($(subtopic_year).val() == $(current_year).val()) {
//                     $current.parent().addClass("has-error");    
//                     $subtopic_order.parent().toggleClass("has-error");  
//                     $(this).parent().toggleClass("has-error");
//                     $(subtopic_year).parent().toggleClass("has-error"); 
//                     return;
//                 } else {
//                     console.log('different subtopic');
//                 };

                
//             } else {
//                 console.log('changed year, but no match of values, ' + $(this).val());
                
//             }
//         })
//     } else {
//         console.log("else of event listener to inputs")
        
//     }
// });