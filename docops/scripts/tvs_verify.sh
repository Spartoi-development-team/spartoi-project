#!/usr/bin/env bash
set -euo pipefail
TASK_ID="$1"
TD="$(pwd)/docops/evidence/$TASK_ID"

echo -e "\n===== TVS Verify: $TASK_ID =====\n"

for f in input_manifest.json run_manifest.json settings_evidence.json gate_report.json verdict.json; do
    test -f "$TD/$f" && echo "✅ $f" || { echo "❌ $f MISSING"; exit 2; }
done

grep -q "PASS" "$TD/gate_report.json" && echo "✅ gate_report PASS" || { echo "❌ gate_report FAIL"; exit 2; }
grep -q "PASS" "$TD/verdict.json" && echo "✅ verdict PASS" || { echo "❌ verdict FAIL"; exit 2; }
grep -q "merge_group" .github/workflows/docops-gatekit.yml && echo "✅ merge_group in workflow" || { echo "❌ merge_group MISSING"; exit 2; }

echo -e "\n✅ TVS VERIFY: ALL PASS\n"
