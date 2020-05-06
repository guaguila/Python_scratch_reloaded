def print_profile(profile):
    """Print the profile"""
    for k in profile:
        print (k.upper() + ": " + profile[k].upper())

def build_profile (first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile ['first_name'] = first
    profile ['last_name'] = last
    for key, value in user_info.items():
        profile [key] = value
    return profile

user_profile = build_profile('gustavo', 'aguilar',
                             location = 'CR',
                             future_location = 'US',
                             field = 'engineering')

print_profile(user_profile)


