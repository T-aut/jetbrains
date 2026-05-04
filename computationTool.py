import json
from collections import defaultdict
from docent import Docent

client = Docent(api_key="")

COLLECTIONS = {
    "Claude 4.5 Opus (high reasoning)": "1ebbdd7a-55b3-4015-9b83-5978cc7fb618",
    "Gemini 3 Flash (high reasoning)": "1ebbdd7a-55b3-4015-9b83-5978cc7fb618",
    "MiniMax M2.5 (high reasoning)": "5b77e003-7328-4003-879e-9b55dd3a0b6f",
    "Claude Opus 4.6": "9243cc78-d399-402f-be97-e366ff63282c",
    "GPT-5-2 Codex": "fb22a2e4-0a41-4d41-8e1e-388d4cb50d80"
}

stats = defaultdict(lambda: defaultdict(int))

for model_name, collection_id in COLLECTIONS.items():
    result = client.execute_dql(
        collection_id,
        "SELECT t.messages FROM transcripts t JOIN agent_runs ar ON ar.id = t.agent_run_id"
    )
    rows = client.dql_result_to_dicts(result)

    for row in rows:
        messages = row["messages"] if isinstance(row["messages"], list) else json.loads(row["messages"])
        stats[model_name]["trajectories"] += 1

        for msg in messages:
            stats[model_name][msg.get("role", "unknown")] += 1

for model, counts in stats.items():
    n = counts["trajectories"]
    total = sum(v for k, v in counts.items() if k != "trajectories")

    print(f"\n{model}\t({n} trajectories)")
    print("─" * 50)
    for role in ["system", "user", "assistant", "tool"]:
        c = counts[role]
        print(f"{role:<12}\t{c:>8}\t\tavg {c/n:.2f}/traj")
    print("─" * 50)
    print(f"{'TOTAL':<12}\t{total:>8}\t\tavg {total/n:.2f}/traj")
    print(f"\n")
