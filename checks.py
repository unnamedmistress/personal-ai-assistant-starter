"""Bounded rules for fictional records, not a live agent permission system."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Result:
    accepted: bool
    reason: str


def reject(reason):
    return Result(False, reason)


def exact(value, keys):
    return isinstance(value, dict) and set(value) == set(keys)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def money(value):
    return type(value) is int and value >= 0


def check_source(record):
    """Compare a structured answer with a caller-supplied fictional catalog."""
    if not exact(record, ('sources', 'answer')):
        return reject('invalid_record')
    sources, answer = record['sources'], record['answer']
    if not isinstance(sources, list) or not sources:
        return reject('invalid_sources')
    for source in sources:
        if not exact(source, ('id', 'status', 'price')):
            return reject('invalid_source')
        if not text(source['id']) or source['status'] not in ('current', 'superseded') or not money(source['price']):
            return reject('invalid_source')
    if len({s['id'] for s in sources}) != len(sources):
        return reject('duplicate_source')
    current = [s for s in sources if s['status'] == 'current']
    if len(current) != 1:
        return reject('ambiguous_current_source')
    if not exact(answer, ('source_id', 'price')) or not text(answer['source_id']) or not money(answer['price']):
        return reject('invalid_answer')
    if answer['source_id'] != current[0]['id']:
        return reject('not_current_source')
    if answer['price'] != current[0]['price']:
        return reject('price_mismatch')
    return Result(True, 'fixture_source_consistent')


def check_completion(record):
    """Check fixture consistency only. No real delivery or permission is verified."""
    if not exact(record, ('expected_destination', 'artifact_version', 'claimed_state', 'delivery')):
        return reject('invalid_record')
    if not text(record['expected_destination']) or not text(record['artifact_version']):
        return reject('invalid_target')
    if record['claimed_state'] != 'complete':
        return reject('not_completion_claim')
    delivery = record['delivery']
    if delivery is None:
        return reject('missing_delivery_evidence')
    if not exact(delivery, ('kind', 'destination', 'artifact_version', 'state', 'receipt_id')):
        return reject('invalid_delivery_record')
    if delivery['kind'] != 'synthetic_delivery':
        return reject('not_synthetic_delivery_record')
    if not text(delivery['receipt_id']):
        return reject('missing_receipt_id')
    if delivery['state'] != 'delivered':
        return reject('delivery_not_successful')
    if delivery['destination'] != record['expected_destination']:
        return reject('destination_mismatch')
    if delivery['artifact_version'] != record['artifact_version']:
        return reject('artifact_version_mismatch')
    return Result(True, 'fixture_delivery_consistent_not_live_proof')


def check_learning(record):
    """Check declared review fields, not the truth or independence of real events."""
    if not exact(record, ('proposed_status', 'confirmations', 'owner_approved', 'regression_passed')):
        return reject('invalid_record')
    if record['proposed_status'] != 'standing_rule':
        return reject('not_standing_rule_proposal')
    confirmations = record['confirmations']
    if not isinstance(confirmations, list):
        return reject('invalid_confirmations')
    for item in confirmations:
        if not exact(item, ('id', 'source_id', 'independently_reviewed')):
            return reject('invalid_confirmation')
        if not text(item['id']) or not text(item['source_id']) or type(item['independently_reviewed']) is not bool:
            return reject('invalid_confirmation')
    if len(confirmations) < 2:
        return reject('insufficient_confirmations')
    if len({c['id'] for c in confirmations}) != len(confirmations):
        return reject('duplicate_confirmation')
    if len({c['source_id'] for c in confirmations}) != len(confirmations):
        return reject('duplicate_confirmation_source')
    if not all(c['independently_reviewed'] is True for c in confirmations):
        return reject('independent_review_missing')
    if record['owner_approved'] is not True:
        return reject('owner_approval_missing')
    if record['regression_passed'] is not True:
        return reject('regression_evidence_missing')
    return Result(True, 'fixture_learning_gate_satisfied')


CHECKS = {'source': check_source, 'completion': check_completion, 'learning': check_learning}
