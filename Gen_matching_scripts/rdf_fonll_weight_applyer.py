import os
import glob
import ROOT
# ============================================================
# 1) INPUT / OUTPUT
# ============================================================

input_dir  = "/eos/user/j/jodedra/AnalysisWork_2024/Analysistimeseff/full_unbiased_for_all_mc/CMSSW_12_4_11_patch3/src/Gen_matching_scripts/"
tree_name  = "DecayTree"

output_dir = "weighted_root_files"
os.makedirs(output_dir, exist_ok=True)
input_files = sorted(glob.glob(os.path.join(input_dir, "*.root")))

# ============================================================
# 2) DECLARE FONLL WEIGHT FUNCTIONS
#    (PASTE YOUR FULL CODE HERE — UNCHANGED)
# ============================================================

gInit = ROOT.gInterpreter.Declare("""
#include <ROOT/RVec.hxx>
using namespace ROOT::VecOps;
float FONLLweightRun3(float ptB){
  if (ptB<1) return 1.15515;
  else if(ptB<2) return 1.18534;
  else if(ptB<3) return 1.16911;
  else if(ptB<4) return 1.14175;
  else if(ptB<5) return 1.11175;
  else if(ptB<6) return 1.01419;
  else if(ptB<7) return 0.907751;
  else if(ptB<8) return 0.817504;
  else if(ptB<9) return 0.78137;
  else if(ptB<10) return 0.738612;
  else if(ptB<11) return 0.732303;
  else if(ptB<12) return 0.73074;
  else if(ptB<13) return 0.740836;
  else if(ptB<14) return 0.750178;
  else if(ptB<15) return 0.758338;
  else if(ptB<16) return 0.763555;
  else if(ptB<17) return 0.816048;
  else if(ptB<18) return 0.80948;
  else if(ptB<19) return 0.820215;
  else if(ptB<20) return 0.83501;
  else if(ptB<21) return 0.853838;
  else if(ptB<22) return 0.865113;
  else if(ptB<23) return 0.87358;
  else if(ptB<24) return 0.893233;
  else if(ptB<25) return 0.909597;
  else if(ptB<26) return 0.919336;
  else if(ptB<27) return 0.926104;
  else if(ptB<28) return 0.940649;
  else if(ptB<29) return 0.963733;
  else if(ptB<30) return 0.97171;
  else if(ptB<31) return 0.967569;
  else if(ptB<32) return 0.948828;
  else if(ptB<33) return 1.05547;
  else if(ptB<34) return 1.00769;
  else if(ptB<35) return 0.988522;
  else if(ptB<36) return 0.995099;
  else if(ptB<37) return 1.04206;
  else if(ptB<38) return 1.02003;
  else if(ptB<39) return 1.0461;
  else if(ptB<40) return 1.04391;
  else if(ptB<41) return 1.02988;
  else if(ptB<42) return 1.09458;
  else if(ptB<43) return 1.02195;
  else if(ptB<44) return 1.00227;
  else if(ptB<45) return 1.042;
  else if(ptB<46) return 1.00599;
  else if(ptB<47) return 1.08266;
  else if(ptB<48) return 1.0664;
  else if(ptB<49) return 0.999711;
  else if(ptB<50) return 1.10879;
  else if(ptB<51) return 1.09674;
  else if(ptB<52) return 1.09955;
  else if(ptB<53) return 1.09597;
  else if(ptB<54) return 1.13401;
  else if(ptB<55) return 1.04907;
  else if(ptB<56) return 1.11719;
  else if(ptB<57) return 1.02235;
  else if(ptB<58) return 1.11178;
  else if(ptB<59) return 1.04314;
  else if(ptB<60) return 0.940032;
  else if(ptB<61) return 1.1208;
  else if(ptB<62) return 1.09524;
  else if(ptB<63) return 1.09587;
  else if(ptB<64) return 1.06172;
  else if(ptB<65) return 1.32325;
  else if(ptB<66) return 1.23206;
  else if(ptB<67) return 0.975764;
  else if(ptB<68) return 1.09389;
  else if(ptB<69) return 1.22962;
  else if(ptB<70) return 1.23585;
  else if(ptB<71) return 1.10778;
  else if(ptB<72) return 0.978404;
  else if(ptB<73) return 0.976452;
  else if(ptB<74) return 0.926465;
  else if(ptB<75) return 1.36474;
  else if(ptB<76) return 1.0219;
  else if(ptB<77) return 1.06599;
  else if(ptB<78) return 1.1451;
  else if(ptB<79) return 0.944286;
  else if(ptB<80) return 1.01788;
  else if(ptB<81) return 1.08498;
  else if(ptB<82) return 0.893767;
  else if(ptB<83) return 1.08491;
  else if(ptB<84) return 0.824411;
  else if(ptB<85) return 1.10867;
  else if(ptB<86) return 1.11823;
  else if(ptB<87) return 1.26815;
  else if(ptB<88) return 1.04035;
  else if(ptB<89) return 1.12364;
  else if(ptB<90) return 0.999843;
  else if(ptB<91) return 1.09449;
  else if(ptB<92) return 0.800113;
  else if(ptB<93) return 0.839017;
  else if(ptB<94) return 1.24008;
  else if(ptB<95) return 1.07787;
  else if(ptB<96) return 1.1578;
  else if(ptB<97) return 0.926529;
  else if(ptB<98) return 1.34082;
  else if(ptB<99) return 1.54135;
  else if(ptB<110) return 0.973232;
  else return 1;
}


float FONLLweightRun3_Up(float ptB){
  if (ptB<1) return	0.538034;
  else if(ptB<2) return	0.583865;
  else if(ptB<3) return	0.615693;
  else if(ptB<4) return	0.640369;
  else if(ptB<5) return	0.659844;
  else if(ptB<6) return	0.63329;
  else if(ptB<7) return	0.592136;
  else if(ptB<8) return	0.552837;
  else if(ptB<9) return	0.551522;
  else if(ptB<10) return 0.534102;
  else if(ptB<11) return 0.542191;
  else if(ptB<12) return 0.549186;
  else if(ptB<13) return 0.561285;
  else if(ptB<14) return 0.572809;
  else if(ptB<15) return 0.583388;
  else if(ptB<16) return 0.591578;
  else if(ptB<17) return 0.636491;
  else if(ptB<18) return 0.635424;
  else if(ptB<19) return 0.647729;
  else if(ptB<20) return 0.663214;
  else if(ptB<21) return 0.681837;
  else if(ptB<22) return 0.694459;
  else if(ptB<23) return 0.704716;
  else if(ptB<24) return 0.723846;
  else if(ptB<25) return 0.740308;
  else if(ptB<26) return 0.75133;
  else if(ptB<27) return 0.759839;
  else if(ptB<28) return 0.774648;
  else if(ptB<29) return 0.796468;
  else if(ptB<30) return 0.805716;
  else if(ptB<31) return 0.804868;
  else if(ptB<32) return 0.791613;
  else if(ptB<33) return 0.882969;
  else if(ptB<34) return 0.845299;
  else if(ptB<35) return 0.831279;
  else if(ptB<36) return 0.838875;
  else if(ptB<37) return 0.88038;
  else if(ptB<38) return 0.863614;
  else if(ptB<39) return 0.887429;
  else if(ptB<40) return 0.887236;
  else if(ptB<41) return 0.876873;
  else if(ptB<42) return 0.933361;
  else if(ptB<43) return 0.872915;
  else if(ptB<44) return 0.857389;
  else if(ptB<45) return 0.892452;
  else if(ptB<46) return 0.862755;
  else if(ptB<47) return 0.929317;
  else if(ptB<48) return 0.916311;
  else if(ptB<49) return 0.860041;
  else if(ptB<50) return 0.954062;
  else if(ptB<51) return 0.94443;
  else if(ptB<52) return 0.947303;
  else if(ptB<53) return 0.944689;
  else if(ptB<54) return 0.977496;
  else if(ptB<55) return 0.90517;
  else if(ptB<56) return 0.963472;
  else if(ptB<57) return 0.882623;
  else if(ptB<58) return 0.958668;
  else if(ptB<59) return 0.900069;
  else if(ptB<60) return 0.812043;
  else if(ptB<61) return 0.965189;
  else if(ptB<62) return 0.942925;
  else if(ptB<63) return 0.942721;
  else if(ptB<64) return 0.913128;
  else if(ptB<65) return 1.1308;
  else if(ptB<66) return 1.05339;
  else if(ptB<67) return 0.838155;
  else if(ptB<68) return 0.935597;
  else if(ptB<69) return 1.04612;
  else if(ptB<70) return 1.04915;
  else if(ptB<71) return 0.94217;
  else if(ptB<72) return 0.834057;
  else if(ptB<73) return 0.830866;
  else if(ptB<74) return 0.788221;
  else if(ptB<75) return 1.13863;
  else if(ptB<76) return 0.862078;
  else if(ptB<77) return 0.895112;
  else if(ptB<78) return 0.955165;
  else if(ptB<79) return 0.793115;
  else if(ptB<80) return 0.848999;
  else if(ptB<81) return 0.89861;
  else if(ptB<82) return 0.746077;
  else if(ptB<83) return 0.891876;
  else if(ptB<84) return 0.686867;
  else if(ptB<85) return 0.902467;
  else if(ptB<86) return 0.905568;
  else if(ptB<87) return 1.01106;
  else if(ptB<88) return 0.839588;
  else if(ptB<89) return 0.896304;
  else if(ptB<90) return 0.801849;
  else if(ptB<91) return 0.865943;
  else if(ptB<92) return 0.647708;
  else if(ptB<93) return 0.673347;
  else if(ptB<94) return 0.950225;
  else if(ptB<95) return 0.834233;
  else if(ptB<96) return 0.882643;
  else if(ptB<97) return 0.72054;
  else if(ptB<98) return 0.986762;
  else if(ptB<99) return 1.09923;
  else if(ptB<100) return 0.738026;
  else return 1;	
}	


float FONLLweightRun3_Down(float ptB){
  if (ptB<1) return 1.83234;
  else if(ptB<2) return	1.81862;
  else if(ptB<3) return	1.74421;
  else if(ptB<4) return	1.68144;
  else if(ptB<5) return	1.62834;
  else if(ptB<6) return	1.47856;
  else if(ptB<7) return	1.31521;
  else if(ptB<8) return	1.17523;
  else if(ptB<9) return	1.11322;
  else if(ptB<10) return 1.04231;
  else if(ptB<11) return 1.02327;
  else if(ptB<12) return 1.01092;
  else if(ptB<13) return 1.01485;
  else if(ptB<14) return 1.01785;
  else if(ptB<15) return 1.01952;
  else if(ptB<16) return 1.01755;
  else if(ptB<17) return 1.07828;
  else if(ptB<18) return 1.06088;
  else if(ptB<19) return 1.06657;
  else if(ptB<20) return 1.07787;
  else if(ptB<21) return 1.0944;
  else if(ptB<22) return 1.10156;
  else if(ptB<23) return 1.10535;
  else if(ptB<24) return 1.12345;
  else if(ptB<25) return 1.13753;
  else if(ptB<26) return 1.14353;
  else if(ptB<27) return 1.14609;
  else if(ptB<28) return 1.15846;
  else if(ptB<29) return 1.18142;
  else if(ptB<30) return 1.18593;
  else if(ptB<31) return 1.17597;
  else if(ptB<32) return 1.14856;
  else if(ptB<33) return 1.27285;
  else if(ptB<34) return 1.21088;
  else if(ptB<35) return 1.18375;
  else if(ptB<36) return 1.18786;
  else if(ptB<37) return 1.2401;
  else if(ptB<38) return 1.21026;
  else if(ptB<39) return 1.23781;
  else if(ptB<40) return 1.23201;
  else if(ptB<41) return 1.21248;
  else if(ptB<42) return 1.2858;
  else if(ptB<43) return 1.19772;
  else if(ptB<44) return 1.17213;
  else if(ptB<45) return 1.21628;
  else if(ptB<46) return 1.17191;
  else if(ptB<47) return 1.25926;
  else if(ptB<48) return 1.23828;
  else if(ptB<49) return 1.1588;
  else if(ptB<50) return 1.28394;
  else if(ptB<51) return 1.26844;
  else if(ptB<52) return 1.27017;
  else if(ptB<53) return 1.26475;
  else if(ptB<54) return 1.30766;
  else if(ptB<55) return 1.20811;
  else if(ptB<56) return 1.28616;
  else if(ptB<57) return 1.17544;
  else if(ptB<58) return 1.27842;
  else if(ptB<59) return 1.1983;
  else if(ptB<60) return 1.0784;
  else if(ptB<61) return 1.288;
  else if(ptB<62) return 1.25825;
  else if(ptB<63) return 1.25911;
  else if(ptB<64) return 1.21956;
  else if(ptB<65) return 1.52622;
  else if(ptB<66) return 1.42001;
  else if(ptB<67) return 1.12053;
  else if(ptB<68) return 1.25962;
  else if(ptB<69) return 1.42077;
  else if(ptB<70) return 1.42973;
  else if(ptB<71) return 1.27954;
  else if(ptB<72) return 1.12792;
  else if(ptB<73) return 1.12687;
  else if(ptB<74) return 1.06902;
  else if(ptB<75) return 1.5963;
  else if(ptB<76) return 1.18579;
  else if(ptB<77) return 1.24077;
  else if(ptB<78) return 1.33889;
  else if(ptB<79) return 1.09856;
  else if(ptB<80) return 1.18972;
  else if(ptB<81) return 1.27425;
  else if(ptB<82) return 1.0438;
  else if(ptB<83) return 1.28047;
  else if(ptB<84) return 0.963848;
  else if(ptB<85) return 1.31702;
  else if(ptB<86) return 1.33288;
  else if(ptB<87) return 1.52721;
  else if(ptB<88) return 1.24271;
  else if(ptB<89) return 1.35246;
  else if(ptB<90) return 1.19906;
  else if(ptB<91) return 1.32426;
  else if(ptB<92) return 0.95335;
  else if(ptB<93) return 1.0054;
  else if(ptB<94) return 1.53069;
  else if(ptB<95) return 1.32206;
  else if(ptB<96) return 1.43344;
  else if(ptB<97) return 1.13283;
  else if(ptB<98) return 1.69517;
  else if(ptB<99) return 1.98366;
  else if(ptB<100) return 1.20852;
  else return 1;	
}


RVec<float> FONLLweightRun3_vec(const RVec<float>& ptB){
  RVec<float> out(ptB.size());
  for(size_t i=0; i<ptB.size(); i++) out[i] = FONLLweightRun3(ptB[i]);
  return out;
}

RVec<float> FONLLweightRun3_Up_vec(const RVec<float>& ptB){
  RVec<float> out(ptB.size());
  for(size_t i=0; i<ptB.size(); i++) out[i] = FONLLweightRun3_Up(ptB[i]);
  return out;
}

RVec<float> FONLLweightRun3_Down_vec(const RVec<float>& ptB){
  RVec<float> out(ptB.size());
  for(size_t i=0; i<ptB.size(); i++) out[i] = FONLLweightRun3_Down(ptB[i]);
  return out;
}

""")

print(f"[INFO] Found {len(input_files)} ROOT files")

for infile in input_files:

    print(f"[INFO] Processing: {infile}")

    # Output filename (preserve basename)
    base = os.path.basename(infile)
    outfile = os.path.join(output_dir, base.replace(".root", "_FONLL.root"))

    # Build dataframe
    df = ROOT.RDataFrame(tree_name, infile)

    # ---- Add weights (these Define lines assume
    #      your FONLL functions are already declared)
    df_w = (
        df
        .Define("FONLL_weight",      "FONLLweightRun3_vec(B_pt)[0]")
        .Define("FONLL_weight_Up",   "FONLLweightRun3_Up_vec(B_pt)[0]")
        .Define("FONLL_weight_Down", "FONLLweightRun3_Down_vec(B_pt)[0]")
    )

    # ---- Write output file
    df_w.Snapshot(tree_name, outfile)

    print(f"[OK] Written: {outfile}")

print("[DONE] All files processed")
