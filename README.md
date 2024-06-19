<img src="https://boltframework.dev/assets/bolthead.svg" width="30" height="30">

# bolt-starter-bare

This is the bare starter kit for [Bolt](https://boltframework.dev/),
which includes [`bolt`](https://boltframework.dev/docs/bolt) itself and [`bolt-dev`](https://boltframework.dev/docs/bolt-dev) for easier development.

## Usage

Make your own copy of this repo by cloning it and starting fresh:

```bash
git clone --depth 1 https://github.com/dropseed/bolt-starter-bare new-project
cd new-project
rm -rf .git
git init
```

Then, install the dependencies (note that you'll need [Poetry](https://python-poetry.org/) installed on your system):

```bash
./scripts/install
```

Now you can fire up the development server and open http://localhost:8000 in your browser:

```bash
bolt dev
```
