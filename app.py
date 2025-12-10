from flask import Flask, render_template, jsonify, request
import random
from words import verbs, adjectives, nouns

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/spin')
def api_spin():
    # Check if alliteration mode is enabled
    alliteration = request.args.get('alliteration', 'false').lower() == 'true'
    
    if alliteration:
        # Pick a random letter that has words in all three categories
        # Get all possible starting letters
        verb_letters = set(word[0].lower() for word in verbs)
        adj_letters = set(word[0].lower() for word in adjectives)
        noun_letters = set(word[0].lower() for word in nouns)
        
        # Find letters that exist in all three lists
        common_letters = list(verb_letters & adj_letters & noun_letters)
        
        if common_letters:
            # Pick a random letter
            chosen_letter = random.choice(common_letters)
            
            # Filter words by chosen letter
            filtered_verbs = [w for w in verbs if w[0].lower() == chosen_letter]
            filtered_adjs = [w for w in adjectives if w[0].lower() == chosen_letter]
            filtered_nouns = [w for w in nouns if w[0].lower() == chosen_letter]
            
            result = {
                'word1': random.choice(filtered_verbs),
                'word2': random.choice(filtered_adjs),
                'word3': random.choice(filtered_nouns)
            }
        else:
            # Fallback to normal mode if no common letters
            result = {
                'word1': random.choice(verbs),
                'word2': random.choice(adjectives),
                'word3': random.choice(nouns)
            }
    else:
        # Normal mode - pick random words
        result = {
            'word1': random.choice(verbs),
            'word2': random.choice(adjectives),
            'word3': random.choice(nouns)
        }
    
    return jsonify(result)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)
