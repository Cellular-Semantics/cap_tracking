# HCA annotation & CL mapping — findings and proposed actions

Non-immune labels across the 61 CAP datasets tagged *Human Cell Atlas*.
Provenance, retrieval and the comparison of sources live in
`analysis/cap_data_sources.md`; source tags here are shorthand, with a legend at
the end. Both documents supersede `analysis/hca_first_pass_ontology_review.md`
(removed).

**Status: first pass.** Every marker claim below is a reading of CAP's curated
`markerGenes` field against latent knowledge. **No differential expression was
run, no `pct_detected` was checked, and no literature was consulted.** CL
searches were lexical. Per the repo's evidence rules these are leads, not
recommendations — see Caveats.

---

## Summary of proposed actions

| Class | Count | Where |
|---|---|---|
| Mis-mapping (wrong branch) | 5 labels | §2 |
| Under-specific, exact CL term exists | 21 labels | §3 |
| Internal inconsistency (same label, two mappings) | 1 | §3 |
| Annotation defect (label/markers, not the mapping) | 8 | §4 |
| New-term proposals — already requested by CAP curators | 9 | §5 |
| New-term proposals — found here | 6 clusters | §5 |
| Already filed as site feedback, awaiting application | 6 | §6 |

---

## 1. Cross-atlas index: one term, several atlases

Grouped by the *current* CL mapping, because the same over-general term is being
reused across unrelated atlases and a fix in one place is usually a fix in
several. `Feedback` marks whether a correction is already filed `[FB]`.

### `CL:0000057` fibroblast — 5 projects, 38 distinct labels

| Atlas | Labels | Proposed action | Feedback |
|---|---|---|---|
| [Trabecular meshwork](https://celltype.info/project/574) | BeamA, BeamB, JCT | → `CL:7770003` / `CL:7770006` / `CL:7770002` | ✔ filed |
| [Trabecular meshwork](https://celltype.info/project/574) | CB_Fibro (n=142,183) | new term: ciliary-body fibroblast | — |
| [Optic nerve](https://celltype.info/project/621) | Fibro_dura, _pia, _arachnoid, _lamina_cribrosa | new terms (meningeal layers) | — |
| [Optic nerve](https://celltype.info/project/621) | Fibro_sclera | → `CL:0000347` scleral cell | — |
| [Ocular surface](https://celltype.info/project/565) | Limbus/Sclera Fibroblasts C1/C2 | disambiguate limbus vs sclera first | — |
| [Ocular surface](https://celltype.info/project/565) | Uveal/TM Fibroblasts | **mis-mapping** → melanocyte (§2) | — |
| [RPE & choroid](https://celltype.info/project/1058) | 15 `Fibroblasts_<gene>+` labels | marker-suffixed subclusters; no CL action | — |
| [Kidney](https://celltype.info/project/1006) | Norn_cells | new term: Norn cell | — |
| [Gut](https://celltype.info/project/1030) | Submucosal (S3), Muscularis Propria | new terms (curator-requested, §5) | — |

### `CL:0000115` endothelial cell → Schlemm's canal — 2 projects, same label name

| Atlas | Dataset | Label | Action | Feedback |
|---|---|---|---|---|
| [Trabecular meshwork](https://celltype.info/project/574) | [1241](https://celltype.info/project/574/dataset/1241), [1242](https://celltype.info/project/574/dataset/1242) | `Schlemm_Endothelium` | → `CL:4033097` | ✔ filed on 1242 only |
| [Ocular surface](https://celltype.info/project/565) | [1208](https://celltype.info/project/565/dataset/1208), [1209](https://celltype.info/project/565/dataset/1209) | `Schlemm Endothelium` | → `CL:4033097` | — |

`CL:4033098` / `CL:4033099` (inner / outer wall) are available if the clusters
separate. The filed feedback also adds **PROX1** to the marker list.

### `CL:0000148` melanocyte → `CL:4030000` choroidal melanocyte — 3 projects

| Atlas | Labels | Feedback |
|---|---|---|
| [Trabecular meshwork](https://celltype.info/project/574) | Uveal_Melanocyte | ✔ filed on 1242 only |
| [Optic nerve](https://celltype.info/project/621) | Melanocyte, Melanocytes | — |
| [Ocular surface](https://celltype.info/project/565) | Uveal_Melanocytes, Conj_Melanocytes | — |

### `CL:0004215` type 5a cone bipolar cell → `CL:4033085` diffuse bipolar 5 cell — 2 projects

`DB5` is mapped to the **mouse** BC5A type in four datasets across two projects,
while the primate term `CL:4033085` exists. The label's own rationale says
"Mapped to mouse BC5C" — i.e. a mouse type it explicitly says it is *not*.

| Atlas | Datasets | Source |
|---|---|---|
| [Retina](https://celltype.info/project/544) | [1154](https://celltype.info/project/544/dataset/1154), [1156](https://celltype.info/project/544/dataset/1156) | `[OLS]` |
| [Retina](https://celltype.info/project/544) | [1157](https://celltype.info/project/544/dataset/1157) | `[CAS]` |
| [Optic nerve](https://celltype.info/project/621) | [1489](https://celltype.info/project/621/dataset/1489) | `[CAS]` |

### `CL:0000066` epithelial cell / `CL:0011026` progenitor cell — 2 projects

| Atlas | Labels | Action |
|---|---|---|
| [Ocular surface](https://celltype.info/project/565) | Epi-TDC, Epi-PMC, Epi-TDC/PMC, Limbus_Epi, Limbus_Epi-C1/C2, Unknown Epithelium | corneal / limbal epithelium terms (§3) |
| [Ocular surface](https://celltype.info/project/565) | LPC, Fetal_Epi/LSC/LPC | → `CL:4033093` limbal epithelial stem cell of cornea |
| [HEOCA lung organoid](https://celltype.info/project/604) | club cells (level_1), progenitors | see §3 |

The ocular-surface epithelial labels also carry `categoryOntologyTermId`
`CL:0000255` **eukaryotic cell**, which is not a usable category.

---

## 2. Mis-mappings — wrong branch, not a granularity gap

The serious class: the mapping points at the wrong lineage, so a more specific
term would not fix it.

### [Human liver cell atlas](https://celltype.info/project/1045) — 3 labels

Read from `[OBS]` on [dataset 3440](https://celltype.info/project/1045/dataset/3440),
confirmed against `[CAS]`. Seeing the whole labelset at once is what makes these
unambiguous:

| Label | n | Currently | Markers | Proposed | Verdict |
|---|---|---|---|---|---|
| LSEC | — | `CL:1000398` endothelial cell of hepatic sinusoid | CLEC4G, CLEC4M, CD14 | — | correct |
| Periportal LSEC | — | `CL:0019021` ...**periportal** hepatic sinusoid | CD36 | — | correct |
| **Central Venous LSEC** | 22,202 | `CL:1000413` **endothelial cell of artery** | CD14, **LYVE1**, FCGR2B, **STAB1** | **`CL:0019022`** endothelial cell of pericentral hepatic sinusoid `[CL]` | **wrong branch** |
| **Hepatic Artery** | — | `CL:0002544` **aortic endothelial cell** | SYT1, FBLN5, SEMA3G | `CL:1000413` endothelial cell of artery | **wrong branch** |
| Portal Vein | — | `CL:0009094` endothelial cell of hepatic portal vein | CPE, CDH11, CD320 | — | correct |
| **Cycling** | 202–5,342 | `CL:4033069` **cycling T cell** | TOP2A, MKI67 | not a T cell; a cell-cycle *state* | **wrong branch** |

The annotators plainly knew the LSEC branch — they used `CL:1000398` for the
parent and `CL:0019021` for the periportal sibling. `CL:0019022` is the matching
pericentral term, defined as "*An endothelial cell found in the centrilobular
region hepatic sinusoid, near the central vein*". Every curated marker agrees:
LYVE1/STAB1 are the canonical pericentral LSEC pair. The label's
`categoryOntologyTermId` is already `CL:0000071` blood vessel endothelial cell,
so the category is right and only the specific term is wrong — a one-term fix.

**`Cycling` repeats across four liver datasets** —
[3440](https://celltype.info/project/1045/dataset/3440) endothelia,
[3441](https://celltype.info/project/1045/dataset/3441) **hepatocyte**,
[3442](https://celltype.info/project/1045/dataset/3442) all cells,
[3443](https://celltype.info/project/1045/dataset/3443) lymphocyte — all on
`cycling T cell` with TOP2A/MKI67 alone. A proliferating hepatocyte cluster on a
T cell term.

### Elsewhere

| Atlas | Label | n | Currently | Problem |
|---|---|---|---|---|
| [Ocular surface](https://celltype.info/project/565) | Uveal/TM Fibroblasts | 859 | `CL:0000057` fibroblast | markers **TRPM1, PMEL, TYR, PAX3, ABCB5** are melanocyte. → `CL:4030000` choroidal melanocyte, or the label is a doublet |
| [RPE & choroid](https://celltype.info/project/1058) | Fibroblasts_Fetal_GRHL2 | 10 | `CL:0000057` fibroblast | markers **GRHL2, MIR205HG** are epithelial. Its own rationale concedes it: "*defined as fibroblasts given this sub-class clustered together with other fibroblast sub-class*" |

---

## 3. Under-specific mappings where an exact CL term exists

All target terms confirmed present and non-obsolete `[CL]`, 2026-10-02.

### [Trabecular meshwork & ciliary body](https://celltype.info/project/574) `[CAS]`

The strongest case in the review: CL carries terms that read as if minted from
this atlas.

| Label | n | Currently | Proposed | Evidence | Feedback |
|---|---|---|---|---|---|
| **BeamA** | 31,160 | `CL:0000057` | `CL:7770003` beam A cell | CL's definition: "*molecularly distinguished by **FABP4** expression in humans*"; the label's markers are BMP5, **FABP4**, EDN3 | ✔ filed |
| **BeamB** | 11,113 | `CL:0000057` | `CL:7770006` beam B cell, human | — | ✔ filed |
| **JCT** | 23,671 | `CL:0000057` | `CL:7770002` juxtacanalicular tissue cell | the label is the term's acronym | ✔ filed |
| **Schlemm_Endothelium** | 635 | `CL:0000115` | `CL:4033097` Schlemm's canal endothelial cell | — | ✔ filed |
| **Uveal_Melanocyte** | 21,599 | `CL:0000148` | `CL:4030000` choroidal melanocyte | — | ✔ filed |

**All five are filed on [dataset 1242](https://celltype.info/project/574/dataset/1242) (scRNA) only, not on [1241](https://celltype.info/project/574/dataset/1241) (snRNA).** The fix needs applying to both arms.

### [Human retina](https://celltype.info/project/544) `[OLS]` — ON/OFF subtypes collapsed to their parent

| Label | n | Currently | Proposed | Feedback |
|---|---|---|---|---|
| MG_OFF | 200,402 | `CL:4023188` midget ganglion cell of retina | `CL:4033047` **OFF midget ganglion cell** | ✔ filed (refine + disagree) |
| **MG_ON** | 151,685 | `CL:4023188` | `CL:4033046` **ON midget ganglion cell** | — |
| **PG_ON** | 6,184 | `CL:4023189` parasol ganglion cell of retina | `CL:4033052` **ON parasol ganglion cell** | — |
| **PG_OFF** | 10,104 | `CL:4023189` | `CL:4033051` **OFF parasol ganglion cell** | — |
| **ipRGC** | 1,292 | `CL:0000740` retinal ganglion cell | `CL:0020014` **intrinsically photosensitive retinal ganglion cell** | — |

`ipRGC` is the worst: mapped three levels up to the class parent, while CL's term
is defined by melanopsin — and the label's own `canonicalMarkerGenes` is `OPN4`,
the melanopsin gene.

`ON-SAC` / `OFF-SAC` are both on `CL:0004232` starburst amacrine cell; CL has no
ON/OFF split there, so that is a **new-term pair**, not an error (§5).

`DB5` → `CL:4033085`: see §1. `DB4a` / `DB4b` both on `CL:4033031`: genuine gap,
new terms (§5).

### [Human ocular surface](https://celltype.info/project/565) `[CAS]`

| Label | n | Currently | Proposed |
|---|---|---|---|
| Epi-TDC | 72,541 | `CL:0000066` | `CL:0000575` corneal epithelial cell (KRT12, rising KRT3) |
| Epi-PMC, Epi-TDC/PMC | 64,378 / 17,770 | `CL:0000066` | corneal epithelium; differentiation-stage terms needed |
| Limbus_Epi, Limbus_Epi-C1/C2 | 1,719–37,332 | `CL:0000066` | limbal epithelium; `CL:4033093` for the KRT15-high one |
| LPC | 28,208 | `CL:0011026` progenitor cell | `CL:4033093` limbal epithelial stem cell of cornea |
| Limbus/Sclera Fibroblasts | 1,179–108,407 | `CL:0000057` | `CL:0000347` scleral cell / keratocyte — but "Limbus/Sclera" pools two compartments; disambiguate first |

**Two labels are flagged as doubtful by the annotators themselves** —
`Unknown Epithelium` ("*not sure whether we should keep this cluster*") and
`Fetal_Epi/LSC/LPC` (same wording). Resolve before mapping.

### [Human optic nerve](https://celltype.info/project/621) `[CAS]`

Eight `Fibro_*` labels, all on `CL:0000057`, all anatomically named:

| Label | n | Markers | CL status |
|---|---|---|---|
| Fibro_arachnoid | 32,368 | CEMIP, PKP2, BICC1 | nearest `CL:4023058` mesothelial fibroblast of the leptomeninx, `CL:4023097` arachnoid barrier cell |
| Fibro_dura | 26,885 | SLC47A1, THSD4, BICC1 | no dura **fibroblast** term (`CL:1000298` is *mesothelial*) → **new** |
| Fibro_pia | 25,789 | ABCA9, BICC1 | `CL:4023058` candidate |
| Fibro_sclera | 15,056 | NOX4, BICC1 | `CL:0000347` scleral cell |
| Fibro_lamina_cribrosa | 3,674 | SHOX, SMOC2, BICC1 | nothing in CL → **new**, glaucoma-relevant |
| Fibro_RPEchoroid | 9,425 | BMP5, BICC1 | — |
| Fibro_perivascular | 3,598 | MGP, APOD, BICC1 | check `CL:4052030` adventitial fibroblast |
| Fibro_x | 2,130 | EBF2, SLC22A3, DCN | unnamed by the annotators |

### [HEOCA lung organoid](https://celltype.info/project/604) `[CAS]` — an internal inconsistency

| Labelset | Label | n | Mapped to | Verdict |
|---|---|---|---|---|
| `level_2` | club cells | 33,832 | `CL:0000158` **club cell** | **correct** |
| `level_1` | club cells | 1,257 | `CL:0000066` epithelial cell | **wrong — same name, same dataset** |

The dataset maps the same label name correctly in one labelset and to a generic
parent in the other. Also `progenitors` (n=44,881) on `CL:0011026` with
`markerGenes: unknown` and `rationale: N/A` — unmappable as it stands.

### [Human kidney cell atlas](https://celltype.info/project/1006) `[OLS]`

Here CAP's own `ontologyAssessment` proposes a term, and is wrong twice:

| Label | n | Currently | CAP proposes | Verdict |
|---|---|---|---|---|
| **VSMC_REN / VSMC_REN+** | 184 | `CL:0000359` vascular associated smooth muscle cell | `CL:1001066` kidney arteriole SMC | **both wrong.** CAP's own `synonyms` field says *granular cell*; `CL:0000648` **kidney granular cell** has synonyms "JG cell, juxtaglomerular cell, **renin secreting cell**" and is defined as "*A smooth muscle cell that synthesizes, stores, and secretes the enzyme renin*" |
| **Norn_cells** | 77 / 226 | `CL:0000057` fibroblast | `CL:4052030` | **wrong.** `CL:4052030` is *adventitial fibroblast* — a vascular-adventitia cell, not the EPO-producing peritubular interstitial cell. CL has **no Norn cell term** → new term (§5) |
| POD_ECMmodulating | 446 / 366 | `CL:0000653` podocyte | `CL:0002525` metanephric podocyte | **correct** as a mapping — but see §4 |

---

## 4. Annotation defects — the label, not the mapping

A better CL term fixes none of these.

| Atlas | Label | n | Defect |
|---|---|---|---|
| [Kidney](https://celltype.info/project/1006) | POD_ECMmodulating | 446 / 366 | discriminating markers given as **AIF1**, SPOCK2. AIF1 is myeloid/microglial — reads as macrophage doublet contamination. "ECM modulating" is a *state*, asserted with no ECM gene in the panel |
| [HLCA core](https://celltype.info/project/684) | Neuroendocrine | 159 | markers `FOXI1, CALCA, TMEM61, ASCL5, CHGA`. CALCA/CHGA/ASCL5 are PNEC; **FOXI1 is the defining ionocyte TF** (`CL:0017000`). Cluster likely pools PNECs and ionocytes |
| [HLCA core](https://celltype.info/project/684) | Smooth muscle FAM83D+ | 335 | proposes "*FAM83D-positive smooth muscle cell*". FAM83D is a mitotic-spindle gene — a proliferation **state**, not a type. Also no airway/vascular distinction |
| [Retina](https://celltype.info/project/544) | ML_Cone | 118,559 | asserts **M and L** pooled; mapped to `CL:0003048` **L cone** alone while `CL:0003049` M cone exists. Split, or map to parent `CL:0000573`. Rationale also misstates: "*The marker for **S Cone** are OPN1LW and OPN1MW*" — those are the L and M opsins |
| [Retina](https://celltype.info/project/544) | HAC72 | 483 | markers `TF, RLBP1, RGR, COLEC12, CDH23` are **Müller glia**, not amacrine. Folded into the amacrine new-term proposal; should be excluded until resolved |
| [RPE & choroid](https://celltype.info/project/1058) | Fibroblasts IL6+ | 6,038 | label says IL6; `markerGenes` says **IL16**. Unrelated genes |
| [Ocular surface](https://celltype.info/project/565) | Fetal Endothelium and Endothelial Progenitors | 7,313 | names two populations; markers (TPM1, TPM2, MYL9, TAGLN, SORBS1) are mural/myofibroblast, not endothelial. Rationale admits "*unsure majorclass*" |
| [RPE & choroid](https://celltype.info/project/1058) | 11 fibroblast labels | — | all share the rationale "*This Fibroblasts PI16+ sub-class is annotated by markers PDGFRA, X*" where X varies. Only one is the PI16 subclass, so **ten rationales name the wrong cluster** |

### Systematic rationale quality `[CAS]`

Across 401 deduplicated recovered labels: 43 say "*Annotated based on the listed
marker genes*" (circular), 13 say "*N/A*", and the 11 above are one copy-pasted
template.

---

## 5. New-term proposals

### 5a. Already requested by CAP's curators via `ontologyAssessment`

`ontologyAssessment` is populated on 261 of 7,872 report rows (3.3%) — the only
field where a curator writes *to* the ontology. Every non-immune claim that "no
CL term exists" was checked `[CL]`:

| Atlas | Label | Claim | Verdict |
|---|---|---|---|
| [Gut](https://celltype.info/project/1030) | Colonocyte Progenitors | no such term | **correct** — CL has only `CL:1000347`, `CL:4047018` early, `CL:4047052` BEST4+ |
| [Gut](https://celltype.info/project/1030) | Crypt Top Colonocytes | no late/crypt-top term | **correct** |
| [Gut](https://celltype.info/project/1030) | Mid Crypt Colonocytes | intermediate exists in data | **correct** |
| [Gut](https://celltype.info/project/1030) | Enterocyte Progenitors | no such term | **correct** — `CL:4047019` early enterocyte is nearest |
| [Gut](https://celltype.info/project/1030) | Mid Villus Enterocytes | no mid-villus term | **correct**, but see 5c |
| [Gut](https://celltype.info/project/1030) | Secretory Progenitors | no intestinal term | **correct** |
| [Gut](https://celltype.info/project/1030) | Submucosal Fibroblasts (S3) | no submucosal gut fibroblast | **correct** — CL has subepithelial, sub*serosal*, lamina propria, crypt-bottom, crypt-top, fibroblastic reticular; no submucosal |
| [Gut](https://celltype.info/project/1030) | Muscularis Propria Fibroblasts | doesn't fit S1/S2/S3 | **correct** |
| [Gut](https://celltype.info/project/1030) | Contractile Pericytes | "*could also be a state change*" | **hedge is right** — `analysis/mural_cell_annotation_review.md` finds the label misannotated (arteriolar vSMC). **Do not create this term** |
| [HEOCA intestine](https://celltype.info/project/604) | mLTo cells | new term | **reasonable** — mesenchymal lymphoid tissue organizer cell is well described |

**8 of 9 non-immune gut assessments are well-founded**, and the ninth correctly
flags its own uncertainty. These are a ready-made worklist, not claims to
re-litigate.

### 5b. Found in this review, priority order

1. **Optic-nerve meningeal fibroblasts by layer** — dura, arachnoid, pia, lamina
   cribrosa. Four populations, 3.6k–32k cells, marker-separated, in a
   compartment CL covers thinly.
2. **Norn cell** (kidney) — CL has nothing, and CAP's proposed synonym is wrong.
3. **Ciliary-body fibroblast** (`CB_Fibro`, n=142,183).
4. **Diffuse bipolar 4a / 4b** (retina).
5. **ON / OFF starburst amacrine cell** (retina).
6. **GABAergic-glycinergic amacrine** — see 5d.

### 5c. Interim mappings the assessments overlooked

Right that no exact term exists, yet still leaving the label needlessly general:

| Label | Currently | Better today |
|---|---|---|
| Mid Villus Enterocytes (n=30,619) | `CL:0000584` enterocyte | `CL:1000335` **enterocyte of epithelium of intestinal villus** — correct now, no zonation claim, strictly more specific |
| Secretory Progenitors (n=4,875) | `CL:1100001` secretory epithelial cell | not an intestinal term at all; `CL:0009012` transit amplifying cell of small intestine is closer to what the assessment describes |

### 5d. The amacrine proposal needs work before submission

Ten `HAC*` labels in the retina share one assessment proposing a single term,
"GABAergic Glycinergic amacrine cells". Three problems:

1. **The evidence is asserted, not shown.** The assessment names GAD1, GAD2 and
   SLC6A9 as deciding; **none of the ten labels lists any of them**. Needs
   `pct_detected` per label before it goes to CL.
2. **One term for ten clusters** ranging n=39 to n=44,445, mapping to distinct
   mouse/macaque types in their own rationales. That is a *grouping* request;
   the clusters would still need terms.
3. **HAC72 does not belong** (§4).

### 5e. `ontologyAssessment` as a field

Four incompatible conventions in one unschematised column:

| Convention | Atlas | Actionability |
|---|---|---|
| Prose stating gap + justification | Gut | **best in the report** |
| `Parent term - X, Synonym term: Y, DOIs: ...` | Kidney | structured but **wrong in 2 of 3**; the `Synonym term` slot means "move here" in one row and "loosely related" in another |
| Identical one-line boilerplate ×7, same DOI | HEOCA intestine | **least actionable**; proposed names like `mesoderm 1 (HAND1)` cannot be CL labels |
| One text copy-pasted ×10 | Retina amacrine | see 5d |

Two gut assessments **ask CL a direct question** — "*are these present across
tissues to warrant a CO label?*", "*We should find a consensus from fibroblast
experts*" — and nothing routes them anywhere. That is the most actionable
process gap found.

It also **carries DOIs that `rationaleDois` does not**: the kidney rows supply
three DOIs in free text while `rationaleDois` is empty. Anything counting
evidence from `rationaleDois` alone undercounts.

---

## 6. Site feedback `[FB]` — already filed, and awaiting application

93 labels across 15 of 61 HCA datasets carry feedback; 46 datasets have none,
including every gut, liver, optic nerve, ocular surface and adipose dataset.

### 6a. Six corrections in this document were already filed

| Label | Atlas / dataset | Filed refine | § |
|---|---|---|---|
| BeamA | [TM 1242](https://celltype.info/project/574/dataset/1242) | `CL:0000057` → `CL:7770003` (by `do12`) | §3 |
| BeamB | [TM 1242](https://celltype.info/project/574/dataset/1242) | `CL:0000057` → `CL:7770006` | §3 |
| JCT | [TM 1242](https://celltype.info/project/574/dataset/1242) | `CL:0000057` → `CL:7770002` | §3 |
| Schlemm_Endothelium | [TM 1242](https://celltype.info/project/574/dataset/1242) | `CL:0000115` → `CL:4033097`, markers +PROX1 | §3 |
| Uveal_Melanocyte | [TM 1242](https://celltype.info/project/574/dataset/1242) | `CL:0000148` → `CL:4030000` | §1 |
| MG_OFF | [Retina 1153](https://celltype.info/project/544/dataset/1153) | `CL:4023188` → `CL:4033047` (refine + an independent disagree) | §3 |

**These are not new findings.** They are evidence the channel works and that its
contents reach neither the labels nor the OLS report. All five trabecular ones
sit on the scRNA arm only — the fix needs applying to both.

Everything else in §2–§5 is **not** covered by any filed feedback.

### 6b. Substantive critiques visible only in feedback

| Atlas | Label | Critique |
|---|---|---|
| [HLCA](https://celltype.info/project/684) | NK cells (16,978) | "*differential TRGV9 (marker of Vg9 gd T cells) among the top DEGs suggests it is a cytotoxic gd T cell*" |
| [HLCA](https://celltype.info/project/684) | Non-classical monocytes (8,834) | "*more like activated inflammatory monocytes in the absence of FCGR3A, CX3CR1, MS4A7*" |
| [HLCA](https://celltype.info/project/684) | Migratory DCs | "*no markers listed*"; proposes CCR7, FSCN1 |
| [Neural organoid](https://celltype.info/project/580) | astrocyte (66,990) | "*I don't see GFAP or ALDH1L1... looks like a group of multiple distinct cells*"; sibling `mature astrocyte` gets an agree for having both |
| [Breast](https://celltype.info/project/1035) | Vascular endothelial (277,259), B-lymphocyte | two `split` proposals with per-cluster marker evidence |
| [HEOCA intestine](https://celltype.info/project/604) | colonocytes, immune | asks about BEST4/OTOP2/CA7/GUCA2A/B/SPIB; doubts `immune` exists at all in repeatedly passaged organoids |
| [RPE & choroid](https://celltype.info/project/1058) | 5 RPE labels | marker-addition requests (SCNN1A, KCNK13/TNFRSF12A, CCDC60/FAP) |

**Marker-addition is the commonest substantive ask**, and nothing routes it back
into `markerGenes`.

---

## 7. Caveats

- **Lexical and read-through only.** No DE, no `pct_detected`. Every marker
  statement reads CAP's curated field against latent knowledge — enough to flag
  a lead, not to publish one.
- **No literature consulted.** LYVE1/STAB1 for LSEC, FOXI1 for ionocytes, GRHL2
  for epithelium, AIF1 for myeloid, FAM83D as mitotic — all hypotheses, not
  citations. They must be sourced before going to CAP or CL.
- **CL lookups were lexical**, built from the labels' own wording — exactly the
  search that cannot find a term named differently. The "no suitable term"
  claims (Norn cell, lamina cribrosa, dura fibroblast, ciliary-body fibroblast)
  have **not** had the semantic pass `searchClassesWithEmbeddingModel` that
  CLAUDE.md step 5 requires, and may be wrong for that reason. §5a's
  verifications carry the same limitation.
- **`[CAS]` was spot-checked on 2 of 35 datasets.** Both matched `[OBS]` exactly,
  but that does not test staleness after an edit.
- **`[FB]` parses rendered HTML**, will break silently on a CAP build change, and
  under-reported one dataset before a retry guard was added. Treat 93/15 as a
  floor.
- **Immune labels were excluded by dataset and label name**, so immune labels
  inside a non-immune dataset (macrophages in the optic nerve, T cells in the
  liver) were skipped unsystematically rather than cleanly.
- **The breast atlas exposes no CAS JSON**, so its labelsets are not covered
  except via `[FB]`.
- Data fetched 2026-10-02; the OLS report reflects an earlier, unknown state.
  Where they disagree about a label, the live sources are more recent.

---

## 8. Source tags

| Tag | Meaning |
|---|---|
| `[OLS]` | present in the exported OLS report (`data/raw/`) |
| `[CAS]` | recovered from CAP's CAS JSON export (`data/derived/cap_json_reconstructed.tsv`) |
| `[OBS]` | read from the dataset's h5ad `obs` |
| `[GQL]` | from CAP's GraphQL API via the `cap` CLI |
| `[FB]` | from a dataset's `/feedback` page (`data/derived/cap_feedback.tsv`) |
| `[CL]` | checked against the Cell Ontology via OLS4 |

Retrieval for each is in `analysis/cap_data_sources.md`.
