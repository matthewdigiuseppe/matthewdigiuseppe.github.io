---
title: "Ad Machina: Partisanship and Support for Delegating Government Decisions to Autonomous Algorithms"
authors: ["Matthew DiGiuseppe", "Katrin Paula", "Tobias Rommel"]
year: 2025
status: "Working paper (under review)"
topics: ["AI & Politics"]
url: "https://www.matthewdigiuseppe.com/papers/ad-machina-partisanship-support-delegating.md"
links: {"Preprint on OSF": "https://osf.io/preprints/socarxiv/rnj5h_v2"}
full_text: true
---

# Ad Machina: Partisanship and Support for Delegating Government Decisions to Autonomous Algorithms

DiGiuseppe, M., Paula, K., & Rommel, T. (2025). Ad Machina: Partisanship and Support for Delegating Government Decisions to Autonomous Algorithms.

- Status: Working paper (under review)
- Topics: AI & Politics
- Preprint on OSF: https://osf.io/preprints/socarxiv/rnj5h_v2
- Listed on: https://www.matthewdigiuseppe.com/#research

<!-- END OF GENERATED HEADER: edit freely below this line; scripts/build_agent_files.py keeps it -->

## Abstract

Under which conditions are citizens willing to delegate government responsibilities to artificial intelligence? We hypothesize that the identity of incumbent policymakers impacts public support for delegating decisions to AI. In highly polarized societies, AI has the potential to be perceived as a decision maker with apolitical or less partisan motivations in governance decisions. We thus reason that individuals will prefer co-partisans to AI or algorithmic decision making. However, a switch to AI decision making will have more public support when out-partisans hold policy control. To test our hypothesis, we fielded a survey experiment in the summer of 2024 that asked about 2500 respondents in the US to register their support for AI making the most important economic decision in the world -- the setting of the base interest rate by the US Federal Reserve. The basis of our experimental treatments is the fact that Jerome Powell, the current chair of the Fed, was appointed first by President Trump, a Republican, and later re-appointed by President Biden, a Democrat. We find that when we inform respondents that Powell was appointed by a president from another party, support for delegation to AI increases compared to the condition when the Fed chair is appointed by a co-partisan. The complier average causal effect (CACE) indicates that change perception of the Fed Chair to an outpartisan increases support for delegating to AI by over 45%.

## Full text

> Extracted automatically from the preprint dated July 3, 2025: https://osf.io/preprints/socarxiv/rnj5h_v2. Tables, figures and equations may be garbled or missing; quote the PDF, not this text.

**Ad Machina: Partisanship and Support for Delegating Government Decisions to Autonomous Algorithms**

Matthew DiGiuseppe* · Katrin Paula

Leiden University · Technical University of Munich

Tobias Rommel

Technical University of Munich

July 3, 2025

Abstract Under which conditions are citizens willing to delegate government responsibilities to artificial intelligence? We hypothesize that the identity of incumbent policymakers impacts public support for delegating decisions to AI. In highly polarized societies, AI has the potential to be perceived as a decision maker with apolitical or less partisan motivations in governance decisions. We thus reason that individuals will prefer co-partisans to AI or algorithmic decision making. However, a switch to AI decision making will have more public support when out-partisans hold policy control. To test our hypothesis, we fielded a survey experiment in the summer of 2024 that asked about 2500 respondents in the US to register their support for AI making the most important economic decision in the world – the setting of the base interest rate by the US Federal Reserve. The basis of our experimental treatments is the fact that Jerome Powell, the current chair of the Fed, was appointed first by President Trump, a Republican, and later re-appointed by President Biden, a Democrat. We find that when we inform respondents that Powell was appointed by a president from another party, support for delegation to AI increases compared to the condition when the Fed chair is appointed by a co-partisan. The complier average causal effect (CACE) indicates that change perception of the Fed Chair to an outpartisan increases support for delegating to AI by over 45%.

*Corresponding author: [email removed]

On January 23, 2025, just days after taking office, Mr. Trump issued an executive order, which aims at promoting artificial intelligence (AI) and removing regulatory constraints that might limit its usability.[^1] This executive action marks a sharp reversal from former President Biden’s policy[^2] and now prioritizes technological acceleration over data privacy and civil liberties (Shepardson, 2025). In light of this new way of governing technological advances, the administration quickly moved to expand its use of generative AI in decision-making processes regarding critical state infrastructure, such as employment in federal agencies or disbursement of benefits by the Social Security Administration. While these rapid developments in the US are undoubtedly extreme, they still resemble a broader trend in which governments more and more frequently employ AI for core administrative functions (Raviv, 2025; Taeihagh, 2021; Wuttke, Rauchfleisch, and Jungherr, 2025). Yet, delegating political authority to artificial intelligence systems presents a fundamental challenge to democratic governance and raises critical political questions about public support: under what conditions do citizens accept AI as an authoritative decision-maker relative to humans?

Delegation is a core feature of democratic governance, where citizens routinely transfer authority to elected officials and, in some cases, to independent experts (Beiser-McGrath et al., 2022; Bertsou, 2022). However, delegating authority to algorithms raises distinct accountability concerns, as algorithmic systems lack direct mechanisms for public oversight. Unlike elected representatives, AI systems offer limited transparency and recourse, especially when decisions produce adverse outcomes (McKernan and Davies, 2024; Sambhav, Sambhav, and Joshi, 2024). Moreover, delegating collective decision-making to AI differs fundamentally from private-sector applications, as it involves collective and binding choices that affect large parts of the population (Burgess, 2022). Delegating inherently political decisions to algorithms is thus not only a technical matter of efficiency (Lemke, Trein, and Varone, 2024), but a political act shaped by trust, accountability, and perceptions of legitimacy.

Prior research identifies several factors that have been found to shape support for AI-based decision-making, including greater knowledge, prior dispositions,and familiarity with AI (Horowitz and Kahn, 2024; Dietvorst, Simmons, and Massey, 2018; Zhang and Dafoe, 2019; Zhang, 2023). Delegating to algorithms is more likely when AI assists rather replaces human decision-makers and when it is used for collective rather than individual decisions (Raviv, 2025). Support is also higher when perceived risks of adverse consequences are low, when it is expected to outperform humans, and when algorithmic biases are disclosed transparently (Waggoner et al., 2019; Kennedy, Waggoner, and Ward, 2022; Schiff et al., 2025). In sum, scholars find that citizens’ willingness to delegate to AI depends on both individual-level characteristics, task-specific attributes, and the nature of the AI system. Importantly, existing research that investigates the role of AI as a policy-maker tends to focus on issues of subsidiary governance – such as AI use in food stamp allocation, police patrol deployment, and bail eligibility (Margalit and Raviv, 2023; Raviv, 2025) – largely without considering the political identity of the human decision-maker that AI is supposed to replace. How citizens evaluate AI as an authoritative alternative to partisan decision-makers is thus an underexplored topic in the growing literature on AI governance, which our article aims to fill.

We argue that public support for delegating key policy decisions to AI depends not only on individual factors and perceptions of the technology itself, but also on the identity of the incumbent human decision-maker. Social identity theory suggests that an essential feature of human behavior is that individuals classify others into in-groups and out-groups (Tajfel, 1970; Tajfel and Turner, 1979; Tajfel, 1981). Because individuals favor the former and distrust the latter, these trust differentials manifest in distinctions between groups (Brewer, 2008; Foddy, Platow, and Yamagishi, 2009; Platow et al., 2012). When facing complex and consequential decisions, individuals should thus be especially skeptical of actors they perceive as misaligned with their interests – such as members of the out-group. Affective polarization, defined as “the tendency for partisans to dislike and distrust those from the other party” (Druckman et al., 2021, 28), is rooted in this logic (Iyengar, Sood, and Lelkes, 2012). Partisanship is a particularly salient and stable form of group identity, formed early in life and reinforced through recurrent election cycles and political campaigns (Iyengar et al., 2019).

The status quo of delegated decision-making in democracies is shaped by group identities, which likely revolve around the issue of partisanship. Along these lines, empirical studies consistently show that co-partisanship enhances trust in institutions and authorities (Keele, 2005; Jacob and Schenke, 2020; Yasun, 2023), while out-partisan control is associated with fears of misrepresentation and policy bias. Consequently, citizens tend to accept co-partisan decision-makers but reject out-partisans. Our argument introduces AI as a third actor in this delegation game. While AI may be perceived as a neutral or depoliticized alternative, delegating complex decisions to algorithms likely triggers skepticism rooted in uncertainty and accountability concerns. This phenomenon, known as algorithmic aversion (Mahmud et al., 2022), suggests that citizens may be reluctant to abandon the familiar partisan status quo in favor of a novel, non-human authority. However, citizen should be more willing to accept AI-based governance when the human status quo is associated with an opposing party, meaning affective polarization outweighs algorithmic aversion. In such cases, algorithmic systems – despite concerns over transparency or accountability – may be perceived as the lesser evil: a politically more neutral actor in an otherwise partisan contest.

We test this argument in a unique vignette experiment embedded in a survey of about 2,500 respondents, which we fielded in the United States in August 2024. Instead of investigating hypothetical delegation decisions, we focus on a concrete proposal which is at the same time politically contested as well as collectively binding for all: people’s preferences over who should set the Federal Reserve’s interest rate – a consequential, technically complex, and politically salient decision. Respondents were randomly assigned to experimental conditions in which we gauge whether respondents preferred either an autonomous AI system or the current Federal Reserve Chair, Jerome Powell, to make a decision about the level of the interest rate. As part of our experiment, we manipulated perceptions about Powell’s partisan affiliation, leveraging the fact that he was first appointed by President Trump (a Republican) and later reappointed by President Biden (a Democrat). This setting allows us to identify the causal effect of perceived co-partisan versus out-partisan policy control on support for algorithmic delegation, which relates to our two main, pre-registered hypotheses:

Hypothesis 1. Informing respondents that Jerome Powell was appointed by a president aligned with the respondent’s party preference decreases support for AI delegation compared to those not given this information.

Hypothesis 2. Informing respondents that Jerome Powell was appointed by a president contrary to the respondent’s party preference increases support for AI delegation compared to those not given this information.

Interest rate setting in the US is done by an independent agency, the Federal Reserve, and serves as an influential and suitable case due to the Fed’s global monetary influence and the country’s intense partisan polarization. Interest rate decisions are complex and often poorly understood by the public, yet they remain highly contested because of their significant economic impact. Our study examines whom the public trusts to make and delegate authority over these critical decisions.

Our findings corroborate the striking pattern outlined in these hypotheses: citizens exhibit greater support for AI when the human alternative is affiliated with their political out-group. Among respondents whose perception of Powell’s partisan alignment shifted due to treatment, support for AI increased substantially. The complier average causal effect (CACE) amounts to about 60% of a standard deviation in support for AI delegation – an effect driven entirely by cases in which the Fed Chair was identified as an out-partisan. In contrast, citizens prefer human decision-making when the incumbent is a co-partisan.

These findings contribute to ongoing debates about the legitimacy of algorithmic governance. Prior research shows that citizens are generally skeptical of delegating authority to machines Mahmud et al. (2022), especially in high-risk (Filiz et al., 2023) and morally sensitive domains (Bigman and Gray, 2018). However, our results highlight the conditional nature of this skepticism. When algorithmic decision-makers are compared not to idealized humans but to real-world political actors, especially those from the opposing party, AI can gain substantial support as a supposedly depoliticized alternative. This pattern reflects a deeper logic of partisan identity: in contexts where citizens deeply distrust out-party elites, even opaque alternatives may appear preferable.

Our study also extends existing work in four important ways: First, while previous research typically assesses the abstract support for AI in governance, we focus on a real, concrete, and high-impact policy decision that is already characterized by the frequent use of algorithmic tools through the analysis of vast amounts of quantitative and qualitative data. In addition to its economic importance, interest rate-setting by the Fed resembles a policy that has already been delegated to a nominally independent institution, which arguably reduces partisan bias of its decisions. This makes this case a particularly credible example, given that partisanship should be rather hard to manipulate.

Second, we situate AI within a decision-making context to isolate the effects of algorithm aversion and affective polarization. By presenting respondents with the real-world status quo of interest rate setting in the US, we examine public support for algorithmic governance in a context where expert-driven, depoliticized decision-making should be economically justified, despite politicians still finding ways to circumvent supposedly independent expert decisions (Aklin and Kern, 2021). Since this case involves collective benefits rather than sanctions, it also aligns with typologies predicting comparatively higher public acceptance of AI (Raviv, 2025). Hence, we test algorithmic delegation under conditions, which are generally favorable to public support of AI. In that sense, AI must not only overcome intrinsic skepticism but also be perceived as superior to the current system, in which the leadership position of the decision-making authority is filled by political appointment.

Third, most research on AI delegation focuses on business and healthcare, with limited attention to public attitudes toward AI in nationwide policy decisions. Few existing studies on economic policy, such as tax audits or food stamp allocation, are largely local and may not generalize to broader policy contexts; and the delegation of authority more generally. Our study addresses this gap by examining the willingness to delegate a policy with nationwide impact, rather than discrete algorithmic tasks with unclear systemic consequences.

Finally, focusing on the Federal Reserve offers a key methodological advantage: it allows us to experimentally manipulate partisanship and test its influence on the willingness to delegate authority without deceiving survey participants. The unique position of Jerome Powell, appointed by Republican President Trump and reappointed by Democratic President Biden, provides a rare instance of real-world variation in the perceived partisan identity of incumbent the decision-maker, which our study leverages. Taken together, these innovations underpin our central finding: Especially in polarized societies, where partisanship colors perceptions of authority, AI may emerge as an unlikely beneficiary; not because it is universally trusted, but because it is sometimes distrusted less.

### Design and Results

#### Experimental Design and Sample

We fielded a survey on attitudes towards AI on the Prolific platform in August of 2024. Prolific offers both convenience samples and quota samples, drawing from their pool of respondents. Our sample is the latter and is reflective of the US population along the dimensions of age, gender, and partisanship. To satisfy power requirements, we recruited a sample of 2,500 respondents in total. As part of this survey, we embedded a vignette survey experiment, which is the central pillar of the following empirical analysis.

After an introductory module that asks respondents a number of socio-demographics (age, gender, education, income, military service, state of residency) and political variables (partisanship, importance of US hegemony, and self-assessment of knowledge about the Fed), we start our experiment by presenting each respondent with the following scenario:

“The Federal Reserve, the central bank of the United States, utilizes detailed and complex economic data to determine interest rates. These rates play a pivotal role in influencing the economic well-being of Americans. They affect various financial aspects, including the interest earned on savings, the cost associated with mortgages, car loans, and the interest rates on credit cards. Furthermore, these rates influence the cost of borrowing, which in turn impacts employment levels. Generally, higher interest rates can lead to increased unemployment, whereas lower rates may encourage companies to hire more, thus boosting job creation. It is clear that the Federal Reserve has tremendous power over the US economy. It also has a high degree of independence.”

We then proceed by randomly assigning respondents to one of three distinct groups that receive additional text as well as an image of Jerome Powell. The text of treatment conditions is as follows:

- Control Group The current Fed Chair is Jerome Powell. He will serve until 2026. Until then, he cannot be removed by Congress, the President or the Supreme Court for decisions over interest rates.

- Republican Appointment Treatment The current Fed Chair is Jerome Powell. He was appointed by former President Trump in 2018 and will serve until 2026. Until then, he cannot be removed by Congress, the President or the Supreme Court for decisions over interest rates.

- Democratic Appointment Treatment The current Fed Chair is Jerome Powell. He was reappointed by President Biden in 2022 and will serve until 2026. Until then, he cannot be removed by Congress, the President or the Supreme Court for decisions over interest rates.

Each treatment text is presented alongside an image of Jerome Powell standing at a lectern (Figure 1) either presenting Jerome Powell alone (for the control group) or with the respective President standing in the background (for the two partisan treatments).[^3] Our aim is to visually reinforce the relationship between the policy goals of the President and the Fed Chair. All images are real and we aimed for increasing their similarity.

```text
(a) Control  (b) Republican Alignment  (c) Democratic Alignment
```

Figure 1: Images in the Experimental Conditions.

#### Pre-treatment Questions

In order to distinguish co-partisan and out-partisan identities, we rely on a pre-treatment question, in which we measure party identification on a 7-value scale (ranging from staunch Republican to staunch Democrat). We code respondents’ own partisanship by including those who identify as a party supporter.[^4] We exclude independents - those who select ‘neither’ or ‘other’ in the party identification question. Relating self-reported party identification to the above experimental conditions, we are thus able to code whether a respondent received a co-partisan or out-partisan treatment.

Beyond party identification, we measured several variable pre-treatment to both explore moderating variables and to increase the precision of our estimates. Notably, we coded general willingness to use AI with a series of questions regarding use of AI in the identification of who is at risk of various diseases, in the use of autonomous lethal weapons in the battlefield, job selection and promotion of local officials, and the surveillance of national security threats. Each outcome presents a 4-point scale from ‘very unsupportive’ to ‘very supportive’. We create an aggregate index with the responses to these questions and include it on the right hand side of all models.[^5] In addition, we also measure familiarity with AI.[^6]

#### Outcome Variables

Following the presentation of the vignette, we ask several questions that will serve as our outcome variables. We ask respondents to answer three outcome variables (in the following order). Our first question anchors respondents in the simple costs and benefits of delegating to an AI. It begins with the following piece of information: Experts debate whether to use computer algorithms and artificial intelligence (AI) to set interest rates. Advocates believe it could reduce human biases and errors by focusing on maintaining low inflation and unemployment. Opponents worry about the lack of transparency of AI-based decisions. AI decision-making can be an unclear process and operate like a ‘black box’. We then ask: We are curious what you think of this proposal? On a scale of 0-10, would you support or oppose delegating decisions over interest rates to a well tested artificial intelligence (AI)? The 11-point scale ranges from ‘extremely unsupportive’ to ‘extremely supportive’.

We then ask respondents to indicate how much they trust an interest rate set by several actors, each on a 5-point scale (ranging from ‘completely distrust’ to ‘completely trust’). The actors include (1) ‘A well-tested AI program’, (2) ‘Jerome Powell and the Fed Board’, and (3) ‘The President.’ We use the first question regarding the AI as our second outcome.

The final question asks respondents to make a clear choice between an AI or the current human decision makers at the Fed (Chair and Board): If you had to choose, who would you rather be responsible for setting interest rates: Jerome Powell and the Federal Reserve Board of Governors OR A well tested artificial intelligence (AI) program?

Figure 2 presents the distribution of each outcome regardless of the treatment condition. It is clear that there is little enthusiasm for delegating interest rate setting to an AI. However, we do not see a unanimous opposition either. About 30% of respondents prefer AI to the Fed Chair and Board and the modal category on the trust outcome is 4. Notably, we report in the SA that the mean trust in AI is lower than trust in Jerome Powell but greater than trust in the President to set interest rates.[^7]

#### Estimates

We begin our analysis by examining the effect of our treatments on a respondent choice between Jerome Powell and a well-trained AI in setting interest rates. In each case we estimate the effect of the treatments on the outcomes with ordinary least squares.

The top panel in Figure 3 presents the intention to treat effect (ITT) of the out-party

Figure 2: Dependent Variable Distributions: Each plot shows the distribution of one of the three dependent variables with standard errors.

treatment with either the the co-party treatment (top) or the control group (bottom) when using the binary choice outcome. The choice of AI over Powell increases regardless of the control condition. The difference between the co-party and out-party treatments amounts to a 15% change in support. Against the control, the co-party treatment decreases support for AI by 6% and the out-party treatment increases support by 8%.

As we see in the bottom panel of Figure 4, less than 60% of our respondents see Jerome Powell as aligned with a political party. Thus, it is clear our treatment, though effective, is only effective for a proportion of our respondents. Further, with any online sample, there is a risk that respondents are inattentive. To address both concerns, we also estimate the Complier Average Casual Effect (CACE) with two stage least squares (Blair, Coppock, and Humphreys, 2023). Toward this end, we use our treatment as an instrument to examine how perceptions of Jerome Powell as a co-partisan or aligned with the opposing party influence support for delegation in what is essentially an encouragement design. We use the same outcome presented in Figure 4 to capture if a respondent complied with the treatment

Figure 3: Choice AI or Fed Chair: Panel (a) plots the ITT of the co-party and out-party treatments relative to the baseline from two linear probability models predicting choice of the decision maker (AI vs. Jerome Powell). Panel (b) plots the CACE from four two-stage least squares models. Each coefficient indicates the effect or recalling the treatment in a comparison with just one other treatment group. The corresponding treatments serve as the instrument. The dots represent the ITT and the bars the 95% confidence intervals around the estimate.

(meaning they changed their perception of Powell to either a co-partisan or an out-partisan). The top panels in Figure 4 shows the result linear probability models indicating that the treatment strongly influences the perception of Jerome Powell’s partisanship. As such the first stage of the model predicts the probability of identifying Powell as a member of the out-party or co-party as a function of the treatment conditions and covariates. The second stage then uses this estimated value as a predictor in a model estimating the choice of decision maker.

The bottom panel of Figure 3 presents the CACE estimates. To make the equation tractable, we only include 2 of the 3 treatment conditions in each estimation. For example,

Figure 4: Manipulation Check: The top left and right panels present the ATE of our treatments (reference control group) on the probability of identifying Jerome Powell as aligned with Democratic or Republican policy preferences from linear probability models. The baseline condition in each case pool the other two categories. The bottom panel shows the distribution of all responses to this underlying question. N=1568.

in the first model, we estimate the effect of identifying Powell as an out-party member by instrumenting it with the out party treatment and excluding the observations that received the co-party treatment. The other models vary which condition is dropped and what condition is used as the ‘treatment’. Consistent with the ITT, the CACE shows that among those that received the treatment, support for AI decreases under the co-partisan treatment and increases with the out party treatment. The effect sizes are considerable, hovering around 44-62% change in support for an AI setting interest rate.

Figure 5 present the ITT and CACE for the alternative dependent variables (10-point AI support and trust in AI as a decision maker). The two ordinal outcomes are standardized. As such, these coefficients in these models represent the effect on the treatment in terms of a percentage of a standard deviation in the outcome variables. With these measures, we see inconsistent results with the co-party treatment. The ITT and CACE is insignificant

Figure 5: Alternative Outcomes: Panel (a) plots the ITT of the co-party and out-party treatments relative to the baseline from two linear probability models predicting choice of the decision maker (AI vs. Jerome Powell). Panel (b) plots the CACE from four two-stage least squares models each coefficient indicates the effect or recalling the treatment in a comparison with just one other treatment group. The corresponding treatments serve as the instrument. The dots represent the ITT and the bars the 95% confidence intervals. N=1568 against the control group. The out-party treatment, in contrast, is significant in all estimates, regardless of the control group. the intent to treat effect is between d=0.1 and d=0.2. When we estimate the effect of receiving the treatment, the effect size, again, increases dramatically. Notably, trust in an AI to set interest rate increases by almost a standard deviation among those that received the treatment relative to the control group.

### Discussion

Our results are suggestive of the idea that our distrust of each other may ease the path to governance by artificial intelligence. Utilizing a rare case of co-partisan appointment of the same actor, we show that altering perceptions of the decision maker’s political affiliation has large effects on the public’s support for delegating a decision to AI. Delegation to AI, like many aspects of political life, is subject to the influence of political polarization.

The results show that partisans often prefer AI to incumbent out-partisans and also demonstrate a preference for co-partisans over AI. Practically, situations where a political actors has the opportunity to replace an out-partisan with AI and not a co-partisan are rare. Yet, there are several instances, we think the preference for AI over out-partisans might be relevant. First, this may occur in situations where an party expects to lose decision making authority and has the opportunity to lock in future decision making. Second, delegation may be preferred when compromise between parties is necessary for an appointment. If actors of suspicious of co-partisans and independent actors, AI might emerge as a preferred choice. The logic of delegation here is similar to the delegation to technocrats and independent authorities (de Figueiredo, 2002; Epstein and O’Halloran, 1996; Huber and Shipan, 2002). We avoided hypotheticals in our design. However, future research can test if AI support is greatest in these scenarios and examine if actual delegation decisions are more likely in these scenarios.

### References

Aklin, Michael, and Andreas Kern. 2021. “The Side Effects of Central Bank Independence.” American Journal of Political Science 65 (4): 971–987.

Beiser-McGrath, Liam, Robert Huber, Thomas Bernauer, and Valli Koubi. 2022. “Parliament, People or Technocrats? Explaining Mass Public Preferences on Delegation of Policymaking Authority.” Comparative Political Studies 55 (4): 527–554.

Bertsou, Eri. 2022. “Bring in the Experts? Citizen Preferences for Independent Experts in Political Decision-Making Processes.” European Journal of Political Science 61 (1): 255–267.

Bigman, Yochanan, and Kurt Gray. 2018. “People are averse to machines making moral decisions.” Cognition 181: 21–34.

Blair, Graeme, Alexander Coppock, and Macartan Humphreys. 2023. Research design in the social sciences: declaration, diagnosis, and redesign. Princeton University Press.

Brewer, Marilynn B. 2008. “Depersonalized Trust and Ingroup Cooperation.” In Rationality and Social Responsibility: Essays in Honor of Robyn Mason Dawes, ed. Joachim I. Krueger. Psychology Press pp. 215–232.

Burgess, Paul. 2022. “Algorithmic Augmentation of Democracy: Considering whether Technology Can Enhance the Concepts of Democracy and the Rule of Law through Four Hypotheticals.” AI Society 37: 97–112.

de Figueiredo, Rui J. P. 2002. “Electoral Competition, Political Uncertainty, and Policy Insulation.” American Political Science Review 96 (2): 321–333.

Dietvorst, Berkeley J., Joseph P. Simmons, and Cade Massey. 2018. “Overcoming algorithm aversion: People will use imperfect algorithms if they can (even slightly) modify them.” Management Science 64 (3): 1155–1170.

Druckman, James N, Samara Klar, Yanna Krupnikov, Matthew Levendusky, and John Barry Ryan. 2021. “Affective Polarization, Local Contexts and Public Opinion in America.” Nature Human Behavior 5: 28–38.

Epstein, David, and Sharyn O’Halloran. 1996. “Divided Government and the Design of Administrative Procedures: A Formal Model and Empirical Test.” The Journal of Politics 58 (2): 373–397.

Filiz, Ibrahim, Jan Ren´e Judek, Marco Lorenz, and Markus Spiwoks. 2023. “The extent of algorithm aversion in decision-making situations with varying gravity.” PLoS ONE 18 (2).

Foddy, Margaret, Michael J. Platow, and Toshio Yamagishi. 2009. “Group-Based Trust in Strangers: The Role of Stereotypes and Expectations.” Psychological Science 20 (4): 419–422.

Horowitz, Michael, and Lauren Kahn. 2024. “Bending the Automation Bias Curve: A Study of Human and AI-Based Decision Making in National Security Contexts.” International Studies Quarterly 68 (2).

Huber, John D., and Charles R. Shipan. 2002. Deliberate Discretion? The Institutional Foundations of Bureaucratic Autonomy. Cambridge Studies in Comparative Politics Cambridge, UK: Cambridge University Press.

Iyengar, Shanto, Gaurav Sood, and Yphtach Lelkes. 2012. “Affect, Not Ideology: A Social Identity Perspective on Polarization.” Public Opinion Quarterly 76 (3): 405–431.

Iyengar, Shanto, Yphtach Lelkes, Matthew Levendusky, Neil Malhotra, and Sean J. Westwood. 2019. “The Origins and Consequences of Affective Polarization in the United States.” Annual Review of Political Science 22: 129–146.

Jacob, Marc, and Greta Schenke. 2020. “Partisanship and institutional trust in Mongolia.” Democratization 27 (4): 605–623.

Keele, Luke. 2005. “The authorities really do matter: Party control and trust in government.” The Journal of Politics 67 (3): 873–886.

Kennedy, Ryan P., Philip D. Waggoner, and Matthew M. Ward. 2022. “Trust in Public Policy Algorithms.” The Journal of Politics 84 (2): 1132–1148.

Lemke, Nicole, Philipp Trein, and Frederic Varone. 2024. “Defining artificial intelligence as a policy problem: A discourse network analysis from Germany.” European Policy Analysis 10 (2): 162–187.

Mahmud, Hasan, A.K.M. Najmul Islam, Syed Ishtiaque Ahmed, and Kari Smolander. 2022. “What influences algorithmic decision-making? A systematic literature review on algorithm aversion.” Technological Forecasting and Social Change 175: 121390.

Margalit, Yotam, and Shir Raviv. 2023. “The Politics of Using AI in Policy Implementation: Evidence from a Field Experiment.” SSRN Electronic Papers (September 15): https: //dx.doi.org/10.2139/ssrn.4573250.

McKernan, Bethan, and Harry Davies. 2024. “‘The Machine Did It Coldly’: Israel used AI to identify 37,000 Hamas targets.” The Guardian (April 3): https://www.theguardian.com/world/2024/apr/03/israel--gaza--ai--database--hamas--airstrikes.

Platow, Michael J., Margaret Foddy, Toshio Yamagishi, Li Lim, and Aurore Chow. 2012. “Two Experimental Tests of Trust in In-group Strangers: The Moderating Role of Common Knowledge of Group Membership.” European Journal of Social Psychology 42 (1): 30–35.

Raviv, Shir. 2025. “When Do Citizens Resist The Use of AI Algorithms in Public Policy? Theory and Evidence.” Journal of Politics OnlineFirst.

Sambhav, Tapasya, Kumar Sambhav, and Divij Joshi. 2024. “How an Algorithm Denied Food to Thousands of Poor in India’s Telangana.” Al Jazeera January 24: https://aje.io/6smr2o.

Schiff, Kaylyn Jackson, Daniel S. Schiff, Ian T. Adams, Joshua McCrain, and Scott M. Mourtgos. 2025. “Institutional Factors Driving Citizen Perceptions of AI in Government: Evidence from a Survey Experiment on Policing.” Public Administration Review 85 (2): 451–467.

Shepardson, David. 2025. “Trump Revokes Biden Executive Order on Addressing AI Risks.” Reuters (January 21): https://www.reuters.com/technology/artificial--intelligence/trump--revokes--biden--executive--order--addressing--ai--risks--2025--01--21/.

Taeihagh, Araz. 2021. “Governance and Artificial Intelligence.” Policy and Society 40 (2): 137–157.

Tajfel, Henri. 1970. “Experiments in Intergroup Discrimination.” Scientific American 223 (5): 96–103.

Tajfel, Henri. 1981. Human Groups and Social Categories: Studies in Social Psychology. Cambridge University Press.

Tajfel, Henri, and John C. Turner. 1979. “An Integrative Theory of Intergroup Conflict.” In The Social Psychology of Intergroup Relations, ed. William G. Austin, and Stephen Worchel. Brooks/Cole pp. 33–47.

Waggoner, Philip D., Ryan Kennedy, Hayden Le, and Myriam Shiran. 2019. “Big Data and Trust in Public Policy Automation.” Statistics, Politics and Policy 10 (2): 115–136.

Wuttke, Alexander, Adrian Rauchfleisch, and Andreas Jungherr. 2025. “Artificial Intelligence in Government: Why People Feel They Lose Control.”. URL: https://arxiv.org/abs/2505.01085

Yasun, Salih. 2023. “Co-partisanship with mayors, institutional performance, and citizen trust in local governance institutions: Evidence from Tunisia.” Party Politics 29 (5): 952– 968.

Zhang, Baobao. 2023. “Public Opinion Toward Artificial Intelligence.” In The Oxford Handbook of AI Governance, ed. Justin B. Bullock, Yu-Che Chen, Johannes Himmelreich, Valerie M. Hudson, Anton Korinek, Matthew M. Young, and Baobao Zhang. Oxford: Oxford University Press pp. 553–571.

Zhang, Baobao, and Allan Dafoe. 2019. “Artificial Intelligence: American Attitudes and Trends.” Center for the Governance of AI, Future of Humanity Institute p. University of Oxford.

### Appendix

#### A1 Results by Party

Figure A1: This figure replicates the Analysis above but on samples that are restricted to Democrats

Figure A2: This figure replicates the Analysis above but on samples that are restricted to Republicans

#### A2 Results with “Leaners”

In our main analysis, we presented results in which we defined partisanship as respondents who reported being either strong or weak democrats. In this analysis, we include self reported independents or non-partisans who claim to “lean” toward a party in our definition. Our preanalysis plan was unfortunately imprecise about how we would code partisanship to create our central dependent variable. As such, we report the alternative option here. The magnitude of the effects change a bit when

Figure A3: Choice AI or Fed Chair: Panel (a) plots the ITT of the co-party and out-party treatments relative to the baseline from two linear probability models predicting choice of the decision maker (AI vs. Jerome Powell). Panel (b) plots the CACE from four two-stage least squares models each coefficient indicates the effect or recalling the treatment in a comparison with just one other treatment group. The corresponding treatments serve as the instrument. The dots represent the ITT and the bars the 95% confidence intervals.

Figure A4: Alternative outcomes (Leaners):

#### A3 Trust in AI, Fed, & President

Figure A5: Mean Trust in Setting Interest Rates: The plot shows the mean values for trust in the following actors to set interest rates (Jerome Powell, a well-trained AI, and the President). N=2529

#### A4 Models with LASSO Selection

Figure A6: Choice AI or Fed Chair: Panel (a) plots the ITT of the co-party and out-party treatments relative to the baseline from two linear probability models predicting choice of the decision maker (AI vs. Jerome Powell). Panel (b) plots the CACE from four two-stage least squares models. Each coefficient indicates the effect or recalling the treatment in a comparison with just one other treatment group. The corresponding treatments serve as the instrument. The dots represent the ITT and the bars the 95% confidence intervals around the estimate. Covariates selected by a LASSO estimator are included in the estimation. N=1568.

Figure A7: Alternative Outcomes: Panel (a) plots the ITT of the co-party and out-party treatments relative to the baseline from two linear probability models predicting choice of the decision maker (AI vs. Jerome Powell). Panel (b) plots the CACE from four two-stage least squares models each coefficient indicates the effect or recalling the treatment in a comparison with just one other treatment group. The corresponding treatments serve as the instrument. The dots represent the ITT and the bars the 95% confidence intervals. Covariates selected by a LASSO estimator are included in the estimation. N=1568.

#### A5 Instrumental Variable Analysis

```text
Out- vs.  Co- vs.  Out-Party vs. Co-Party vs.
Co-Party  Out-Party  vs. Control  Control
Out-party Treated  0.435***  0.440**
```

(0.081)  (0.155)

```text
Co-party Treated  −0.624***  −0.496*
```

(0.135)  (0.223)

```text
AI favor.  0.171***  0.178***  0.146***  0.121***
(0.019)  (0.023)  (0.023)  (0.023)
(Intercept)  −0.265***  0.007  −0.205*  0.100
(0.058)  (0.056)  (0.100)  (0.068)
Instrument  Out-Party  Co-Party  Out-Party  Co-Party
Num.Obs.  1039  1039  1045  1052
R2  0.082  −0.260  0.059  −0.249
```

Table A1: 2SLS Analysis with Choice Outcome

* p <0.05, ** p <0.01, *** p <0.001

```text
Out- vs.  Co- vs.  Out-Party vs. Co-Party vs.
Co-Party  Out-Party  vs. Control  Control
Out-party Treated  0.608***  0.676*
```

(0.167)  (0.314)

```text
Co-party Treated  −0.873***  −0.600
```

(0.262)  (0.432)

```text
AI favor.  0.688***  0.697***  0.702***  0.703***
(0.042)  (0.047)  (0.047)  (0.049)
(Intercept)  −1.890*** −1.509***  −1.956***  −1.627***
(0.129)  (0.116)  (0.201)  (0.132)
Instrument  Out-Party  Co-Party  Out-Party  Co-Party
Num.Obs.  1039  1039  1045  1052
R2  0.169  0.011  0.140  0.097
```

Table A2: 2SLS Analysis with Support Outcome

* p <0.05, ** p <0.01, *** p <0.001

```text
Out- vs.  Co- vs.  Out-Party vs. Co-Party vs.
Co-Party Out-Party  vs. Control  Control
Out-party Treated  0.535**  0.920**
```

(0.169)  (0.335)

```text
Co-party Treated  -0.768**  -0.078
```

(0.253)  (0.398)

```text
AI favor.  0.686***  0.695***  0.722***  0.723***
(0.043)  (0.046)  (0.050)  (0.044)
(Intercept)  -1.804***  -1.470***  -2.069***  -1.804***
(0.134)  (0.115)  (0.216)  (0.121)
Instrument  Out-Party  Co-Party  Out-Party  Co-Party
Num.Obs.  1039  1039  1045  1052
R2  0.151  0.072  0.024  0.249
```

Table A3: 2SLS Analysis with Trust Outcome

* p <0.05, ** p <0.01, *** p <0.001

#### A6 Consent Form

We start the survey by asking whether respondents agree to take part in our study. We screen out respondents who do not agree to participate after the following initial text:

Thank you for agreeing to take part in this research study. The data we collect will be used in academic research to help us understand your perspectives on government policies. If you agree to participate in this study, you will be asked to complete an on-line survey that will take about 7 minutes. There are no foreseeable risks associated with this project. However, your participation in this study is completely voluntary and you are free to withdraw at any time. Your survey responses will be strictly confidential and data from this research will be reported only in anonymized form. The data will be stored on a secure server and will be opened only by the researchers when conducting analysis on aggregate data. None of your personal information will be collected. We will preserve your data in perpetuity and protect any confidential data. Anonymized data will be shared with others upon publication of any academic papers resulting from the project. We will use the data to conduct statistical analysis from which we will draw general conclusions. The project will be published in open access format so that individuals that are interested can see the final project. By clicking I agree below you are indicating that you are at least 18 years old, have read and understood this consent form, and agree to participate in the research study. [I agree; I do not agree]

#### A7 Ethics

We received ethical approval from the German Association for Experimental Economic Research e.V. (No. 39cUYan7) on August 23, 2024.

#### A8 Power Analysis

We conducted simulations using Declare Design (Blair, Coppock, and Humphreys, 2023) to inform our sample size. To do so, we assume a total sample of N=2,500 of which only we make a conservative estimate that only 67% have a partisan affiliation. As such, our power analysis considers a sample of N=1,665. With this sample, we simulate the power for each assumed effect size between 0 and 0.5. We find that we have 80% power to detect an effect of d = 0.135 as can be seen in Figure A8.

#### A9 Attention Check

We evaluate respondents’ attention to the question wording before we present the treatments using the following survey item:

People are very busy these days and many do not have time to look up specific pieces of information. There are many websites offering the same content at different levels of detail. Some have the time to search for information all day, but some do not even have the time to read questions carefully. To show that you’ve read this much, please ignore the question

Figure A8: Minimum Detectable Effect, N=2500

Figure A9: Our estimates of the minimum detectable effect are conduced with Declare Design Package in R. We assume a sample of N=2500 and a set of covariates that correlate with the outcome at 0.20. Our estimates of the power rely on 1000 simulations of each value of the average treatment effect (ATE).

below and just click the answer that includes seven. About how many web sites do you visit daily to look up information on current issues? [0; 1-2; 3-5; 6-9; 10 and more]

### Notes

[^1]: https://www.whitehouse.gov/presidential-actions/2025/01/removing-barriers-to-american-leadership-in-artificial-intelligence/.
[^2]: https://www.federalregister.gov/documents/2023/11/01/2023-24283/safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence.
[^3]: Picture sources for Figure 1: (a) Federal Reserve via Flickr, (b) Official White House Photo by Andrea Hanks via Flickr (c) Alex Wong/ Staff via Getty Images.
[^4]: Our pre-registration included ‘leaners’ in this characteristic. As we demonstrate in the SA, the sign and significance of our findings remain regardless of how we code partisanship. However, we opt to present the more strict coding of partisans here in a deviation from our preregistration.
[^5]: We preregistered that we would select covariates agnostically with a LASSO. Given the strong power of the experiment we adopted a simpler approach. Furthermore, this index is always selected by the LASSO algorithm. We present the results of our preregistered analysis in the SA.
[^6]: How often do you use artificial intelligence tools like ChatGPT? [5-point scale, ranging from ‘have never used it’ to ‘daily’]
[^7]: Trust in Powell (3.3), AI (2.8), President (2.4).
