import ROOT
ROOT.EnableImplicitMT()

# ============================================================
# GLOBALS
# ============================================================

TREE_NAME = "DecayTree"
WEIGHT_BRANCH = "FONLL_weight"

BASE_PATH = (
    "/eos/user/j/jodedra/AnalysisWork_2024/"
    "Analysistimeseff/full_unbiased_for_all_mc/"
    "CMSSW_12_4_11_patch3/src/Gen_matching_scripts/"
    "weighted_root_files/"
)

# ============================================================
# USER INPUT: MINIAOD RAW COUNTS (AFTER GENFILTER)
# ============================================================

MINIAOD_RAW = {
    "B0_JpsiEE_Kstar":       947766,  # <-- fill these
    "B0_Psi2SEE_Kstar":      98229,
    "Bu_JpsiPi":             1820486,
    "Bu_Chic1_JpsiPiPi":     1996426,
    "Bu_KstarJpsi_K0PiPi":   940945,
    "Bu_KstarPsi2S":         101412,
    "Bu_JpsiEE_Kstar_KPi0":  1938219,
}
INCLUSIVE_OUTFILE = "inclusive_miniaod_count.txt"

# ============================================================
# CORE ENGINE (MINIMALLY EXTENDED)
# ============================================================

def run_efficiency(
    name,
    key,
    filename,
    final_state_defs,
    multiplicity_reqs,
    selection_cut,
):
    print("\n==============================================")
    print(f" {name}")
    print("==============================================")

    df = ROOT.RDataFrame(TREE_NAME, BASE_PATH + filename)

    # -------------------------------
    # Define final-state collections
    # -------------------------------
    for label, pdg in final_state_defs.items():
        df = (
            df
            .Define(f"{label}_pt",  f"pt[abs(pdgId)=={pdg}]")
            .Define(f"{label}_eta", f"eta[abs(pdgId)=={pdg}]")
        )

    # -------------------------------
    # Multiplicity requirements
    # -------------------------------
    for label, n in multiplicity_reqs.items():
        df = df.Filter(f"{label}_pt.size() == {n}")

    # -------------------------------
    # Raw efficiency
    # -------------------------------
    den_raw = df.Count().GetValue()
    num_raw = df.Filter(selection_cut).Count().GetValue()
    eff_raw = num_raw / den_raw if den_raw > 0 else 0.0

    # -------------------------------
    # Weighted efficiency
    # -------------------------------
    df_w = df.Define("w", WEIGHT_BRANCH)
    den_w = df_w.Sum("w").GetValue()
    num_w = df_w.Filter(selection_cut).Sum("w").GetValue()
    eff_w = num_w / den_w if den_w > 0 else 0.0

    # -------------------------------
    # Transfer + ratio
    # -------------------------------
    transfer_factor = den_w / den_raw if den_raw > 0 else 0.0
    eff_ratio = eff_w / eff_raw if eff_raw > 0 else 0.0

    # -------------------------------
    # MiniAOD projections
    # -------------------------------
    miniaod_raw = MINIAOD_RAW.get(key, 0)

    miniaod_fonll_pass = miniaod_raw * eff_ratio

    miniaod_fonll_inclusive = (
        miniaod_raw
        * eff_ratio
        / eff_w
        * transfer_factor
        if eff_w > 0 else 0.0
    )

    # -------------------------------
    # Print
    # -------------------------------
    print(f"Input file                : {filename}")
    print(f"Raw denominator           : {den_raw}")
    print(f"Raw passing               : {num_raw}")
    print(f"Raw efficiency            : {eff_raw:.6f}")
    print("----------------------------------------------")
    print(f"Weighted denominator Σw   : {den_w:.6f}")
    print(f"Weighted passing Σw       : {num_w:.6f}")
    print(f"Weighted efficiency       : {eff_w:.6f}")
    print("----------------------------------------------")
    print(f"Efficiency ratio w/raw    : {eff_ratio:.6f}")
    print(f"Transfer factor <w>       : {transfer_factor:.6f}")
    print("----------------------------------------------")
    print(f"MiniAOD raw (pass GF)     : {miniaod_raw:.6f}")
    print(f"MiniAOD FONLL (pass GF)   : {miniaod_fonll_pass:.6f}")
    print(f"MiniAOD FONLL inclusive   : {miniaod_fonll_inclusive:.6f}")

    # ---- write to text file
    with open(INCLUSIVE_OUTFILE, "a") as f:
        f.write(
            f"{key:30s}  "
            f"{miniaod_fonll_inclusive:.6f}\n"
        )

    print("==============================================")





    print("==============================================")

# ============================================================
# CHANNEL DEFINITIONS (UNCHANGED LOGIC)
# ============================================================

def run_B0_JpsiEE_Kstar():
    run_efficiency(
        name="B0 → J/ψ(e⁺e⁻) K*0",
        key="B0_JpsiEE_Kstar",
        filename="B0_JpsiEE_Kstar_gen_FONLL.root",
        final_state_defs={"e": 11, "k": 321, "pi": 211},
        multiplicity_reqs={"e": 2, "k": 1, "pi": 1},
        selection_cut="""
            e_pt[0] > 3.0 && e_pt[1] > 3.0 &&
            abs(e_eta[0]) < 1.5 && abs(e_eta[1]) < 1.5 &&
            k_pt[0] > 0.5 && pi_pt[0] > 0.5
        """,
    )

def run_B0_Psi2SEE_Kstar():
    run_efficiency(
        name="B0 → ψ(2S)(e⁺e⁻) K*0",
        key="B0_Psi2SEE_Kstar",
        filename="B0_psi2SEE_Kstar_gen_FONLL.root",
        final_state_defs={"e": 11, "k": 321, "pi": 211},
        multiplicity_reqs={"e": 2, "k": 1, "pi": 1},
        selection_cut="""
            e_pt[0] > 3.0 && e_pt[1] > 3.0 &&
            abs(e_eta[0]) < 1.5 && abs(e_eta[1]) < 1.5 &&
            k_pt[0] > 0.5 && pi_pt[0] > 0.5
        """,
    )

def run_Bu_JpsiPi():
    run_efficiency(
        name="Bu → J/ψ(e⁺e⁻) π",
        key="Bu_JpsiPi",
        filename="buto_jpsi_pi_Gen_FONLL.root",
        final_state_defs={"e": 11, "pi": 211},
        multiplicity_reqs={"e": 2, "pi": 1},
        selection_cut="""
            e_pt[0] > 3.0 && e_pt[1] > 3.0 &&
            abs(e_eta[0]) < 1.5 && abs(e_eta[1]) < 1.5 &&
            pi_pt[0] > 0.5
        """,
    )

def run_Bu_Chic1_JpsiPiPi():
    run_efficiency(
        name="Bu → χc1 → J/ψ(e⁺e⁻)",
        key="Bu_Chic1_JpsiPiPi",
        filename="butokpluschic1_chic1tojpsi_jpsitoee_Gen_FONLL.root",
        final_state_defs={"e": 11, "k": 321},
        multiplicity_reqs={"e": 2, "k": 1},
        selection_cut="""
            e_pt[0] > 3.0 && e_pt[1] > 3.0 &&
            abs(e_eta[0]) < 1.5 && abs(e_eta[1]) < 1.5
        """,
    )

def run_Bu_KstarJpsi_K0PiPi():
    run_efficiency(
        name="Bu → K* J/ψ(e⁺e⁻), K*→K0π",
        key="Bu_KstarJpsi_K0PiPi",
        filename="BuToKstarJPsi_KstarToK0Pi_JPsiToEE_K0ToPiPi_Gen_FONLL.root",
        final_state_defs={"e": 11, "pi": 211},
        multiplicity_reqs={"e": 2, "pi": 3},
        selection_cut="""
            e_pt[0] > 3.0 && e_pt[1] > 3.0 &&
            abs(e_eta[0]) < 1.5 && abs(e_eta[1]) < 1.5 &&
            pi_pt[2] > 0.5 && pi_eta[2] < 2.5
        """,
    )

def run_Bu_KstarPsi2S():
    run_efficiency(
        name="Bu → K* ψ(2S)(e⁺e⁻)",
        key="Bu_KstarPsi2S",
        filename="BuToKstarPsi2s_KstarToK0Pi_Psi2sToEE_K0ToPiP_Gen_FONLL.root",
        final_state_defs={"e": 11, "pi": 211},
        multiplicity_reqs={"e": 2, "pi": 3},
        selection_cut="""
            e_pt[0] > 3.0 && e_pt[1] > 3.0 &&
            abs(e_eta[0]) < 1.5 && abs(e_eta[1]) < 1.5 &&
            pi_pt[2] > 0.5 && pi_eta[2] < 2.5
        """,
    )


def run_Bu_JpsiEE_Kstar_KPi0():
    run_efficiency(
        name="Bu → J/ψ(e⁺e⁻) K*+(→ K⁺ π⁰)",
        key="Bu_JpsiEE_Kstar_KPi0",
        filename="BuToKstarJPsi_JPsiToEE_KstarToKplusPi0_gen_FONLL.root",
        final_state_defs={
            "e": 11,
            "k": 321,
            "pi0": 111,
        },
        multiplicity_reqs={
            "e": 2,
            "k": 1,
            "pi0": 1,
        },
        selection_cut="""
            e_pt[0] > 3.0 && e_pt[1] > 3.0 &&
            abs(e_eta[0]) < 1.5 && abs(e_eta[1]) < 1.5 &&
            k_pt[0] > 0.5 && abs(k_eta[0]) < 2.5 &&
            pi0_pt[0] > 0.5 && abs(pi0_eta[0]) < 2.5
        """,
    )


# ============================================================
# RUN ALL
# ============================================================

run_B0_JpsiEE_Kstar()
#run_B0_Psi2SEE_Kstar()
#run_Bu_JpsiPi()
#run_Bu_Chic1_JpsiPiPi()
run_Bu_KstarJpsi_K0PiPi()
#run_Bu_KstarPsi2S()
#run_Bu_JpsiEE_Kstar_KPi0()