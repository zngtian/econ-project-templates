# Release Notes

## v0.6.4 -- March 2023

Incorporate more feedback from EPP students, @janosg:

- Fix paths for LaTeX files (#133).
- Fix GHA workflow (#134).
- Pre-commit autoupdate / fix ruff complaints.
- Use default sequence style of yamlfix.

## v0.6.3 -- January 2023

Incorporate more feedback from EPP students, @janosg:

- Do not add linters by default, but give an option to add them.
- Add github actions back in, make codecov meaningful.

## v0.6.2 -- January 2023

Incorporate feedback from EPP students, @janosg, @tobiasraabe.

- Update warning message for R, better explanations for examples and links to issues.
- Add scripts as explicit dependencies.
- Use git_remote_url option again.
- Add yaml linters, run them. Update versions of pre-commit hooks also in inner project.
- Ditch flake8 in favor of ruff.
- Get rid of refurb's complaints.
- Ignore complexity in post_gen_project.

## v0.6 -- December 2022

- Add R example (#105, @carolinalvarez, @timmens)
- Complete re-write of example, structure, docs (#98, #108, #111, #115, #118, #119, @timmens)
- Convert Documentation from reST to Markdown (#117, @mj023)

## v0.5 -- January 2022

- Move to plotly (#92, @timmens)
- Cleaning up (@hmgaudecker)

## v0.4 -- January 2021

- Move from Waf to Pytask (#86, @tobiasraabe, @hmgaudecker)
- Move to GitHub Actions for CI (@janosg, WIP)

## v0.3 -- October 2019

- Much improved documentation (@raholler)
- Extensive instructions for use on Windows (@raholler)
- Re-use previously-entered data when cookiecutter fails
  (@tobiasraabe, @raholler)
- Fix Stata template by setting <span
  class="title-ref">--shell-escape=1</span> (#63, @raholler)
- Add pyupgrade to pre-commit hooks (#59)
- Thanks to students at LMU for pointing lots of this out!

## v0.2 -- September 2019

- Full continuous integration testing on the Azure platform
- R example completely working in Miniconda environment out of the
  box (@raholler)
- Documentation for Stata / R examples (@raholler)
- Much improved instructions for usage on Windows (@raholler)
- Improved structure of docs

## v0.1 -- October 2018

- First version with cookiecutter (thanks, @tobiasraabe
  and @julienschat)
- All the stuff that accumulated over the years with the help of many.
  I wish my memory was better so I would be able to list the
  contributions separately. Thanks, @PKEuS, @philippmuller,
  @julienschat, @janosg, @tdrerup and many more who provided feedback!
