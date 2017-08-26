Title: Technical Vision

Photographers use the Japanese word “bokeh” to describe the blurring of the
out-of-focus parts of an image. Its aesthetic quality can greatly enhance a
photograph, and photographers artfully use focus to draw attention to subjects
of interest. “Good bokeh” contributes visual interest to a photograph and
places its subjects in context.  The `bokeh` library was so named
because it allows users the flexibility to focus on the most important
data without losing track of the rich context that allows it to be
understood.

The `bokeh` library is one tangible outcome from a larger project
designed to address fundamental challenges of large dataset
visualization:

##### How do we look at all the data?

  * What are the best perceptual approaches to honestly and accurately represent the data to domain experts and SMEs so they can apply their intuition to the data?
  * Are there automated approaches to accurately reduce large datasets so that outliers and anomalies are still visible, while we meaningfully represent baselines and backgrounds? How can we do this without “washing away” all the interesting bits during a naive downsampling?
  * If we treat the pixels and topology of pixels on a screen as a bottleneck in the I/O channel between hard drives and an analyst’s visual cortex, what are the best compression techniques at all levels of the data transformation pipeline?

##### How can scientists and data analysts be empowered to use visualization fluidly, not merely as an output facility or one stage of a pipeline, but as an entire mode of engagement with data and models?

  * Are language-based approaches for expressing mathematical modeling and data transformations the best way to compose novel interactive graphics?
  * What data-oriented interactions (besides mere linked brushing/selection) are useful for fluid, visually-enable analysis?

Some of these ideas are now implemented in the standalone and complementary
[`datashader`](https://github.com/bokeh/datashader) library, which
works together with Bokeh to render very large datasets faithfully and
flexibly.

The open-source Bokeh and datashader libraries are part of the broader technical vision
of [Anaconda, Inc.](//anaconda.com). By providing powerful data description and vector
computing on remote and distributed data via [Blaze](http://blaze.pydata.org/), [Dask](http://dask.pydata.org/), and [Numba](http://numba.pydata.org), and providing
interactive visualizations of them via Bokeh and datashader, we enable teams to
collaboratively perform rich analysis, share them with others (including
non-technical members of their team or business), and rapidly create analytical
dashboards and monitoring interfaces.

One guiding principle for the development of our visualization tools is to provide useful
software for people, while incorporating novel ideas from the academic world of
visualization research. Additionally, as modular and open-source projects, we
hope that Bokeh and datashader will enable many other projects to build a rich suite of
domain-specific applications that change existing, legacy paradigms of data
processing workflow.
