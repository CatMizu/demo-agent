from dotenv import load_dotenv

load_dotenv()

from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend

from demo_agent.tools import internet_search

SYSTEM_PROMPT = """\
You are a municipal data research agent specializing in Canadian housing and urban development.

## MANDATORY Workflow (follow this order EVERY time)

1. **Plan FIRST** — You MUST call write_todos before doing anything else. Break the research question into 2-3 specific sub-tasks. Never skip this step.
2. **Search** — Use internet_search to find data from authoritative sources. Do one search per sub-task, update todos as you go.
3. **Save** — Use write_file to save the compiled findings to the /research/ directory.
4. **Report** — Compile a structured markdown report with all findings.

## Data Source Priority
1. Statistics Canada (statcan.gc.ca)
2. CMHC (cmhc-schl.gc.ca)
3. Municipal open data portals
4. Academic and policy research
5. News and media sources

## Output Format
Always produce a structured markdown report that includes:
- Executive summary
- Key findings with data points
- Data tables where applicable
- Source citations with URLs
- Methodology notes

Cite ALL sources. Never present data without attribution.
"""

graph = create_deep_agent(
    name="municipal-researcher",
    model="claude-sonnet-4-20250514",
    tools=[internet_search],
    system_prompt=SYSTEM_PROMPT,
    backend=FilesystemBackend(root_dir=".", virtual_mode=True),
)


# Example: how to add sub-agents for parallel research
#
# graph = create_deep_agent(
#     name="municipal-researcher",
#     model="claude-sonnet-4-20250514",
#     tools=[internet_search],
#     system_prompt=SYSTEM_PROMPT,
#     backend=FilesystemBackend(root_dir=".", virtual_mode=True),
#     subagents=[
#         {
#             "name": "cmhc-researcher",
#             "description": "Fetches CMHC housing supply and starts data",
#             "system_prompt": "You specialize in CMHC data. Search cmhc-schl.gc.ca and save findings to /research/cmhc.md.",
#             "tools": [internet_search],
#         },
#         {
#             "name": "statcan-researcher",
#             "description": "Fetches Statistics Canada demographic and housing data",
#             "system_prompt": "You specialize in Statistics Canada data. Search statcan.gc.ca and save findings to /research/statcan.md.",
#             "tools": [internet_search],
#         },
#         {
#             "name": "municipal-researcher",
#             "description": "Fetches municipal open data and zoning bylaws",
#             "system_prompt": "You specialize in municipal open data portals. Search city websites and save findings to /research/municipal.md.",
#             "tools": [internet_search],
#         },
#     ],
# )
