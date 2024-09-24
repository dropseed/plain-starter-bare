# plain-starter-bare

This is the bare starter kit for [Plain](https://plainframework.com/),
which includes [`plain`](https://plainframework.com/docs/plain) itself and [`plain-dev`](https://plainframework.com/docs/plain-dev) for easier development.

## Usage

Make your own copy of this repo by cloning it and starting fresh:

```bash
git clone --depth 1 https://github.com/dropseed/plain-starter-bare new-project
cd new-project
rm -rf .git
git init
```

Then, install the dependencies (note that you'll need [uv](https://docs.astral.sh/uv/getting-started/installation/) installed on your system):

```bash
./scripts/install
```

Now you can fire up the development server and open http://localhost:8000 in your browser:

```bash
plain dev
```
