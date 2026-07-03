import ROOT
from DataFormats.FWLite import Events, Handle
from tqdm import tqdm

ROOT.gROOT.SetBatch(True)

# ============================================================
# 1) DECAY TABLES
# ============================================================

DECAY_TABLES = {

    "Bu_JpsiEE_Kstar_KPi0": [

        # B+
        {
            "pdgId": 521,
            "children": [
                {
                    "pdgId": 443,
                    "children": [
                        {"pdgId": -11},
                        {"pdgId": 11},
                    ],
                },
                {
                    "pdgId": 323,
                    "children": [
                        {"pdgId": 321},
                        {"pdgId": 111},
                    ],
                },
            ],
        },

        # B-
        {
            "pdgId": -521,
            "children": [
                {
                    "pdgId": 443,
                    "children": [
                        {"pdgId": -11},
                        {"pdgId": 11},
                    ],
                },
                {
                    "pdgId": -323,
                    "children": [
                        {"pdgId": -321},
                        {"pdgId": 111},
                    ],
                },
            ],
        },
    ],
}

# ============================================================
# 2) JOB CONFIGURATION
# ============================================================

JOBS = [
    {
        "name": "Bu_JpsiEE_Kstar_KPi0",
        "filelist": "/eos/user/j/jodedra/AnalysisWork_2024/Analysistimeseff/full_unbiased_for_all_mc/CMSSW_12_4_11_patch3/src/filelist/files_BuToKstarJPsi_JPsiToEE_KstarToKplusPi0.txt",
        "decay": "Bu_JpsiEE_Kstar_KPi0",
        "output": "Bu_JpsiEE_Kstar_KPi0_gen.root",
    },
]

# ============================================================
# 3) DECAY MATCHING LOGIC
# ============================================================

def match_decay(genp, decay_node):
    if genp.pdgId() != decay_node["pdgId"]:
        return None

    matched = {"particle": genp, "children": []}

    if "children" not in decay_node:
        return matched

    daughters = [genp.daughter(i) for i in range(genp.numberOfDaughters())]

    for child_def in decay_node["children"]:
        found = False
        for d in daughters:
            res = match_decay(d, child_def)
            if res:
                matched["children"].append(res)
                daughters.remove(d)
                found = True
                break
        if not found:
            return None

    return matched


def find_first_decay(gen_particles, decay_defs):
    for decay_def in decay_defs:
        for p in gen_particles:
            res = match_decay(p, decay_def)
            if res:
                return res
    return None


def flatten_decay(match):
    parts = [match["particle"]]
    for c in match["children"]:
        parts.extend(flatten_decay(c))
    return parts

# ============================================================
# 4) CORE PROCESSING FUNCTION
# ============================================================

def process_sample(name, filelist_path, decay_defs, output_root):

    print(f"\n=== Processing {name} ===")

    # ---- Read input files
    files = []
    with open(filelist_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                files.append(line)

    events = Events(files)

    handle_gen = Handle("std::vector<reco::GenParticle>")
    label_gen = ("genParticles")

    # ---- Output ROOT file
    fout = ROOT.TFile(output_root, "RECREATE")
    tree = ROOT.TTree("DecayTree", name)

    # ---- Branches
    B_pt     = ROOT.std.vector("float")()
    B_eta    = ROOT.std.vector("float")()
    B_phi    = ROOT.std.vector("float")()
    B_mass   = ROOT.std.vector("float")()
    B_charge = ROOT.std.vector("int")()

    pdgId  = ROOT.std.vector("int")()
    pt     = ROOT.std.vector("float")()
    eta    = ROOT.std.vector("float")()
    phi    = ROOT.std.vector("float")()
    mass   = ROOT.std.vector("float")()
    charge = ROOT.std.vector("int")()

    for name_, vec in [
        ("B_pt", B_pt),
        ("B_eta", B_eta),
        ("B_phi", B_phi),
        ("B_mass", B_mass),
        ("B_charge", B_charge),
        ("pdgId", pdgId),
        ("pt", pt),
        ("eta", eta),
        ("phi", phi),
        ("mass", mass),
        ("charge", charge),
    ]:
        tree.Branch(name_, vec)

    # ---- Event loop
    for event in tqdm(events, total=events.size(), desc=name):
        event.getByLabel(label_gen, handle_gen)
        gens = handle_gen.product()

        decay = find_first_decay(gens, decay_defs)
        if not decay:
            continue

        for v in [B_pt, B_eta, B_phi, B_mass, B_charge,
                  pdgId, pt, eta, phi, mass, charge]:
            v.clear()

        B = decay["particle"]
        B_pt.push_back(B.pt())
        B_eta.push_back(B.eta())
        B_phi.push_back(B.phi())
        B_mass.push_back(B.mass())
        B_charge.push_back(B.charge())

        parts = flatten_decay(decay)[1:]
        for p in parts:
            pdgId.push_back(p.pdgId())
            pt.push_back(p.pt())
            eta.push_back(p.eta())
            phi.push_back(p.phi())
            mass.push_back(p.mass())
            charge.push_back(p.charge())

        tree.Fill()

    fout.Write()
    fout.Close()

    print(f"Saved → {output_root}")

# ============================================================
# 5) RUN ALL JOBS
# ============================================================

for job in JOBS:
    process_sample(
        name=job["name"],
        filelist_path=job["filelist"],
        decay_defs=DECAY_TABLES[job["decay"]],
        output_root=job["output"],
    )
