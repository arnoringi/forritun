def is_valid(scores):
    scores_list = scores.split()
    if len(scores_list) < 2:
        print("At least two scores needed!")
    else:
        return scores_list

def sum_of_scores(scores_list):
    """ Sum of scores (two lowest removed) """
    try:
        # Convert to float
        float_list = [float(i) for i in scores_list]

        # Remove 2 lowest
        for i in range(2):
            float_list.remove(min(float_list))
        
        # Sum of all
        sum_float = 0
        for digit in float_list:
            sum_float += digit
        
        print("Sum of scores (two lowest removed):", round(sum_float, 1))
    except AttributeError:
        pass

# Main program starts here
scores = input("Enter scores separated by space: ")
scores_list = is_valid(scores)
sum_of_scores(scores_list)