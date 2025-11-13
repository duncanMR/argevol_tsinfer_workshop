
### Hack below - can be removed when questions are saved to JSON files named Q1.json, Q2.json etc
# This allows answers to be hidden from the casual viewer. Then we can simply set the url to a string instead of a class
class FakeURL(dict):
    def __add__(self, prefix):
        return self[prefix]
WB_base = FakeURL()
true, false= True, False  # just to allow easy conversion to JSON format
### hack ends

WB_base["Q1.json"] = [{
    "question": "The <code>shape</code> fields shows the named dimensions of arrays like 'variants'. By considering variable names and their shapes, how many <b>diploid individuals</b> are there in this dataset?",
    "type": "numeric",
    "answers": [
        {"type": "value", "value": 100, "correct": true, "feedback": "Yes, there are 100 diploid individuals (referred to as 'samples' in this context)"},
        {"type": "default", "feedback": "Hint: the ploidy of the organism is 2, which is one of the named dimensions."}
    ]
}]

WB_base["Q2.json"] = [{
    "question": "Challenge question: How many singletons are in this dataset? Use the box below",
    "type": "numeric",
    "answers": [
        {"type": "value", "value": 2822, "correct": true, "feedback": "Correct!"},
        {"type": "default", "feedback": "Hint: <code>np.sum</code> can count the 1s in an array..."}
    ]
}]

WB_base["Q3.json"] = [{
    "question": "Redo <code>match_samples</code> with a crazy high mismatch ratio of 100 in the box below (don't do this with your real data!). Challenge question: How many recurrent sites are there?",
    "type": "numeric",
    "answers": [
        {"type": "value", "value": 1185, "correct": true, "feedback": "Correct!"},
        {"type": "value", "value": 2022, "correct": false, "feedback": "No: some sites have more than 1 recurrent mutation so you can't just calculate num_mutations - num_sites here."},
        {"type": "default", "feedback": "Hint: The code block with a loop over sites may be helpful.."}
    ]
}]


WB_base["Q4.json"] = [{
    "question": "Explore the various tabs of tsbrowse. Using the Tables, how many mutations are on Tree 1?",
    "type": "numeric",
    "answers": [
        {"type": "value", "value": 26, "correct": true, "feedback": "Correct!"},
        {"type": "default", "feedback": "Nope: make sure you're not using the 100 mismatch ratio ARG!"}
    ]
}]