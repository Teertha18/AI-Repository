"""
Prompt Builder
"""

import json


class PromptBuilder:

    @staticmethod
    def build(context: dict) -> str:

        return f"""
You are a Senior Google Cloud Architect and FinOps Expert.

Analyze the following Google Cloud environment.

Cloud Metrics:

{json.dumps(context, indent=2)}

Your tasks:

1. Analyze the health of each service.
2. Predict utilization for the next 30 days.
3. Explain your reasoning.
4. Recommend optimization actions.
5. Mention business impact.
6. Assign a confidence score (0-100).

Return ONLY valid JSON.

Expected format:

{{
  "executive_summary":"",

  "services":[
    {{
      "service":"bigquery",

      "health":"Healthy",

      "prediction":"",

      "confidence":95,

      "reasoning":"",

      "recommendation":"",

      "business_impact":""
    }}
  ]
}}
"""