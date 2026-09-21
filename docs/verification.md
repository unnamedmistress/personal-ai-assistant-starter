# What the checks prove

This package has three parts. The forms guide you and your assistant. The Python code checks fixed rules on made-up records. You must still check proof from a real source or service. None of these parts can stand in for all the others.

## Current-source check

The made-up catalog marks one source as current. The code checks the chosen source and price against that catalog. It rejects an old source even when the old price matches that source. It also rejects a wrong price or an unknown source. If two sources are marked current, it rejects the record.

This checks a price field. It does not read a whole document for meaning. Someone supplied the catalog’s current label. The code cannot prove that the label is true or that a real business changed its price.

## Completion check

The code checks a made-up claim against a made-up send record. It checks where the file went, which version was sent, and whether the send passed. A draft is not enough. Missing proof, a failed send, and the wrong target or version all fail the check.

All send records here are made up. A passing check means the fields match the rule. No real send or lookup took place. No person received a message. A pass does not grant permission to contact anyone. A forged record could pass too. Real work needs a trusted source outside this sample.

## Learning check

The code asks for two distinct confirming records, each marked as reviewed. It also asks for owner approval and a passed test of the proposed rule. Duplicate record IDs or source IDs fail the check. These are sample IDs. The code cannot prove that the real events are separate or true.

The count of two is a teaching rule for this starter. It is not a scientific test of truth. A person must judge whether the lesson makes sense and when to retire it.

## Record an actual assistant trial

Use [assistant-trial.md](../templates/assistant-trial.md) to record your trial. Save the tool, model if known, date, and exact made-up inputs. Keep the first answer and compare it with what you expected. One good answer does not prove that a tool is supported for every task.

## What is outside scope?

The code does not block tool calls or set permissions on an AI platform. It cannot catch every false claim, verify email, or stop prompt injection. Do not give it passwords or API keys. The automated tests check this code and its sample records. They do not test a live assistant or a real business process.
