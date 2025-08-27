from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from langchain_openai import ChatOpenAI
from typing import List, Dict
import os
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class TravelSurpriseAi():
    """Travel Surprise AI crew for personalized travel planning"""

    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self) -> None:
        super().__init__()
        # Create output directory if it doesn't exist
        self.output_dir = "output"
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Define LLM configuration for all agents
        self.llm = ChatOpenAI(
            model="gpt-4o",          # Most powerful OpenAI model
            temperature=0.5,         # Good balance for creative travel planning
            max_tokens=4000         # Sufficient for detailed travel profiles
        )

    def check_existing_outputs(self) -> Dict[str, bool]:
        """Check if output files already exist to avoid unnecessary AI calls"""
        travel_profile_file = os.path.join(self.output_dir, 'travel_profile_analysis.md')
        destination_file = os.path.join(self.output_dir, 'destination_recommendations.md')
        
        return {
            'travel_profile_exists': os.path.exists(travel_profile_file) and os.path.getsize(travel_profile_file) > 0,
            'destination_exists': os.path.exists(destination_file) and os.path.getsize(destination_file) > 0
        }

    def load_existing_output(self, filename: str) -> str:
        """Load content from existing output file"""
        filepath = os.path.join(self.output_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading existing file {filepath}: {e}")
            return ""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def travel_profile_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['travel_profile_analyst'], # type: ignore[index]
            llm=self.llm,  # Use the configured LLM
            verbose=True
        )

    @agent
    def destination_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['destination_researcher'], # type: ignore[index]
            llm=self.llm,  # Use the configured LLM
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def analyze_travel_profile(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_travel_profile'], # type: ignore[index]
            output_file=os.path.join(self.output_dir, 'travel_profile_analysis.md')
        )

    @task
    def research_destinations(self) -> Task:
        return Task(
            config=self.tasks_config['research_destinations'], # type: ignore[index]
            output_file=os.path.join(self.output_dir, 'destination_recommendations.md')
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TravelSurpriseAi crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
