# To run sentence count, download Stanford Core NLP package and its python wrapper.
# I used pycorenlp. You can download it by simply using pip command.
# To run this code, you need to start a CoreNLP server.
# Fire up command prompt and traverse to stanford-corenlp-full-2015-12-09 directory
# or whichever version you downloaded and run:
# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer
# Author: Shobhit Lamba, Mohit Adwani

from pycorenlp import StanfordCoreNLP

if __name__ == '__main__':
    nlp = StanfordCoreNLP('http://localhost:9000')

    text = ("I am happy I am a king.")
    output = nlp.annotate(text, properties={
        'annotators': 'parse',
        'outputFormat': 'json'
    })

    count = 0

    for index in range(len(output['sentences'])):
        parseTree = output['sentences'][0]['parse']
        parsedList = parseTree.split(' ' or '\r\n')
        for i, char in enumerate(parseTree):
            if char == 'S' and parseTree[i - 1] == '(' and parseTree[i + 1] != 'B':
                count += 1

    print("Number of sentences: ", count)
