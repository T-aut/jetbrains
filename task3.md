# Task #3

> Read the paper “Towards a Science of AI Agent Reliability”. Write a short, multi-paragraph summary of the paper and describe the main findings of the work.

The paper "Towards a Science of AI Agent Reliability" addresses the issue of model peformance in benchmarks, as compared to their performance in real-world production scenarios by presenting a new evaluation framework, which takes inspiration from safety-critical engineering principles in other industries (e. g. aviation, ICS, automotive).

The authors claim that accuracy is no longer a viable metric for modern LLM/agentic systems. Increases in model accuracy in the past few years do not inherently translate to an increase model reliability. Accuracy does not distinguish between benign failiures and catastrophic ones (e. g. incomplete output vs deleting a DB).

The two main contributions of the paper are:

- A formal taxonomy and suite of metrics for model evaluation;
- A comprehensive reliablity profile of modern agents, based on the proposed evaluation framework.

For the first contribution - the notion of (model) reliability is further deconstructed into four distinct dimensions: _consistency_ (similar results under identical conditions), _robustness_ (performance under different adverse environments), _predictability_ (expressed confidence against actual performance) and _safety_ (severity and frequency of harmful behaviours). The authors note that this framework measure aspects which are independent of raw capability. For example, a highly capable system can still be highly unreliable, and a less "smart and capable" system may prove to be very reliable. The authors do not disregard the importance of model accuracy, but stress that accuracy is not a substitution for reliability, and vice versa.

From the four dimensions, the authors take care to explain the importance of model _safety_. The authors claim that it is a distinc metric that should not be averaged/aggregated with the rest of the dimensions. In safety-critical systems, from which the framework in question is grounded in, this metric is non-negiotable. It is important to investigate each individual metrics for different deployment scenarios, as the overall average may be misleading for certain use-cases.

For the second contribution - the authors evaluate 14 models ...

// RATHER instead of conclusion, write a finally section that "this is not the end-all framework"

In conclusion, the rapid gains of model capability have not yielded similar gains in model reliability. High accuracy does not mean a model is more consistent, robust to prompt variations, or will succeed in _N_ amount of steps each time. The authors propose an evaluation framework, which goes beyond the metric accuracy, but also evaluates how consistent, robust and most importantly safe an agentic system is. This is not a framework to end all future frameworks, but rather a "core shift in perspective", upon which future work in the field of AI Agent evaluation should build upon.

? during experiments they create prompt pertrubations using another LLM, how is this sound methodically? How to verify theyre semantically correct?
