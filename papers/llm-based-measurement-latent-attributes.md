---
title: "LLM-Based Measurement of Latent Attributes in Trade Data"
authors: ["Matthew DiGiuseppe", "Xuelong Fu", "Michael E. Flynn"]
year: 2026
status: "Working paper"
topics: ["AI & Politics"]
url: "https://www.matthewdigiuseppe.com/papers/llm-based-measurement-latent-attributes.md"
links: {"Preprint on OSF": "https://osf.io/preprints/socarxiv/394w2"}
full_text: true
---

# LLM-Based Measurement of Latent Attributes in Trade Data

DiGiuseppe, M., Fu, X., & Flynn, M. (2026). LLM-Based Measurement of Latent Attributes in Trade Data.

- Status: Working paper
- Topics: AI & Politics
- Preprint on OSF: https://osf.io/preprints/socarxiv/394w2
- Listed on: https://www.matthewdigiuseppe.com/#research

<!-- END OF GENERATED HEADER: edit freely below this line; scripts/build_agent_files.py keeps it -->

## Abstract

Trade data are available at a high level of disaggregation, allowing scholars to examine flows of highly specific goods. Yet the sheer number of goods classifications (5,000+) makes it difficult to analyze trade flows and tariff policy at a mid-level of aggregation beyond a few existing categorizations. Here, we outline a method that can scale---not merely classify---traded goods on researcher-defined dimensions that are orthogonal to existing classification schemes. We propose that the embedded knowledge in large language models (LLMs) can be used to conduct pairwise comparisons (PWCs) of Harmonized System (HS) product descriptions by determining their relative proximity to a specific concept. A Bayesian Bradley--Terry model then uses these PWCs to place individual items on a latent scale of interest. These estimates and their associated uncertainty can then be used for downstream descriptive or causal analysis.

## Full text

> Extracted automatically from the preprint dated March 23, 2026: https://osf.io/preprints/socarxiv/t8wdg_v1. Tables, figures and equations may be garbled or missing; quote the PDF, not this text.

**LLM-Based Measurement of Latent Attributes in Trade Data**

Matthew DiGiuseppe · Xuelong Fu Leiden University · Cambridge University [email removed] · [email removed] Michael Flynn Kansas State University [email removed] March 23, 2026

Abstract Trade data are available at a high level of disaggregation, allowing scholars to examine flows of highly specific goods. Yet the sheer number of goods classifications (5,000+) makes it difficult to analyze trade flows and tariff policy at a mid-level of aggregation beyond a few existing categorizations. Here, we outline a method that can scale—not merely classify—traded goods on researcher-defined dimensions that are orthogonal to existing classification schemes. We propose that the embedded knowledge in large language models (LLMs) can be used to conduct pairwise comparisons (PWCs) of Harmonized System (HS) product descriptions by determining their relative proximity to a specific concept. A Bayesian Bradley–Terry model then uses these PWCs to place individual items on a latent scale of interest. These estimates and their associated uncertainty can then be used for downstream descriptive or causal analysis.

Declaration of generative AI and AI-assisted technologies in the manuscript preparation process: During the preparation of this work, the author(s) used ChatGPT 5.2 and Claude Opus 4.5 to write R code and copyedit the manuscript. After using these tools, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the published article.

Economists and political scientists often use product-level trade statistics at the tariff-line (HS–6 or SITC). Gravity models of trade at the individual-good level are useful for assessing how narrowly targeted policies and shocks reallocate products (e.g., Bown and Crowley (2007)). More granular data can also be used to better assess the impact of external events on local industries. Famously, matching imports to local industry (in a specific country) was useful for understanding the multiple consequences of the China shock (Autor et al., 2020). Similarly, disaggregated trade data are helpful for examining the economic effects of the recent US–China trade war(s) (Fajgelbaum and Khandelwal, 2022). These data are also useful for examining how institutions condition trade flows and for comparing the similarity of trade portfolios (Kim et al., 2019, 2020). Further, these data are useful for exploring how tariff rates differ across sectors (Kim, 2017). Finally, scholars often use these data to study flows or tariffs on a small subset of easily identifiable goods (Wellhausen, 2025; Betz et al., 2021).

Product-level trade flow or tariff data are less useful when scholars are interested in categories of goods that (a) are not limited to a small subset of items and (b) are orthogonal to existing trade classification schemes (e.g., intermediate goods, final consumption, or industry). Existing trade data classification schemes are designed for tariff administration—not academic research. Accordingly, using product-level trade data in ways that deviate from existing schemes requires scholars to reclassify goods at a higher level of aggregation. For example, a scholar interested in trade in dual-use goods (with both civilian and military applications) would have to apply an external measure of “dual use” to the existing classification system. This generates several problems. First, hand-coding over 5,000 goods is costly. Second, binary classification schemes may miss goods’ latent attributes; continuing with the dual-use example, goods can be more or less relevant for military applications, rather than either/or. Finally, even expert human coders may lack knowledge about the uses of all traded goods and how they relate to researcher-defined concepts. Many traded goods are obscure, and coders may not know how they relate to global (or local) consumption patterns or where they fit in complex global supply chains.

We propose that LLMs can help researchers address these problems by scaling goods on latent dimensions of interest using pairwise comparisons (PWCs) (e.g., DiGiuseppe and Flynn (2026); Licht et al. (2025)), allowing scholars to make better use of this rich data source. LLMs reduce the cost of scaling and classifying data, but they also draw on broad embedded knowledge about how goods are used in production and how they are consumed. Frontier LLMs have demonstrated strong domain knowledge across a variety of subjects, including politics, economics, and consumption (Gilardi et al., 2023; Buckmann et al., 2025; DiGiuseppe and Flynn, 2026). In particular, Marra de Arti˜nano et al. (2025) find that LLMs are highly accurate at sorting products into HS codes—an important task for exporters.

Pairwise comparisons (PWCs) have well-known advantages for scaling (Carlson and Montgomery, 2017). However, PWCs often require roughly 30× more tasks than simple scaling. The method relies on multiple comparisons of different goods to identify which good more closely aligns with the judged dimension (a “winner”) and which aligns less closely (a “loser”). With these comparisons in hand, a statistical model can be fit to estimate a coefficient (score) for each good along the judged dimension. Because the approach relies on binary decisions, any bias that does not flip a decision is averaged out. Moreover, the subsequent model can identify nuanced differences from independent comparisons in a way that would be infeasible if humans or LLMs were asked to place independent items directly on a 10- or 100-point scale. As DiGiuseppe and Flynn (2026) show, LLMs tend to cluster responses when asked to scale items. Finally, unlike many other scaling approaches, the model returns uncertainty estimates that can be propagated in downstream analyses. The high cost of coding thousands of pairs has historically limited the use of PWC-based scaling methods, but this is a problem LLMs readily solve.

By combining PWC-based scaling with the embedded knowledge of LLMs, scholars can unlock the richness of text-based data, such as trade product classifications. In our case, this approach helps us better understand trade flows and trade policy. We illustrate its utility by replicating Betz et al. (2021), who identify a “pink tax” in tariff policy using a subset of goods labeled by their target gendered market. Rather than relying on this prelabeled subset, we scale all goods by their propensity to be consumed by women relative to men, recovering the same pattern and showing that the pink tax extends well beyond easily identified goods.

### Workflow

Our method begins by randomly assigning N pairs of goods from the Harmonized System (HS) six-digit trade identification codes and descriptions. The value of N is set by the researcher, but larger values generally yield smaller posterior uncertainty. However, computational costs increase with N . We generally recommend at least 20 pairs per item to distinguish among individual estimates. As computing costs rise, researchers may prefer to increase N only until improvements in precision begin to plateau.

Once pairs are assigned, we prompt an LLM to consider each item in the pair and judge whether item i or item j more closely aligns with the target construct, or whether the goods are tied. For simplicity in estimation, we randomly assign “winners” and “losers” after the API call when the LLM codes a pairing as a tie. Alternatively, researchers can model ties directly using a Bradley–Terry–Davidson model (Davidson, 1970). Researchers could also adjust the prompt to force a winner or a loser. In practice, these choices should have minimal impact on the final scale.

After the LLM has judged all PWCs, we estimate a Bayesian Bradley–Terry (BT) model. BT models fit using maximum likelihood estimation (MLE) require the comparison graph to be connected—that is, every item must be reachable from every other item through a chain of direct comparisons. When this condition fails, the likelihood surface becomes flat for isolated subgraphs, and MLE may not converge or may yield degenerate estimates. Even when the graph is connected, MLE-based BT models typically require anchoring one item to a fixed value (e.g., 0 or 1) to achieve identification, and the resulting uncertainty estimates are often weakly identified (Issa Mattos and Martins Silva Ramos, 2022). Bayesian estimation sidesteps these issues: a prior over item parameters regularizes the posterior even when connectivity is imperfect, and estimation yields a full posterior distribution for each item rather than a point estimate and standard error. This enables credible intervals that can be directly propagated into downstream analyses.

Consequently, we follow DiGiuseppe and Flynn (2026) and estimate a Bayesian BT model:

eλi Pr(i > j) = pij = eλi + eλj  (1) The BT model is a multilevel logistic regression. We use regularizing priors to stabilize estimation when comparisons are sparse and to speed model convergence.[^1] The item-level intercepts—λ—give each item’s position on the latent scale, and Pr(i > j ) follows from inserting λi and λj into Equation 1. The brms syntax is as follows:

brms::brm(Y ~ 0 + (1|mm(item1, item2, weights = cbind(weight1, weight2), scale = FALSE)

Users should also note that the weights argument simply corresponds to a +1 and −1 weight assigned to the first and second items, respectively. Users who want to estimate a “home field advantage“ can replace the 0 term in the equation with a 1, which will tell brms to estimate a population-level intercept. This will estimate the log-odds that the first item “wins”.

The model yields each good’s position on the user’s defined scale and uncertainty (credible intervals). The researcher can then merge these estimates with trade data to analyze flows or tariff levels. In both cases, researchers will likely have to manage the concordance between revisions of the classifications systems. We use and recommend the concordance R package to manage the translations (Liao et al., 2020).

For downstream analyses, researchers can use a point estimate of the latent score (e.g., posterior mean/median), but this ignores measurement uncertainty. To carry that uncertainty forward, one can draw M realizations of each unit’s latent score from its posterior, estimate the downstream model on each draw, and combine the resulting estimates via Rubin’s rules (multiple overimputation) (Blackwell et al., 2017; Rubin, 2004). This yields inference that incorporates uncertainty in the latent measure. Figure 1 outlines the process.

LLM com- Sample pairings parisons for  Handle ties

For each item,  Fit Bayesian each (i, j)  Random tie-break pair with N others  Bradley–Terry Prompt re-  / force winner (N ≪ total)

turns A/B/tie

Posterior  Downstream

```text
summaries  Merge with  models
Median, 50/95%  trade/tariff data  Multiple over-
```

Manage HS/SITC CIs; keep S  imputation with

```text
draws per good  concordances  S posterior draws
```

Figure 1: Proposed Work Flow

### Illustration: The Tariff Pink Tax

Betz et al. (2021) show that apparel labeled for women faces higher tariff rates than apparel labeled for men, and that greater women’s representation in a country’s legislature reduces this gap. Their analysis uses only a subset of HS apparel items with explicit gender labels— 78 items in total. We extend their analysis by using all final consumption goods as identified by the Broad Economic Categories classification (BEC v5). This leaves us with 1,481 goods from the 2022 version of the HS.

We randomly paired each good with 15 others (≈ 30 pairs per item). We then prompted OpenAI’s GPT-4.1 LLM to compare each product and indicate whether A or B was more likely to be consumed by a woman than by a man. We used the following prompt:

#### LLM Configuration for Pairwise Comparisons

system prompt: ‘‘You are a validator. Reply with exactly one token: ‘A’, ‘B’, or ‘tie’. No explanation.’’ prompt: ‘‘Here are two product descriptions from the Harmonized System used to catalog international trade. Which one of these products (A or B) is more likely to be consumed by a woman than a man? Please reply with A or B. In the event neither or both are equally likely, respond with ‘tie’. Reply with ‘A’, ‘B’ or ‘tie’, and nothing else.

Good A: {good a} Good B: {good b}’’

The comparisons returned 4,258 A responses, 4,413 B responses, and 13,542 ties. The A/B balance suggests little order bias; therefore, directly estimating potential order effects (i.e., “home-field advantage”) is unnecessary. Next, we randomly assigned a “winner” to tied goods, estimated the Bayesian Bradley–Terry model, and retrieved good-level estimates and standard errors.[^2]

Figure 2 plots the estimates and their 95% credible intervals from lowest to highest. We highlight in purple goods that are explicitly labeled with a gender in the description (e.g., Women’s, Men’s, Girls’, Boys’). Most goods are indistinguishable by gender, as one might expect and consistent with the high number of ties. However, the scale increases sharply for about 20% of goods. Here, we see a cluster of gender-labeled goods mixed among 43 other goods with scores greater than 2.0.

Table 1 presents the top 10 unlabeled goods by Bradley–Terry estimate. Consistent with the intended construct, these goods are predominantly associated with female consumption (e.g., cosmetics, hosiery, wigs, and perfumery). Table 2 presents the bottom 10 unlabeled goods, which skew toward male-associated consumption (e.g., unmanned aerial

Figure 2: Women’s consumption Bradley–Terry score (low to high). This figure shows Bradley–Terry estimates and 95% confidence intervals for all consumption goods in the HS (2022) product list. Goods shown in purple explicitly mention gender in the product description.

vehicles, firearms, and petroleum lubricants). Notably, the scale recovers this gender signal from HS product descriptions alone, without any explicit gender label. This is non-trivial: HS descriptions are written for tariff administration, not consumer profiling, and several high-scoring goods are described in technical language that obscures their end use. HS 2710, for instance, describes petroleum oils and preparations—language that gives no direct indication of gendered consumption—yet the model correctly places it among goods consumed predominantly by men. This suggests that the LLM is drawing on embedded knowledge of consumption patterns rather than surface-level textual cues.

We next replicate the main analysis of Betz et al. (2021) using our new measure. Given our data structure, we adopt a country–product–year unit of analysis and estimate the average tariff rate for each good as a function of the good’s Bradley–Terry estimate and the country-year seat share. We use average tariff rates from the World Bank’s World Integrated Trade Solution (WITS) database (World Bank, 2026). Consistent with our workflow, we take 10 draws from the posterior distribution of each estimate, run 10 models, and aggregate

Table 1: Top 20 non-labeled goods by BT score

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

results using Rubin’s rules. We standardize all covariates to ease interpretation and drop the top 5% of tariff rates to reduce the influence of outliers.

Table 3: Gendered Consumption and Average Tariff Level (Robustness: Dropping Top 5% Outliers)

```text
Pink  Simple  Full
Gender Score  1.149*** (0.032) 1.149*** (0.032)  1.160*** (0.032)
Ln(Female Seats)  0.261*** (0.021) 0.228*** (0.021)  0.255*** (0.023)
Ln(Female Seats)  0.211*** (0.014)  0.255*** (0.017)
```

x Gender Score GDP Growth  -0.035*** (0.005) GDP per Capita  0.118*** (0.035) Female Labor Force  0.120** (0.060)

```text
Observations  1,137,094  1,137,094  1,085,893
R-squared  0.028  0.029  0.030
```

Standard errors clustered by country-product. * p<0.1, ** p<0.05, *** p<0.01 Coefficients and SEs reflect aggregation from 10 draws of the BT scores.

Tariffs above the 95th percentile dropped. Country and Year Fixed effects included.

Table 4: Regression Results (Excluding Goods with Explicit Gender Labels)

```text
Pink  Simple  Full
Gender Score  0.952*** (0.062) 0.951*** (0.061)  0.949*** (0.059)
Ln(Female Seats)  0.273*** (0.023) 0.277*** (0.023)  0.326*** (0.025)
Ln(Female Seats)  0.109*** (0.023)  0.154*** (0.027)
```

x Gender Score GDP Growth  -0.024*** (0.006) GDP per Capita  0.362*** (0.034) Female Labor Force  0.008 (0.063)

```text
Observations  984,554  984,554  940,554
R-squared  0.013  0.013  0.014
```

Standard errors clustered by country-product. * p<0.1, ** p<0.05, *** p<0.01 Coefficients and SEs reflect aggregation from 10 draws of the BT scores.

Sample excludes all goods with gender term flag = 1. Tariffs above the 95th percentile dropped. Country and Year Fixed effects included.

Model 1 of Table 3 replicates evidence of a pink tax across the full range of consumption items. We find a positive and statistically significant relationship: a one-standard-deviation increase in the Bradley–Terry score is associated with a 1.15% increase in the average tariff rate. Models 2 and 3 estimate the conditional effect. Here, we find the opposite pattern from Betz et al. (2021): tariffs on women’s goods increase with the share of legislative seats held by women. We follow up in Table 4 by replicating the analysis while excluding goods that explicitly mention gender in the product description. Even when excluding these goods, the pink tax remains apparent, and the coefficient is only slightly diminished. Thus, tariff bias extends beyond the subset of goods used by Betz et al. (2021), demonstrating the value of examining a wide range of goods.

### Conclusion

Trade data are rich in detail. Yet existing classification schemes limit how researchers can leverage that detail to analyze trade policy and trade flows. Here, we propose that LLMs can help researchers understand relationships among traded goods along researcher-defined dimensions. Our approach improves our understanding of how these dimensions respond to external stimuli. As we show, it also helps clarify how the nature of a good may influence its treatment in trade policy.

Using pairwise comparisons, we leverage the embedded knowledge in LLMs to scale goods along multiple dimensions in a way that preserves uncertainty while allowing for nuanced differentiation. Despite their promise, LLMs are a new technology, and their outputs are produced by a black-box process. Researchers should validate pairwise comparisons with expert human coders where possible. While prior work suggests that LLMs can exceed the performance of crowdsourced workers on classification tasks (Gilardi et al., 2023), it remains unclear whether LLMs can match human raters across all domains and concepts.

### References

Autor, David , David Dorn, Gordon Hanson, and Kaveh Majlesi (2020). Importing political polarization? the electoral consequences of rising trade exposure. American Economic Review 110 (10), 3139–3183.

Betz, Timm , David Fortunato, and Diana Z O’brien (2021). Women’s descriptive representation and gendered import tax discrimination. American Political Science Review 115 (1), 307–315.

Blackwell, Matthew , James Honaker, and Gary King (2017). A unified approach to measurement error and missing data: overview and applications. Sociological Methods & Research 46 (3), 303–341.

Bown, Chad P. and Meredith A. Crowley (2007). Trade deflection and trade depression. Journal of International Economics 72 (1), 176–201.

Buckmann, Marcus , Quynh Anh Nguyen, and Edward Hill (2025). Revealing economic facts: Llms know more than they say. arXiv preprint arXiv:2505.08662 .

Carlson, David and Jacob M Montgomery (2017). A pairwise comparison framework for fast, flexible, and reliable human coding of political texts. American Political Science Review 111 (4), 835–843.

Davidson, Roger R (1970). On extending the bradley-terry model to accommodate ties in paired comparison experiments. Journal of the American Statistical Association 65 (329), 317–328.

DiGiuseppe, Matthew and Michael Flynn (2026). Scaling open-ended survey responses using llm-paired comparisons.

Fajgelbaum, Pablo D and Amit K Khandelwal (2022). The economic impacts of the us–china trade war. Annual Review of Economics 14 (1), 205–228.

Gilardi, F. , M. Alizadeh, and M. Kubli (2023). Chatgpt outperforms crowd workers for textannotation tasks. Proceedings of the National Academy of Sciences 120 (30), e2305016120.

Issa Mattos, David and ´Erika Martins Silva Ramos (2022). Bayesian paired comparison with the bpcs package. Behavior Research Methods 54 (4), 2025–2045.

Kim, In Song (2017). Political cleavages within industry: Firm-level lobbying for trade liberalization. American Political Science Review 111 (1), 1–20.

Kim, In Song , Steven Liao, and Kosuke Imai (2020). Measuring trade profile with granular product-level data. American Journal of Political Science 64 (1), 102–117.

Kim, In Song , John Londregan, and Marc Ratkovic (2019). The effects of political institutions on the extensive and intensive margins of trade. International Organization 73 (4), 755–792.

Liao, Steven , In Song Kim, Sayumi Miyano, and Hao Zhang (2020). concordance: Product Concordance. R package version 2.0.0.

Licht, Hauke , Rupak Sarkar, Patrick Y Wu, Pranav Goel, Niklas Stoehr, Elliott Ash, and Alexander Miserlis Hoyle (2025). Measuring scalar constructs in social science with llms. arXiv preprint arXiv:2509.03116 .

Marra de Arti˜nano, Ignacio , Franco Riottini Depetris, and Christian Volpe Martincus (2025). Automatic product classification in international trade: Machine learning and large language models. Review of International Economics.

Rubin, Donald B (2004). Multiple imputation for nonresponse in surveys, Volume 81. John Wiley & Sons.

Wellhausen, Rachel L (2025). Tariffs as environmental protection: Evidence from the global south after the china garbage shock. British Journal of Political Science 55, e160.

World Bank (2026). World integrated trade solution (WITS) - TRAINS database. urlhttps://wits.worldbank.org/. Accessed: 2026-01-21.

### Notes

[^1]: The method we propose here produces results that are extremely similar to the default results produced by alternative packages like the bpcs package. Users should note that while the general rankings between the two approaches are very similar, the specific estimates for the individual items, as well as the range of estimates, may differ. Much of this variation is attributable to the differences in the default priors used by the two packages. Tests of sample data provided by the bpcs package yield results correlated > 0.99 between the two approaches.
[^2]: Sampling used four chains with 2,000 iterations per chain (1,000 warmup), yielding 4,000 retained posterior draws.
