---
title: "Scaling Open-ended Survey Responses Using LLM-Paired Comparisons"
authors: ["Matthew R DiGiuseppe", "Michael E Flynn"]
year: 2026
status: "Published"
venue: "Public Opinion Quarterly, 90(1)"
topics: ["Political Behavior & Policy Preferences"]
doi: "10.1093/poq/nfag013"
url: "https://www.matthewdigiuseppe.com/papers/scaling-open-ended-survey-responses.md"
links: {"PDF on OSF": "https://osf.io/preprints/socarxiv/39ajg_v2"}
full_text: true
---

# Scaling Open-ended Survey Responses Using LLM-Paired Comparisons

DiGiuseppe, M., & Flynn, M.E. (2026). Scaling Open-ended Survey Responses Using LLM-Paired Comparisons. Public Opinion Quarterly, 90(1).

- Status: Published
- Topics: Political Behavior & Policy Preferences
- DOI: https://doi.org/10.1093/poq/nfag013
- PDF on OSF: https://osf.io/preprints/socarxiv/39ajg_v2
- Listed on: https://www.matthewdigiuseppe.com/#research

<!-- END OF GENERATED HEADER: edit freely below this line; scripts/build_agent_files.py keeps it -->

## Abstract

Survey researchers rely heavily on closed-ended questions to measure latent respondent characteristics like knowledge, policy positions, emotions, ideology, and various other traits. Closed-ended questions are easy to analyze and collect, but necessarily limit the depth and variability of responses. Open-ended responses allow for greater depth and variability in responses, but are labor intensive to code. Large language models (LLMs) may help with this problem, but existing approaches to using LLMs have a number of limitations. In this paper, we propose and test a pairwise comparison method to scale open-ended survey responses on a continuous scale. The approach relies on LLMs to make pairwise comparisons of statements that identify which statement “wins” and “loses.” With this information, we employ a Bayesian Bradley-Terry model to recover a “score” on a latent dimension for each statement. This approach allows for finer discrimination between items, reduced anchoring bias, better measurement of uncertainty, and is more flexible than methods relying on Maximum Likelihood Estimation techniques. We demonstrate the utility of this approach on an open-ended question probing knowledge of interest rates in the US economy. A comparison of six LLMs of various sizes reveals that pairwise comparisons show greater consistency than zero-shot 0–10 ratings across a variety of model sizes. Further, comparison of pairwise decisions is consistent with knowledgeable crowdsourced workers.

## Full text

> Extracted automatically from the preprint (the version before journal publication): https://osf.io/preprints/socarxiv/39ajg_v2. Tables, figures and equations may be garbled or missing; quote the PDF, not this text.

**Scaling Open-ended Survey Responses Using LLM-Paired Comparisons**

Matthew DiGiuseppe · Michael Flynn Associate Professor · Professor Leiden University · Kansas State University [email removed] · [email removed] June 24, 2025

Abstract Survey researchers rely heavily on closed-ended questions to measure latent respondent characteristics like knowledge, policy positions, emotions, ideology, and various other traits. Closed-ended questions are easy to analyze and collect, but necessarily limit the depth and variability of responses. Open-ended responses allow for greater depth and variability in responses, but are labor-intensive to code. Large Language Models (LLMs) may help with this problem, but existing approaches to using LLMs have a number of limitations. In this paper, we propose and test a pairwise comparison method to scale open-ended survey responses on a continuous scale. The approach relies on LLMs to make pairwise comparisons of statements that identify which statement “wins” and “loses”. With this information, we employ a Bayesian Bradley-Terry model to recover a ‘score’ on a the relevant latent dimension for each statement. This approach allows for finer discrimination between items, reduced anchoring bias, better measurement of uncertainty, and is more flexible than methods relying on Maximum Likelihood Estimation techniques. We demonstrate the utility of this approach on an open-ended question probing knowledge of interest rates in the US economy. A comparison of six LLMs of various sizes reveals that pairwise comparisons show greater consistency than zero-shot 0-10 ratings across a variety of model sizes. Further, comparison of pairwise decisions is consistent with knowledgeable crowd source workers.[^1]

Public opinion scholars and survey researchers are often interested in the latent traits of individual respondents like political knowledge, literacy, comprehension, engagement, ideology, emotions, and values. Due to convenience, most scholars use closed-ended questions independently or in scales to measure these traits. However, closed-ended responses come with several undesirable properties. They introduce ceiling and floor e!ects. They can also introduce measurement error from false or inadvertent responses, and force an assumption of linearity on scales. Most importantly, they reduce the richness of responses and often introduce concepts that would otherwise be apparent to respondents.

Alternatively, open-ended responses o!er an unstructured and more flexible alternative that allows for in-depth and detailed responses that captures substantive uncertainty and important qualifications. However, open-ended responses have traditionally required costly human coders before they are usable in statistical analysis (Lazarsfeld, 1944; Geer, 1991; Converse, 1984; Haaland et al., 2024; Andre et al., 2024; Roberts et al., 2014). Given a large number of potentially lengthy responses, coding the various dimensions for all respondents can be labor intensive. More often than not, this process also reduces these high-dimension data to linear discrete scales that reintroduce some issues of closed-ended questions.

Advances in text as data methods (Roberts et al., 2014) in the past 10-15 years have opened the door to automated text analysis. These techniques are particularly useful in identifying di!erences in sophistication or word use among groups (Kraft, 2024; Zollinger, 2024). However, they are ill-suited for applications that require background knowledge and the comprehension of concepts embedded in long strings of text. Large Language Models (LLMs) excel in this regard and have the added benefit of prompting via text. Consequently, LLMs have significantly reduced the learning curve for analyzing text and the monetary cost of annotating and scaling open-ended questions (Rathje et al., 2024; Heseltine and Clemm von Hohenberg, 2025; Le Mens and Gallego, 2025). Notably, frontier LLMs have the added benefit of strong domain knowledge often exceeding the abilities of crowd workers or undergraduate research assistants (Gilardi et al., 2023; Bermejo et al., 2024; Ludwig et al., 2024; Ornstein et al., 2025). While LLMs open new possibilities for survey researchers, using LLMs in place of research assistants for scaling responses typically generates unanchored scores, which also lack corresponding estimates of uncertainty. Further, LLMs vary in their output across di!erent LLMs and even di!erent versions of the same LLMs in classification and annotation tasks (Barrie et al., 2024). Accordingly, there remains substantial uncertainty regarding the suitability of LLMs for survey research.

In this paper, we introduce a framework for using LLMs to scale latent dimensions in open-ended responses with pairwise comparisons (PWC) that helps address existing concerns. First, researchers prompt an LLM to make zero-shot, independent comparisons of two random responses and indicate which is more closely aligned with the latent concept, or if they are too similar to distinguish. After collecting N comparisons, researchers use the results of the PWC to fit a Bayesian Bradley-Terry (BT) model to generate a latent variable for respondent knowledge that we then use to scale and rank the individual respondents (Bradley and Terry, 1952; Davidson, 1970). The estimate of this latent dimension and the error surrounding the estimate can then be used in downstream analyses.

Just as in using PWC with human raters (Carlson and Montgomery, 2017), LLM PWCs have several advantages over placement on a scale. Importantly, the approach produces an estimates on a latent scale relative to other observations in the dataset rather than the unanchored responses. Next, because of the large-number of comparisons possible, it is easier to recover an estimate closer to the true parameter, with smaller errors. This subsequently allows researchers to recover more nuanced di!erences among observations. The credible intervals around the latent variable estimates can also be used to incorporate the inherent uncertainty associated with any given observation or measure into subsequent analyses. Additionally, by forcing a binary ordering, rather than a ranking, unobserved biases that do not influence rank order of pairs wash out. As we show below, this approach also allows for the generation of latent estimates even with sparse comparisons, using readily available software, reducing dependence upon customized packages for estimating pairwise comparison models.

Others have demonstrated the utility of using PWC made by crowdsource workers to scale uni-dimensional latent concepts in text (Carlson and Montgomery, 2017). LLMs broaden the applications of this approach. They enable pair-wise comparisons on large datasets (that often exceed N=1,000) that would require thousands of coder-hours. Additionally, frontier LLMs have strong domain knowledge across a variety of subjects—including economics and finance—which we use in our illustration (Yang et al., 2024; Hultberg et al., 2024), enabling researchers to scale tasks that required expert coders.

Notably, Wu et al. (2023a) are the first to identify the utility of pairing LLMs with PWC in the evaluation of sentiment in ‘tweets’ in the context of a chain of thought framework. Our contribution is to demonstrate the utility of this approach within the realm of open-ended survey responses and with zero-shot prompting and validate against a close-to-expert benchmark. We illustrate how PWC can scale ‘interest rate knowledge’ from an original open-ended survey question about how interest rates are determined.

Our application demonstrates the usefulness of the approach and how it performs relative to zero-shot ratings. It also shows that LLMs are useful beyond sentiment analysis and multidimensional classification (Le Mens and Gallego, 2025; Mellon et al., 2024). The embedded domain knowledge in LLMs can be used, in some cases, in place of close-to-expert coders. As such, it allows for scaling of concepts that are outside the reach of students or the average crowd sourced worker.

#### LLMs & Pairwise Comparisons

The utility of using the embedded knowledge in LLMs to annotate, classify, and scale text has been widely demonstrated in a variety of social science fields (Heseltine and Clemm von Hohenberg, 2025; Mellon et al., 2024; Gilardi et al., 2023; T¨ornberg, 2024). Applications are diverse. Mellon et al. (2024) uses LLMs to code the most important problem identified in open-ended responses. A number of studies use LLMs to code the sentiment or other characteristics of tweets, news reports, or other text (Gilardi et al., 2023; T¨ornberg, 2024; Heseltine and Clemm von Hohenberg, 2025; Ornstein et al., 2025; Rathje et al., 2024).

These contributions demonstrate that LLMs often meet or exceed crowd-source workers on annotation and scaling tasks. However, several well-known limitations, that also apply to human-coded data, exist. First, in scaling tasks, the responses of LLMs are unanchored. As such, what di!erentiates the maximum and the minimum values, or various other items on a scale is uncertain. Second, LLMs are black boxes. There is likely unobserved bias that influences scale placement. Third, the LLM generated responses do not produce uncertainty estimates. Consequently, subsequent models cannot discern between di!erences on a scale that are in fact distinct or di!erences that appear distinct but are in fact statistically indistinguishable. Beyond these issues, the enthusiasm for reducing the cost of dimension reduction is further dampened by concerns about replicability between LLM models and within models over time. In a series of tests, Barrie et al. (2024) show that the variance across and within models across time is ‘unacceptably high.’

Given these issues, can survey researchers feel confident in using LLMs to scale open-ended questions? LLMs are likely to improve and grow more consistent, and their biases may become more transparent, but until such time researchers are faced with the task of finding alternative methods for dealing with these issues. Some of the challenges of using existing models can be improved by using LLMs to make pairwise comparisons of text and then using these judgments to generate estimates of the desired latent traits with a BT model.

Pairwise comparison is not new to social science research. They are used to measure political sophistication (Benoit et al., 2019), persuasiveness of political arguments (Loewen et al., 2012), and the dimensions of government actors (Zucco Jr et al., 2019). The approach yields several benefits over traditional scaling techniques. First, it produces a relative assessment of each response. A well-known measurement issue with scaling text is that the responses are unanchored. This means that there is bound to be a lack of clarity on what each value on a scale means relative to the subjective construct the researcher wants to scale. Training coders can partially alleviate this concern but cannot fully resolve it. When using human coders, biases may also emerge from the order of appearance or variability across coders. It is still unclear what problem this poses for LLMs. Conceivably, prompt instructions remain constant across one-shot calls, the actual prompt may change based on the added human written response that is unique to each respondent. As such, it is di”cult to know how this impacts how the LLM places items on a scale across numerous calls. Human coders can eventually converge on an anchor by completing multiple responses assuming that they consistently apply coding rules. For LLMs this convergence is not easily achieved. Each zero-shot or even multiple shot calls relies on a new call of the model which entails a ‘clean slate’ requiring a repetition of instructions. Additionally, if a long chain of thought could be achieved (at increasing cost in input tokens), some worry that LLMs exhibit recency bias (Peysakhovich and Lerer, 2023). Further, e!orts at multi-shot prompting relies on picking examples in an attempt to anchor scaling. Yet, it remains unclear how the choices of these examples impact the final dataset given the opaque nature of LLMs. In sum, the subjectivity inherent in placing items on scale likely generates error that is not directly observable to the researcher.

As Carlson and Montgomery (2017) argue, PWC ameliorates this unobserved bias when using human raters. If one rater tends to rate higher or lower on a scale, this is irrelevant because the forced comparison requires a single cut point. Where on the scale an item is placed is not relevant for the final estimate unless it changes which item “wins” or “loses” a comparison. Similarly, there is concern that LLMs are inconsistent (Barrie et al., 2024) and thus a similar logic should apply. If di!erent LLMs or di!erences in the prompt language (or language within a piped in response) lead to di!erent placement on a scale, this should only be relevant when the separate individual ratings move enough to change the outcome. For example, let us assume that a human coder or an LLM rates a knowledge response higher (lower) because grammar and spelling are flawless (sloppy). This may lead to a higher (lower) score for responses with perfect (flawed) writing. On a 0-10 scale, this might result in real di!erences in responses that have the same knowledge but are presented in di!erent ways. In the PWC framework, this bias is only relevant if results flip the rank ordering, changing the winning response to the a losing response.

The second benefit of the approach is that it naturally incorporates uncertainty into the estimates, allowing us to recognize when observed di!erences may not be statistically meaningful. While some items can be clearly distinguished from others because of real di!erences, in many cases, the di!erence between two statements is ambiguous and should be treated as such. In contrast, a simple rating-based approach may produce distinctions that are seemingly meaningful as a one-point di!erence on a 10-point scale—that downstream models might treat as reliable information. By explicitly incorporating uncertainty into subsequent analyses (Blackwell et al., 2017), the risk of over-interpreting minor di!erences is reduced.

PWCs also make use of fine-grained and nuanced di!erences in a way that are di”cult to implement with a fixed scale. Nuanced di!erences are di”cult to map on a scale without placing large cognitive demands on human raters and potentially exaggerates measurement bias with LLMs (Benoit et al., 2019). Consider the cognitive demands needed to determine the di!erence between 65 and 66 on a 100-point scale without a clear reference point or, from the perspective of a human rate, multiple cases that were coded previously. Then consider the di”culty of determining which statement is “better” than the other even if the di!erence is nuanced. The later is inherently easier and quicker to assess. LLMs, while impressive, may have a similarly hard time making consistent judgments on a large scale given it would be di”cult to have clear instructions for di!erences on a scale that would allow for fine-grained distinctions. By utilizing multiple pairwise comparisons, LLMs, like humans coders, can produce more fine-grained di!erences among observations.

Until recently, PWC has relied on crowd workers, students, or experts. While the benefits of PWC are clear from a measurement perspective (Carlson and Montgomery, 2017), the cost of employing crowd-workers or RAs to engage in numerous comparisons is likely responsible for its infrequent adoption. LLMs easily remedy this concern. Scholars have demonstrated that the embedded knowledge of LLMs is su”cient to carry out these comparisons with significantly lower cost. For example, Wu et al. (2023b) use LLMs comparisons to recreate latent ideology scores of US Senators. Di Leo et al. (2025) use a similar approach to estimate the ideology of European parties. The expertise of LLMs extends beyond political judgments. LLMs have strong knowledge of economic and psychological concepts (Geerling et al., 2023; Rathje et al., 2024).

In sum, LLMs have the embedded knowledge to replace expert coders in classification and scaling tasks. However, they are often used in a way that fails to address the subjectivity of rankings and lacks a measure of corresponding uncertainty. Below, we show that pairwise comparisons o!er a better alternative to scaling approaches and can be done with reasonable costs. We also show where they may fail to produce acceptable data.

#### Pairwise Comparison Work Flow

Figure 1 outlines the workflow to take individual open-ended responses and create estimates to be used in subsequent analyses. After collecting open-ended survey responses, researchers first create pairs of responses. In our analysis, we started with each response and randomly paired it with 20 other responses from the dataset without replacement. Once the pairs have been assigned, researchers must develop a prompt that 1) clearly outlines the task the LLM will perform, 2) provides each of the open ended responses, and 3) requests a response to identify which response best aligns with the concept or if they are indistinguishable. The prompt can then be used in calls to an LLM API or, for smaller models, run locally. Once the LLM returns the judgments, a BT model can be fitted to the responses.

Following the estimation of the BT model, we retrieve the median estimate and the errors. If the researcher is interested in using the estimates in downstream analyses either as an outcome or predictor then the researcher can sample from the posterior distribution and incorporate the sample values into subsequent analyses as needed, thereby allowing the researcher to easily incorporate the uncertainty from the BT models directly into additional models.

```text
Collect responses  comparisons  each pair of
```

```text
Estimate  Retrieve medianscores, standard  Incorporate into
Bradley-Terry  errors, and/or  downstream
(BT) model  full posterior  as neededanalyses
```

Prompt LLM Create pairwise  to compare responses and code winner distribution

Figure 1: Workflow Diagram of the Estimation Process

##### MLE or Bayesian Estimation?

Once we have obtained the paired responses the LLM will make judgments about the domain knowledge contained within each response. The instructions ask the LLM to decide if response #1 wins, if response #2 wins, or if the two responses are equivalent (i.e. a tie). Once we have the scores for each comparison we can then fit a BT model to generate a latent variable capturing the underlying trait the researcher cares about (e.g. knowledge, emotion, etc.).

Traditionally BT models have been fit with Maximum Likelihood Estimation (MLE) methods. Here we adopt an alternative Bayesian framework. While others have utilized Bayesian methods for estimating similar models the approach is not yet widespread (see Carpenter, 2018; Mattos and Ramos, 2022; Kaye and Firth, 2022; van Paridon et al., 2023). The Bayesian approach has several desirable properties relative to traditional MLE approaches. First, MLE methods can be fast, but the researcher’s ability to use MLE rests on the assumption that they have pairwise comparisons for all possible items or responses (Mattos and Ramos, 2022; Kaye and Firth, 2022). Where the researcher does not have pairwise comparisons for every item, MLE methods will fail to converge. Sometimes this is within the researcher’s control, but in many cases this will be out of a researchers reach. The cost of LLM pairwise comparison in money, time, or energy might be prohibitive. For example, in our dataset of 1,400 responses, a pairwise comparison of each response would require almost 2 million comparisons. Using 20 comparisons of each response requires only 28,000 comparisons in contrast.

Further, in cases where the number of items to be ranked is very large, MLE methods may struggle with the computational complexity. Alternatively, while Markov Chain Monte Carlo sampling methods may sometimes run more slowly, they are able to generate estimates of the desired parameters even in cases where there are a large number of items to rank, and where not every item is paired with every other item. However, modern software for fitting Bayesian models, like Stan and its Hamiltonian Monte Carlo sampling procedures, have greatly reduced the time it takes to fit even more complex Bayesian models. Where speed might still be an issue, the choice to reduce the number of comparisons can still save the researcher time, though at the expense of larger errors in the posterior distributions of the latent parameters.

Bayesian approaches also provide us with several options for dealing with the inherent uncertainty associated with the latent estimates derived from the BT models. Packages like brms include functions like me() that can be used to account for measurement error in particular predictors. Alternatively, as we demonstrate below, researchers can simply sample from the posterior distributions of the BT estimates and run multiple iterations of downstream models to directly incorporate the uncertainty into their estimates.

Finally, while there are several R packages that can estimate BT Models, many rely on MLE for estimation, or they may depend upon package maintainers to keep functions updated and working. The approach we outline here demonstrates how researchers can use Stan and brms to estimate BT models as multimembership mixed e!ects models. Depending on the structure of the pairwise comparison data, these models can be estimated using binomial or logistic regression and are generally easy to fit without relying on customized BT packages (for example see Firth, 2005; van Paridon et al., 2023).

We provide a toy example in our supplementary materials that lays out the entire process, in R code, outlined in Figure1.

#### Illustration: Scaling Economic Knowledge

To demonstrate the utility of the approach, we draw on data collected by DiGiuseppe et al. (2024) that measures knowledge about monetary policy. The data, collected on the Prolific platform (N=1,400), prompted respondents with the following question: “In a few sentences and without looking it up, can you explain how interest rates (i.e. the cost of borrowing money to buy a house or car) go up or down in the US economy?” Respondents were asked to reply in 2-3 sentences. One aim of the study was to explore how knowledge about interest rates influences individual assessment of the Federal Reserve and support for its independence. This dataset is useful for our purposes because it collects both open and closed-ended questions relating to knowledge of the Federal Reserve and that assessing these responses is a potentially di”cult task for both human coders and LLMs. Further, the survey used quota sampling to reflect the US population in terms of age, gender, and partisanship.

We carry out this exercise with LLMs of various sizes and a mix of proprietary and open-source models (see Table 1). The use of multiple models is useful for testing the limits of the approach and to compare consistency across models. These models include frontier LLMs (GPT-4o, GPT-4o mini, Llama 3.1 405B), two smaller large language models (Llama 3.1 8b and Google’s Gemma 3 4B) and a mid-sized model (Gemma 3 27B). We use API calls for the OpenAI models and the large Llama 3.1 model. We run the small and mid-sized models locally using OLlama and the the R package roLlama to call on these models locally in the R environment (Gruber and Weber, 2024). We used a higher end commercial laptop, an Apple Macbook with an M3-Pro chip and 36GB of memory, for inference of these models. Other users might struggle to run the 27 Billion parameter model locally. However, these can also be accessed via API at a cost.

Model  Parameters Open Access Proportion Transitivity

```text
Source  Ties  Score
Llama 3.1 405B  405 Billion  Yes  API  0.024  99.06
Gemma 3 27B  27.4 Billion  Yes  Local  0.057  97.42
GPT-4o mini  Unspecified  No  API  0.040  96.98
GPT-4o  Unspecified  No  API  0.008  96.12
Gemma 3 4B  4.3 Billion  Yes  Local  0.021  96.04
Llama 3.1 8B  8 Billion  Yes  Local  0.062  95.95
```

Table 1: Properties of LLMs used in Illustration. We used the following versions of the server accessed models: GPT-4o-mini 2024-07-18, gpt-4o-2024-05-13, Llama-v3p1- 405B-instruct. The Llama 3.1 405B models was accessed via Fireworks.ai API. The OpenAI models were accessed via the OpenAI API.

In line with the workflow we described above, we paired each response with 20 other randomly selected responses, ensuring that responsei →= responsej . This results in approximately 30–40 total comparisons for each response as any given respondent appears 20 times as responsei and anywhere from 7 to 33 times as responsej. In total, this yields a little over 28,000 total comparisons or lines in the data. Following the workflow, we prompt each LLM with the following prompt:

Pairwise Comparison LLM Prompt “You are an expert in US economic policy. Your task is to determine which of two given statements contains a more knowledgeable response to the following question: “In a few sentences and without looking it up, can you explain how interest rates (i.e. the cost of borrowing money to buy a house or car) go up or down in the US economy? Respond with either ‘1’ if the first statement contains more knowledge, ‘2’ if the second statement contains more knowledge, or ‘0’ if they are equal or incomparable. Compare these two statements and respond with “1, 2, or 0:”, 1: [Statement 1], 2: [Statement 2]. Only reply with the integer 1, 2, or 0”

Table 1 shows that there are relatively few ties in most models. This suggests that the LLMs were able to distinguish between most comparisons in the dataset. We next examined the consistency of judgments across triplets where we had judgments for A, B, and C and examined how often there was a violation of transitivity. We see that no model is perfect. Yet, the transitivity scores ( [total triplets ↑ triplets with violations]/[total triplets]) demonstrate strong consistency even among the small and mid-sized models.

Once we have the LLMs’ judgments for these 28,000+ comparisons, we estimate a Bradley–Terry Model for the comparisons of each LLM. The first step is to resolve any ties in the data. Resolving these ties can be handled several ways. Here, we randomly assign wins between the two options.[^2]

Once the ties are resolved we fit a BT model, which estimate the following:

P r(i > j) = pij = ωi ↑ ωj  (1) The data are organized with two columns for respondenti and respondentj wherein the values in each vector correspond to an individual respondent ID number. A third column contains a binary indicator denoting whether respondenti won the comparison, with a 1 indicating yes and a 0 otherwise.

Rather than using a customized package to estimate the BT Model, we fit a multimembership mixed e!ects logit model using the brms package and Stan programming language (B¨urkner, 2017, 2018; Stan Development Team, 2024; Gabry et al., 2024). The model is simply a varying intercept logistic regression model where we estimate separate intercepts for each individual respondent. Equation 2 shows the basic linear model structureto determine if player i beats player j . ε represents the varying intercept estimate for respondents i and j. The varying intercept estimates are on the log-odds scale, and are each multiplied by a weight, denoted by W . Because we are modeling the probability that respondent i wins a given comparison (i.e. Pr(i > j)), the weight for respondent i (i.e. Wi) takes on a value of 1 while the weight for respondent j (i.e. Wj ) takes on a value of ↑1. The outcome of Equation 2 provides us with the joint log-odds, yij, for a given pairing of i and j.

yij = εi ↓ Wi + εj ↓ Wj  (2)

To derive the probability that player i beats player j we simply take the log-odds value of yij that we obtain from Equation 2 and plug it into Equation 3. This is simply the inverse logistic function.

eyij

Pr(i > j) = pij = (1 + eyij)  (3) Equations 2 and 3 are useful because they provide a link between the regression-based syntax and the result of the BT models. Alternatively, we can work more directly with the varying intercept values for the two players and derive Pr(i > j) with Equation 4:

eωi Pr(i > j) = pij = eωi + eωj  (4) As we discuss above, we estimate this model as a multi-membership multilevel model using brms. The basic formula syntax of the brms model is as follows:

brms::brm(Y ~ 0 + (1|mm(id1, id2, weights = cbind(weight1, weight2), scale = FALSE)

In this case we set weight1 to equal 1 and weight2 to equal ↑1.

This represents the basic BT model, but we are often more interested in obtaining latent estimates of respondent knowledge than we are in the estimates of P r(i beats j). Here we use the estimates of individual respondent knowledge provided by ε to rank order respondents according to their knowledge and ability to accurately answer the questions posed.[^3]

##### Human-LLM Comparison of Comparisons

Our own prompting indicates that LLMs have a good understanding of the central process of setting interest rates. Beyond this, there is some indication that LLMs have strong domain knowledge in economics and finance (Yang et al., 2024; Hultberg et al., 2024). For example, an older version of ChatGPT, version 3.0, scored 91st percentile on the Test of Understanding in College Economics (Geerling et al., 2023). However, systematic evidence on LLMs domain knowledge in this, and most areas, is limited. As such, we validate the LLMs against human coders in this specific task and recommend that researchers do the same for domains where questions still remain about the alignment of LLMs with authoritative sources.

To create a human benchmark for this di”cult subject, we recontacted 20 respondents from our original sample that o!ered an expert-level answer on our initial survey. Based on the results of the LLM ratings, we selected the top-20 responses in terms of knowledge. We then reviewed those responses to verify that they in fact provided an ‘expert-level’ response to the question on interest rates. We then recontacted these crowd-workers, via the Prolific Platform, and asked them to take part in a pairwise comparison exercise to rank several 20 pairs of responses randomly drawn from our dataset.[^4] We ended up with 300 pairs of human

Figure 2: Comparisons Human-LLM - F1 Score: This figure reports the F1 score for Human-LLM comparisons of pairwise comparison results for a subset of the original dataset (N=300).

rated pairs. We then prompted each of the LLMs to compare these same pairs with similar instructions.

Figure 2 reports the F1 score comparing the human raters with the LLMs for the small set of responses coded by the human coders.[^5] The large frontier models (GPT-4o, GPT- 4o mini, and Llama 3.1 405B) and the mid-sized model (Gemma 3 27B) exceeded an F1 score of 0.8, indicating a strong alignment with human assessments. The smaller models showed modest agreement but are clearly lagging behind the larger models. The F1 should be interpreted in context. In this exercise, we asked the respondents and the LLMs to select the profile with a “small preference” rather than indicate a tie to ease interpretation to make a comparison tractable. Many of the human responses are going to have similar levels of knowledge. As such, there are likely to be a high number of ambiguous cases in the dataset. Compared to classification tasks which may have clearer borders between cases, the task here will naturally lead to more disagreement. Still, we find a strong F1 scores that are consistent across multiple models. This gives us confidence that the underlying task generating the data is one that is well handled by LLMs.[^6] For a more qualitative assessment, in the appendix B.4 we present, several examples of comparisons and their ratings by a human and each of the LLMs.

##### Comparison with Closed Ended Responses

Thus far, we have seen that the pairwise comparison approach is well-suited for large and mid-sized frontier models and the underlying task of comparisons is closely related to human decision making. We take an additional step to compare the estimates within respondent by comparing our BT estimates of individuals respondents to their own responses on closed-ended questions in the same survey. We compare these responses with the BT estimates derived from the pairwise comparisons of the largest open-source model, Llama 3.1 with 405 billion parameters. We chose this model given our preference for an open-source model motivated by concerns of replicability.

In Figure 3, we plot the BT estimates in order but classify them based on how a respondent responded to the question “How familiar are you with the following US institution: The Federal Reserve”. We see, in line with expectations, that those that “have a fairly accurate idea of the duties of the institution” and “have an approximate idea of the duties of the institution” score higher on the scale. Those that “only know the institution by name” or “don’t know” the institution rank consistently lower on the scale. Next, we turn to factual questions about the Federal Reserve. Given the large role of the Federal Reserve in setting interest rates, knowledge about the institutional structure of the Federal Reserve should be strongly related to knowledge about interest rates. Figure 4 presents the mean BT estimate by correctness of three factual questions in which respondents had to pick the correct answer from 4 choices. We see that those who could not identify which institution in the US government sets interest rates, who appoints the Chair, and those who could not identify the Fed

Figure 3: BT Estimates by Self Reported Knowledge of the Fed: Here we randomly selected 200 responses (for visibility) and plot the BT estimates in order of knowledge. The error bars of the estimates are colored based on responses to query about a respondents self reported knowledge of the Federal Reserve.

Chair have significantly lower BT estimates. This gives us confidence that the BT estimates align with the the underlying construct—knowledge about the Federal Reserve and Interest Rates.

##### Comparing LLMs

We now proceed to compare the final BT estimates from the pairwise comparisons of each LLM. First, Figure 5 plots the 95% credible intervals around each respondent’s latent estimate from each of the six models. In each figure we sort latent estimates according to the median of their posterior distributions from the lowest to highest respondent knowledge ability within each model. The plots demonstrate a similar pattern across all but the smallest model.

Table 2 presents the correlations of the final BT scores for each model. Each correlation exceeds 0.87. Correlation among the largest models (GPT-4o and Llama 3.1 405B) exceeds 0.95. This suggests that, with this specific task, the LLMs are largely in agreement about

Figure 4: Mean BT Estimate by Correct and Incorrect Answers to Factual Questions about the Fed

what constitutes a highly knowledgeable answer. This provides confidence that LLMs can produce consistent scales when used to produce pair-wise comparisons.

```text
Gemma 3 Gemma 3 Llama 3.1 Llama 3.1  GPT  GPT
4B  27B  8B  405B  4o mini  4o
Gemma 3:4B  1.000  0.894  0.908  0.898  0.899  0.876
Gemma 3:27B  0.894  1.000  0.884  0.942  0.931  0.919
Llama 3.1:8B  0.908  0.884  1.000  0.902  0.908  0.879
Llama 3.1:405B  0.898  0.942  0.902  1.000  0.949  0.948
GPT-4o Mini  0.899  0.931  0.908  0.949  1.000  0.926
GPT-4o  0.876  0.919  0.879  0.948  0.926  1.000
```

Table 2: Correlation of BT Estimates of Pairwise Comparisons by LLM

For comparison, we also prompted each LLM to engage in zero-shot numerical ratings of individual statements. We asked each LLM to place each statement on scale reflecting the knowledge about interest rates from completely incorrect or irrelevant (0) to highly knowledgeable and accurate (10).[^7]

Figure 5: Bayesian Bradley-Terry Estimates of Interest Rate Knowledge by LLM. Each panel plots the 95% credible interval for the posterior distributions for each respondent in our dataset. Items are sorted highest to lowest within each panel.

```text
Gemma 3 Gemma 3 Llama 3.1 Llama 3.1  GPT  GPT
4B  27B  8B  405B  4o mini  4o
Gemma 3:4B  1.000  0.841  0.775  0.824  0.822  0.792
Gemma 3:27B  0.841  1.000  0.785  0.914  0.879  0.862
Llama 3.1 8b  0.775  0.785  1.000  0.807  0.751  0.724
Llama 3.1 405B  0.824  0.914  0.807  1.000  0.911  0.847
GPT-4o mini  0.822  0.879  0.751  0.911  1.000  0.882
GPT-4o  0.792  0.862  0.724  0.847  0.882  1.000
```

Table 3: Correlation of 0-10, One-shot, Ratings by LLM

Figure 6: Distribution of ratings: This figures presents the distributions of the 0-10 ratings of interest rate knowledge for each of the LLMs (N=1,402).

Figure 6 plots the distribution of these results and Table 3 presents the correlations of these ratings. Several things stand out. First, we see that while the models are given range of values to place a statement, several models rely on a fraction of those values. As such, zero-shot ratings may inherently limit the nuance of their output and thus miss key distinctions between responses. This also gives further pause as it appears the patterns do not follow an apparent logic. It suggests that there is an inherent bias in selecting some numbers over others. Next, we see that the correlation among the models is strong. Yet, the consistency across models falls short of the consistency of the BT estimates. For example, among the two largest models (GPT-4o and Llama 3.1 405B), the ratings are correlated at 0.85, compared with 0.95 in the BT estimates.

Figure 7: Coe!cient of Interest Rate Knowledge on Support for Central Bank Independence: Both panels plot the standardized coe”cients and 95% CI of ‘interest rate knowledge’ in a linear model predicting support for central bank independence for each of the LLMs used in our analyses. Each model also includes controls for income and education. The left plot relies on a 0-10 one shot rating on knowledge.

While our analysis here is limited to one domain, the findings suggest that one-shot ratings may be a less costly option, though they under-perform compared to a pair-wise comparison approach. The findings in an additional task we present in the appendix (B.2) support this conclusion.

The last step in our workflow is to draw from the distribution of Bradley Terry estimates and use a multiple (over)imputation framework to recover an aggregate estimate that incorporates the uncertainty in the latent variable. Here we use our latent variable, interest rate knowledge, as a predictor of support for central bank independence.[^8] We expect people with greater knowledge will favor independence. As such, we estimate linear models that include interest rate knowledge plus potential confounders: education and income.

The right panel of Figure 7 presents the standardized coe”cients of interest rate knowledge for each the LLM derived latent variables and the corresponding 95% confidence interval. We see that the point estimates for the larger models appear to be bigger. If there is indeed a relationship, it suggest that the more capable models are more adept at picking up the underlying concept. For comparison, we also plot the standardize coe”cients of similar linear models for the zero-shot 0-10 ratings in the left panel. First, the two approaches provide point estimates of di!erent sizes. The coe”cients of the BT estimates are about 75% the size of the rating coe”cients. Further, the confidence intervals around the BT estimate coe”cient are considerably larger given the incorporation on the estimate uncertainty.[^9] Depending on the underlying LLM comparisons, this can result in the di!erence between a significant or insignificant result. Overall, the analysis illustrates the potential consequences of relying solely on one-shot numerical ratings in downstream models.

#### Scope and Limitations

Open-ended questions have been under utilized because of the cost of hand-coding text or the limitations of current algorithms to uncover latent dimensions that researchers care about. LLMs have opened the door to using open-ended questions more often and in more applications. We go further and suggest that LLMs also unlock the benefits of PWC to scale open-ended responses. If hand rating text is expensive, a su”cient number of comparisons in large datasets is, in most applications, prohibitive. LLMs can again reduce barriers to this scaling technique that hold several theoretical advantages over one-shot ratings. Notably, PWC reduces bias, increase precision, and allows for measures of uncertainty. Further, we show that, at least when it comes to this task, LLMs’ judgments correspond closely to expert or near-expert human coders, there is high agreement among di!erent LLMs, and they outperform numerical ratings.

Beyond our application here, PWC by LLM can be deployed in numerous ways. For example, researchers can pull multiple dimensions from the same source. Open-ended text can hold multiple dimensions and often those concepts may confound each other. The process we outlined above can be used to scale numerous dimensions independently and thus “control” for confounding dimensions in downstream analyses. Tapping di!erent dimensions from the same text might also be helpful in experimental settings where researchers may wonder if they have manipulated the intended variable or a closely related concept. Similarly, our approach could be helpful in the choice of survey instruments in pilot analysis. As researchers now can test if di!erent questions wordings tap the similar constructs by pooling responses and looking for separation in the BT estimates.

The method itself can also be refined to reduce costs. For example, researchers can implement an adaptive BT model to reduce the absolute number of comparisons (Maystre and Grossglauser, 2017) by focusing more attention on statements that are close in proximity.

While the method is useful, it does have several limitations. First, researchers must be able to identify and phrase a question that will reveal the latent dimension of interest. Some concepts may still be better probed in the context of discrete factual questions. While others might benefit from a longer exposition. Further, the domain knowledge of LLMs have not been fully mapped. It is still necessary to validate the use of LLMs with high quality benchmarks (Gilardi et al., 2023).

Second, some concepts may be easier to identify than others. The task is best suited to applications where researchers require a single, easily inferred, dimension. We carried out an additional illustration (see appendix B.2) in which we asked an LLM to identify ‘uncertainty’ in respondents expectations of the economic consequences of government action. Here, we see less agreement across LLMs. However, the method still produces more consistent output than numerical ratings. Consequently, researchers should do their due diligence to demonstrate that LLM output is consistent across and within models and that the findings are not dependent on the judgments of a single LLM.

Third, the ability of various LLMs to accurately and consistently evaluate the factual content of respondent answer depends on the integrity of the underlying LLM model and training data. If a given LLM cannot “retain” a piece of factual information then its ability to evaluate how factual a given response is will likely not be stable over time (Khatun and Brown, 2024). Other factors, like the framing of questions/prompts or the inclusion of extra or unnecessary language in prompts, can produce incorrect responses. Similarly, while multiple LLMs may rank particular options as the most likely correct responses, it is di”cult to assess the degree of confidence or uncertainty across various LLMs, or how stable they are over time (Wang et al., 2024).

Finally, while LLMs may potentially bring new life to the use of open-ended questions in survey research they also bring risks beyond the structural and mechanical problems of the LLMs themselves. The increasingly widespread use of LLMs for completing various user tasks may interfere with e!orts to collect user knowledge from surveys. We were suspicious that several of the open-ended responses from our Prolific respondents were themselves generated by LLMs. To explore this further, when we recontacted respondents to serve as our human benchmarks we again asked them to answer the question about interest rates. This time, we hid an additional request in the html in very and small transparent font. We asked that the response “mention Alan Greenspan”. This served the purpose of providing a very specific instruction that is unlikely to be included without prompting but also one that would not arise too much suspicion if read by the human pasting in to the survey. We found that 5 of our top 20 respondents were using AI to answer the open-ended question. We removed these responses from the final dataset. While the use of LLMs by survey respondents were not detrimental to our analysis, it does show that respondents may rely on LLMs for cognitively demanding tasks like open-ended questions. The prospect of AI agents completing surveys on their own raise the risk that entire survey forms will be completed by AI. Consequently, survey researchers, whether using open or closed questions, should design strategies to identify these responses and drop them from the dataset.

#### References

Andre, Peter , Ingar Haaland, Christopher Roth, Mirko Wiederholt, and Johannes Wohlfart (2024). Narratives about the macroeconomy. Technical report, SAFE Working Paper.

Barrie, Christopher , Alexis Palmer, and Arthur Spirling (2024). Replication for language models: Problems, principles, and best practice for political science. https://github.com/ArthurSpirling/LargeLanguageReplication?tab=readme-ov-file. Working Paper.

Benoit, Kenneth , Kevin Munger, and Arthur Spirling (2019). Measuring and explaining political sophistication through textual complexity. American Journal of Political Science 63 (2), 491–508.

Bermejo, Vicente J , Nicol´as Harari, Ramiro H G´alvez, and Andres Gago (2024). Llms outperform outsourced human coders on complex textual analysis. Available at SSRN .

Blackwell, Matthew , James Honaker, and Gary King (2017). A unified approach to measurement error and missing data: overview and applications. Sociological Methods & Research 46 (3), 303–341.

Bradley, Ralph Allan and Milton E Terry (1952). Rank analysis of incomplete block designs: I. the method of paired comparisons. Biometrika 39 (3/4), 324–345.

B¨urkner, Paul-Christian (2017). brms: An R package for Bayesian multilevel models using Stan. Journal of Statistical Software 80 (1), 1–28.

B¨urkner, Paul-Christian (2018). Advanced Bayesian multilevel modeling with the R package brms. The R Journal 10 (1), 395–411.

Carlson, David and Jacob M Montgomery (2017). A pairwise comparison framework for fast, flexible, and reliable human coding of political texts. American Political Science Review 111 (4), 835–843.

Carpenter, Bob (2018). The bradley-terry model of ranking via paired comparisons. RPubs .

Converse, Jean M (1984). Strong arguments and weak evidence: The open/closed questioning controversy of the 1940s. Public Opinion Quarterly 48 (1B), 267–282.

Davidson, Roger R (1970). On extending the bradley-terry model to accommodate ties in paired comparison experiments. Journal of the American Statistical Association 65 (329), 317–328.

Di Leo, Riccardo , Chen Zeng, Elias Dinas, and Reda Tamtam (2025). Mapping (a) ideology: A taxonomy of european parties using generative llms as zero-shot learners. Political Analysis, 1–8.

DiGiuseppe, Matthew , Carolina Garriga, and Andreas Kern (2024). Information, party politics, and public support for central bank independence. Working paper.

Firth, David (2005). Bradley-terry models in r. Journal of Statistical Software 12.

Gabry, Jonah , Rok ˇCeˇsnovar, Andrew Johnson, and Steve Bronder (2024). cmdstanr: R Interface to ’CmdStan’. R package version 0.8.1, https://discourse.mc-stan.org.

Geer, John G (1991). Do open-ended questions measure “salient” issues? Public Opinion Quarterly 55 (3), 360–370.

Geerling, Wayne , G. ˜Dirk Mateer, Jadrian Wooten, and Nikhil Damodaran (2023, April). Chatgpt has aced the test of understanding in college economics: Now what? The American Economist 68 (2), 233–245.

Gilardi, F. , M. Alizadeh, and M. Kubli (2023). Chatgpt outperforms crowd workers for textannotation tasks. Proceedings of the National Academy of Sciences 120 (30), e2305016120.

Gruber, Johannes B. and Maximilian Weber (2024, Apr). rollama: An r package for using generative large language models through ollama. arXiv preprint . A Preprint.

Haaland, Ingar K , Christopher Roth, Stefanie Stantcheva, and Johannes Wohlfart (2024). Measuring what is top of mind. Technical report, National Bureau of Economic Research.

Heseltine, Michael and Bernhard Clemm von Hohenberg (2025). Large language models as a substitute for human experts in annotating political text. Research & Politics 12, 1–10.

Hultberg, Patrik T , David Santandreu Calonge, Firuz Kamalov, and Linda Smail (2024). Comparing and assessing four ai chatbots’ competence in economics. Plos one 19 (5), e0297804.

Kaye, Ella and David Firth (2022). Bradleyterryscalable.

Khatun, Aisha and Daniel G. Brown (2024). Trutheval: A dataset to evaluate llm truthfulness and reliability.

Kraft, Patrick W (2024). Women also know stu!: challenging the gender gap in political sophistication. American Political Science Review 118 (2), 903–921.

Lazarsfeld, Paul F (1944). The controversy over detailed interviews—an o!er for negotiation. Public opinion quarterly 8 (1), 38–60.

Le Mens, Ga¨el and Aina Gallego (2025). Positioning political texts with large language models by asking and averaging. Political Analysis 33 (3), 274–282.

Loewen, Peter John , Daniel Rubenson, and Arthur Spirling (2012). Testing the power of arguments in referendums: A bradley–terry approach. Electoral Studies 31 (1), 212–221.

Ludwig, Jens , Sendhil Mullainathan, and Ashesh Rambachan (2024). Large language models: An applied econometric framework. arXiv preprint arXiv:2412.07031 .

Mattos, David Issa and ´Erika Martins Silva Ramos (2022). Bayesian paired comparison with the bcps package. Behavior Research Methods 54, 2025–2045.

Maystre, Lucas and Matthias Grossglauser (2017). Just sort it! a simple and e!ective approach to active preference learning. In International Conference on Machine Learning, pp. 2344–2353. PMLR.

Mellon, Jonathan , Jack Bailey, Ralph Scott, James Breckwoldt, Marta Miori, and Phillip Schmedeman (2024). Do ais know what the most important issue is? using language models to code open-text social survey responses at scale. Research & Politics 11 (1), 20531680241231468.

Ornstein, Joseph T. , Elise N. Blasingame, and Jake S. Truscott (2025). How to train your stochastic parrot: large language models for political texts. Political Science Research and Methods, 1–18.

Peysakhovich, Alexander and Adam Lerer (2023). Attention sorting combats recency bias in long context language models.

Rathje, Steve , Dan-Mircea Mirea, Ilia Sucholutsky, Raja Marjieh, Claire E Robertson, and Jay J Van Bavel (2024). Gpt is an e!ective tool for multilingual psychological text analysis. Proceedings of the National Academy of Sciences 121 (34), e2308950121.

Roberts, Margaret E , Brandon M Stewart, Dustin Tingley, Christopher Lucas, Jetson Leder- Luis, Shana Kushner Gadarian, Bethany Albertson, and David G Rand (2014). Structural topic models for open-ended survey responses. American journal of political science 58 (4), 1064–1082.

Stan Development Team (2024). Stan Modeling Language Users Guide and Reference Manual, v2.36.0.

T¨ornberg, Petter (2024). Large language models outperform expert coders and supervised classifiers at annotating political social media messages. Social Science Computer Review , 08944393241286471.

van Paridon, JP , Ben Bolker, and Phillip Alday (2023). lmerMultiMember: Multiple membership random e!ects. R package version 0.11.8.

Wang, Weixuan , Barry Haddow, Alexandra Birch, and Wei Peng (2024, June). Assessing factual reliability of large language model knowledge. In K. Duh, H. Gomez, and S. Bethard (Eds.), Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), Mexico City, Mexico, pp. 805–819. Association for Computational Linguistics.

Wu, Patrick Y , Jonathan Nagler, Joshua A Tucker, and Solomon Messing (2023a). Conceptguided chain-of-thought prompting for pairwise comparison scaling of texts with large language models. arXiv preprint arXiv:2310.12049 .

Wu, Patrick Y , Jonathan Nagler, Joshua A Tucker, and Solomon Messing (2023b). Large language models can be used to estimate the latent positions of politicians. arXiv preprint arXiv:2303.12057 .

Yang, Cehao , Chengjin Xu, and Yiyan Qi (2024). Financial knowledge large language model. arXiv preprint arXiv:2407.00365 .

Zollinger, Delia (2024). Cleavage identities in voters’ own words: Harnessing open-ended survey responses. American Journal of Political Science 68 (1), 139–159.

Zucco Jr, Cesar , Mariana Batista, and Timothy J Power (2019). Measuring portfolio salience using the bradley–terry model: An illustration with data from brazil. Research & Politics 6 (1), 2053168019832089.

### Supplementary Appendix for Scaling Open-ended Survey Responses Using LLM-Paired Comparisons

Matthew DiGiuseppe  Michael Flynn Associate Professor  Professor Leiden University  Kansas State University [email removed]  [email removed]

##### June 24, 2025

#### Contents

A Appendix: AAPOR-Required Disclosure Elements  2 B Additional Analyses and Information  5

B.1 Chain of Thought Prompting & Reasoning Models . . . . . . . . . . . . . . .  5 B.2 Additional Illustration: Uncertainty . . . . . . . . . . . . . . . . . . . . . . .  7 B.3 Incorporating Character Length of Responses . . . . . . . . . . . . . . . . . 11 B.4 Response and Decision Examples . . . . . . . . . . . . . . . . . . . . . . . . 17 B.5 A note on ELO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20 B.6 Resolving Ties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21 B.7 LLM Model Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

#### A Appendix: AAPOR-Required Disclosure Elements

First data source: Survey data collected by DiGiuseppe, Garriga and Kern (2025) via the Prolific online platform to measure knowledge about monetary policy and interest rates. The data used in the example in the Appendix was collected by DiGiuseppe and Shea (2025) via the Prolific online platform to measure uncertainty about the consequences of a debt ceiling increase.

Data Collection Strategy: Online survey employing both closed and open-ended questions to capture respondent knowledge about how interest rates are determined in the US economy.

###### Research Sponsor and Conductor: [REDACTED]

Measurement Tools/Instruments:

- Interest rate Illustration: ‘In a few sentences and without looking it up, can you explain how interest rates (i.e. the cost of borrowing money to buy a house or car) go up or down in the US economy?” Respondents were asked to reply in 2-3 sentences. Additional closed-ended questions measured self-reported knowledge of the Federal Reserve and factual knowledge questions about Federal Reserve structure and leadership.

- Uncertainty Illustration: “In one or two sentences, what do you think will happen if the government DOES NOT increase the debt ceiling?” Experimental manipulation included images and accompanying text designed to increase uncertainty about debt ceiling consequences. Population Under Study: US adults. The study used quota sampling to reflect the US population in terms of age, gender, and partisanship. Methods Used to Generate and Recruit the Sample: 1. Non-probability sample recruited through the Prolific platform 2. Quota sampling methodology used to achieve representativeness on age, gender, and partisanship 3. No specific eligibility requirements mentioned beyond standard Prolific participation criteria 4. Geographic location: United States Method(s) and Mode(s) of Data Collection: Web-based survey administered through the Prolific platform. Language: English. Dates of Data Collection:

- Interest Rate Survey: August 6th, 2024

- Uncertainty Survey: May 2nd, 2023

Sample Sizes and Precision of Results:

- Initial Interest rate sample: N=1,400

- Initial Uncertainty sample: N=1,486

- Human validation subsample: N=20 expert-level respondents recontacted for pairwise comparison validation. N=300 pairs Whether and How the Data Were Weighted: Quota sampling was employed to reflect US population demographics on age, gender, and partisanship. No post-stratification weighting procedures are described. How the Data Were Processed and Procedures to Ensure Data Quality:

- Responses were analyzed using six di!erent Large Language Models (LLMs): GPT-4o, GPT-4o Mini, Llama 3.1 405b, Llama 3.1 8b, Gemma 3 4b, and Gemma 3 27b

- Pairwise comparison methodology used where each response was randomly paired with 20 other responses

- Human validation conducted with expert-level respondents

- Detection method for AI-generated responses: Hidden HTML request to “mention Alan Greenspan” identified 5 of 20 validation respondents using LLMs, who were removed from analysis

- Bayesian Bradley-Terry models estimated using Stan and brms packages in R.

Study Stimuli: The open-ended question about interest rate determination.

Dispositions or Response or Participation Rates: Not provided in the manuscript. [Authors should provide participation rates from Prolific platform]

Sample Sizes: Unweighted sample size of N=1,400 for main analysis. Human validation subsample of N=20 (reduced to N=15 after removing AI-generated responses).

Measurement and Model Specification:

- Bayesian Bradley-Terry models estimated using multimembership mixed e!ects logistic regression

- Model formula: Y ~ 0 + (1|mm(id1, id2, weights = cbind(weight1, weight2), scale = FALSE))

- Software: R packages brms and Stan

- Each response paired with 20 others, resulting in approximately 28,000 total comparisons

###### A General Statement Acknowledging Limitations of the Design and Data Collection: This study uses a non-probability convenience sample from Prolific with quota

sampling, which may limit generalizability to the broader US population. The detection of AI-generated responses among validation participants highlights the challenge of ensuring authentic human responses in online surveys. The LLM analysis methodology is novel and requires validation across di!erent domains and tasks.

#### B Additional Analyses and Information

##### B.1 Chain of Thought Prompting & Reasoning Models

In addition to asking an LLM to return just a final answer on which statement best aligned with the latent dimension of interest (knowledge), we also attempted a Chain of Thought (CoT) pair-wise comparison prompting approach following the recommendation of (Wu et al., 2023) and used a reasoning model (GPT-4o mini) to carry out our pair wise tasks. For the reasoning model, we simply provided the same prompt we used in the comparisons analysis we presented in the main manuscript. For the CoT analysis, we used the following prompt with the Llama 3.1 405b model:

”You are an expert in US economic policy. Your task is to determine which of two given statements contains a more knowledgeable response to the following question:”, ”In a few sentences and without looking it up, can you explain how interest rates (i.e., the cost of borrowing money to buy a house or car) go up or down in the US economy?”, ”Follow these steps to complete the task:”, ”Step 1: Write out your evaluation of Statement 1, discussing its strengths, weaknesses, and gaps in knowledge.”, ”Step 2: Write out your evaluation of Statement 2, discussing its strengths, weaknesses, and gaps in knowledge.”, ”Step 3: Compare your evaluations of the two statements and explain which one demonstrates greater knowledge, or why they are equal or incomparable.”, ”Step 4: Based on your reasoning, provide your final decision.”, ”Your response should include the full reasoning for each step, and the final decision must be presented as:”, ”Final Decision: [1] or Final Decision: [2] or Final Decision: [0]”, ”Here are the statements to evaluate:”, ”1:”, [statement1], ”2:”, [statement2], ”Write out your full evaluation and conclude with the final decision in the specified format.”

We find, contrary to our expectations, that the CoT prompt performed worse than the direct prompt against the “close to expert” benchmark. This builds on recent evidence that CoT prompting may have been useful for smaller and older models but is no longer necessary with frontier LLMs (Meincke et al., 2025).

Similarly, the reasoning model did not generate appreciable gains over the non-reasoning models. As such, we present only the results from the more cost-e!ective one-shot, non-reasoning models in our main analysis. We suspect that for this task, the frontier LLMs are su”cient and there are no appreciable gains to be made by further prompting either internally (reasoning models) or externally (CoT).

Figure A1: F1 - LLM-Human Comparison including Chain of Thought prompt

(a) Control Figure  (b) Treatment Figure

Figure A2: Caption place holder

##### B.2 Additional Illustration: Uncertainty

In addition to the illustration above, we also applied our framework to an experimental setting where the variable of interest is a dependent variable. In a recent paper, DiGiuseppe and Shea (2025) attempt to manipulate respondents’ uncertainty over the consequences of a debt ceiling breach in the run-up to the 2023 debt ceiling deadline in the United States. The survey was deployed on a quota representative sample on Prolific (N=1486). Figure A2 presents the images in the experiment that accompanied text that reinforced the goal of the figures. As a manipulation check, the authors asked respondents, post treatment, “In one or two sentences, what do you think will happen if the government DOES NOT increase the debt ceiling?” In their analysis (reported in the Appendix), the authors used and LLM (GPT-4) to rate the uncertainty of respondent expectations in each response on 5, 11, or 101 point scale. Using this measure, they find that the LM ranked the statements in the ‘uncertain’ condition as having higher and statistically significant uncertainty score when using each of these scales.

Here, we apply a pairwise comparison approach to this data and try to replicate their findings and examine di!erences between di!erent models and between the BT estimates and 0-10 ratings as we did with the example in our main analysis.

The figures and tables in this section indicate a few things. First, there is much less consistency in the model output in this task. The correlations are much lower among both the BT estimates and the 0-10 rankings. The BT estimates appear to be more consistent among the high-end models. Among the 3 frontier models (Llama 3.1 405b, GPT-4o and GPT-4o mini), the correlation of the final output ranges from 0.59 to 0.82. Still, this may be too low to have confidence in any particular model for this task. Unfortunatley, we do not have a human-benchmark to compare these findings. Lastly, the figure A5 shows that LLM choice can have a dramatic impact on inference where LLMs are inconsistent in their comparisons.

The exercise suggests that the usefulness of LLMs to scale latent variables from text is conditional on the specific task. Still, it is worth noting that, the pairwise comparisons still demonstrate more consistency than the zero-shot ratings. Theoretically, this aligns with the benefits of pairwise comparisons to eliminate bias that does not impact the ranking of two statements.

Gemma 3:4B Gemma 3:27B Llama 3.1:8B Llama 3.1:405B GPT4o Mini GPT4o

```text
Gemma 3:4B  1.00  0.35  0.69  0.21  0.49  -0.02
Gemma 3:27B  0.35  1.00  0.23  0.50  0.47  0.58
Llama 3.1:8B  0.69  0.23  1.00  0.34  0.55  0.03
Llama 3.1:405B  0.21  0.50  0.34  1.00  0.79  0.82
GPT4o Mini  0.49  0.47  0.55  0.79  1.00  0.64
GPT4o  -0.02  0.58  0.03  0.82  0.64  1.00
```

Table A1: Correlation of BT Estimates of Pairwise Comparisons by LLM: Uncertainty

Gemma 3:4B Gemma 3:27B Llama 3.1:8B Llama 3.1:405B GPT4o Mini GPT4o

```text
Gemma 3:4B  1.00  0.25  0.27  0.28  0.19  0.31
Gemma 3:27B  0.25  1.00  0.53  0.58  0.69  0.60
Llama 3.1:8B  0.27  0.53  1.00  0.59  0.52  0.45
Llama 3.1:405B  0.28  0.58  0.59  1.00  0.64  0.59
GPT4o Mini  0.19  0.69  0.52  0.64  1.00  0.57
GPT4o  0.31  0.60  0.45  0.59  0.57  1.00
```

Table A2: Correlation of Uncertainty Ratings by LLM

Figure A3: Bayesian BT knowledge scores

Figure A4: Distribution of Uncertainty 0-10 Ratings by LLM

Figure A5: ATE of treatments based on LLM codings of ‘Uncertainty DV’: The point estimates indicate the average treatment e!ect and bars indicate the 95% confidence intervals.

##### B.3 Incorporating Character Length of Responses

It is possible that LLMs are evaluating the knowledge contained in responses by standards other than the factual content of the answer. For example, it may be that LLMs are inclined to more highly rate longer responses over short responses. In such cases the risk would be that responses with longer answers are more likely to win a given matchup when we make our paired comparisons.

To better understand this issue we run our six primary LLM models again using our Bradley–Terry framework, but this time we include a variable that adjusts for the di!erence in the length of the responses as measured by the number of characters contained in each response. In these models we measure the di!erence in response lengths as follows:

Di!erenceij = Response Lengthi → Response Lengthj  (1) Where Response Length is simply a count of the number of characters in the respondent’s answer. Positive values indicate that respondent i had a longer answer and negative values indicate that respondent j had a longer answer. We use this di!erence-based measure because using the length of a single player’s response tells us little without the additional context of the other player’s response length. With this measure we should expect positive values to correlate positively with a win for player i, assuming the LLM is privileging longer answers.

Figure A6 shows the distribution of the response lengths across all individual respondents, as well as the distribution of the di!erences in responses that we use in the Bradley–Terry models to adjust for the relative length of the players’ responses. The bulk of the distribution of the responses is largely concentrated around 150 characters, with a mean of 161 and a median of 129, with some outliers with several hundred characters. However, after randomly pairing respondents we can see that the distribution fo the di!erence variable is normally distributed, with the bulk of the respondents having fairly small di!erences.

Figure A7 shows the coe”cients for the di!erences in response lengths. Across all six

Figure A6: In this model, we compare BT estimates that include a parameter for character length with the models we estimated above that omitted character length.

of the models we examine we find positive coe”cients for the response length di!erence variable, indicating that as the length of player i’s response increases compared to player j, there is an increase in probability that the LLM chooses player i as the winner. If the length of the response made no di!erence then we should expect to see coe”cients and posterior distributions clustering around 0. In this case the coe”cients and posterior distributions for all six models fall well above 0, indicating a positive e!ect for response length relative to a player’s opponent.

Additionally, the magnitude of these coe”cients is fairly small at first glance, with most values concentrated around a value of 0.02 and the Llama 3 405b model producing a slightly larger coe”cient of approximately 0.045. Though it is normally di”cult to tell the substantive magnitude of the e!ects from looking at a logit coe”cients on their own, the population intercept is set to 0 in our models, meaning that this coe”cient represents the populationaverage e!ect for a one-unit change in the response length di!erence variable relative to 0. Furthermore, the median positive and negative di!erence values are approximately 91,

Figure A7: Coe”cients for the variable measuring the di!erence in response lengths for players i and j in the Bradley–Terry models.

which means that this coe”cient is better understood in practice as representing a change of approximately ± 1.8–2.0 on the log odds scale in many practical cases. This is a fairly sizable shift given the practicable range of the log odds scale.

As a further check we look at the correlation between the individual-level knowledge estimates from our base models and those generated by the models that include the covariate for the di!erence in response lengths. Figure A8 shows the correlation between all of the base models and the those with the response length variable. Ultimately we find that both sets of models are producing knowledge estimates that are largely in line with one another. The lowest correlation coe”cient is 0.88 with a median of 0.91 and a mean of 0.93. In general the models are both producing knowledge estimates and rankings that are comparable with only minor slippage between the base models and the adjusted models.

Finally, we include two additional figures to show how the rankings of randomly chosen

Figure A8: Correlation plot for the individual player rankings generated from the base models including in the main text and the supplementary models that include a variable adjusting for the di!erence in the length of the respondents’ answers.

Figure A9: Varying intercept plots for the GPT-4o base model showing rankings for randomly selected ID numbers.

respondent IDs compare between the base model and the adjusted model. Figure A9 shows the rankings for seven randomly chosen respondents based on the baseline BT models and the models that adjust for the di!erences in the length of the responses. For the most part we see consistency in terms of the relative ordering of the chosen respondents, but we do see some shifting along the x axis indicating that there is some shifting in the absolute rankings of the respondents across models. In general these shifts are fairly modest, though some across see larger swings than others. For example, in Figure A9 we see that the green bar moves from the 766th highest rank to the 424th. The remaining respondents are fairly consistent in their ranks between the base and adjusted models.

GPT-4o is one of the more common LLMs and the coe”cient for the adjustment variable is in line with all of the other LLMs with the exception of the Llama 405b model. The coe”cient for this model was by far the largest, suggesting that rankings may be more

Figure A10: Varying intercept plots for the Llama 405b base model showing rankings for randomly selected ID numbers.

sensitive to the inclusion of the response length adjustment variable.

As above, Figure A10 shows the rankings of the same randomly selected respondents in both the base and adjusted models. Here we see more substantial slippage for some of the respondents. Here we see that the gold bar slips from the 25 to 111. Alternatively, the pink bar moves from 766 up to 580 in the adjusted models.

On the whole these shifts appear to be fairly mild and both sets of models still appear to capture useful variation in rankings across the full range of respondents. Parsing di!erences between individual respondents is, of course, a much more di”cult task, and one benefit of the Bayesian approach is that the posterior distributions around each individual varying intercept estimate remind us of the uncertainty inherent in this work, while also providing us with a way to incorporate that uncertainty into downstream analyses.

##### B.4 Response and Decision Examples

Table A3: Comparison for Pair 1: Statements 834 vs 1323 Statement A (ID: 834)  Statement B (ID: 1323)

If the Fed(Federal Reserve) raises the in- Generally the Fed sets their interest rates terest rates it is a snowball e!ect amongst based on what they want the economy to lenders with credit cards and small loan do. Other interest rates, for banks, credit companies causing the most damage to cards, consumer loans, etc., are keyed in the average person. Those companies will some way to the federal loan rate. Also begin charging close to 30% on what you plain supply and demand can influence inborrow from them. In the long run, a 1% terest rates: too many people chasing too increase in a 30 year mortgage could also little available money can drive up interturn into hundreds of thousands of extra est rates, and the reverse can happen. dollars that the person with the mortgage has to pay.

Rater  Preference Human  Statement B GPT-4o  Statement B GPT-4o Mini  Statement B Llama 3.1 8b  Statement B Llama 3.1 405b Statement B Gemma 3 4b  Statement B Gemma 3 27b  Statement B

Table A4: Comparison for Pair 2: Statements 461 vs 1373 Statement A (ID: 461)  Statement B (ID: 1373)

I think that interest rates are high right The Fed looks at how the economy is pernow so trying to purchase something is forming and raises the interest rates or hard because you cant purchase as much lowers them in order to avoid inflation or of anything because of interest rates  a recession.

Rater  Preference Human  Statement B GPT-4o  Statement B GPT-4o Mini  Statement B Llama 3.1 8b  Statement B Llama 3.1 405b Statement B Gemma 3 4b  Statement B Gemma 3 27b  Statement B

Table A5: Comparison for Pair 3: Statements 1295 vs 779 Statement A (ID: 1295)  Statement B (ID: 779)

Im not sure. I know the federal reserve Interest rates are set by the Federal Redecides whether to raise, lower, or keep serve. The try to control inflation rates the same interest rates. I think they raise and economic stimulation by raising rates them when things are going well econom- for the former and lower rates for the ically and lower them when prices go up later.

on consumer goods.

Rater  Preference Human  Statement B GPT-4o  Statement B GPT-4o Mini  Statement B Llama 3.1 8b  Statement B Llama 3.1 405b Statement B Gemma 3 4b  Statement B Gemma 3 27b  Statement B

Table A6: Comparison for Pair 4: Statements 154 vs 1020 Statement A (ID: 154)  Statement B (ID: 1020)

I dont know.  Supply and demand has an impact. If demand goes down, rates will too.

Rater  Preference Human  Statement B GPT-4o  Statement B GPT-4o Mini  Statement B Llama 3.1 8b  Statement B Llama 3.1 405b Statement B Gemma 3 4b  Statement B Gemma 3 27b  Statement B

Table A7: Comparison for Pair 5: Statements 1373 vs 827 Statement A (ID: 1373)  Statement B (ID: 827)

The Fed looks at how the economy is per- When inflation goes up the interest rates forming and raises the interest rates or go up to slow down the spending.

lowers them in order to avoid inflation or a recession.

Rater  Preference Human  Statement A GPT-4o  Statement A GPT-4o Mini  Statement A Llama 3.1 8b  Statement B Llama 3.1 405b Statement A Gemma 3 4b  Statement B Gemma 3 27b  Statement A

Table A8: Comparison for Pair 1: Statements 162 vs 755 Statement A (ID: 162)  Statement B (ID: 755)

I dont know. Supply and demand  I dont know but I assume it has to do with the state of the economy and value of the US dollar and stock markets. Everything is plummeting and getting worse so in turn interest rates soar.

Rater  Preference Human  Statement A GPT-4o  Statement B GPT-4o Mini  Statement B Llama 3.1 8b  Statement B Llama 3.1 405b Statement B Gemma 3 4b  Statement B Gemma 3 27b  Statement A

##### B.5 A note on ELO

Alternative methods of rating players and predicting the probability of wins, like Elo-based approaches, are similar to the approach used here and are workable in other contexts but make less sense for this kind of application.

First, these approaches generally assume scores are updated as players face new opponents in a sequential fashion. In these cases the content of each “match” for each player is di!erent. In our case the content for each player remains the same across matches. Nor are games sequential in our case. While we could engineer sequential “games” in the data, such an iterative process would substantially increase the computational intensity of the estimation process for no clear gains in terms of estimation accuracy.

Additionally, Elo methods require users to specify a K-factor parameter, which specifies the maximum possible adjustment to an individual player’s rating resulting from a win or loss, which again assumes sequential matches between players. The approach we adopt here requires fewer assumptions on the part of the user (See Berg (2020)).

##### B.6 Resolving Ties

In our framework, we randomly assign a winner to help illustrate the simplest implementation of the procedure and one that does not introduce bias but may introduce noise. Given the relatively small number of ties in our data we can do so without significantly impacting the results. However, we could easily modify the approach we use here to use an ordered logit model in place of the binary logit. In this case outcome variables could be coded as ordered factor variables with values of “Player i loses”, “Tie”, and “Player i wins”. This approach comes at the expense of added computational intensity with some models taking at least twice as long to run as the binary logit models, but with negligible returns. For example, the correlation between the estimates of the binary logit and ordered logit for the GPT-4o models is 0.99. Alternatively, users can also prompt an LLM to resolve the ties for them before estimating the models (for more see Davidson, 1970).

##### B.7 LLM Model Details

Table A9: LLM checkpoints and quantisation details used in the study

```text
Model  Parameters  Quantisation  File size (GB) OLlama digest
Gemma-3 4B  4.3B  Q4K M  3.3  a2af6cc3
Gemma-3 27B  27.4B  Q4K M  17.4  a418f583
Llama-3.1 8B  8.0B  Q4K M  4.9  46e0c10c
Llama-3.1 405B (Fireworks)  405B  server-side bf16  n/a  fireworks.ai
GPT-4o-mini 2024-07-18  unspecified server-side bf16  n/a  OpenAI API
GPT-4o 2024-05-13  unspecified server-side bf16  n/a  OpenAI API
```

#### References

Berg, Arthur (2020, July). Statistical Analysis of the Elo Rating System in Chess. CHANCE 33 (3), 31–38.

Davidson, Roger R (1970). On extending the bradley-terry model to accommodate ties in paired comparison experiments. Journal of the American Statistical Association 65 (329), 317–328.

DiGiuseppe, Matthew and Patrick E Shea (2025). Information, uncertainty, and public support for brinkmanship during the 2023 debt limit negotiations. British Journal of Political Science 55, e14.

Meincke, Lennart , Ethan Mollick, Lilach Mollick, and Dan Shapiro (2025). Prompting science report 2: The decreasing value of chain of thought in prompting. Technical report, Generative AI Labs, The Wharton School of Business, University of Pennsylvania. SSRN Working Paper.

Wu, Patrick Y , Jonathan Nagler, Joshua A Tucker, and Solomon Messing (2023). Conceptguided chain-of-thought prompting for pairwise comparison scaling of texts with large language models. arXiv preprint arXiv:2310.12049 .

### Notes

[^1]: Corresponding Author: Matthew DiGiuseppe - [email removed]
[^2]: We randomly assign a winner to help illustrate the simplest implementation of the procedure. We discuss alternative approaches to handling ties in the Supplementary Appendix (appendix) B.6.
[^3]: When estimating the models we use broadly regularizing priors to facilitate model convergence.
[^4]: As we note below, we screened out those that have used LLMs themselves.
[^5]: The F1 score reports a balance between the model’s precision (correctness of its positive predictions) and recall (ability to identify all positive instances), representing a combined measure of the model’s accuracy!  " on the positive class. F1 Score = 2 ↓ PrecisionPrecision+Recall→Recall . Recall = True Positives+False NegativesTrue Positives  . Precision = True Positives+False PositivesTrue Positives  .
[^6]: We also compared our human raters to a chain-of-thought prompt and a reasoning model (OpenAI’s o4-mini). Neither model demonstrated an improvement over the large frontier models employed in our analysis.
[^7]: The prompt reads as follows: “You are an expert in US economic policy. Your task is to rate the given statement on a scale of 0-10 based on how knowledgeable it is in response to the following question: In a few sentences and without looking it up, can you explain how interest rates (i.e. the cost of borrowing money to buy a house or car) go up or down in the US economy? Rate the following statement on a scale of 0-10, where 0 is completely incorrect or irrelevant, and 10 is highly knowledgeable and accurate: [statement]. Respond ONLY with a single integer from 0 to 10, with no additional text.”
[^8]: The respondents were asked “People disagree about the independence of to the Federal Reserve. Do you think this independence should be decreased or increased?” after reading a vignette that describes the current independence of the Federal Reserve.
[^9]: Note that increasing comparisons will likely shrink the confidence intervals.
