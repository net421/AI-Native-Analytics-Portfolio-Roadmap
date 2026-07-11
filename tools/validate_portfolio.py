from __future__ import annotations
import csv,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LEDGER=ROOT/'PORTFOLIO_RELEASE_LEDGER.json'
CSV_LEDGER=ROOT/'PORTFOLIO_EVIDENCE_LEDGER.csv'
EXACT_FROZEN_RULE='Los siete repositorios históricos aportan evidencia al portafolio, pero permanecen fuera del backlog de implementación, corrección, estandarización y publicación.'
REQUIRED_DOCS=['README.md','ROADMAP.md','INTEGRATION_ARCHITECTURE.md','FROZEN_HISTORICAL_REPOSITORIES.md','PORTFOLIO_EVIDENCE.md','RECRUITER_GUIDE.md','JOB_TARGETS.md','SKILL_COVERAGE_MATRIX.md','BACKLOG.md','PUBLISHING_CHECKLIST.md']
class ValidationError(Exception): pass

def validate(root:Path=ROOT)->dict:
 data=json.loads((root/'PORTFOLIO_RELEASE_LEDGER.json').read_text())
 active=data['active_repositories']; frozen=data['frozen_historical_repositories']
 errors=[]
 if len(active)!=12 or data.get('active_repository_count')!=12: errors.append('active repository count must be 12')
 if len(frozen)!=7 or data.get('frozen_repository_count')!=7: errors.append('frozen repository count must be 7')
 names=[x['name'] for x in active]
 fnames=[x['name'] for x in frozen]
 if len(set(names))!=12: errors.append('active names must be unique')
 if len(set(fnames))!=7: errors.append('frozen names must be unique')
 if set(names)&set(fnames): errors.append('active and frozen sets overlap')
 cats={c:sum(x['category']==c for x in active) for c in ['control_plane','foundational','ai_native']}
 if cats!={'control_plane':1,'foundational':6,'ai_native':5}: errors.append(f'invalid category counts: {cats}')
 for x in active:
  if x['status']!='complete_for_portfolio_scope': errors.append(f"{x['name']}: invalid status")
  if not x['url'].startswith('https://github.com/net421/'): errors.append(f"{x['name']}: invalid URL")
  if x['name']=='AI-Native-Analytics-Portfolio-Roadmap':
   if x.get('commit_ref')!='main': errors.append('Roadmap must reference main')
  elif not re.fullmatch(r'[0-9a-f]{40}',x.get('commit_sha','')): errors.append(f"{x['name']}: invalid release SHA")
  for dep in x.get('strict_dependencies',[]):
   if dep not in names: errors.append(f"{x['name']}: unknown active dependency {dep}")
   if dep in fnames: errors.append(f"{x['name']}: dependency on frozen repository {dep}")
 for x in frozen:
  if x.get('lifecycle')!='historical_frozen' or x.get('immutable') is not True or x.get('implementation_backlog') is not False:
   errors.append(f"{x['name']}: frozen policy violated")
 for doc in REQUIRED_DOCS:
  if not (root/doc).is_file(): errors.append(f'missing document {doc}')
 readme=(root/'README.md').read_text()
 frozen_doc=(root/'FROZEN_HISTORICAL_REPOSITORIES.md').read_text()
 if EXACT_FROZEN_RULE not in readme or EXACT_FROZEN_RULE not in frozen_doc: errors.append('exact frozen-repository rule missing')
 with (root/'PORTFOLIO_EVIDENCE_LEDGER.csv').open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
 if {r['repository'] for r in rows}!=set(names): errors.append('CSV ledger must cover exactly 12 active repositories')
 if any(r['status']!='complete_for_portfolio_scope' for r in rows): errors.append('CSV ledger contains non-final status')
 if data['claim_boundary'].get('autonomous_operational_actions') is not False: errors.append('autonomous operational actions must remain false')
 if errors: raise ValidationError('; '.join(errors))
 return {'status':'pass','active_repositories':len(active),'frozen_repositories':len(frozen),'category_counts':cats,'strict_dependency_edges':sum(len(x.get('strict_dependencies',[])) for x in active),'documents_validated':len(REQUIRED_DOCS)}

def main():
 try: print(json.dumps(validate(),indent=2,sort_keys=True))
 except ValidationError as e:
  print(str(e),file=sys.stderr); raise SystemExit(1)
if __name__=='__main__': main()
