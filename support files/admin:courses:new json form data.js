{
    "course": {
        "course_description": "a;lskjfa;ls", 
        "course_grade": "primary", 
        "course_name": "jfals;f;askfj", 
        "topic_1": {
            "subtopic_1": {
                "subtopic_description": "a;vwoevaw;eo", 
                "subtopic_name": "slkjcaoiwe", 
                "subtopic_order": "1"
            }, 
            "subtopic_10": {
                "subtopic_description": "saefawef", 
                "subtopic_name": "asfasdf", 
                "subtopic_order": "4"
            }, 
            "subtopic_2": {
                "subtopic_description": "vaweo;j", 
                "subtopic_name": "alvweo;ivaw;oe", 
                "subtopic_order": "2"
            }, 
            "subtopic_3": {
                "subtopic_description": "nawoevawe", 
                "subtopic_name": "vawo;ievawjev", 
                "subtopic_order": "3"
            }, 
            "topic_description": "asfkjas;flk", 
            "topic_name": "aslkjas;lfk", 
            "topic_order": "1"
        }, 
        "topic_2": {
            "subtopic_11": {
                "subtopic_description": "", 
                "subtopic_name": "asfasfdads", 
                "subtopic_order": "4"
            }, 
            "subtopic_12": {
                "subtopic_description": "svjwaoeifj", 
                "subtopic_name": "vawfawefjwo;", 
                "subtopic_order": "5"
            }, 
            "subtopic_13": {
                "subtopic_description": "jawoiefjawfje", 
                "subtopic_name": "jafeoaifjeaw;fe", 
                "subtopic_order": "6"
            }, 
            "subtopic_14": {
                "subtopic_description": "jwo;eifjawefj", 
                "subtopic_name": "ajwoiejacwoe", 
                "subtopic_order": "7"
            }, 
            "subtopic_15": {
                "subtopic_description": "aojfwaeo;ifjawof", 
                "subtopic_name": "woefijaweof;i", 
                "subtopic_order": "8"
            }, 
            "subtopic_16": {
                "subtopic_description": "nefawejfoawejfawo", 
                "subtopic_name": "foawjefo;iaewj", 
                "subtopic_order": "9"
            }, 
            "subtopic_17": {
                "subtopic_description": "wjefajwfawi", 
                "subtopic_name": "faewfawf", 
                "subtopic_order": "10"
            }, 
            "subtopic_4": {
                "subtopic_description": "wvoei;vawelkj", 
                "subtopic_name": "vwa;eoiawv;o", 
                "subtopic_order": "1"
            }, 
            "subtopic_5": {
                "subtopic_description": "sjv", 
                "subtopic_name": "salkdfjaso;if", 
                "subtopic_order": "2"
            }, 
            "subtopic_6": {
                "subtopic_description": "vwaoenijewaofij", 
                "subtopic_name": "vvawoeivjwavk", 
                "subtopic_order": "3"
            }, 
            "topic_description": "vjeoawevjawe;oi", 
            "topic_name": "v;aowiveaw;ov", 
            "topic_order": "2"
        }, 
        "topic_3": {
            "subtopic_7": {
                "subtopic_description": "cawjoiejaw;of", 
                "subtopic_name": "alfjeawoifj", 
                "subtopic_order": "1"
            }, 
            "subtopic_8": {
                "subtopic_description": "wjoeifjawfj", 
                "subtopic_name": "vaowiefjawflka", 
                "subtopic_order": "2"
            }, 
            "subtopic_9": {
                "subtopic_description": "wjeofajiwefo", 
                "subtopic_name": "ovwjeofiawjf", 
                "subtopic_order": "3"
            }, 
            "topic_description": "weoijaflakjf", 
            "topic_name": "avwoejfalwj", 
            "topic_order": "3"
        }
    }
}


<input name="course[course_name]" value="course name">
<input name="course[course_grade]" value="course grade">
<input name="course[course_description]" value="course description">
<input name="course[topic_1][topic_name]" value="topic name">
<input name="course[topic_1][topic_order]" value="topic name">
<input name="course[topic_1][topic_description]" value="topic description">

<input name="course[topic_1][subtopic_1][subtopic_name]" value="subtopic name">
<input name="course[topic_1][subtopic_1][subtopic_order]" value="subtopic name">
<input name="course[topic_1][subtopic_1][subtopic_description]" value="subtopic name">

name="course[topic_%topicdata%][topic_name]"
name="course[topic_%topicdata%][topic_order]"
name="course[topic_%topicdata%][topic_description]"

name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_name]"
name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_order]"
name="course[topic_%topicdata%][subtopic_%subtopicdata%][subtopic_description]"


{
	"course":{
		"name":"course name",
		"grade":"course grade",
		"description" : "course description",
		"topic_1" : {
			"topic_name" : "topic name",
			"topic_order" : "topic order",
			"topic_description" : "topic description",
			"subtopic_1" : {
				"subtopic_name" : "subtopic name",
				"subtopic_order" : "subtopic order",
				"subtopic_description" : "subtopic description"
			},
			"subtopic_2" : {
				"subtopic_name" : "subtopic name"
			}

		},
		"topic_2" : {
			"topic_name" : "topic name",
			"subtopic_3" : {
				"subtopic_name" : "subtopic name"
			}
		}
    }
 }
  

  },
  "wombat":["b"],
  "hello":{
    "panda":["c"]
  },
  "animals":[
    {
      "name":"d",
      "breed":"e"
    }
  ],
  "crazy":[
    null,
    [
      {"wonky":"f"}
    ]
  ],
  "dream":{
    "as":{
      "vividly":{
        "as":{
          "you":{
            "can":"g"
          }
        }
      }
    }
  }
}