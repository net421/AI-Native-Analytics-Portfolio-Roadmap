import json,tempfile,unittest
from pathlib import Path
from tools.validate_portfolio import ROOT,ValidationError,validate

class PortfolioTests(unittest.TestCase):
 def copied(self):
  import shutil
  t=tempfile.TemporaryDirectory(); dst=Path(t.name)/'repo'; shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns('.git','__pycache__')); return t,dst
 def test_current_portfolio_passes(self):
  self.assertEqual(validate()['status'],'pass')
 def test_missing_active_repository_fails(self):
  t,d=self.copied(); data=json.loads((d/'PORTFOLIO_RELEASE_LEDGER.json').read_text()); data['active_repositories'].pop(); (d/'PORTFOLIO_RELEASE_LEDGER.json').write_text(json.dumps(data));
  with self.assertRaises(ValidationError): validate(d)
  t.cleanup()
 def test_bad_release_sha_fails(self):
  t,d=self.copied(); data=json.loads((d/'PORTFOLIO_RELEASE_LEDGER.json').read_text()); data['active_repositories'][1]['commit_sha']='bad'; (d/'PORTFOLIO_RELEASE_LEDGER.json').write_text(json.dumps(data));
  with self.assertRaises(ValidationError): validate(d)
  t.cleanup()
 def test_frozen_mutation_target_fails(self):
  t,d=self.copied(); data=json.loads((d/'PORTFOLIO_RELEASE_LEDGER.json').read_text()); data['frozen_historical_repositories'][0]['implementation_backlog']=True; (d/'PORTFOLIO_RELEASE_LEDGER.json').write_text(json.dumps(data));
  with self.assertRaises(ValidationError): validate(d)
  t.cleanup()
 def test_dependency_on_frozen_fails(self):
  t,d=self.copied(); data=json.loads((d/'PORTFOLIO_RELEASE_LEDGER.json').read_text()); data['active_repositories'][1]['strict_dependencies']=[data['frozen_historical_repositories'][0]['name']]; (d/'PORTFOLIO_RELEASE_LEDGER.json').write_text(json.dumps(data));
  with self.assertRaises(ValidationError): validate(d)
  t.cleanup()

if __name__=='__main__': unittest.main()
