music_few_shot_examples = [
            {"input": "Play the latest song by Taylor Swift.", "query": "latest song by Taylor Swift"},
            {"input": "I want to listen to some relaxing piano music.", "query": "relaxing piano music"},
            {"input": "Play Pushpa 2 title song.", "query": "Pushpa 2 title song"},
            {"input": "Find and play some jazz music.", "query": "jazz music"},
            {"input": "Despacito song", "query": "Despacito song"},
            {"input": "I want the title song from the movie Pushpa.", "query": "title song from the movie Pushpa"},
            {"input": "Play the Devara Telugu movie title song.", "query": "Devara Telugu movie title song"},
            {"input": "Play something classical.", "query": "classical music"},
            {"input": "Can you find a remix of Shape of You?", "query": "Shape of You remix"},
            {"input": "Play Arijit Singh's latest hit.", "query": "Arijit Singh latest hit song"},
            {"input": "Find and play a calming meditation track.", "query": "calming meditation track"},
            {"input": "I want to hear Bollywood romantic songs.", "query": "Bollywood romantic songs"},
            {"input": "Play a workout playlist.", "query": "workout playlist"},
            {"input": "Do you have any rock music?", "query": "rock music"},
            {"input": "Find a Telugu devotional song for me.", "query": "Telugu devotional song"},
            {"input": "Play Ed Sheeran's Perfect.", "query": "Ed Sheeran Perfect"},
            {"input": "Play the background score of Interstellar.", "query": "Interstellar background score"},
            {"input": "Can you play 'Kala Chashma'?", "query": "Kala Chashma song"},
            {"input": "I want to listen to a live version of Rolling in the Deep.", "query": "live version of Rolling in the Deep"},
            {"input": "Find a trending pop song.", "query": "trending pop song"},
            {"input": "Play some 90s hits.", "query": "90s hits"},
            {"input": "Find an acoustic version of Hotel California.", "query": "acoustic version of Hotel California"},
            {"input": "Play a party anthem.", "query": "party anthem"},
            {"input": "Play something by Imagine Dragons.", "query": "Imagine Dragons songs"},
            {"input": "I want to listen to Lofi beats.", "query": "Lofi beats"},
            {"input": "Can you play the theme song from Harry Potter?", "query": "Harry Potter theme song"},
            {"input": "Play a motivational song.", "query": "motivational song"},
            {"input": "Find a Tamil melody.", "query": "Tamil melody"},
            {"input": "Play the OST from Game of Thrones.", "query": "Game of Thrones OST"},
            {"input": "Can you play a recent K-pop hit?", "query": "recent K-pop hit"},
            {"input": "Play the soundtrack of Titanic.", "query": "Titanic soundtrack"}
        ]

def music_prompt_template(user_input, few_shot_text):
     prompt = f"""
        You are a music query extraction assistant. Your task is to strictly extract the specific song name and language (if mentioned) 
        from the user's input. Follow these rules:

        1. Output only the song name or genre and the language (if specified).
        2. Do not include any additional interpretation, explanation, or context.
        3. If the input is unclear or ambiguous, return only the most relevant key terms directly related to the song or genre or print the user input directly if it is not clear.

        Here are examples:

        {few_shot_text}

        Input: {user_input}
        Query:
        """
     return prompt