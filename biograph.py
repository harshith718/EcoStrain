# ============================================
#   BioGraph – Combined Sequence Visualizer
#           Clean MIT-Level Version
# ============================================

import os
import json
import matplotlib.pyplot as plt
from collections import Counter

# -------------------------------------------------------
# CONFIG — automatic folder paths (based on your setup)
# -------------------------------------------------------

# Your structure:
# micro_ecs/
#   └── ecostrain_or_biograph/
#         ├── code/
#         ├── graphs/
#         ├── final_best_sequence.txt
#         └── geneflux_final_best_sequence.txt

BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))

BIOSPIRE_SEQ = os.path.join(BASE_DIR, "final_best_sequence.txt")
GENEFLUX_SEQ = os.path.join(BASE_DIR, "geneflux_final_best_sequence.txt")
OUT_DIR = os.path.join(BASE_DIR, "graphs")

os.makedirs(OUT_DIR, exist_ok=True)

# Optional research doc (ignored if not found)
UPLOADED_RESEARCH_DOC = "/mnt/data/f414c8e7-313c-4086-8571-96aa847171bb (1).docx"


# -------------------------------------------------------
# Helper — load sequence (FASTA or raw TXT)
# -------------------------------------------------------
def load_sequence(path):
    if not os.path.exists(path):
        return None

    text = open(path, "r").read().strip()

    # If FASTA (starts with ">")
    if text.startswith(">"):
        lines = text.split("\n")
        text = "".join(lines[1:]).strip()

    # Keep only DNA characters
    clean = "".join([c for c in text.upper() if c in "ACGT"])
    return clean


# -------------------------------------------------------
# Plot nucleotide composition as bar chart
# -------------------------------------------------------
def plot_nt_composition(seq, title, outpath):
    counts = Counter(seq)
    labels = ["A", "C", "G", "T"]
    values = [counts[b] for b in labels]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=["#4C8BF5", "#3DB34A", "#F5A623", "#D93333"])
    plt.title(title)
    plt.xlabel("Nucleotide")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()


# -------------------------------------------------------
# Plot k-mer frequency (k=2)
# -------------------------------------------------------
def plot_kmer_heatmap(seq, title, outpath):
    kmers = [seq[i:i+2] for i in range(len(seq) - 1)]
    counts = Counter(kmers)

    all_kmers = [
        a + b for a in "ACGT" for b in "ACGT"
    ]  # 16 combos

    values = [counts[k] for k in all_kmers]
    matrix = [values]  # 1 row

    plt.figure(figsize=(10, 1.8))
    plt.imshow(matrix, cmap="viridis", aspect="auto")
    plt.yticks([])
    plt.xticks(range(16), all_kmers)
    plt.title(title)

    plt.colorbar(label="frequency")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()


# -------------------------------------------------------
# MAIN PIPELINE
# -------------------------------------------------------
def run_biograph():
    print("Loading sequences...")

    seq1 = load_sequence(BIOSPIRE_SEQ)
    seq2 = load_sequence(GENEFLUX_SEQ)

    if not seq1 and not seq2:
        print("ERROR: No sequences found.")
        print("Expected:", BIOSPIRE_SEQ)
        print("          ", GENEFLUX_SEQ)
        return

    if seq1:
        print("Processing BioSpire sequence…")
        plot_nt_composition(
            seq1,
            "BioSpire: Nucleotide Composition",
            os.path.join(OUT_DIR, "biograph_nt_biospire.png"),
        )
        plot_kmer_heatmap(
            seq1,
            "BioSpire: 2-mer Heatmap",
            os.path.join(OUT_DIR, "biograph_kmer_biospire.png"),
        )

    if seq2:
        print("Processing GeneFlux sequence…")
        plot_nt_composition(
            seq2,
            "GeneFlux: Nucleotide Composition",
            os.path.join(OUT_DIR, "biograph_nt_geneflux.png"),
        )
        plot_kmer_heatmap(
            seq2,
            "GeneFlux: 2-mer Heatmap",
            os.path.join(OUT_DIR, "biograph_kmer_geneflux.png"),
        )

    print("\nDONE! Graphs saved in:")
    print(" →", OUT_DIR)


# -------------------------------------------------------
# Run if executed directly
# -------------------------------------------------------
if __name__ == "__main__":
    run_biograph()
