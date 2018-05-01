# author: Shobhit Lamba

import re
import nltk
from nltk.corpus import stopwords

# Eight lists of relevant words according to topics
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

# List of words unique to each topic used to find out which essay topic we are dealing with
topic_keyword = ["twenty","time","older","advertisements","knowledge","ideas","Successful","tour"]

def topic_coherence(text, topic):
    # data cleaning
    text = re.sub('[^A-Za-z]+', ' ', text)
    stop_words = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(text)
    tokens = [w for w in tokens if not w in stop_words]
    count = 0

    # tokninzing topic to be able to easily traverse and check for availability of keyword
    topic = re.sub('[^A-Za-z]+', ' ', topic)
    topic_tokens = nltk.word_tokenize(topic)

    # After topic matching done, go through the essay and count occurences of each relevant word
    for i in range(len(topic_keyword)):
        if topic_keyword[i] in topic_tokens:
            for j in relevant_words[i]:
                for token in tokens:
                    if j == token:
                        count += 1

    return count

#text = "I completely agree with the statement 'most advertisements make products seem much better than they really are.'"
#topic = "Do you agree or disagree with the following statement?		Most advertisements make products seem much better than they really are.		Use specific reasons and examples to support your answer."
#topic_coherence(text, topic)
