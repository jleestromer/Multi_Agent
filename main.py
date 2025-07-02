from core.orchestrator import Orchestrator
import sys

if __name__ == "__main__":
    requirement = sys.argv[1] if len(sys.argv) > 1 else "Create a BMI calculator"
    orchestrator = Orchestrator()
    result = orchestrator.run(requirement)
    print(result["code"])
