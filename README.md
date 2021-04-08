# g4SimHit_SpeedUp

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TH1F.h>
// #include <TH2F.h>
#include <TMath.h>
#include "Math/LorentzVector.h"
#include "TLorentzVector.h"
#include "TVector.h"
#include "TVector2.h"
#include "TVector3.h"
// // Header file for the classes stored in the TTree if any.
#include <vector>
#include <fstream>
#include <iostream>
// Header file for the classes stored in the TTree if any.
#include "TClonesArray.h"
#include "TObject.h"
#include "TVector3.h"
#include "TGraph.h"
#include "TGraphErrors.h"
#include "TStyle.h"
#include "TF1.h"
#include "TColor.h"
//to open the root file
void plot(){
        TFile* file0 = TFile::Open("/uscms_data/d3/hguerrer/YOURWORKINGAREA/CMSSW_11_0_0/src/Test1.root");
        TFile* file1 = TFile::Open("/uscms_data/d3/hguerrer/YOURWORKINGAREA/CMSSW_11_0_0/src/Test2.root");
//here you need to put the path on the root file
        TH1F *resx0 = (TH1F*)file0->Get("Events/PCaloHits_g4SimHits_EcalHitsEB_SIM/PCaloHits_g4SimHits_EcalHitsEB_SIM.obj/energyEM");
        TH1F *resx1 = (TH1F*)file1->Get("Events/PCaloHits_g4SimHits_EcalHitsEB_SIM/PCaloHits_g4SimHits_EcalHitsEB_SIM.obj/energyEM");
        resx0 -> SetLineColor(1);
        resx1 -> SetLineColor(2);
        TCanvas* canresx = new TCanvas("canresx");
        canresx->cd();
        resx0->SetTitle("Charge distribution for clusters of size 1");
        resx0->SetStats(kFALSE);
        resx0->SetAxisRange(0,3100,"Y");
        resx0->SetAxisRange(0.0,30000,"X");
        resx0->Draw("hist");
        resx41->Draw("same,hist");
        TLegend *legresx = new TLegend(.8, .7, 0.9, .898);
        legresx->SetBorderSize(0);
        legresx->SetLineColor(1);
        gStyle->SetFillColor(0);
        gStyle->SetCanvasColor(10);
        legresx->AddEntry(resx0, " 0 deg", "L");
        legresx->AddEntry(resx1, " 4 deg", "L");
        legresx->Draw();
        canresx->SaveAs("Charge Distribution for Clusters of size 1.pdf");
}
