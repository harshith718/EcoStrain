# ============================================
# BioGraph – Combined Sequence Visualizer
# ============================================

import os
import matplotlib.pyplot as plt
from collections import Counter

# -------------------------------------------------------
# Paths
# -------------------------------------------------------

BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), ".."))

BIOSPIRE_SEQ = os.path.join(BASE_DIR, "final_best_sequence.txt")
GENEFLUX_SEQ = os.path.join(BASE_DIR, "geneflux_final_best_sequence.txt")
OUT_DIR = os.path.join(BASE_DIR, "graphs")

os.makedirs(OUT_DIR, exist_ok=True)

# -------------------------------------------------------
# Load sequence (FASTA or raw)
# -------------------------------------------------------
def load_sequence(path):
    if not os.path.exists(path):
        return None

    with open(path, "r") as f:
        text = f.read().strip()

    if text.startswith(">"):
        text = "".join(text.splitlines()[1:])

    return "".join(c for c in text.upper() if c in "ACGT")

# -------------------------------------------------------
# Nucleotide composition plot
# -------------------------------------------------------
def plot_nt_composition(seq, title, outpath):
    counts = Counter(seq)
    labels = ["A", "C", "G", "T"]
    values = [counts[b] for b in labels]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values)
    plt.title(title)
    plt.xlabel("Nucleotide")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

# -------------------------------------------------------
# 2-mer frequency heatmap
# -------------------------------------------------------
def plot_kmer_heatmap(seq, title, outpath):
    kmers = [seq[i:i+2] for i in range(len(seq) - 1)]
    counts = Counter(kmers)

    all_kmers = [a + b for a in "ACGT" for b in "ACGT"]
    values = [counts[k] for k in all_kmers]

    plt.figure(figsize=(10, 2))
    plt.imshow([values], aspect="auto", cmap="viridis")
    plt.yticks([])
    plt.xticks(range(16), all_kmers)
    plt.title(title)
    plt.colorbar(label="Frequency")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

# -------------------------------------------------------
# Run
# -------------------------------------------------------
def run_biograph():
    seq1 = load_sequence(BIOSPIRE_SEQ)
    seq2 = load_sequence(GENEFLUX_SEQ)

    if not seq1 and not seq2:
        print("No sequences found.")
        return

    if seq1:
        plot_nt_composition(
            seq1,
            "BioSpire: Nucleotide Composition",
            os.path.join(OUT_DIR, "biograph_nt_biospire.png")
        )
        plot_kmer_heatmap(
            seq1,
            "BioSpire: 2-mer Frequency",
            os.path.join(OUT_DIR, "biograph_kmer_biospire.png")
        )

    if seq2:
        plot_nt_composition(
            seq2,
            "GeneFlux: Nucleotide Composition",
            os.path.join(OUT_DIR, "biograph_nt_geneflux.png")
        )
        plot_kmer_heatmap(
            seq2,
            "GeneFlux: 2-mer Frequency",
            os.path.join(OUT_DIR, "biograph_kmer_geneflux.png")
        )

    print("Graphs saved to:", OUT_DIR)

# -------------------------------------------------------
if __name__ == "__main__":
    run_biograph()
