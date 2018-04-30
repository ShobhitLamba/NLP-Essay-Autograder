# author: Shobhit Lamba

import re
import nltk
from nltk.corpus import stopwords

relevant_words = [["agree","Agree",
        "concur","Concur",
        "differ","Differ",
        "disagree","Disagree",
        "Cars","cars",
        "Car","car",
        "few","fewer",
        "Few","Fewer",
        "less","Less",
        "lesser","Lesser",
        "today","Today"],
        ["agree","Agree",
        "concur","Concur",
        "differ","Differ",
        "disagree","Disagree",
        "young","Young",
        "younger","Younger",
        "youth","Youth",
        "time","Time",
        "nowadays","Nowadays",
        "enough","Enough",
        "help","Help",
        "helping","Helping",
        "community","Community",
        "communities","Communities"],
        ["agree","Agree",
        "concur","Concur",
        "differ","Differ",
        "disagree","Disagree",
        "young","Young",
        "younger","Younger",
        "youth","Youth",
        "enjoy","Enjoy",
        "life","Life",
        "old","Old",
        "older","Older",
        "people","People"],
        ["agree","Agree",
        "concur","Concur",
        "differ","Differ",
        "disagree","Disagree",
        "better","Better",
        "broad","Broad",
        "knowledge","Knowledge",
        "academic","Academic",
        "subject","Subject",
        "subjects","Subjects",
        "specialize","Specialize",
        "specific","Specific",
        "particular","Particular"],
        ["agree","Agree",
        "concur","Concur",
        "differ","Differ",
        "disagree","Disagree",
        "advertisements","Advertisements",
        "products","Products",
        "product","Product",
        "better","Better"],
        ["agree","Agree",
        "concur","Concur",
        "differ","Differ",
        "disagree","Disagree",
        "important","Important",
        "student","Student",
        "students","Students",
        "understand","Understand",
        "idea","Idea",
        "ideas","Ideas",
        "concept","Concept",
        "concepts","Concepts",
        "learn","Learn",
        "fact","Fact",
        "facts","Facts"],
        ["agree","Agree",
        "concur","Concur",
        "differ","Differ",
        "disagree","Disagree",
        "success","Success",
        "successful","Successful",
        "people","People",
        "try","Try",
        "new","New",
        "things","Things",
        "risks","Risks",
        "only doing",
        "already","Already",
        "know","Know"],
        ["agree","Agree",
        "concur","Concur",
        "differ","Differ",
        "disagree","Disagree",
        "best","Best",
        "way","Way",
        "travel","Travel",
        "travelling","Travelling",
        "group","Group",
        "tour","Tour",
        "guide","Guide"]]

topic_list = ["Do you agree or disagree with the following statement? In twenty years there will be fewer cars in use than there are today. Use reasons and examples to support your answer.",
              "Do you agree or disagree with the following statement? Young people enjoy life more than older people do. Use specific reasons and examples to support your answer.",
              "Do you agree or disagree with the following statement? Young people enjoy life more than older people do. Use specific reasons and examples to support your answer.",
              "Do you agree or disagree with the following statement? It is better to have broad knowledge of many academic subjects than to specialize in one specific subject. Use specific reasons and examples to support your answer.",
              "Do you agree or disagree with the following statement? Most advertisements make products seem much better than they really are. Use specific reasons and examples to support your answer.",
              "Do you agree or disagree with the following statement? It is more important for students to understand ideas and concepts than it is for them to learn facts. Use reasons and examples to support your answer.",
              "Do you agree or disagree with the following statement? Successful people try new things and take risks rather than only doing what they already know how to do well. Use reasons and examples to support your answer.",
              "Do you agree or disagree with the following statement? The best way to travel is in a group led by a tour guide. Use reasons and examples to support your answer."]
def topic_coherence(text, topic):
    text = re.sub('[^A-Za-z]+', ' ', text)
    stop_words = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(text)
    tokens = [w for w in tokens if not w in stop_words]
    count = 0

    for i in topic_list:
        if topic_list[i] == topic:
            for j in relevant_words[i]:
                for token in tokens:
                    if i == token:
                        count += 1

    csv_file.close()
    return count

#topic_coherence(text, topic)
