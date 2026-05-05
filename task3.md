# Task #3

> Read the paper “Towards a Science of AI Agent Reliability”. Write a short, multi-paragraph summary of the paper and describe the main findings of the work.

The paper addresses the issue of model peformance in benchmarks, as compared to their performance in real-world production scenarios by presenting a new evaluation framework, which takes inspiration from safety-critical engineering principles in other industries (e. g. aviation, ICS, automotive).

The authors claim that accuracy is no longer the only important metric for modern LLM/agentic systems. Increases in model accuracy in the past few years do not inherently translate to an increase model reliability. Accuracy does not distinguish between benign failiures and catastrophic ones (e. g. incomplete output against database deletion).

The two main contributions of the paper are:

- A formal taxonomy and suite of metrics for model evaluation;
- A comprehensive reliablity profile of modern agents, based on the proposed evaluation framework.

For the first contribution - the notion of (model) reliability is further deconstructed into four distinct dimensions: _consistency_ (similar results under identical conditions), _robustness_ (performance under different adverse conditions), _predictability_ (expressed confidence against actual performance) and _safety_ (severity and frequency of harmful behaviours). The authors note that this framework measures aspects which are independent of raw capability. For example, a highly capable system can still be highly unreliable. The authors do not disregard the importance of model accuracy, but stress that accuracy is not a substitution for reliability, and vice versa.

From the four dimensions, care is taken to explain the importance of model _safety_. The authors claim that it is a distinc metric that should not be averaged/aggregated with the rest of the dimensions. In safety-critical systems, from which the framework in question is grounded in, this metric is quintessential. Furthremore, it is important to investigate each individual metric for different deployment scenarios, as the overall average may be misleading for certain use-cases.

For the second contribution - the authors evaluate 14 models, and found that:

- **consistency** remains low across all evaluated models;
- **robustness** - many models remain susceptible to surface-level prompt reformulations;
- **predictability** - models have become more predictable;
- **safety** - newest models have significantly lower violation rates, and violations that do occur are mostly of low-moderate severity. However, the threat of high-stakes violations remains (such as the 2025 Replit's AI incident).

According to the authors, the findings suggest that "_improving raw task performance may not be sufficient for building dependable AI agents_".

Finally, the evaluation framework as it is proposed may have different framings or decompositions. The authors claim that instead the most important idea is the "core shift in perspective", upon which further work in the field of AI agent evaluation can build upon.
