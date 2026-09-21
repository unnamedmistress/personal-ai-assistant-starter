"""Run the fixed educational fixtures without network access or model calls."""

import json
from pathlib import Path

from checks import CHECKS


def main():
    folder = Path(__file__).resolve().parent / 'examples'
    expected = json.loads((folder / 'expected-results.json').read_text(encoding='utf-8'))
    failures = 0
    print('FICTIONAL FIXTURES ONLY. These checks do not test a live AI assistant.')
    for name, check in CHECKS.items():
        records = json.loads((folder / f'{name}.json').read_text(encoding='utf-8'))
        for variant in ('flawed', 'corrected'):
            result = check(records[variant])
            observed = {'accepted': result.accepted, 'reason': result.reason}
            matches = observed == expected[f'{name}.{variant}']
            failures += not matches
            print(f'{name}.{variant}: {"PASS" if matches else "FAIL"} | {result.reason}')
    print('PASS means the checker matched the expected fixture result, including expected rejections.')
    print('No delivery, model behavior, source truth, or business result was verified.')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
