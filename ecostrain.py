# EcoStrain: minimal ecology micro-simulation
# Population dynamics with resource limitation and efficiency mutation
# Outputs: summary plot (graphs) and JSON history (logs)

import random
import os
import json
import matplotlib.pyplot as plt

# ----------------- OUTPUT PATHS -----------------
OUT_GRAPHS = "../graphs"
OUT_LOGS = "../logs"
os.makedirs(OUT_GRAPHS, exist_ok=True)
os.makedirs(OUT_LOGS, exist_ok=True)

# ----------------- MODEL -----------------
class Agent:
    def __init__(self, efficiency: float = 0.5):
        # efficiency controls resource → reproduction conversion
        self.eff = efficiency

    def mutate(self, rate: float = 0.05):
        self.eff = max(0.01, min(1.0, self.eff + random.uniform(-rate, rate)))

def run_sim(
    days: int = 80,
    init_pop: int = 40,
    init_resource: float = 200.0,
    regen: float = 10.0,
    mutrate: float = 0.05
):
    pop = [Agent(eff=random.uniform(0.3, 0.7)) for _ in range(init_pop)]
    resource = init_resource

    history = {
        "day": [],
        "pop_size": [],
        "avg_eff": [],
        "resource": []
    }

    for d in range(days):
        # resource demand proportional to population efficiency
        total_need = sum(0.5 + a.eff for a in pop)
        available = min(resource, total_need)

        new_pop = []
        for a in pop:
            share = (0.5 + a.eff) / (total_need or 1) * available

            # reproduction condition
            if share > 0.6:
                new_pop.append(Agent(eff=a.eff))

            # survival condition
            if share > 0.2 or random.random() < 0.5:
                new_pop.append(a)

        # mutate traits
        for a in new_pop:
            if random.random() < 0.1:
                a.mutate(rate=mutrate)

        # population cap for stability
        pop = new_pop[:200]

        # resource regeneration and stochastic shock
        resource = max(0.0, resource - available) + regen
        if random.random() < 0.03:
            resource *= random.uniform(0.4, 0.8)

        # record stats
        history["day"].append(d)
        history["pop_size"].append(len(pop))
        history["avg_eff"].append(
            sum(a.eff for a in pop) / len(pop) if pop else 0.0
        )
        history["resource"].append(resource)

    # ----------------- SAVE OUTPUTS -----------------
    # Plot summary
    plt.figure(figsize=(7, 3))
    plt.plot(history["day"], history["pop_size"], label="population size")
    plt.plot(history["day"], history["avg_eff"], label="avg efficiency")
    plt.plot(history["day"], history["resource"], label="resource")
    plt.xlabel("Day")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_GRAPHS, "ecostrain_summary.png"))
    plt.close()

    # Save history log
    with open(os.path.join(OUT_LOGS, "ecostrain_history.json"), "w") as f:
        json.dump(history, f, indent=2)

    print("EcoStrain complete.")
    print("Graph saved to:", os.path.abspath(OUT_GRAPHS))
    print("Log saved to:", os.path.abspath(OUT_LOGS))

if __name__ == "__main__":
    run_sim()
