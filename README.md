# Build a personal AI assistant you can check

Set up a personal AI assistant around your real work, with clear sources, approval rules, and a way to check what it has done.

I’m Chrysti Reichert, founder of [My AI Evolution](https://www.myaievolution.com/?utm_source=github&utm_medium=referral&utm_campaign=personal_ai_assistant_starter&utm_content=readme_intro). I teach people how to use AI, catch its mistakes, and keep control of the work. This free starter draws on the design of my own working system, My AI Evolution OS.

Use it to plan one workflow, keep the facts in a known place, decide what needs your approval, and check the result. The files are yours to adapt under the [MIT license](LICENSE). You do not need to buy coaching to use them.

## Start with one real workflow

Open [Start here](docs/start-here.md). Copy the [workflow template](templates/workflow.md) into your own private folder and fill it in with a task you already handle. The guide links to each supporting template. You can read and edit the Markdown files as plain text; no code setup is needed for this part.

Keep private work out of public repositories and issue reports. Use fictional data while learning. An AI tool may store what you share according to its own settings and terms, so check those before using real business information.

## Try three failure exercises

An assistant uses an old price. It says a draft has been delivered. It treats a lesson from one attempt as a permanent rule. Each [fictional exercise](examples/README.md) includes a flawed record, a corrected record, and a specific expected result.

The Python checker tests these records against fixed rules. It does not call an AI, connect to your accounts, send anything, or prove that a real assistant will follow the rules. Read [what the checks prove](docs/verification.md) before using the results.

With Python 3.11 or newer installed, download this repository using GitHub’s **Code → Download ZIP**, extract it, and open a terminal in the extracted folder. Run the exercises:

```sh
python run_examples.py
```

Run the regression tests:

```sh
python -m unittest discover -s tests -v
```

On systems where Python is named `python3`, use that command instead. On Windows, `py -3` may be available. There are no third-party Python packages to install. The fixture checks use no paid services. If you later try the prompts with an AI assistant, that tool may require a subscription or charge for usage.

## What makes this approach different?

The method connects source checking, human approval, and proof of completion. It also treats a lesson from one attempt as something to check before making it a lasting rule. The point is to make those checks usable in your own work.

Personal AI systems, memory, and approval flows already exist. This starter makes no claim to have invented them. See [related work and sources](docs/sources.md) for the tools and ideas that help put this approach in context.

## How do I check an AI assistant’s memory?

Give it an old note and a clearly marked current source. Ask it to use the current information and name the source. Compare its answer with the source yourself. The [source map](templates/source-map.md) helps you decide which document owns each fact and when it needs another check.

## How do I know a task is finished?

Define what finished means before the assistant starts. A completed draft proves a draft exists. An approved delivery needs evidence of delivery to the right destination. The [completion record](templates/completion-record.md) keeps those facts separate.

## How do I set approval rules?

Use the [approval template](templates/approval-rules.md) to record what the assistant can prepare and what needs your review. Written instructions guide behavior; they do not enforce account permissions. The code in this repository does not connect these rules to tools or accounts.

## Can these checks prevent every AI mistake?

No. Passing a fixture test means that the sample checker handled that record as expected. It does not prove that a model is reliable, a delivery occurred, or a source is true. You still need to check the evidence for your actual task. Missing evidence stays unknown.

## Build your own setup with me

Bring a real workflow to [Personal AI Assistant Coaching at My AI Evolution](https://www.myaievolution.com/ai-assistant-coaching?utm_source=github&utm_medium=referral&utm_campaign=personal_ai_assistant_starter&utm_content=readme). I’ll work with you to set up an assistant for your business and practice checking its work. You keep the decisions that belong to you.

## Project scope and support

This is an educational starter, not a hosted service or a security product. The templates are tool-neutral. The automated examples test local Python rules only; they do not certify compatibility with any AI product. See [support and contributions](CONTRIBUTING.md) before opening an issue, and [security reporting](SECURITY.md) if you find a security concern. Coaching is optional and separate from community support.
