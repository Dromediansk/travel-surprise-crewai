#!/usr/bin/env python
import sys
import warnings

from .crew import TravelSurpriseAi
from .inputs import get_input, list_available_inputs

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(input_type="default"):
    """
    Run the travel profile analysis crew with cost optimization.
    Checks for existing output files before running AI agents.
    
    Args:
        input_type (str): Type of input to use (default, family_vacation, solo_adventure, etc.)
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
    user_input = get_input(input_type)
    print(f"📝 Using input type: {input_type}")
    
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
    user_input = get_input("training")
    
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
    user_input = get_input("test")
    
    inputs = {
        "user_input": user_input
    }
    
    try:
        TravelSurpriseAi().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


# Wrapper functions for project.scripts (no arguments needed)
def run_default():
    """Wrapper function for project.scripts - runs with default input"""
    return run("default")

def train_default():
    """Wrapper function for project.scripts - trains with default parameters"""
    try:
        user_input = get_input("training")
        inputs = {"user_input": user_input}
        TravelSurpriseAi().crew().train(n_iterations=2, filename="training_output.json", inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def test_default():
    """Wrapper function for project.scripts - tests with default parameters"""
    try:
        user_input = get_input("test")
        inputs = {"user_input": user_input}
        TravelSurpriseAi().crew().test(n_iterations=2, eval_llm="gpt-4o", inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def replay_default():
    """Wrapper function for project.scripts - replays last task"""
    try:
        # You would need to specify an actual task_id here
        print("❌ Replay requires a task_id. Use: python -m src.travel_surprise_crew.main replay <task_id>")
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def list_inputs():
    """Wrapper function for project.scripts - lists available inputs"""
    return list_available_inputs()


# Add execution logic
if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "run":
            # Check if input type is specified
            input_type = sys.argv[2] if len(sys.argv) > 2 else "default"
            run(input_type)
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
        elif command == "inputs" or command == "list-inputs":
            list_available_inputs()
        else:
            print(f"❌ Unknown command: {command}")
            print("Available commands: run, train, replay, test, inputs")
            print("💡 Use 'inputs' to see available input configurations")
            sys.exit(1)
    else:
        # Default to run if no command is provided
        print("No command provided. Running default 'run' command...")
        print("💡 Use 'python main.py inputs' to see available input configurations")
        run()
