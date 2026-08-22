#!/usr/bin/env node
// Fetch and normalize India Post pincode data from api.postalpincode.in.
// No API key needed. Requires Node 18+ (built-in fetch).
//
// Usage:
//   node scripts/fetch-pincode.js 560001
//   node scripts/fetch-pincode.js --selftest

const assert = require('node:assert');

function normalizePincodeResponse(raw) {
  const result = Array.isArray(raw) ? raw[0] : raw;
  if (!result || result.Status !== 'Success') {
    return { status: 'error', pincode: null, offices: [] };
  }
  return {
    status: 'ok',
    pincode: result.PostOffice?.[0]?.Pincode ?? null,
    offices: (result.PostOffice || []).map((po) => ({
      name: po.Name,
      branchType: po.BranchType,
      district: po.District,
      state: po.State,
    })),
  };
}

function selftest() {
  const sample = [{
    Status: 'Success',
    PostOffice: [
      { Name: 'Rajajinagar', Pincode: '560010', BranchType: 'Sub Post Office', District: 'Bangalore', State: 'Karnataka' },
    ],
  }];
  const out = normalizePincodeResponse(sample);
  assert.strictEqual(out.status, 'ok');
  assert.strictEqual(out.pincode, '560010');
  assert.strictEqual(out.offices.length, 1);
  assert.strictEqual(out.offices[0].state, 'Karnataka');

  const bad = normalizePincodeResponse([{ Status: 'Error' }]);
  assert.strictEqual(bad.status, 'error');
  assert.strictEqual(bad.offices.length, 0);

  console.log('selftest passed');
}

async function main() {
  const arg = process.argv[2];
  if (!arg || arg === '--selftest') {
    selftest();
    return;
  }
  const res = await fetch(`https://api.postalpincode.in/pincode/${arg}`);
  const raw = await res.json();
  console.log(JSON.stringify(normalizePincodeResponse(raw), null, 2));
}

if (require.main === module) {
  main().catch((err) => {
    console.error(err.message);
    process.exit(1);
  });
}

module.exports = { normalizePincodeResponse };
