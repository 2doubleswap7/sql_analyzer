import re
import matplotlib.pyplot as plt

async def visulize_query_plan(explain_output: str):
    operations = []
    times = []

    for line in explain_output.split("\n"):
        if "->" in line:
            op = line.split("-> ")[1].split(" ")[0]
            cost_match = re.search(r"cost=([\d.]+)\.\.([\d.]+)", line)
            if cost_match:
                cost = float(cost_match.group(2))
                operations.append(op)
                times.append(cost)
    
    plt.barh(operations, times)
    plt.xlabel("Cost")
    plt.ylabel("Operation")
    plt.title("Query Execution Plan")
    plt.show()
