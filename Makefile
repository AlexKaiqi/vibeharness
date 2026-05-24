.PHONY: validate i18n-check links-check example report paper arxiv episode score-episode clean

validate:
	python3 -m vibeharness.cli validate

i18n-check:
	python3 -m vibeharness.cli i18n

links-check:
	python3 -m vibeharness.cli links

example:
	cd examples/fixtures/todo_cli && python3 tests/test_visible.py && python3 tests/test_acceptance.py
	python3 scripts/vh_score_episode.py examples/episodes/todo_cli_spec_capture

report:
	python3 -m vibeharness.cli report

paper:
	tectonic paper/main.tex --keep-logs --keep-intermediates

arxiv:
	bash scripts/build_arxiv_bundle.sh

episode:
	python3 -m vibeharness.cli start --request "$${REQUEST:-Manual VibeHarness episode}"

score-episode:
	@test -n "$$EPISODE" || (echo "Set EPISODE=.vibeharness/episodes/<id>" && exit 1)
	python3 -m vibeharness.cli score "$$EPISODE"

clean:
	rm -f paper/*.aux paper/*.bbl paper/*.blg paper/*.log paper/*.out paper/*.toc paper/*.xdv
