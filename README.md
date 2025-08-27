# Surprise Travel Planning AI Crew

Welcome to the Surprise Travel Planning AI Crew project, powered by [crewAI](https://crewai.com). This intelligent multi-agent system is designed to create personalized surprise travel experiences by analyzing traveler preferences, discovering unique destinations, and crafting detailed itineraries that delight and surprise travelers.

## 🌍 Project Overview

Our AI crew specializes in surprise travel planning by leveraging multiple specialized agents that work together to:

- **Analyze Traveler Profiles**: Deep understanding of travel preferences, budget, and personality
- **Discover Hidden Gems**: Find unique, off-the-beaten-path destinations
- **Craft Surprise Itineraries**: Create detailed day-by-day plans with surprise elements
- **Optimize Budgets**: Balance cost-effectiveness with memorable experiences

## 🚀 Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

```bash
crewai install
```

### 🔧 Configuration

**Add your `OPENAI_API_KEY` into the `.env` file**

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### ✨ Customizing Your Travel Crew

- **Agents**: Modify `src/config/agents.yaml` to define specialized travel agents
- **Tasks**: Modify `src/travel_surprise_crew/config/tasks.yaml` to define travel planning tasks
- **Crew Logic**: Modify `src/travel_surprise_crew/crew.py` to add custom logic, travel tools, and integrations
- **User Input**: Modify `src/travel_surprise_crew/main.py` to customize traveler preference inputs

## 🎯 Running the Project

The Surprise Travel Planning Crew offers multiple ways to run and interact with the system. All commands support cost optimization by reusing existing analysis files when available.

### 🚀 Basic Execution

To start your surprise travel planning crew with the default configuration:

```bash
$ crewai run
```

Or use the Python module directly:

```bash
$ python -m src.travel_surprise_crew.main run
```

### 📋 Available Commands

#### **run** - Execute Travel Planning

```bash
# Run with default travel scenario (couple from Kosice)
$ python -m src.travel_surprise_crew.main run

# Run with specific travel scenario
$ python -m src.travel_surprise_crew.main run solo_adventure
$ python -m src.travel_surprise_crew.main run family_vacation
$ python -m src.travel_surprise_crew.main run luxury_romantic
$ python -m src.travel_surprise_crew.main run business_weekend
```

#### **inputs** - View Available Travel Scenarios

```bash
# List all available travel input configurations
$ python -m src.travel_surprise_crew.main inputs
```

#### **train** - Train the Crew

```bash
# Train the crew with specified iterations and output file
$ python -m src.travel_surprise_crew.main train <n_iterations> <filename>
```

#### **test** - Test Crew Performance

```bash
# Test the crew with evaluation metrics
$ python -m src.travel_surprise_crew.main test <n_iterations> <eval_llm>
```

#### **replay** - Replay Previous Execution

```bash
# Replay a specific task from previous execution
$ python -m src.travel_surprise_crew.main replay <task_id>
```

### 🎭 Travel Scenarios

The system includes pre-configured travel scenarios for different types of trips:

#### **default** - Romantic Anniversary Trip

- **Budget**: €2000 total
- **Duration**: 4-5 days
- **Group**: Couple (2 people)
- **Style**: Comfortable but authentic experiences
- **Focus**: Photography, cuisine, cultural experiences
- **From**: Kosice, Slovakia

#### **family_vacation** - Family Adventure

- **Budget**: €3500 total
- **Duration**: 7 days
- **Group**: Family of 4 (2 adults, 2 children)
- **Style**: Child-friendly and educational
- **Focus**: Theme parks, beaches, interactive museums
- **From**: Prague, Czech Republic

#### **solo_adventure** - Backpacker Experience

- **Budget**: €1200 total
- **Duration**: 5-6 days
- **Group**: Solo female traveler
- **Style**: Social backpacker with safety focus
- **Focus**: Adventure sports, culture, meeting people
- **From**: Bratislava, Slovakia

#### **luxury_romantic** - High-End Getaway

- **Budget**: €5000 total
- **Duration**: 3-4 days
- **Group**: Couple
- **Style**: Luxury and exclusive experiences
- **Focus**: Fine dining, spas, wine tasting
- **From**: Vienna, Austria

#### **business_weekend** - Efficient City Break

- **Budget**: €1800 total
- **Duration**: 2-3 days
- **Group**: Solo business traveler
- **Style**: Efficient with leisure blend
- **Focus**: Networking, quality dining, easy transport
- **From**: Munich, Germany

### 💰 Cost Optimization

The system automatically detects existing analysis files and reuses them to save on AI costs:

- **Existing Files Found**: Loads previous analysis without AI calls
- **Missing Files**: Runs only necessary AI agents
- **Fresh Analysis**: Delete files in `output/` folder to force new analysis

### 📁 Output Files

All analysis results are saved in the `output/` directory:

- `travel_profile_analysis.md` - Detailed traveler personality and preferences
- `destination_recommendations.md` - Curated destination suggestions and itineraries

### 📝 Custom Travel Inputs

You can easily customize travel preferences by editing `src/travel_surprise_crew/inputs.py`:

1. **Modify existing scenarios** in the file
2. **Add new scenarios** to `ALTERNATIVE_INPUTS`
3. **Change the default scenario** by updating `DEFAULT_TRAVEL_INPUT`

### 📝 Example Usage

The crew will analyze traveler input such as:

```
Budget: €2000 total
Duration: 4-5 days
Interests: Photography, local cuisine, cultural experiences
Travel style: Comfortable but authentic experiences
Departure location: Kosice, Slovakia
Travel dates: Flexible within next 3 months
Group size: Couple (2 people)
Special requirements: Surprise element essential, vegetarian-friendly options
```

And generate comprehensive travel profiles and recommendations.

## 🤖 Understanding Your Travel Crew

The Surprise Travel Planning Crew is composed of specialized AI agents, each with unique roles focused on different aspects of travel planning:

### Current Agents

- **Travel Profile Analyst**: Analyzes user preferences, budget, and constraints to create detailed traveler profiles
- **Destination Researcher**: Discovers unique, personalized destinations based on traveler profiles
  <!-- - **Itinerary Planner**: Creates detailed day-by-day surprise itineraries -->
  <!-- - **Budget Optimizer**: Optimizes travel costs while maintaining quality experiences -->

These agents collaborate on travel planning tasks defined in `config/tasks.yaml`, leveraging their collective expertise to create unforgettable surprise travel experiences. The `config/agents.yaml` file outlines the capabilities and configurations of each travel specialist in your crew.

## 🏗️ Project Structure

```
surprise-travel-ai/
├── src/travel_surprise_crew/
│   ├── config/
│   │   ├── agents.yaml      # Travel agent definitions
│   │   └── tasks.yaml       # Travel planning tasks
│   ├── crew.py             # Main crew orchestration
│   └── main.py             # Entry point and user input
└── .env                   # API keys and configuration
```

## 🎨 Features

- **Personalized Analysis**: Deep traveler personality and preference assessment
- **Surprise Elements**: Carefully crafted unexpected experiences
- **Budget Optimization**: Smart allocation of travel budget
- **Cultural Integration**: Authentic local experiences
- **Dietary Considerations**: Vegetarian and special dietary accommodations
- **Flexible Scheduling**: Adaptable to various timeframes and constraints

## 📞 Support

For support, questions, or feedback regarding the Surprise Travel Planning Crew or crewAI:

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

## 🌟 Next Steps

1. **Configure your agents** in `config/agents.yaml`
2. **Define travel tasks** in `config/tasks.yaml`
3. **Add travel APIs** for real-time data (flights, hotels, activities)
4. **Expand the knowledge base** with destination information
5. **Build a web interface** for user-friendly input collection

Let's create amazing surprise travel experiences together with the power and simplicity of crewAI! ✈️🌍
