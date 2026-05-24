# arXiv Submission Checklist

I cannot submit to arXiv on behalf of an author because submission requires the
author's arXiv account, authorship metadata, license choices, endorsement status,
and final human approval. This checklist keeps the project ready for submission.

## Before Submission

- Replace `Anonymous Author(s)` in `paper/main.tex`.
- Run the benchmark and replace all `TODO` placeholders with empirical results.
- Ensure the paper is an empirical benchmark/method paper rather than a pure
  position or survey article.
- Confirm that all real traces are de-identified and have redistribution rights.
- Decide primary category, likely `cs.SE`, with optional `cs.AI` or `cs.CL`.
- Prepare source, bibliography, figures, and any generated `.bbl` file.
- Compile the source locally and inspect the PDF.
- Current local compile path: `make paper`, using `tectonic`.

## Submission Package

From `paper/`, create a package containing:

- `main.tex`
- `references.bib` or generated `main.bbl`
- figures, if any
- any style files not included in standard TeX distributions

arXiv requires a source package and metadata; the source must compile to a usable
PDF before the submission leaves the working state.

## Metadata Draft

Title:

Harnessing the Vibe: Benchmarking Intervention-Driven Harness Recovery for
Coding Agents

Abstract:

Use the final abstract from `main.tex` after results are added.

Suggested categories:

- Primary: `cs.SE`
- Secondary: `cs.AI`, `cs.CL`
