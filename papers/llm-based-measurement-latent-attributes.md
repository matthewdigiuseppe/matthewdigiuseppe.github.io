---
title: "LLM-Based Measurement of Latent Attributes in Trade Data"
authors: ["Matthew DiGiuseppe", "Xuelong Fu", "Michael E. Flynn"]
year: 2026
status: "Working paper"
topics: ["AI & Politics"]
url: "https://www.matthewdigiuseppe.com/papers/llm-based-measurement-latent-attributes.md"
links: {"Preprint on OSF": "https://osf.io/preprints/socarxiv/t8wdg_v2"}
full_text: true
---

# LLM-Based Measurement of Latent Attributes in Trade Data

DiGiuseppe, M., Fu, X., & Flynn, M. (2026). LLM-Based Measurement of Latent Attributes in Trade Data.

- Status: Working paper
- Topics: AI & Politics
- Preprint on OSF: https://osf.io/preprints/socarxiv/t8wdg_v2
- Listed on: https://www.matthewdigiuseppe.com/#research

<!-- END OF GENERATED HEADER: edit freely below this line; scripts/build_agent_files.py keeps it -->

## Abstract

Trade data are available at a highly disaggregated level. Yet the sheer number of goods classifications (5,000+) makes it difficult to analyze trade flows and tariff policy at a mid-level of aggregation. In this Research Note, we outline a method that can scale—not merely classify—traded goods on researcher-defined dimensions that do not overlap clearly with existing classification schemes. We propose that the embedded knowledge in large language models (LLMs) can be used to conduct pairwise comparisons (PWCs) of Harmonized System (HS) product descriptions by determining their relative proximity to a specific concept. Bayesian Bradley–Terry estimates and their associated uncertainty can then be used for downstream descriptive or causal analysis. We provide three illustrations. First, we replicate the tariff “pink tax” of Betz et al. (2021) across final consumption goods. Second, we use LLMs to scale the military relevance of goods. We show that the scale aligns with existing “dual-use” classifications and US Department of Defense procurement. Third, because existing classifications might sit in the models’ training data, we test whether LLM-generated scales can predict events outside the training data. We show LLM estimates can predict which goods were exposed to the 2026 closure of the Strait of Hormuz. In all, the method shows how researchers can use LLMs to give new life to this very rich but overlooked data source.

## Full text

> Extracted automatically from the preprint dated November 13, 2026: https://osf.io/preprints/socarxiv/t8wdg_v2. Tables, figures and equations may be garbled or missing; quote the PDF, not this text.

**LLM Measurement of Latent Attributes in Trade Data**

Matthew DiGiuseppe · Xuelong Fu Leiden University · Cambridge University [email removed] · [email removed] Michael Flynn Kansas State University [email removed] November 13, 2026

Abstract Trade data are available at a highly disaggregated level. Yet the sheer number of goods classifications (5,000+) makes it difficult to analyze trade flows and tariff policy at a mid-level of aggregation. In this Research Note, we outline a method that can scale—not merely classify—traded goods on researcher-defined dimensions that do not overlap clearly with existing classification schemes. We propose that the embedded knowledge in large language models (LLMs) can be used to conduct pairwise comparisons (PWCs) of Harmonized System (HS) product descriptions by determining their relative proximity to a specific concept. Bayesian Bradley–Terry estimates and their associated uncertainty can then be used for downstream descriptive or causal analysis. We provide three illustrations. First, we replicate the tariff “pink tax” of Betz et al. (2021) across final consumption goods. Second, we use LLMs to scale the military relevance of goods. We show that the scale aligns with existing “dual-use” classifications and US Department of Defense procurement. Third, because existing classifications might sit in the models’ training data, we test whether LLM-generated scales can predict events outside the training data. We show LLM estimates can predict which goods were exposed to the 2026 closure of the Strait of Hormuz. In all, the method shows how researchers can use LLMs to give new life to this very rich but overlooked data source.

Declaration of generative AI and AI-assisted technologies in the manuscript preparation process: During the preparation of this work, the author(s) used a variety of LLMs (ChatGPT 5.2 through GPT-6 Astra and Claude Opus 4.5–5.5) to write R code and copyedit the manuscript. After using these tools, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the published article. Economists and political scientists often use highly disaggregated product-level trade statistics (e.g., the six-digit Harmonized System [HS6] or the Standard International Trade Classification [SITC]). Gravity models of trade at the individual-good level are useful for assessing how narrowly targeted policies and shocks reallocate products (e.g., Bown and Crowley, 2007). More granular data can also be used to better assess the impact of external events on local industries. Famously, matching imports to local industry (in a specific country) was useful for understanding the multiple consequences of the China shock (Autor et al., 2020). Similarly, disaggregated trade data are helpful for examining the economic effects of the recent US–China trade war(s) (Fajgelbaum and Khandelwal, 2022). These data are also useful for examining how institutions condition trade flows and for comparing the similarity of trade portfolios (Kim et al., 2019, 2020). Further, these data are useful for exploring how tariff rates differ across products within the same industry (Kim, 2017). Finally, scholars often use these data to study flows or tariffs on a small subset of easily identifiable goods (Wellhausen, 2025; Betz et al., 2021).

Product-level trade flow or tariff data are less useful when scholars are interested in categories of goods that (a) are not limited to a small subset of items or (b) do not overlap clearly with existing trade classification schemes (e.g., intermediate goods, final consumption, or industry). The HS, the most detailed scheme, is designed for customs and tariff administration—not academic research. Accordingly, using product-level trade data in ways that deviate from existing schemes requires scholars to reclassify goods at a higher level of aggregation. For example, a scholar interested in trade in dual-use goods (i.e., goods with both civilian and military applications) would have to apply an external measure of “dual use” to the existing classification system. This generates several problems. First, hand-coding over 5,000 goods is costly. Second, binary classification schemes may miss goods’ latent attributes; continuing with the dual-use example, the military applications of a particular good may be a matter of degree, rather than either/or. Finally, even expert human coders may lack knowledge about the uses of all traded goods and how they relate to researcher-defined concepts. Many traded goods are obscure, and coders may not know how they relate to global (or local) consumption patterns or where they fit in complex global supply chains.

We propose that LLMs can help researchers address these problems by scaling goods on latent dimensions of interest using pairwise comparisons (PWCs; e.g., DiGiuseppe and Flynn, 2026; Licht et al., 2025), allowing scholars to make better use of this rich data source. LLMs reduce the cost of scaling and classifying data, but they also draw on broad embedded knowledge about how goods are used in production and how they are consumed. LLMs have approached expert level in annotation and classification (Gilardi et al., 2023), encode detailed economic information (Buckmann et al., 2025), and correctly judge the economic knowledge of voters (DiGiuseppe and Flynn, 2026). In particular, Marra de Arti˜nano et al. (2026) find that LLMs classify agricultural and food products into six-digit HS codes with about 80 percent accuracy—an important task for exporters.

Our approach pairs this embedded knowledge and capability with pairwise comparison (PWC) scaling. Pairwise comparisons have well-known advantages for scaling (Carlson and Montgomery, 2017). The method relies on multiple comparisons of different goods to identify which good more closely aligns with the judged dimension (a “winner”) and which aligns less closely (a “loser”). With these comparisons in hand, a statistical model can be fit to estimate a coefficient (score) for each good along the judged dimension. Moreover, the subsequent model can identify nuanced differences from independent comparisons in a way that would be harder if humans or LLMs were asked to place independent items directly on a 10- or 100-point scale. As DiGiuseppe and Flynn (2026) show, LLMs tend to cluster responses when asked to scale items. Finally, unlike many other scaling approaches, the model returns uncertainty estimates that can be propagated in downstream analyses. The high cost of coding thousands of pairs has historically limited the use of PWC-based scaling methods, but this is a problem LLMs readily solve. This problem compounds when you consider few, if any, humans have knowledge of all 5,000+ HS goods and their place in the global economy.

By combining PWC-based scaling with the embedded knowledge of LLMs, scholars can unlock the richness of text-based data, such as trade product classifications. We present three applications that show the promise of LLMs in this domain and also demonstrate the validity of the LLM-created scales.

We first build a scale of the gendered nature of HS goods. We then replicate a study by Betz et al. (2021). They identify a “pink tax” in tariff policy using a subset of goods labeled by their target gendered market. Expanding on their pre-labeled subset, we scale all final consumption goods by how likely they are to be consumed by women, recovering the same tariff gap and showing that the pink tax extends well beyond easily identified goods.

Next, we create a new measure of good-level military relevance. This is useful because (1) existing classifications of dual-use goods give us a benchmark for our scale and (2) binary classifications of dual use are almost certainly too coarse. LLM-PWC can retrieve a continuous score that indicates how relevant each good is to the military, relative to all others. We show that the measure strongly predicts existing classifications. We also show that the goods it ranks highest come from the industries the US Department of Defense buys from most, relative to their size, while the purchases of civilian departments such as Health and Human Services and Agriculture show no such pattern.

Lastly, while comparing LLM-generated scales to existing classifications goes some way toward validating the measures, the practice carries a serious risk. The human-created classifications are likely in the models’ training data, so agreement might reflect recall rather than substantive judgment. We therefore follow DiGiuseppe (2026) and use the consequences of an event outside the training data, the closure of the Strait of Hormuz, to assess whether the LLM (GPT-5.4) does in fact have sufficient embedded knowledge of HS goods. We find that a scale built from pairwise judgments of which goods are more exposed to a severe disruption of the Strait of Hormuz predicts which goods’ unit values rose months after the actual closure.

### Workflow

To scale good-level trade data, our process begins by randomly assigning N pairs of goods from the Harmonized System (HS) six-digit trade identification codes and descriptions. The value of N is set by the researcher, but larger values generally yield lower levels of uncertainty in the posterior distributions. However, computational costs increase with N . We generally recommend at least 20 pairs per item to distinguish between individual estimates. As computing costs rise, researchers may prefer to increase N only until improvements in precision begin to plateau. Understanding niche goods and their place in supply chains is difficult, which may favor larger LLMs, but larger models cost more. In our military application, a 26-billion-parameter model did as well as a 235-billion-parameter one, so researchers should test whether a smaller model is enough for their task. Scaling all 5,613 HS goods,[^1] with 20 pairs drawn per good (so each good appears in about 40 comparisons), results in 112,260 LLM-PWCs. At OpenAI’s posted prices in October 2026, and assuming about 340 input and 22 output tokens per comparison, this costs about $3 to $5 with its smallest model (GPT-6 Luna) and about $250 (Batch API) to $505 (standard API) with GPT-6 Astra at low reasoning effort (OpenAI, 2026a).[^2] Scholars could also employ a ladder approach in which smaller models produce initial rankings and larger models then judge the more similar, and more difficult to differentiate, pairs. We recommend that researchers experiment with models of different sizes and vendors to assess how stability and performance scale with model size for their specific task.

Once pairs are assigned, we prompt an LLM to consider each item in the pair and judge whether item i or item j more closely aligns with the target construct, or whether the goods are tied. For simplicity in estimation, we randomly assign “winners” and “losers” after the API call when the LLM codes a pairing as a tie. Alternatively, researchers can model ties directly using a Bradley–Terry–Davidson model (Davidson, 1970). Researchers could also adjust the prompt to force a winner or a loser. When ties are common, as in our gender task, the coin flip adds noise to the scale, though it does not change our pink-tax estimates.[^3]

After the LLM has judged all PWCs, we estimate a Bayesian Bradley–Terry (BT) model. BT models fit using maximum likelihood estimation (MLE) require the comparison graph to be connected—every item must be reachable from every other item through a chain of direct comparisons. When this condition fails, the likelihood surface becomes flat for isolated subgraphs, and MLE may not converge or may yield degenerate estimates. Even when the graph is connected, MLE-based BT models typically require anchoring one item to a fixed value (e.g., 0 or 1) to achieve identification (Issa Mattos and Martins Silva Ramos, 2022). Bayesian estimation sidesteps these issues. A prior over item parameters regularizes the posterior even when connectivity is imperfect, and estimation yields a full posterior distribution for each item rather than a point estimate and standard error.

Consequently, we follow DiGiuseppe and Flynn (2026) and estimate a Bayesian BT model:

eλi Pr(i > j) = pij = eλi + eλj  (1) The BT model is a multilevel logistic regression. We use regularizing priors to stabilize estimation when comparisons are sparse and to speed model convergence: a half-normal(0, 3) prior on the standard deviation of the item scores for the gender scale, an exponential(1) prior for the other three scales, and the brms default prior on the intercept.[^4] The item-level intercepts—λ—give each item’s position on the latent scale, and Pr(i > j ) follows from inserting λi and λj into Equation 1. The model we estimate also adds a population-level intercept α to the log-odds implied by Equation 1, where i is the item shown first. It captures any advantage for the first position and so serves as a check on position bias. The brms (B¨urkner, 2017) syntax is as follows:

brms::brm(Y ~ 1 + (1|mm(item1, item2, weights = cbind(weight1, weight2), scale = FALSE)), family = bernoulli(link = "logit"), data = pairs)

Users should also note that the weights argument simply corresponds to a +1 and −1 weight assigned to the first and second items, respectively. The 1 term estimates the intercept α: the extra log-odds that the item shown first “wins” when the two items have equal scores (a “home-field advantage”). Users who are confident there is no order effect can replace it with 0.

The model estimates each good’s position on the user-defined conceptual scale, providing posterior distributions that can be used to derive point estimates and uncertainty estimates. The researcher can then merge these estimates with trade data to analyze flows or tariff levels. In both cases, researchers will likely have to manage the concordance between revisions of the classification systems. We use and recommend the concordance R package to manage the translations (Liao et al., 2020).

For downstream analyses, researchers can use a point estimate of the latent score (e.g., posterior mean/median) or they can carry the uncertainty from the BT models into the downstream model. Frequentist models may follow a similar approach but will likely need to adjust their standard errors. A tempting fix is to sample from each good’s posterior distribution, estimate the downstream model on each draw, and combine the estimates with Rubin’s rules (Rubin, 2004). Because these draws ignore the outcome, they add noise to the regressor and pull the slope toward zero, in proportion to the share of score variance that is posterior noise. Multiple overimputation avoids this by drawing from a model that includes the outcome (Blackwell et al., 2017). We therefore report models on posterior means, and we recommend that researchers for whom a fully Bayesian approach is not feasible, and who need both an unbiased slope and full uncertainty estimates, model the scores and the outcome jointly. Figure 1 outlines the process.

LLM com- Sample pairings parisons for  Handle ties Draw N random  Fit Bayesian

```text
pairs (N ≪ all  each (i, j)  Random tie-break  Bradley–Terry
```

Prompt re-  / force winner possible pairs)

turns A/B/tie

```text
summaries  Merge with  models
```

Posterior  Downstream trade/tariff data

Mean, 50/95% cred-  Posterior means;

```text
ible intervals; keep  Manage HS/SITC  joint model for
the posterior draws  concordances  full uncertainty
```

Figure 1: Proposed Workflow

Alt text: Flow chart of seven steps: sample pairings; LLM comparisons for each pair; handle ties; fit a Bayesian Bradley–Terry model; summarize the posterior and keep the draws; merge with trade or tariff data; and fit downstream models on posterior means, or jointly with the scores for full uncertainty.

### Replicating the Pink Tax in Trade

Betz et al. (2021) show that apparel labeled for women faces higher tariff rates than apparel labeled for men, and that greater women’s representation in a country’s legislature reduces this gap in democracies. Their analysis uses only a subset of HS apparel items with explicit gender labels—78 matched pairs of men’s and women’s products. We extend their analysis by using all final consumption goods as identified by the Broad Economic Categories classification (BEC v5; United Nations 2016). This leaves us with 1,481 goods from the 2022 version of the HS.

We drew 15 random pairs per good (22,215 pairs), so each good appears in about 30 pairs on average. We then prompted OpenAI’s GPT-4.1[^5] to compare the two products in each pair and indicate whether A or B was more likely to be consumed by a woman. We used the following prompt:

##### LLM Configuration for Pairwise Comparisons

system prompt: ‘‘You are a validator. Reply with exactly one token: ‘A’, ‘B’, or ‘tie’. No explanation.’’ prompt: ‘‘Here are two product descriptions from the Harmonized System used to catalog international trade. Which one of these products (A or B) is more likely to be consumed by a woman? Please reply with A or B. In the event neither or both are equally likely, respond with ‘tie’. Reply with ‘A’, ‘B’ or ‘tie’, and nothing else.

Good A: {good a} Good B: {good b}’’

The comparisons returned 4,258 A responses, 4,413 B responses, and 13,542 ties. Next, we randomly assigned a “winner” to tied pairs, estimated the Bayesian Bradley–Terry model, and retrieved good-level posterior means and standard deviations.[^6] Figure 2 plots the posterior estimates and their 95% credible intervals from lowest to highest. We highlight in purple goods whose description names women or girls (e.g., Women’s, Girls’). Most goods are indistinguishable by gender, as one might expect and consistent with the high number of ties. However, the scale increases sharply for about 20% of goods. Here, we see a cluster of women’s-labeled goods mixed among 43 other goods with scores greater than 2.0.

Table 1 presents the top 10 unlabeled goods by Bradley–Terry estimate. Consistent with the intended construct, these goods are predominantly associated with female consumption (e.g., cosmetics, hosiery, wigs, and perfumery). Table 2 presents the bottom 10 unlabeled goods, which have little association with women’s consumption (e.g., unmanned aircraft, swords and bayonets, and petroleum oils). Notably, the scale recovers this gender signal from HS product descriptions alone, without any explicit gender label. This is an important detail: HS descriptions are written for tariff administration, not consumer profiling, and

Figure 2: Women’s consumption Bradley–Terry score (low to high). This figure shows Bradley–Terry estimates and 95% credible intervals for all consumption goods in the HS (2022) product list. Goods shown in purple mention women or girls in the product description.

Alt text: Plot of 1,481 goods ranked from lowest to highest score, each with a 95 percent credible interval.

Most scores sit near zero; the top fifth of goods rise steeply. Purple points, the goods whose descriptions name women or girls, cluster at the top.

several goods at both ends of the scale are described in technical language that obscures their end use. HS 2710, for instance, describes petroleum oils and preparations—language that gives no direct indication of gendered consumption—yet the model places it near the bottom of the scale. This suggests that the LLM is drawing on embedded knowledge of consumption patterns rather than surface-level textual cues. A pilot with human raters supports this reading. Participants on Prolific, judging the same pairs, agreed with GPT- 4.1 nearly as often as they agreed with each other, and rarely chose the opposite good (Appendix A.1).

Table 1: Top 10 non-labeled goods by BT score

HS code Score Short description 670420  2.886 HS 670420: Wigs, false beards, eyebrows and eyelashes, switches and the like, of human or animal hair o...

611522  2.873 HS 611522: Hosiery; panty hose, tights, stockings, socks and other hosiery, including graduated compres...

330430  2.741 HS 330430: Cosmetic and toilet preparations; beauty, makeup and skin care preparations (excluding medic...

961511  2.683 HS 961511: Combs, hairslides and similar; hairpins, curling pins, curling grips and hair curlers and th...

330420  2.656 HS 330420: Cosmetic and toilet preparations; beauty, makeup and skin care preparations (excluding medic...

330499  2.647 HS 330499: Cosmetic and toilet preparations; beauty, makeup and skin care preparations (excluding medic...

330790  2.633 HS 330790: Perfumery, cosmetic or toilet preparations; preshave, shaving, aftershave, bath preparations...

330491  2.630 HS 330491: Cosmetic and toilet preparations; beauty, makeup and skin care preparations (excluding medic...

330710  2.628 HS 330710: Perfumery, cosmetic or toilet preparations; preshave, shaving, aftershave, bath preparations...

711320  2.598 HS 711320: Jewellery articles and parts thereof, of precious metal or of metal clad with precious metal...

We next replicate the main analysis of Betz et al. (2021) using our new measure. Given our data structure, we adopt a country–product–year unit of analysis and estimate the average tariff rate for each good as a function of the good’s Bradley–Terry estimate and the logged share of legislative seats held by women in that country-year. We use average tariff rates from the World Bank’s World Integrated Trade Solution (WITS) database (World Bank, 2026). Women’s seat share and the country-level controls come from the replication data of Betz et al. (2021). The sample covers 89 countries coded as democracies in those

Table 2: Bottom 10 non-labeled goods by BT score

HS code  Score Short description 270119  -2.147 HS 270119: Coal; briquettes, ovoids and similar solid fuels manufactured from coal Coal; (other than an...

851490  -2.143 HS 851490: Industrial or laboratory electric furnaces and ovens (including those functioning by inducti...

930700  -2.131 HS 930700: Arms; swords, cutlasses, bayonets, lances and the like, parts thereof and scabbards and shea...

970529  -1.993 HS 970529: Collections and collectors’ pieces; of archaeological, ethnographic, historical, zoological,...

880692  -1.888 HS 880692: Unmanned aircraft Unmanned aircraft; for other than remotecontrolled flight and other than f...

880624  -1.888 HS 880624: Unmanned aircraft Unmanned aircraft; for remotecontrolled flight only, for other than for ca...

271012  -1.843 HS 271012: Petroleum oils and oils from bituminous minerals, not crude; preparations n.e.c, containing ...

460121  -1.834 HS 460121: Plaits and similar products of plaiting materials, assembled into strips or not; plaiting ma...

271019  -1.788 HS 271019: Petroleum oils and oils from bituminous minerals, not crude; preparations n.e.c, containing ...

271020  -1.785 HS 271020: Petroleum oils and oils from bituminous minerals, not crude; preparations n.e.c, containing ...

data, from 1995 to 2015, and the 1,390 scored goods that appear in the tariff data. Tariff lines are converted to HS 2017 with the concordance package and matched to our goods by identical six-digit codes, so most of the 91 goods that drop out are HS 2022 codes with no identically numbered HS 2017 code. We use each good’s posterior mean. We standardize all covariates to ease interpretation and drop the top 5% of tariff rates to reduce the influence of outliers. Following Betz et al. (2021), we cluster standard errors by country-product pair.

Model 1 of Table 3 replicates evidence of a pink tax across the full range of consumption items. We find a positive and statistically significant relationship. A one-standard-deviation increase in the Bradley–Terry score is associated with an average tariff rate 1.32 percentage points higher. Models 2 and 3 estimate the conditional effect of interacting women’s seat share with the gender score. Here, we find the opposite pattern from Betz et al. (2021). Tariffs on women’s goods increase with the share of legislative seats held by women. Models 4 to 6 repeat the analysis while excluding goods that explicitly mention gender in the product description. Even when excluding these goods, the pink tax remains apparent: the coefficient on the gender score falls only from 1.32 to 1.20, although the interaction with seat share is

Table 3: Gendered consumption and average tariffs

All consumption goods  Excluding gender-labeled goods

```text
(1)  (2)  (3)  (4)  (5)  (6)
Gender score  1.316***  1.316***  1.329***  1.199*** 1.198***  1.196***
(0.019)  (0.018)  (0.019)  (0.026)  (0.026)  (0.027)
Ln(women’s seat share)  0.260***  0.222***  0.247***  0.273*** 0.279***  0.329***
(0.021)  (0.021)  (0.022)  (0.023)  (0.023)  (0.024)
Ln(women’s seat share) ×  0.244***  0.297***  0.140***  0.196***
gender score  (0.014)  (0.017)  (0.022)  (0.025)
GDP growth  -0.035***  -0.024***
```

(0.005)  (0.006)

```text
GDP per capita  0.120***  0.365***
```

(0.035)  (0.034)

```text
Female labor force  0.119**  0.008
```

(0.060)  (0.063)

```text
Observations  1,137,094 1,137,094 1,085,893 984,554  984,554  940,554
R-squared  0.032  0.033  0.035  0.017  0.017  0.018
```

Note: OLS with country and year fixed effects. Gender score is each good’s posterior mean, standardized. Standard errors clustered by country-product in parentheses. Tariffs above the 95th percentile dropped. Columns 4–6 exclude every good whose HS description names a gender. *p < 0.1, **p < 0.05, ***p < 0.01.

about 40 percent smaller. Thus, tariff bias extends beyond the subset of goods used by Betz et al. (2021), demonstrating the value of examining a wide range of goods.

### Military Relevance of Traded Goods

Measuring the military relevance of normally traded goods is important for policymakers and a variety of research questions related to national security and political economy. Thus far, however, scholars have had only coarse binary measures, often produced through political processes for the purpose of export control. These lists cannot distinguish the relative military relevance of “dual-use” goods, and they likely omit militarily relevant goods that fall short of listing thresholds. Our approach can improve measurement of the concept only if LLMs have embedded knowledge about the uses of specific goods.

In our second application, we scored all 5,613 HS6 goods on their military relevance. We ran this exercise on open-weight models rather than through a commercial API, to show that the workflow does not depend on commercial providers. We used two LLMs in this exercise to give an informal sense of performance across model size: Qwen3-235B-A22B-Instruct-2507 (4-bit AWQ weights) and Google’s Gemma 4 26B-A4B (instruction-tuned).[^7]

The BT scores and errors are presented low to high in Figure 3. We highlight goods listed as dual-use in the EU’s classification scheme. As expected, they cluster at the top end of the list. Importantly, we see strong variation across the scale, including among goods on the EU list. This suggests our measure is bringing greater nuance to a concept usually measured as a binary.

Table 4: Military-relevance scale against official lists

Goods Share  AUC [95% CI]

```text
List  flagged  (%)  Qwen3-235B  Gemma 4 26B
EU dual-use list (Annex I)  965  17.2 0.82 [0.80, 0.83] 0.84 [0.83, 0.85]
Korea strategic-items list  1,119  19.9 0.79 [0.78, 0.80] 0.81 [0.79, 0.82]
China dual-use catalog  330  5.9 0.86 [0.84, 0.87] 0.87 [0.85, 0.88]
Common High Priority List  50  0.9 0.87 [0.85, 0.90] 0.89 [0.87, 0.92]
US EAR Part 746, Supp. 7  53  0.9 0.88 [0.85, 0.91] 0.90 [0.87, 0.92]
JRC strategic-trade basket  192  3.4 0.91 [0.89, 0.93] 0.92 [0.90, 0.93]
Arms and ammunition (HS 93)  18  0.3 0.99 [0.99, 1.00] 0.99 [0.99, 1.00]
```

Note: All 5,613 HS6 goods. AUC is the probability that a randomly chosen flagged good scores above a randomly chosen unflagged good (0.5 = chance); DeLong confidence intervals. Flags from list entries truncated to six digits, so a flagged subheading may contain only some controlled lines. Sources: EU CN correlation table (1 January 2026); KOSTI HSK correlation (May 2026); MOFCOM/GAC license catalog (2026); CHPL (February 2024); 15 CFR 746 Supp. 7 (October 2026); JRC Strategic Trade Atlas (2026).

Next, we draw on five more lists that governing bodies use to flag strategic or dual-use goods and examine how well our model predicts the classification. Table 4 reports these lists, plus a dummy for HS chapter 93 (arms and ammunition) as an additional check. It also lists the area under the ROC curve (AUC), the probability that a randomly chosen good on a list scores above a randomly chosen good off it. The AUCs run from 0.79 to 0.92, and the LLMs are largely equivalent despite the difference in size. Agreement is highest for the narrow, battlefield-oriented lists (the Common High Priority List and the US supplement) and for the JRC list. It is lowest for the broad EU and Korean lists, which flag about a fifth of all goods. Arms and ammunition sit at the very top, with an AUC of 0.99 for both models.[^8]

Figure 3: Military-relevance scores for all 5,613 HS6 goods, ranked from lowest to highest, with 95% credible intervals, for Gemma 4 26B (top) and Qwen3-235B (bottom). Goods flagged by the EU dual-use list (Annex I) are in purple; all others are in gray.

Alt text: Two panels, Gemma 4 26B on top and Qwen3-235B below, each ranking 5,613 goods from lowest to highest score with 95 percent credible intervals. The 965 goods on the EU list, in purple, are sparse at the low end and fill most of the top third of both rankings.

Lastly, we examine if our measure predicts military relevance outside the export-control lists, which the models may have seen during training. We posit that the goods that rank highest should come from industries that the Department of Defense buys from heavily relative to their size, more so than civilian agencies do.[^9] We measure this with US federal contract data. For each six-digit North American Industry Classification System (NAICS) manufacturing and mining industry, we divide the Department of Defense’s mean annual prime-contract obligations in fiscal years 2019 to 2023 (from USAspending; USAspending.gov 2026) by the industry’s 2022 value of shipments (from the Economic Census; U.S. Census Bureau 2026a). We link each HS6 good to an industry with the Census Bureau’s import concordance (U.S. Census Bureau, 2026b) and average the goods’ percentile ranks on the Gemma 4 26B scale within each industry, which leaves 293 industries.[^10] We repeat the exercise for six other departments and agencies: NASA, Homeland Security, Energy (which runs the nuclear weapons laboratories), Health and Human Services, Veterans Affairs and Agriculture.

Figure 4 reports the results of a simple model in which we include department-specific dummy variables for each department. Both the industry score and the purchase intensity enter as standardized ranks, so each slope is a rank correlation. The results show that Defense, NASA and Homeland Security purchases rank high on our measure. NASA is not a military agency, but it buys many highly dual-use goods, such as aerospace and rocket technologies. Homeland Security is responsible for domestic security and requires many of the goods also used for national security. The results, in all, suggest that our measure is picking up the underlying conceptual construct.

### Out-of-Training-Data Prediction

One issue with our validation strategy for the dual-use exercise is that the lists we compared the LLM-created measure to are likely in the LLMs’ training data. The results may therefore be a product of recall rather than capability. Our final illustration demonstrates that LLMs

0.75

0.50

tment's ed coefficient)

0.25

0.00

Correlation with the depar

−0.25

purchase intensity (standardiz

```text
Defense  NASA  Homeland  Energy  Health and  Veterans  Agriculture
Security  Human Services  Affairs
```

Figure 4: Rank correlation between the military-relevance score of an industry’s goods and each US department’s purchase intensity (mean annual prime-contract obligations, fiscal years 2019–2023, divided by 2022 shipments), for 293 US manufacturing and mining industries. Estimates come from one regression with a department-specific intercept and slope; bars are 95% confidence intervals with standard errors clustered by industry. Score: Gemma 4 26B. Sources: USAspending; US Census Bureau, 2022 Economic Census.

Alt text: Dot plot with seven US departments on the horizontal axis and the correlation on the vertical axis. Defense (0.44) and NASA (0.52) are highest, Homeland Security and Energy are lower but positive, Health and Human Services and Veterans Affairs are close to zero, and Agriculture is slightly negative.

have embedded knowledge of HS6 goods and their place in the world economy that is unlikely to be due to recall.

For tasks that would otherwise require a panel of expert coders, prediction of events outside of training data (either withheld or temporally excluded) is the only reliable way to probe a model’s capabilities outside of nomological construct validity. Because there is a considerable lag between the end of an LLM’s pre-training and its public release, researchers can look for relevant events they know about but the model does not and see if the LLM can predict responses to an event relevant to the domain knowledge.

Here, we adopt this approach and ask an LLM (GPT-5.4) to predict which HS6 goods are most exposed to a severe disruption of the Strait of Hormuz, an event that, from the model’s point of view, did not occur. GPT-5.4 was released on 5 March 2026, and its documented knowledge cutoff is 31 August 2025 (OpenAI, 2026b). Its documented training data therefore predate the war, which began on 28 February 2026, the subsequent closure of the Strait, and any information about how the prices and values of goods moved in response. This is a strong test of the LLM’s capabilities because it requires the model to consider where a good was made, how its inputs relate to items shipped out of the Gulf, the elasticity of these goods, and possible substitutes that might increase in value. That is, we are asking the model to consider a high number of dimensions when evaluating each individual good.

Between 6 and 9 April 2026, we scored all 5,613 HS6 goods on their exposure to a severe disruption of the Strait of Hormuz. Importantly, the requests did not allow for web search. We followed the workflow in Figure 1, drawing 15 random pairs per good (84,195 comparisons, so each good appears in about 30), of which 84,192 returned a valid verdict.[^11] The comparison graph formed a single connected component covering all 5,613 items. The task produced only 6 ties (under 0.01 percent of verdicts), against 13,542 (61 percent) in the gendered-consumption task. The prompt supplied no examples and named no goods:

##### LLM Configuration for Hormuz Exposure Comparisons

system prompt: ‘‘You are a validator. Use only the product descriptions and your internal general knowledge. Do not browse, search, retrieve, or mention external sources. Reply with exactly one token: ‘A’, ‘B’, or ‘tie’. No explanation.’’ prompt: ‘‘Consider a severe disruption of the Strait of Hormuz in March 2026.

Which product is more likely to experience tighter supply or a higher traded price as a result of that event?

Consider both direct and indirect exposure through shipping dependence, energy dependence, and upstream input dependence.

If product A is more likely, reply A.

If product B is more likely, reply B.

If they are about equally likely, reply tie. Reply with only A, B, or tie.

Good A: {good a} Good B: {good b}’’

After estimating the scale with the Bayesian Bradley–Terry model, we waited until trade data were reported in the UN Comtrade monthly trade statistics (United Nations Statistics Division, 2026). We retrieved the 2026 data on 6 October 2026 and the 2025 comparison months on 13 October 2026. Our dependent variable is the change in each good’s log unit value between two months, where unit value is reported trade value divided by reported net weight ($/kg). We use unit value rather than total trade value because a chokepoint disruption should raise prices. Total value confounds price with quantity.

Comtrade’s monthly reporting is staggered. The set of countries reporting January differs from the set reporting June, and a raw month-to-month comparison may confound exposure with reporting. We therefore only report data from countries reporting in all periods. This leaves 61 importers and 62 exporters, including the United States. July is available for a smaller set of 44 importers, which we report separately.

Table 5 reports the coefficient on the standardized LLM-created exposure score for a series of windows.[^12] We begin with a placebo. Comparing January to February, which ends on the day the disruption began, gives coefficients that are indistinguishable from zero for both imports and exports. In the months right after the event, the scale has no positive relationship with import unit values: the event-month coefficient is negative, though only marginally significant (−0.013, p = 0.06), and April and May are indistinguishable from zero. Export unit values turn positive in May. We attribute the delay to how trade is contracted. Shipping and supply contracts are often settled well before shipment, and traded goods’ prices adjust slowly. Research, for example, shows that the median US import price stays unchanged for 10.6 months (Gopinath and Rigobon, 2008).

Four months after the event, on the fixed panel of 44 importers that report July, import unit values rise 0.028 log points (about 2.9 percent) per standard deviation of the score (p = 0.01).[^13]

Table 5: Exposure scores predict post-shock unit-value changes

Import unit value  Export unit value Window  Coefficient Goods Coefficient Goods

```text
January → February (placebo)  0.0044  5,578  -0.0054  5,548
```

(0.0051)  (0.0057)

```text
February → March (event month)  -0.0134*  5,579  -0.0025  5,552
```

(0.0067)  (0.0068)

```text
February → April (+1)  0.0085  5,578  0.0089  5,550
```

(0.0077)  (0.0085)

```text
February → May (+2)  -0.0015  5,576  0.0322***  5,549
```

(0.0094)  (0.0112)

```text
February → June (+3)  0.0169*  5,581  0.0274**  5,546
```

(0.0087)  (0.0108)

```text
February → July (+4)†  0.0285**  5,562  —  —
```

(0.0105)

Notes: Outcome is the change in log unit value ($/kg) for each HS6 good between the two months, aggregated over a fixed panel of 61 importers and 62 exporters present in every month January–June 2026. The regressor is the standardized Bradley–Terry exposure score, estimated in April 2026 with the 5 March 2026 snapshot of GPT-5.4, from product descriptions alone. Standard errors clustered by HS chapter (CR2) in parentheses. †July is available for only 44 importers, so this row uses that smaller fixed panel. *p < 0.1, **p < 0.05, ***p < 0.01.

Importantly, the result does not rest on any single reporting country. Dropping one reporter at a time from the 44-importer July panel and re-estimating the February-to-July specification gives coefficients between 0.024 and 0.033, significant at p < 0.05 in all 44 leave-one-out samples. Estimating the same specification separately within each reporter gives a mean coefficient of 0.013 and a median of 0.014, positive in 84 percent of countries and different from zero at p < 0.001.

Readers might suspect that the LLM is simply picking out the fuel and chemical chapters of the HS. The suspicion is reasonable and somewhat supported but consistent with the task. Goods in HS chapters 27, 28, 29 and 31 (mineral fuels, inorganic and organic chemicals, and fertilizers) make up 48 percent of the top five percent of goods on our exposure score, against 8 percent of goods in the bottom 90 percent. The rest of the top five percent consists mostly of plastics, synthetic filament yarn, aluminum, synthetic staple fibers and rubber. The highest-scoring goods outside these four chapters are petrochemical derivatives and energyintensive materials. As far as we can tell, the scale is picking up how goods are produced (from oil and gas feedstocks, or with large energy inputs) and not only which HS chapter they sit in.

Where the scale misses is also informative (Appendix A.6). Low-scoring goods whose unit values had a sharp increase are likely noise. They are mostly goods that are historically volatile. High-scoring goods whose prices did not rise are mostly products made from oil and gas, such as plastics and synthetic fabrics, which may respond later because of a longer lag. Lastly, among calm goods the score works about as well for rarely traded goods as for widely traded ones, so we find little sign that the model knows obscure goods less well.

In all, the exercise suggests that a frontier LLM, given only a product description and a short prompt, knows enough about goods and supply chains to rank which goods’ prices would rise after an event that it had no knowledge of. As such, it gives us further confidence that the LLM’s embedded knowledge is sufficient to scale the nature of these traded goods and the results above are likely not solely a product of recall.

### Conclusion

Trade data are rich in detail. Yet existing classification schemes limit how researchers can leverage that detail to analyze trade policy and trade flows. Here, we propose that LLMs can help researchers understand relationships among traded goods along researcher-defined dimensions. Using pairwise comparisons, we leverage the embedded knowledge in LLMs to scale goods along multiple dimensions in a way that preserves uncertainty while allowing for nuanced differentiation.

Scaling trade data on new dimensions opens up uses of these data that would previously have required expert coders. Beyond the three dimensions we coded here, researchers can use our approach to examine the environmental impact of these goods, their relationship to consumption patterns beyond gender, their broader exposure to other chokepoints and supply-chain disruptions, or their dependence on critical minerals subject to export controls. Each of these constructs is continuous, cuts across the HS chapter structure, and depends on knowledge spread across many specialists rather than held by any one of them. With these scales, researchers can study both the flows of individual goods and their trade policy treatment, conditional on where the goods sit on the scale.

### References

Autor, David , David Dorn, Gordon Hanson, and Kaveh Majlesi (2020). Importing political polarization? The electoral consequences of rising trade exposure. American Economic Review 110 (10), 3139–3183.

Betz, Timm , David Fortunato, and Diana Z O’Brien (2021). Women’s descriptive representation and gendered import tax discrimination. American Political Science Review 115 (1), 307–315.

Blackwell, Matthew , James Honaker, and Gary King (2017). A unified approach to measurement error and missing data: overview and applications. Sociological Methods & Research 46 (3), 303–341.

Bown, Chad P. and Meredith A. Crowley (2007). Trade deflection and trade depression. Journal of International Economics 72 (1), 176–201.

Buckmann, Marcus , Quynh Anh Nguyen, and Edward Hill (2025). Revealing economic facts: LLMs know more than they say. Staff Working Paper 1150, Bank of England.

B¨urkner, Paul-Christian (2017). brms: An R package for Bayesian multilevel models using Stan. Journal of Statistical Software 80 (1), 1–28.

Carlson, David and Jacob M Montgomery (2017). A pairwise comparison framework for fast, flexible, and reliable human coding of political texts. American Political Science Review 111 (4), 835–843.

Davidson, Roger R (1970). On extending the Bradley–Terry model to accommodate ties in paired comparison experiments. Journal of the American Statistical Association 65 (329), 317–328.

DiGiuseppe, Matthew (2026). Using AI for superhuman tasks in social science research. Unpublished manuscript.

DiGiuseppe, Matthew and Michael Flynn (2026). Scaling open-ended survey responses using LLM-paired comparisons. Public Opinion Quarterly 90 (3), 630–656.

Fajgelbaum, Pablo D and Amit K Khandelwal (2022). The economic impacts of the US– China trade war. Annual Review of Economics 14 (1), 205–228.

Gilardi, Fabrizio , Meysam Alizadeh, and Ma¨el Kubli (2023). ChatGPT outperforms crowd workers for text-annotation tasks. Proceedings of the National Academy of Sciences 120 (30), e2305016120.

Gopinath, Gita and Roberto Rigobon (2008). Sticky borders. Quarterly Journal of Economics 123 (2), 531–575.

Issa Mattos, David and ´Erika Martins Silva Ramos (2022). Bayesian paired comparison with the bpcs package. Behavior Research Methods 54 (4), 2025–2045.

Kim, In Song (2017). Political cleavages within industry: Firm-level lobbying for trade liberalization. American Political Science Review 111 (1), 1–20.

Kim, In Song , Steven Liao, and Kosuke Imai (2020). Measuring trade profile with granular product-level data. American Journal of Political Science 64 (1), 102–117.

Kim, In Song , John Londregan, and Marc Ratkovic (2019). The effects of political institutions on the extensive and intensive margins of trade. International Organization 73 (4), 755–792.

Liao, Steven , In Song Kim, Sayumi Miyano, and Feng Zhu (2020). concordance: Product Concordance. CRAN. R package version 2.0.0.

Licht, Hauke , Rupak Sarkar, Patrick Y Wu, Pranav Goel, Niklas Stoehr, Elliott Ash, and Alexander Miserlis Hoyle (2025). Measuring scalar constructs in social science with LLMs. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pp. 32144–32171.

Marra de Arti˜nano, Ignacio , Franco Riottini Depetris, and Christian Volpe Martincus (2026). Automatic product classification in international trade: Machine learning and large language models. Review of International Economics 34 (1), 3–19.

OpenAI (2026a). API pricing. https://developers.openai.com/api/docs/pricing. Accessed 30 October 2026.

OpenAI (2026b). GPT-5.4 model documentation. https://developers.openai.com/api/docs/models/gpt-5.4. Accessed 30 October 2026.

Rubin, Donald B (2004). Multiple imputation for nonresponse in surveys. John Wiley & Sons.

Shi, Lin , Chiyu Ma, Wenhua Liang, Xingjian Diao, Weicheng Ma, and Soroush Vosoughi (2025). Judging the judges: A systematic study of position bias in LLM-as-a-judge. In Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics, pp. 292–314.

United Nations (2016). Classification by Broad Economic Categories, Rev.5. Number 53, Rev.5 in Statistical Papers, Series M. New York: United Nations.

United Nations Statistics Division (2026). UN comtrade database: Monthly trade data. https://comtradeplus.un.org. Retrieved 6 and 13 October 2026.

U.S. Census Bureau (2026a). 2022 economic census: Manufacturing and mining basic statistics (tables EC2231BASIC and EC2221BASIC). https://www.census.gov/programs-surveys/economic-census.html. Accessed 30 October 2026.

U.S. Census Bureau (2026b). Import concordance, 2022 (HTS to NAICS). https://www.census.gov/foreign-trade/reference/codes/concordance/impconcord22.xlsx. Accessed 30 October 2026.

USAspending.gov (2026). Federal spending by NAICS code, prime award types A–D, fiscal years 2019–2023. https://www.usaspending.gov. Retrieved 30 October 2026.

Wellhausen, Rachel L (2025). Tariffs as environmental protection: Evidence from the Global South after the China garbage shock. British Journal of Political Science 55, e160.

World Bank (2026). World integrated trade solution (WITS) – TRAINS database. https: //wits.worldbank.org/. Accessed: 2026-01-21.

### Supplementary Appendix

#### A.1 Human validation of the gendered-consumption verdicts

Comparing the gender scale with goods whose descriptions name a gender is somewhat circular, since the model reads the label. We therefore asked people to make the same judgment on the same pairs. We drew 300 pairs from the GPT-4.1 comparisons used in the main text (half that GPT-4.1 decided for one good, half it called a tie) and fielded them as a pilot on Prolific with 50 participants in the United Kingdom. Each participant judged 30 pairs, using the wording of the LLM prompt, and could answer A, B or tie. Because HS descriptions are hard to read, each good was shown as a one-sentence plain-English rewrite, with the official HS description beside it. The rewrites were produced by gpt-4.1-mini under a prompt that forbade adding any user group, gender, age, class or country not present in the original. We used six pairs with an obvious answer as attention checks. The pilot yielded 1,471 ratings covering 297 pairs.

Table A1 reports the results. The crowd majority matches GPT-4.1’s verdict on about three pairs in five, which is close to the rate at which people agree with each other. When we split each pair’s raters at random, the two sides agree on 64 percent of pairs. This compares to 60 percent for GPT-4.1.

Most of the 117 disagreements involve a tie. In 104 disagreements, one side called the pair a tie and the other chose a good. The crowd majority chose the opposite good from GPT-4.1 on only 13 of the 150 pairs where GPT-4.1 did not choose tie. Next, on the 213 pairs in which neither description names a gender, the crowd majority matches GPT-4.1 on 62 percent and chooses the opposite good on 5 of the 77 pairs GPT-4.1 decided. We read this as evidence that GPT-4.1’s gender judgments track how people see the same goods.

Table A1: Human validation of the gendered-consumption verdicts (UK pilot)

```text
Comparison  Pairs Agreement [95% CI]  κ
LLM vs crowd majority (A / B / tie)  297  61% [55, 66]  0.39
LLM vs crowd majority, pairs the LLM called A or B  150  63% [55, 71]  0.42
Individual A/B votes on the LLM’s side (LLM A/B pairs)  143  85% [79, 90]  –
```

Like-for-like benchmark (pairs with four or more raters, 500 random splits)

```text
Half of the crowd vs the other half  215  64% [60, 67]  –
LLM vs half of the crowd  215  60% [58, 62]  –
```

Note: 50 UK participants recruited through Prolific, 30 pairs each, 1,471 ratings of 297 pairs drawn from the GPT-4.1 comparisons (stratified: half that GPT-4.1 called A or B, half it called a tie). Crowd majority: the most common answer, with a tie when two answers are equally common. Confidence intervals from 2,000 bootstrap resamples of pairs; the benchmark row reports the mean and 2.5th–97.5th percentiles across splits. κ is Cohen’s kappa.

#### A.2 Military-relevance prompt

Both LLMs received the prompt below, with the same pairs as the Hormuz task. We ran every pair twice, once in each presentation order, and stacked the two runs. The Bradley– Terry model for this task includes the population-level intercept described in the workflow section, which absorbs any advantage for the good shown first.

##### LLM Configuration for Military-Relevance Comparisons

system prompt: ‘‘You are a validator. Use only the information in the product descriptions and your internal general knowledge. Do not browse, search, retrieve, or mention external sources. Reply with exactly one token: `A`, `B`, or `tie`.’’ prompt: ‘‘Which product has greater military relevance?

A product has military relevance if it is used in, or as an input to, military equipment, weapons, munitions, or weapons programmes (including chemical, biological, nuclear, or missile programmes).

Some goods are made solely for military use, such as weapons and munitions. These have the highest military relevance. Other goods are dual-use: they have both civilian and military applications. For these, consider how important and how direct the military use is relative to the civilian uses. If product A has greater military relevance, reply `A`.

If product B has greater military relevance, reply `B`. If they are about equal, reply `tie`.

Reply with only `A`, `B`, or `tie`. Good A: `{good a}` Good B: `{good b}`’’

#### A.3 Alternatives to the military-relevance scale

Here we compare the LLM scale to three alternatives that are easily available to researchers. The first counts military keywords in each HS description. The dictionary uses the construct wording in the prompt plus direct synonyms (military, weapon, munition, ammunition, arms, missile, nuclear, explosive, firearm, gun, rifle, pistol, revolver, bomb, grenade, torpedo, armored, warship, radar, rocket). The second is the TF-IDF cosine similarity between each description and a short summary of the construct as described in the prompt. The third is the share of goods on a list within the good’s HS section or chapter, estimated with 10-fold cross-validation. Because it uses the list labels, this measure is supervised, which favors it over our scale.

Table A2 reports the AUCs. The keyword and TF-IDF measures barely beat chance (0.51 to 0.55 on the six lists). The chapter base rate does much better. It beats the Gemma scale on the Korean list and the two narrow battlefield lists, roughly ties on the EU list, and falls short on the Chinese list and well short on the JRC list. Adding the Gemma score to the chapter base rate raises the AUC on every list, by 0.03 to 0.10, so the score carries information that the HS chapter does not.

#### A.4 Defense purchase data

We draw contract obligation data from the USAspending API (spending by NAICS, prime-contract award types A to D, fiscal years 2019–2023, retrieved 30 October 2026; USAspending.gov 2026). Shipment data come from the 2022 Economic Census values for manufacturing

Table A2: Military-relevance scale against cheaper alternatives: AUC by list

```text
LLM pairwise  Text baselines  HS base rate (CV)  Chapter
```

List  Gemma Qwen Keyword TF-IDF Section Chapter + Gemma

```text
EU dual-use list (Annex I)  0.84  0.82  0.51  0.52  0.77  0.83  0.87
Korea strategic-items list  0.81  0.79  0.51  0.53  0.77  0.83  0.86
China dual-use catalog  0.87  0.86  0.51  0.55  0.75  0.83  0.89
Common High Priority List  0.89  0.87  0.52  0.52  0.88  0.92  0.95
US EAR Part 746, Supp. 7  0.90  0.88  0.51  0.52  0.88  0.91  0.95
JRC strategic-trade basket  0.92  0.91  0.54  0.55  0.74  0.82  0.92
Arms and ammunition (HS 93)  0.99  0.99  1.00  0.73  1.00  1.00  –
```

Note: All 5,613 HS6 goods. AUC is the probability that a randomly chosen flagged good scores above a randomly chosen unflagged good (0.5 = chance). Keyword: count of military terms in the HS description (dictionary in the text). TF-IDF: cosine similarity between the description and the construct definition in the prompt. HS base rate: the share of goods on the list in the good’s HS section or chapter, estimated with 10-fold cross-validation, so it uses the list labels and is a supervised baseline. Last column: logit of the list flag on the chapter base rate plus the Gemma score (in-sample).

and mining (U.S. Census Bureau, 2026a). We linked HS6 goods to industries with the Census Bureau’s 2022 import concordance (U.S. Census Bureau, 2026b), and each good takes the industry of most of its ten-digit tariff lines. Importantly, agricultural industries are not included in the Economic Census, so we exclude farm goods. We also exclude goods whose industry codes are not in the 2022 Economic Census.

Our test covers 293 industries and 4,437 goods. Two features of the data work against finding a correlation. Prime contracts credit a purchase to the main contractor’s industry, so inputs that contractors buy (chips, bearings, specialty metals) are not credited to the industries that make them. Contracts also bundle research and services, so the ratio exceeds one for a few industries (1.29 for guided missiles); the analysis uses only ranks.

#### A.5 Alternatives to the Hormuz scale

Table A3 repeats the comparison in Appendix A.3 for the Hormuz closure scale, using the outcome and reporter panels of Table 5. The keyword dictionary here is petroleum, crude, natural gas, gas, fuel, energy, hydrocarbon and liquefied, again fixed before we saw any results. The chapter base rate needs a list of flagged goods, so in its place we use a dummy for the fuel and chemical chapters (HS 27, 28, 29 and 31).

Again, the LLM score beats the keyword and TF-IDF (similarity) measures in every temporal window. The fuel and chemical dummy is a stronger rival. Still, our LLM result shows a significant effect when controlling for this dummy variable in our main February-to- July analysis.

#### A.6 Hormuz closure scale misses

Here we take a closer look at where the Hormuz closure scale missed its prediction. This gives greater insight on whether the misses were due to systematic failures of the LLM or idiosyncratic changes the LLM could not have anticipated.

We look at goods in the bottom half of the exposure score whose unit-value change is in the top decile (surprises). We also look at goods in the top decile of the score whose change

Table A3: Hormuz exposure scale against cheaper alternatives and within HS groups

```text
Imports  Exports  Imports
Regressor (coefficient reported)  Feb → Jun  Feb → Jun  Feb → Jul
```

LLM score  0.017* (0.009) 0.027** (0.011) 0.028** (0.010)

```text
Keyword  0.010 (0.006)  0.013** (0.004)  0.012 (0.009)
TF-IDF  0.007 (0.006)  -0.001 (0.003)  0.011 (0.009)
Fuel/chemical chapters dummy  0.070 (0.031) 0.134*** (0.011)  0.061 (0.026)
```

LLM score, controlling for keyword  0.016* (0.008) 0.026** (0.011) 0.027** (0.010) LLM score, controlling for TF-IDF  0.017* (0.009) 0.027** (0.011) 0.029** (0.011)

```text
LLM score, controlling for fuel/chemical dummy  0.010 (0.006)  0.014 (0.009)  0.025** (0.010)
LLM score, HS section FE  0.006 (0.010)  0.019 (0.011)  0.023 (0.015)
LLM score, HS chapter FE  0.011 (0.013)  0.008 (0.014)  0.046** (0.019)
```

Note: Outcome and panels as in Table 5. Keyword and TF-IDF are standardized; the fuel and chemical dummy marks HS chapters 27, 28, 29 and 31. Rows reading “controlling for” report the LLM coefficient with the named regressor added; FE rows add HS section or HS chapter fixed effects. Standard errors clustered by HS chapter (CR2) in parentheses. *p < 0.1, ** p < 0.05, ***p < 0.01.

is below the median (false alarms). In the February-to-July import window there are 313 surprises and 146 false alarms among the 5,516 goods with January data. Table A4 reports this window and both June windows.

We find that surprises look like noise. Among bottom-half goods, a top-decile rise is about as common as a bottom-decile fall (11.3 against 12.5 percent). Surprises are also concentrated among goods whose unit values were volatile before the closure: 1.6 percent of the calmest third of bottom-half goods are surprises, against 24.3 percent of the noisiest third (Panel A). Once volatility is controlled, neither the score nor Gulf import share, the fuel and chemical chapters or value per kilogram (a proxy for air freight) predicts the movement of these goods.

In contrast, false alarms are unrelated to volatility (Panels A and B). They are concentrated in organic chemicals, plastics, synthetic yarns and fabrics, rubber and aluminum, which are made from oil and gas or with large energy inputs. We speculate that price increases may not have passed down the supply chain by July. We cannot test this until later months are reported.

Further, seasonal price patterns do not explain the result. In the same reporters’ 2025 data, the score does not predict the change over the same months, and controlling for each good’s 2025 change leaves the 2026 coefficients unchanged (Panel D). Subtracting the 2025 change keeps the July import and June export coefficients significant but not the June import one. None of the differenced coefficients survives HS chapter fixed effects.

Finally, if the model knew rarely traded goods less well, the score should predict worse for them. Among calm goods, the score coefficient is similar for the least and most traded thirds, and the interaction of the score with world trade is close to zero in every window (Panel C). Net of volatility, rarely traded goods are somewhat more likely to be surprises in the July import and June export windows, and to be export false alarms (Panel B). World trade is a rough proxy for how often a good appears in training text, and this test cannot rule out that the model reuses patterns from earlier shocks.

Table A4: Where the Hormuz exposure scale misses

```text
Imports  Imports  Exports
Feb → Jul  Feb → Jun  Feb → Jun
```

A. Miss rates by pre-shock volatility

```text
Surprise rate, calmest third  1.6%  0.4%  1.7%
Surprise rate, middle third  6.3%  4.9%  6.5%
Surprise rate, noisiest third  24.3%  26.5%  23.5%
False-alarm rate, calmest third  28.4%  29.2%  27.8%
False-alarm rate, middle third  19.9%  25.1%  22.5%
False-alarm rate, noisiest third  31.7%  31.8%  29.3%
```

B. Logit coefficients (regressors standardized; score included)

```text
Surprise on volatility index  0.75*** (0.08)  0.96*** (0.08)  0.72*** (0.06)
Surprise on world trade (net of volatility)  -0.20*** (0.07)  -0.12 (0.07)  -0.44*** (0.10)
False alarm on volatility index  0.03 (0.11)  0.14 (0.10)  0.15 (0.11)
False alarm on world trade (net of volatility)  -0.07 (0.27)  -0.28 (0.23)  -0.57*** (0.13)
```

C. Score coefficient by world trade Calmest third, least traded third  0.033*** (0.009) 0.028*** (0.006) 0.035*** (0.010)

```text
Calmest third, middle third  0.026*** (0.008)  0.024** (0.009)  0.016 (0.011)
Calmest third, most traded third  0.031** (0.012)  0.033** (0.012)  0.030** (0.010)
Score × world trade (chapter FE)  -0.006 (0.016)  -0.012 (0.015)  -0.009 (0.019)
```

D. Seasonal check: same months of 2025, same reporters

```text
2025 change, same months (placebo)  -0.002 (0.006)  -0.001 (0.006)  -0.008 (0.007)
2026 change, controlling for 2025 change  0.029** (0.011)  0.018* (0.010)  0.026** (0.011)
2026 minus 2025 change  0.030** (0.013)  0.018 (0.012)  0.034*** (0.011)
2026 minus 2025 change, chapter FE  0.017 (0.017)  0.004 (0.015)  0.013 (0.015)
```

Note: Reporter panels as in Table 5. A surprise is a good in the bottom half of the score whose unit-value change is in the top decile; a false alarm is a good in the top decile of the score whose change is below the median. Rates in Panel A are shares of the bottom-half (surprise) or top-decile (false alarm) goods in each volatility third. Volatility index: mean of the standardized absolute January-to-February change in log unit value, the cross-reporter standard deviation of log unit value in January, and minus the log number of reporters in January, all measured before the closure. World trade: log January plus February 2026 imports over the 62 reporters in our Comtrade extract. Panel C (rows 1–3) has no chapter fixed effects; its last row interacts the score with world trade, controlling for score × volatility. Goods without January data are dropped from Panels A–C, so their samples are 33 to 46 goods smaller than in Table 5. Panel D uses goods with unit values in both 2025 and 2026; its rows report the score coefficient on the 2025 change, on the 2026 change with the 2025 change as a control, and on the difference between the two. Standard errors clustered by HS chapter in parentheses: CR2 for the linear models in Panels C and D, and the cluster-robust estimator with an HC1 small-sample adjustment for the logits in Panel B. *p < 0.1, **p < 0.05, ***p < 0.01.

### Notes

[^1]: The 5,613 codes are UN Comtrade’s list of HS 2022 six-digit codes.
[^2]: Costs rise steeply with higher reasoning effort: our GPT-5.4 run at high effort averaged about 1,300 completion tokens per comparison and cost over $1,000.
[^3]: Researchers should also look for position bias in the final outcomes. LLM judges can favor the item shown first or second, especially when the two items are hard to tell apart (Shi et al., 2025).
[^4]: The method we propose here produces results that are extremely similar to the default results produced by alternative packages like the bpcs package (Issa Mattos and Martins Silva Ramos, 2022). Users should note that while the general rankings between the two approaches are very similar, the specific estimates for the individual items, as well as the range of estimates, may differ. Much of this variation is attributable to the differences in the default priors used by the two packages. Tests of sample data provided by the bpcs package yield results correlated > 0.99 between the two approaches.
[^5]: We used the gpt-4.1 model alias through the Chat Completions API on 20 January 2026, with temperature 0, top p 0.3 and at most 100 output tokens. Two requests failed with server errors, leaving us with 22,213 verdicts.
[^6]: Sampling used four chains with 2,000 iterations per chain (1,000 warmup), yielding 4,000 retained posterior draws. The A/B balance suggests little order bias, and the estimated first-position effect is close to zero (−0.02; 95% credible interval −0.05 to 0.01).
[^7]: Both models ran on a university computing cluster with vLLM 0.26.0 on NVIDIA A100 GPUs. Model revisions 96548f6 (Qwen, QuantTrio AWQ release; recorded at download) and 4d7ae49 (Gemma). Temperature 0, seed 0, thinking disabled for Gemma (the Qwen model has no thinking mode), at most eight output tokens. We ran every pair in both presentation orders. The full run took 50 minutes per presentation order for Qwen on two GPUs and 15 minutes for Gemma on one, including model loading, at no marginal cost. Ties were 42 percent of Gemma’s verdicts and 28 percent of Qwen’s.
[^8]: Appendix Table A2 compares the scale with simpler benchmarks. The LLM does far better than keyword and text-similarity measures, and it adds information beyond a benchmark built from the lists themselves.
[^9]: We thank Anthropic’s Claude for this recommendation.
[^10]: We average the goods’ percentile ranks within each industry regardless of the total flow of the good. Weighting each good by its 2022 US imports plus exports, or by the log of that value, moves no department’s correlation by more than 0.04 (Defense: 0.43 and 0.44).
[^11]: We used gpt-5.4-2026-03-05, the 5 March 2026 snapshot of GPT-5.4, through the OpenAI Batch API, with reasoning effort set to high and a limit of 8,192 completion tokens per comparison. GPT-5.4 showed slight position bias. The intercept of the Bradley–Terry model absorbs this. The scale uses posterior means.
[^12]: We cluster standard errors by HS chapter.
[^13]: The smaller July panel is not responsible for the gap between the June and July coefficients. On the same 44 importers, the February-to-June coefficient is 0.018 (p = 0.06), close to the 0.017 on all 61. Among the 17 importers that have not yet reported July, it is 0.020 (p = 0.09). The larger July coefficient therefore reflects timing, not which countries report.
