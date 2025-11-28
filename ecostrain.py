# ecostrain.py
# Tiny ecology micro-sim: population vs resource with mutation of efficiency trait.
import random, os
import matplotlib.pyplot as plt
import json

OUT = "../graphs"
os.makedirs(OUT, exist_ok=True)

class Agent:
    def __init__(self, efficiency=0.5):
        self.eff = efficiency  # how well it converts resource -> reproduction

    def mutate(self, rate=0.05):
        self.eff = max(0.01, min(1.0, self.eff + random.uniform(-rate, rate)))

def run_sim(days=80, init_pop=40, init_resource=200.0, regen=10.0, mutrate=0.05):
    pop = [Agent(eff=random.uniform(0.3,0.7)) for _ in range(init_pop)]
    resource = init_resource
    history = {"day":[], "pop_size":[], "avg_eff":[], "resource": []}
    for d in range(days):
        # resource consumption proportional to pop*eff
        total_need = sum(0.5 + a.eff for a in pop)
        available = min(resource, total_need)
        # reproduction chance per agent based on share of available
        new_pop = []
        for a in pop:
            share = (0.5 + a.eff) / (total_need or 1) * available
            # reproduction if share above threshold
            if share > 0.6:
                new_pop.append(Agent(eff=a.eff))
            # survival: keep agent sometimes
            if share > 0.2 or random.random() < 0.5:
                new_pop.append(a)
        # mutate new population traits
        for a in new_pop:
            if random.random() < 0.1:
                a.mutate(rate=mutrate)
        pop = new_pop[:200]  # cap population
        # resource regen
        resource = max(0.0, resource - available) + regen
        # occasional shock
        if random.random() < 0.03:
            resource *= random.uniform(0.4,0.8)
        # record
        history["day"].append(d)
        history["pop_size"].append(len(pop))
        history["avg_eff"].append(sum(a.eff for a in pop)/len(pop) if pop else 0.0)
        history["resource"].append(resource)
    # save plot
    plt.figure(figsize=(7,3))
    plt.plot(history["day"], history["pop_size"], label="pop_size")
    plt.plot(history["day"], history["avg_eff"], label="avg_eff")
    plt.plot(history["day"], history["resource"], label="resource")
    plt.legend()
    plt.tight_layout()
    fname = os.path.join(OUT, "ecostrain_summary.png")
    plt.savefig(fname)
    plt.close()
    # save json
    with open(os.path.join(OUT, "ecostrain_history.json"), "w") as f:
        json.dump(history, f, indent=2)
    print("Saved graph + history to", OUT)

if __name__ == "__main__":
    run_sim()
