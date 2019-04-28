from ChefRamsey import answerQuery
import nltk
from nltk.tokenize import RegexpTokenizer

questions = ["How should the celery be cut in Asian Pear Slaw?", "Can you substitute the ginger in Asian Pear Slaw?", "How long does Asian Pear Slaw take?", "How much fresh lime juice is needed in Asian Pear Slaw?", "What kind of peeler do I use for carrots in Asian Pear Slaw?", "Do you cut the celery into 1/4-inch-thick matchsticks in Asian Pear Slaw?", "Can I use any peeler in Asian Pear Slaw?", "How many Asian pears are used in Asian Pear Slaw?", "Does Asian Pear Slaw include any added sugar?", "What ingredients are in Asian Pear Slaw?", "How long does Asian Pear Slaw need to rest before serving?", "Is Asian Pear Slaw vegan?", "How much cilantro do I add to Asian Pear Slaw?", "What kind of pears should be used in Asian Pear Slaw?", "What temperature should the oven be preheated to in Bacon Crackers?", "How long should you bake Bacon Crackers?", "Why should we avoid getting sugar on the cracker in Bacon Crackers?", "How many strips of bacon do I make in Bacon Crackers?", "What are the ingredients in Bacon Crackers?", "How many slices of bacon are needed for Bacon Crackers?", "How much dark brown sugar do I use for Bacon Crackers?", "How do I make a fancified version of Bacon Crackers?", "What temperature do I preheat my gas grill in Baja Fish Tacos?", "How many flour tortillas do I need in Baja Fish Tacos?", "What type of slaw do I use for Baja Fish Tacos?", "What are the ingredients of Baja Fish Tacos?", "What fish is used in Baja Fish Tacos?", "Should I bake, fry, or grill the fish in Baja Fish Tacos?", "What spices will I need to make Baja Fish Tacos?", "What juice do I use in Baja Fish Tacos?", "How much olive oil do I need in Bahian Chicken and Shrimp Stew?", "How long do I marinate Bahian Chicken and Shrimp Stew?", "What is the special equipment for Bahian Chicken and Shrimp Stew?", "How long will it take to cook the chicken all the way through in Bahian Chicken and Shrimp Stew?", "How many calories are in Bahian Chicken and Shrimp Stew?", "How much lime juice do I use in Bahian Chicken and Shrimp Stew?", "How much salted roasted cocktail peanuts do I use in Bahian Chicken and Shrimp Stew?", "What are the ingredients in Bahian Chicken and Shrimp Stew?", "What do I heat the oven to for Banana Bread?", "How long do you bake the Banana Bread for?", "What kind of pan do I bake the Banana Bread in?"]

answers = ["The celery should be cut into 1/4-inch-thick matchsticks.", "No.", "1 Hour", "3 Tablespoons", "A y-shaped peeler.", "Yes.", "Yes.", "2 Asian pears.", "No.", "Asian Pear Slaw has celery, juice, vinegar, ginger, scallions, cilantro, hot red chile, and Asian pears.", "Asian Pear Slaw needs to rest at room temperature for 15 minutes before serving.", "Yes.", "1/4 cup fresh cilantro leaves", "firm Asian pears", "250°F", "1 to 1 1/2 hours", "It will burn.", "4", "The ingredients of Bacon Crackers are 12 bacon slices (not thick-cut), 48 saltines or buttery crackers, such as Club brand, 48 fresh rosemary tips (for Herbed Bacon Crackers), 6 teaspoons dark brown sugar (for Brown Sugar Bacon Crackers).", "12", "6 teaspoons", "The addition of a tine bundle of rosemary needles", "Medium-High", "8", "Southwestern", "The ingredients of Baja Fish Tacos are 2 lb mahi-mahi, 1/2 cup vegetable oil, 3 tbsp lime juice, 5 tsp chili powder, 1 1/2 tsp ground cumin, 1 1/2 tsp ground coriander, 1 1/2 tsp minced garlic, Salt, to taste, 8 flour tortillas, 8 inches in diameter, Southwestern Slaw, 1 cup Chipotle Pico de Gallo, 1/2 cup Mexican Crema.", "Mahi-mahi", "Grill", "5 tsp chili powder, 1 1/2 tsp ground cumin, 1 1/2 tsp ground coriander, 1 1/2 tsp minced garlic, Salt", "Lime", "2 tablespoons", "30 minutes", "An electric coffee/spice grinder", "25 to 30 minutes", "889.0", "2 tablespoons", "1/2 cup", "The ingredients of Bahian Chicken and Shrimp Stew are 1/4 cup extra-virgin olive oil, 1/4 cup fresh lime juice, 3 garlic cloves, chopped, 1 1/2 teaspoons salt, 3/4 teaspoon black pepper, 1 (3 1/2-lb) chicken, cut into 8 serving pieces, 1/2 lb medium shrimp in shell (21 to 25 per lb), peeled and deveined, 1 oz dried shrimp*, 1/2 cup salted roasted cocktail peanuts, 1/2 cup salted roasted cashews, 2 medium onions, chopped, 1 green bell pepper, chopped, 1 lb fresh tomatoes, chopped, 4 bottled red malagueta peppers** or 1- to 2-inch fresh red Thai chiles, 1 3/4 cups chicken stock or reduced-sodium chicken broth (14 fl oz), 1 cup well-stirred canned unsweetened coconut milk (8 fl oz), 1/2 cup chopped fresh cilantro, 2 tablespoons dendê oil***, optional, Special equipment: an electric coffee/spice grinder.", "350°F", "50 to 60 minutes", "9x5-inch loaf pan"]

number = 0

result = 0

tokenizer = RegexpTokenizer(r'\w+')

# TODO:
# tag tokens
# count tags
# build weighting on tags 

for question in questions:
    answer = answerQuery(question)
    answer = answer.lower()
    tokenized_answer = tokenizer.tokenize(answer)
    expected_answer = tokenizer.tokenize(answers[number].lower())
    expected_word_count = len(expected_answer)
    score = 0.0
    for word in tokenized_answer:
        if word in expected_answer:
            score += 100.0/expected_word_count
    result += score
    number += 1


result = result/len(questions)
print("ChefRAMsay has a ", result, "% accuracy!")
