import copy
import json
from pathlib import Path
import unittest

from checks import CHECKS, check_completion, check_learning, check_source


FOLDER = Path(__file__).resolve().parents[1] / 'examples'


def fixture(name, variant='corrected'):
    return json.loads((FOLDER / f'{name}.json').read_text(encoding='utf-8'))[variant]


class CheckTests(unittest.TestCase):
    def test_all_expected_fixture_results(self):
        expected = json.loads((FOLDER / 'expected-results.json').read_text(encoding='utf-8'))
        for name, check in CHECKS.items():
            for variant in ('flawed', 'corrected'):
                with self.subTest(name=name, variant=variant):
                    result = check(fixture(name, variant))
                    self.assertEqual({'accepted': result.accepted, 'reason': result.reason}, expected[f'{name}.{variant}'])

    def test_malformed_top_level(self):
        for check in CHECKS.values():
            for record in (None, [], '', True, 12, {}):
                with self.subTest(check=check.__name__, record=record):
                    self.assertFalse(check(record).accepted)

    def test_unknown_fields_rejected(self):
        for name, check in CHECKS.items():
            data = fixture(name)
            data['trust_me'] = True
            self.assertEqual(check(data).reason, 'invalid_record')

    def test_inputs_not_modified(self):
        for name, check in CHECKS.items():
            data = fixture(name)
            before = copy.deepcopy(data)
            check(data)
            self.assertEqual(data, before)

    def test_no_current_source(self):
        data = fixture('source')
        data['sources'][1]['status'] = 'superseded'
        self.assertEqual(check_source(data).reason, 'ambiguous_current_source')

    def test_conflicting_current_sources(self):
        data = fixture('source')
        data['sources'][0]['status'] = 'current'
        self.assertEqual(check_source(data).reason, 'ambiguous_current_source')

    def test_duplicate_source_ids(self):
        data = fixture('source')
        data['sources'][0]['id'] = data['sources'][1]['id']
        self.assertEqual(check_source(data).reason, 'duplicate_source')

    def test_unknown_source(self):
        data = fixture('source')
        data['answer']['source_id'] = 'unknown'
        self.assertEqual(check_source(data).reason, 'not_current_source')

    def test_wrong_price(self):
        data = fixture('source')
        data['answer']['price'] = 80
        self.assertEqual(check_source(data).reason, 'price_mismatch')

    def test_invalid_prices(self):
        for value in (True, '95', -1, 95.0, None):
            data = fixture('source')
            data['answer']['price'] = value
            self.assertFalse(check_source(data).accepted)

    def test_missing_nested_source_field(self):
        data = fixture('source')
        del data['sources'][0]['price']
        self.assertEqual(check_source(data).reason, 'invalid_source')

    def test_wrong_destination(self):
        data = fixture('completion')
        data['delivery']['destination'] = 'other@example.invalid'
        self.assertEqual(check_completion(data).reason, 'destination_mismatch')

    def test_wrong_artifact_version(self):
        data = fixture('completion')
        data['delivery']['artifact_version'] = 'fictional-brief-v1'
        self.assertEqual(check_completion(data).reason, 'artifact_version_mismatch')

    def test_failed_or_draft_delivery(self):
        for state in ('draft', 'failed', 'queued', None):
            data = fixture('completion')
            data['delivery']['state'] = state
            self.assertEqual(check_completion(data).reason, 'delivery_not_successful')

    def test_receipt_required(self):
        data = fixture('completion')
        data['delivery']['receipt_id'] = ' '
        self.assertEqual(check_completion(data).reason, 'missing_receipt_id')

    def test_no_claim_of_real_evidence(self):
        data = fixture('completion')
        data['delivery']['kind'] = 'real_delivery'
        self.assertEqual(check_completion(data).reason, 'not_synthetic_delivery_record')

    def test_missing_delivery_field(self):
        data = fixture('completion')
        del data['delivery']['destination']
        self.assertEqual(check_completion(data).reason, 'invalid_delivery_record')

    def test_duplicate_confirmation(self):
        data = fixture('learning')
        data['confirmations'][1]['id'] = data['confirmations'][0]['id']
        self.assertEqual(check_learning(data).reason, 'duplicate_confirmation')

    def test_duplicate_confirmation_source(self):
        data = fixture('learning')
        data['confirmations'][1]['source_id'] = data['confirmations'][0]['source_id']
        self.assertEqual(check_learning(data).reason, 'duplicate_confirmation_source')

    def test_independent_review_required(self):
        data = fixture('learning')
        data['confirmations'][0]['independently_reviewed'] = False
        self.assertEqual(check_learning(data).reason, 'independent_review_missing')

    def test_approval_must_be_true_boolean(self):
        for value in (False, 'true', 1, None):
            data = fixture('learning')
            data['owner_approved'] = value
            self.assertEqual(check_learning(data).reason, 'owner_approval_missing')

    def test_regression_must_be_true_boolean(self):
        for value in (False, 'true', 1, None):
            data = fixture('learning')
            data['regression_passed'] = value
            self.assertEqual(check_learning(data).reason, 'regression_evidence_missing')

    def test_review_must_be_boolean(self):
        data = fixture('learning')
        data['confirmations'][0]['independently_reviewed'] = 'true'
        self.assertEqual(check_learning(data).reason, 'invalid_confirmation')


if __name__ == '__main__':
    unittest.main()
