import math


def get_influencer_score(num_followers, average_engagement_percentage):
    result = average_engagement_percentage * math.log(num_followers, 2)

    return result

