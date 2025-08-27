"""
Travel input configurations for the surprise travel planning crew.
Modify these inputs to customize your travel preferences without touching the main code.
"""

# Main travel input for the run command
DEFAULT_TRAVEL_INPUT = """
Budget: 2000 euro total
Duration: 4-5 days
Interests: Photography, local cuisine, cultural experiences, history
Travel style: Comfortable but authentic experiences
Departure location: Kosice, Slovakia
Travel dates: Flexible within next 3 months
Group size: Couple (2 people)
Special requirements: Surprise element essential, no extreme sports, prefer unique accommodations
Previous trips: Malaga, Valencia, Barcelona, Nice - loved the food scenes
Accommodation preference: Boutique hotels or unique local stays
Dietary restrictions: Vegetarian-friendly options needed
Additional notes: Anniversary trip, want something romantic but not cliché
"""

# Training input for the train command
TRAINING_INPUT = """
Budget: $2000
Duration: 4 days
Interests: Art, museums, coffee culture
Travel style: Budget-conscious but quality experiences
Departure location: Los Angeles
Group size: Solo traveler
"""

# Test input for the test command
TEST_INPUT = """
Budget: $1500
Duration: 4-5 days
Interests: Nature, hiking, wellness
Travel style: Adventure but comfortable
Departure location: Kosice, Slovakia
Group size: Couple
"""

# Alternative travel scenarios you can use by changing DEFAULT_TRAVEL_INPUT
ALTERNATIVE_INPUTS = {
    "family_vacation": """
Budget: 3500 euro total
Duration: 7 days
Interests: Family activities, theme parks, beaches, educational experiences
Travel style: Comfortable and child-friendly
Departure location: Prague, Czech Republic
Travel dates: Summer holidays
Group size: Family of 4 (2 adults, 2 children aged 8 and 12)
Special requirements: Child-friendly accommodations, activities for kids
Previous trips: Vienna, Munich, Rome - kids loved interactive museums
Accommodation preference: Family hotels with pools and entertainment
Dietary restrictions: No allergies, kids prefer familiar foods
Additional notes: Educational but fun, want memories for the kids
""",
    
    "solo_adventure": """
Budget: 1200 euro total
Duration: 5-6 days
Interests: Adventure sports, local culture, nightlife, meeting people
Travel style: Backpacker style but with some comfort
Departure location: Bratislava, Slovakia
Travel dates: Flexible, prefer off-season
Group size: Solo traveler
Special requirements: Safe for solo female traveler, social opportunities
Previous trips: Budapest, Krakow, Prague - loved the hostel scene
Accommodation preference: Hostels or guesthouses with social atmosphere
Dietary restrictions: None, love trying everything
Additional notes: Want to push comfort zone, meet fellow travelers
""",
    
    "luxury_romantic": """
Budget: 5000 euro total
Duration: 3-4 days
Interests: Fine dining, spas, wine tasting, romantic experiences
Travel style: Luxury and exclusive
Departure location: Vienna, Austria
Travel dates: Valentine's weekend or anniversary
Group size: Couple
Special requirements: Romantic atmosphere, privacy, high-end experiences
Previous trips: Paris, Venice, Santorini - loved luxury hotels
Accommodation preference: 5-star hotels or luxury resorts
Dietary restrictions: None, love fine dining
Additional notes: Special occasion, money no object, want unforgettable
""",
    
    "business_weekend": """
Budget: 1800 euro total
Duration: 2-3 days
Interests: Networking, business districts, efficient transport, quality dining
Travel style: Business traveler efficiency with some leisure
Departure location: Munich, Germany
Travel dates: Weekend extension of business trip
Group size: Solo business traveler
Special requirements: Good wifi, business center, easy airport access
Previous trips: Frankfurt, Zurich, Amsterdam - efficient business-friendly cities
Accommodation preference: Business hotels in city center
Dietary restrictions: None, prefer healthy options
Additional notes: Maximize short time, blend business and pleasure
"""
}

def get_input(input_type="default"):
    """
    Get travel input based on type.
    
    Args:
        input_type (str): Type of input to return
                         - "default": DEFAULT_TRAVEL_INPUT
                         - "training": TRAINING_INPUT  
                         - "test": TEST_INPUT
                         - Or any key from ALTERNATIVE_INPUTS
    
    Returns:
        str: Travel input string
    """
    if input_type == "default":
        return DEFAULT_TRAVEL_INPUT
    elif input_type == "training":
        return TRAINING_INPUT
    elif input_type == "test":
        return TEST_INPUT
    elif input_type in ALTERNATIVE_INPUTS:
        return ALTERNATIVE_INPUTS[input_type]
    else:
        print(f"⚠️  Unknown input type '{input_type}', using default")
        return DEFAULT_TRAVEL_INPUT

def list_available_inputs():
    """List all available input configurations."""
    print("📋 Available travel input configurations:")
    print("  - default: Couple from Kosice, photography & cuisine")
    print("  - training: Solo traveler from LA, art & museums")
    print("  - test: Couple from Kosice, nature & wellness")
    print("\n🎯 Alternative scenarios:")
    for key, _ in ALTERNATIVE_INPUTS.items():
        print(f"  - {key}: {key.replace('_', ' ').title()}")
