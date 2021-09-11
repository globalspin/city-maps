# city-maps

Python-generated detail maps from cities of interest

## Why?

Inspired by https://github.com/marceloprates/prettymaps, these are explorations of places around the world that illustrate interesting city patterns.


## How?

TO DO: Proper dependency management. Oh, Python.

I'm using a Mac, so I needed to get Python and pip up to date, then cover a compiled dependency that the OpenStreetMaps libraries needed, called `libspatialindex`. Luckily Homebrew has a package for it.

```
brew install spatialindex
pip3 install git+https://github.com/abey79/vsketch#egg=vsketch
pip3 install git+https://github.com/marceloprates/prettymaps.git
```
