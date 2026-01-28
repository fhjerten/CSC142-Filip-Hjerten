import random

class Movie:
    def __init__(self, title,):
        self.title = title
        self.reviews =[]  # Makes it able to store various reviews

    def __str__(self):
        return f"Movie title: {self.title}"
    
    def add_review(self, review):
        self.reviews.append(review) # append adds a review to the reviews list

    def average_rating(self):
        
        if not self.reviews:
            return 0  # It is 0 if there is no reviews
        
        total = 0
        for r in self.reviews:
            total += r.rating # add each review's rating to the total rating
        return total / len(self.reviews) 
        # It returns the total rating in reviews divided by the amount of ratings

    def display_reviews(self):

        if not self.reviews: # same here with 0.
            print ("No reviews yet")
            return
        for r in self.reviews:
            print (r)

    def best_review(self):
        if not self.reviews:
            return None
        
        highest = max(r.rating for r in self.reviews)
        return random.choice([r for r in self.reviews if r.rating == highest])
    
    def worst_review(self):

        if not self.reviews:
            return None
        
        lowest = min (r.rating for r in self.reviews)
        return random.choice([r for r in self.reviews if r.rating == lowest])


class Review:
    def __init__(self, rating, text):
        self.rating = rating
        self.text = text

    def __str__(self):
        return f"{self.rating}/5: {self.text}"

# Testing 
#m1 = Movie("Inception")
#r1 = Review(4, "great")
#print (m1, r1) 

# testing avg. rating
#m = Movie("Inception")
#m.add_review(Review(5, "Good movie"))
#m.add_review(Review(1, "Great movie"))
#m.add_review(Review(3, "Amazing movie"))
#print (m.average_rating())
#print ("Best review:", m.best_review()) 
#print ("Worst review:", m.worst_review())


# THE DRIVER CODE

if __name__ == "__main__":
    movie = Movie("Grown Ups 2")

    # The 5 reviews here
    movie.add_review(Review(5, "Amazing movie. Must watch!"))
    movie.add_review(Review(4, "Great movie"))
    movie.add_review(Review(3, "Good movie" ))
    movie.add_review(Review(2.5, "Not so good movie"))
    movie.add_review(Review(0, "I hate it!! no more Adam Sandler"))

    print (movie)
    print ("The average rating of movie is:", movie.average_rating())

    print ("Best review:", movie.best_review())
    print ("Worst review:", movie.worst_review())

    print ("All reviews:")
    movie.display_reviews()



    
    
