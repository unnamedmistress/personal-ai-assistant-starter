# Set up one personal AI assistant workflow

Choose a task you already do, such as preparing a weekly project update from a set of notes. Start with fictional notes so you can practice without sharing private information.

## Define the job

Copy [workflow.md](../templates/workflow.md) into a private folder. Write down the input, the draft you want, the decisions that belong to you, and what would count as finished. Keep the task small enough that you can inspect the whole result.

## Choose the source

Fill in [source-map.md](../templates/source-map.md). Give each fact one current home. If two sources disagree and you cannot tell which is current, mark the fact as unresolved. Ask for the missing evidence instead of combining the two versions.

## Set the approval boundary

Fill in [approval-rules.md](../templates/approval-rules.md). Start with drafting and analysis. Keep sending, publishing, spending, and account changes outside the assistant’s authority unless you have deliberately approved the exact action. These notes do not change tool permissions.

## Save the reason for a decision

Use [decision-record.md](../templates/decision-record.md) to record the choice, why you made it, what you assumed, and what new evidence would make you reconsider. Use [learning-record.md](../templates/learning-record.md) for a possible lesson that has not yet earned the status of a lasting rule.

## Try the failure exercises

Read the [three exercises](../examples/README.md). If you have Python, run `python run_examples.py` from the repository folder. You can also read each JSON record as text. The expected results are in [expected-results.json](../examples/expected-results.json).

To test your own assistant, give it a fictional flawed record and the task described in the exercise. Record its first answer without editing it. Compare it with the stated rule. Keep model errors in the record; changing an answer until it passes is not proof that the first attempt worked.

## Check the result and leave a restart point

Fill in [completion-record.md](../templates/completion-record.md). Keep the result, evidence, and missing checks separate. Then save [restart-note.md](../templates/restart-note.md) with the exact next step. Resume from that note after checking whether the source or task has changed.

## Get help with your own setup

Use the starter on your own, or bring your workflow to [Personal AI Assistant Coaching](https://www.myaievolution.com/ai-assistant-coaching?utm_source=github&utm_medium=referral&utm_campaign=personal_ai_assistant_starter&utm_content=start_here). The free examples do not need coaching to run.
