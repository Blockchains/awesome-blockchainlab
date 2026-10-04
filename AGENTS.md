# AGENTS.md: awesome-blockchainlab

Instructions for AI coding agents (Grok, Cursor, Claude Code, Codex, Copilot and others) working **in** this repo or **using it as a building block**. Humans: see [README.md](README.md).

## What this is

Curated list of 225 open-source blockchain projects (+11 extended) forked under Blockchains and kept in sync by fork-sync, with a machine-readable forge.json (fork, upstream, category, licence, stars, docs, starters, index links).

- Kind: curated-list, dataset · stability: `stable` · licence: CC0-1.0
- Machine-readable manifest: [`blocks.json`](blocks.json) (schema: [BLOCKS-SCHEMA](https://github.com/Blockchains/.github/blob/main/docs/BLOCKS-SCHEMA.md))
- How it fits with the other Blockchains repos: [Build with Blocks](https://github.com/Blockchains/.github/blob/main/docs/BUILD-WITH-BLOCKS.md)

## Setup

```bash
python3 --version
```

## Build and test

```bash
python3 scripts/validate.py   # schema + every fork/upstream reachable
```

Tests hit **live** public networks/APIs (the org rule is no mocks). A failure can be an upstream outage: re-run before changing code.

## Structure

| Path | What |
|---|---|
| `README.md` | the list |
| `forge.json` | machine-readable list |
| `scripts/validate.py` | validator used by CI |

## Conventions

- README and forge.json must list the same forks.
- Selection: OSI licence, ≥1,000 stars (few documented exceptions), active in the last 90 days, not archived.

## Extension points

- Add a fork: fork it under Blockchains, add it to fork-sync forks.json and blockchainlab-index sources, then to forge.json + README.

## Do

- Run the validator before pushing.

## Don't

- Add a fork that fails the list's criteria (licence, stars, activity, not archived) without updating the criteria text.
- Commit secrets, keys or `.env` files. Run `gitleaks` before pushing; CI and the org policy reject leaks.

## Using it from another project

- **forge.json** (file): `https://raw.githubusercontent.com/Blockchains/awesome-blockchainlab/main/forge.json`
- **README.md** (file): `human-readable list by category`

See the README section [Use as a building block](README.md#use-as-a-building-block) for a copy-paste example.

## Related blocks

- [Blockchains/fork-sync](https://github.com/Blockchains/fork-sync): keeps every listed fork in sync
- [Blockchains/blockchainlab-index](https://github.com/Blockchains/blockchainlab-index): code index of the same forks (projects[].index links)
- [Blockchains/blockchainlab-starters](https://github.com/Blockchains/blockchainlab-starters): starters built on these forks
- [Blockchains/blockchainlab-compose](https://github.com/Blockchains/blockchainlab-compose): composes projects from them
