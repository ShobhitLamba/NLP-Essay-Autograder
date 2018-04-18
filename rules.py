verbs = [
	"MD",
	"VB",
	"VBZ",
	"VBD",
	"VBG",
	"VBN",
	"VBP"
]

verbs_with_adverb = [
	"MD",
	"VB",
	"VBZ",
	"VBD",
	"VBG",
	"VBN",
	"VBP",
    "RB"
]

fourgram_rules = [

"VBZ, RB, VBN, VBN",
"VBZ, RB, VBN, VBG",
"MD, RB, VB, VBG",
"MD, RB, VB, VBN"

]

trigram_rules = [

"VBZ, VBN, VBN",
"VBZ, VBN, VBG",
"MD, VB, VBG",
"MD, VB, VBN",

"VBZ, RB, VBG",
"VBZ, RB, VBN",
"VBZ, RB, VB",

"VBP, RB, VBG",
"VBP, RB, VBN",
"VBP, RB, VB",

"VBD, RB, VBG",
"VBD, RB, VBN",
"VBD, RB, VB",

"MD, RB, VB"
]

bigram_rules = [

"VBZ, VBG",
"VBZ, VBN",
"VBZ, VB",

"VBP, VBG",
"VBP, VBN",
"VBP, VB",

"VBD, VBG",
"VBD, VBN",
"VBD, VB",

"MD, VB",

"VBP, RB", #- I am finally fine.
"VBZ, RB", #- He is finally fine
"VBD, RB", #- He sang finally.

]

unigram_rules = [

"VBP", #- I am fine.
"VBZ", #- He is fine
"VBD", #- He sang.

]
