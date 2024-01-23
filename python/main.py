import pandas as pd

d = {
    (
        "https://w3id.org/fair/fip/terms/Available-FAIR-Enabling-Resource",
        "https://w3id.org/fair/fip/terms/declares-current-use-of",
    ): 3,
    (
        "https://w3id.org/fair/fip/terms/Available-FAIR-Enabling-Resource",
        "https://w3id.org/fair/fip/terms/declares-planned-replacement-of",
    ): 3,
    (
        "https://w3id.org/fair/fip/terms/Available-FAIR-Enabling-Resource",
        "https://w3id.org/fair/fip/terms/declares-planned-use-of",
    ): 2,
    (
        "https://w3id.org/fair/fip/terms/FAIR-Enabling-Resource-to-be-Developed",
        "https://w3id.org/fair/fip/terms/declares-current-use-of",
    ): 1,
    (
        "https://w3id.org/fair/fip/terms/FAIR-Enabling-Resource-to-be-Developed",
        "https://w3id.org/fair/fip/terms/declares-planned-replacement-of",
    ): 0,
    (
        "https://w3id.org/fair/fip/terms/FAIR-Enabling-Resource-to-be-Developed",
        "https://w3id.org/fair/fip/terms/declares-planned-use-of",
    ): 1,
}


def get_value(use, relation, d):
    return d[(use, relation)] if (use, relation) in d.keys() else 0


def create_FAIR_matrix(df):
    df["value"] = df.apply(lambda x: get_value(x["resourcetype"], x["rel"], d), axis=1)

    # Do filtering between these lines.
    # ==========================================================================

    df = df[df["c"].str.contains("A")]

    # ==========================================================================

    pivot = pd.pivot_table(
        df,
        values="value",
        columns=["c", "community"],
        index=["sort", "question", "reslabel", "resource_id_used"],
        aggfunc="min",
    )
    return pivot


INPUT_FILE_PATH = "new_matrix.csv"
OUTPUT_FILE_PATH = "output/FAIR_convergence_matrix.xlsx"

if __name__ == "__main__":
    df = pd.read_csv(INPUT_FILE_PATH)
    matrix = create_FAIR_matrix(df=df)
    matrix.to_excel(OUTPUT_FILE_PATH)
