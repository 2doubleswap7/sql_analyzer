import re

from typing import Dict, Any

async def analyze_explain_plan(explain_output: str) -> Dict[str, Any]:
    analysis = {
        "has_seq_scan": False,
        "missing_indexes": [],
        "slowest_operation": None,
        "execution_time": 0.0
    }

    if "Seq Scan" in explain_output:
        analysis["has_seq_scan"] = True
        table_match = re.search(r"Seq Scan on (\w+)", explain_output)
        if table_match:
            analysis["missing_indexes"].append(table_match.group(1))
    
    time_match = re.search(r"Execution Time: ([\d.]+) ms", explain_output)
    if time_match:
        analysis["execution_time"] = float(time_match.group(1))
    
    return analysis
