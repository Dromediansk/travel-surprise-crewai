#!/usr/bin/env python
import sys
import warnings

from .crew import TravelSurpriseAi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the travel profile analysis crew with cost optimization.
    Checks for existing output files before running AI agents.
    """
    print("🚀 Starting travel profile analysis...")
    print("=" * 50)
    
    # Initialize crew instance to check for existing outputs
    travel_crew = TravelSurpriseAi()
    existing_outputs = travel_crew.check_existing_outputs()
    
    # Check if we can reuse existing outputs
    if existing_outputs['travel_profile_exists'] and existing_outputs['destination_exists']:
        print("💰 COST OPTIMIZATION: Found existing output files!")
        print("📁 Reusing previous analysis to save on AI costs...")
        print("-" * 50)
        
        # Load existing travel profile analysis
        travel_profile_content = travel_crew.load_existing_output('travel_profile_analysis.md')
        if travel_profile_content:
            print("✅ Loaded existing travel profile analysis")
            print("📄 File: output/travel_profile_analysis.md")
            print(f"📊 Size: {len(travel_profile_content)} characters")
        
        # Load existing destination recommendations
        destination_content = travel_crew.load_existing_output('destination_recommendations.md')
        if destination_content:
            print("✅ Loaded existing destination recommendations")
            print("📄 File: output/destination_recommendations.md")
            print(f"📊 Size: {len(destination_content)} characters")
        
        print("\n" + "="*60)
        print("🎯 USING EXISTING ANALYSIS (NO AI COST)")
        print("="*60)
        print("💡 To generate fresh analysis, delete files in 'output' folder")
        
        # Return combined existing content
        return {
            'travel_profile': travel_profile_content,
            'destination_recommendations': destination_content,
            'cost_saved': True
        }
    
    else:
        # Some or all files missing, run AI crew
        missing_files = []
        if not existing_outputs['travel_profile_exists']:
            missing_files.append('travel_profile_analysis.md')
        if not existing_outputs['destination_exists']:
            missing_files.append('destination_recommendations.md')
            
        print(f"🤖 Running AI crew - Missing files: {', '.join(missing_files)}")
        print("💸 This will incur AI costs...")
        print("-" * 50)
    
    # Example user input for travel profile analysis
    user_input = """
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
    
    inputs = {
        'user_input': user_input
    }
    
    try:
        result = travel_crew.crew().kickoff(inputs=inputs)
        
        print("\n" + "="*60)
        print("🎯 TRAVEL PROFILE ANALYSIS COMPLETE")
        print("="*60)
        print(result)
        
        return result
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    user_input = """
    Budget: $2000
    Duration: 4 days
    Interests: Art, museums, coffee culture
    Travel style: Budget-conscious but quality experiences
    Departure location: Los Angeles
    Group size: Solo traveler
    """
    
    inputs = {
        "user_input": user_input
    }
    try:
        TravelSurpriseAi().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TravelSurpriseAi().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    user_input = """
    Budget: $1500
    Duration: 4-5 days
    Interests: Nature, hiking, wellness
    Travel style: Adventure but comfortable
    Departure location: Kosice, Slovakia
    Group size: Couple
    """
    
    inputs = {
        "user_input": user_input
    }
    
    try:
        TravelSurpriseAi().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


# Add execution logic
if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "run":
            run()
        elif command == "train":
            if len(sys.argv) < 4:
                print("Usage: python main.py train <n_iterations> <filename>")
                sys.exit(1)
            train()
        elif command == "replay":
            if len(sys.argv) < 3:
                print("Usage: python main.py replay <task_id>")
                sys.exit(1)
            replay()
        elif command == "test":
            if len(sys.argv) < 4:
                print("Usage: python main.py test <n_iterations> <eval_llm>")
                sys.exit(1)
            test()
        else:
            print(f"❌ Unknown command: {command}")
            print("Available commands: run, train, replay, test")
            sys.exit(1)
    else:
        # Default to run if no command is provided
        print("No command provided. Running default 'run' command...")
        run()
