#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from latest_ai_development.crew import LatestAiDevelopment

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew with a single, comprehensive topic input from the user.
    """
    # Prompt the user to provide all search criteria within a single topic string
    topic = input(
        "Enter your vehicle search criteria (e.g., 'Looking for a petrol car "
        "under 15 lakhs with max mileage of 50,000 km'): "
    ).strip()

    inputs = {
        'topic': topic,
        'current_year': str(datetime.now().year)
    }

    try:
        LatestAiDevelopment().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()