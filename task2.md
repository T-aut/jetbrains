# Task #2

> Write a short report of a maximum of one page describing your observations and interesting findings.

The tool was run for the top five models on the leaderboard for mini-SWE-agent-v2. There were two main findings I found interesting.

First, for all five models the number of system (prompt) and user messages are (practically) close to a ratio of 1:1. This means that for each test run, on average a single user-provided prompt (such as a link to a pull request) was enough for the models to reason and achieve the intended outcome.

Secondly, the number of `assistant` and `tool` messages differs significantly between certain models. From the test run, all **high-reasoning** models proved to contain more messages of those types (around 55-60 per trajectory), while Opus 4.6 and GPT-5-2-Codex had the average number of assistant and tool messages at around 30 to 35 per trajectory. The "verbosity" of high-reasoning models is also reflected in the total messages per trajectory average.

The output of the tool provides a decent basis for exploratory data analysis, however more refined metrics would be needed for a coherent performance evaluation.
