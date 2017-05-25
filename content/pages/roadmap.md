Title: Roadmap

Since the Bokeh project's inception, many of the major goals it set out have
been accomplished, but there is still important work to continue.
In broad strokes, here are the big tasks that we are currently planning to
work on or improve as we move towards a 1.0 release.

### Community

- Define and ratify Project Governance, transition to public meetings
- Create a mechanism to make Bokeh extensions easily sharable, discoverable, and installable

### Technical

#### Core BokehJS improvements

- Migrate BokehJS codebase to [TypeScript](https://www.typescriptlang.org/)
- Increase WebGL capability and support to more areas (e.g patches)
- Support for scripted animations and visual transitions
- Built-in capabilities (or easily usable extensions) for Networks/Graphs/Trees

#### Core Python library

- Add support for integrating with [Altair](//github.com/altair-viz/altair)
- Expand the initial basic theming functionality
- Add a "develop" mode to the Bokeh server
- Better support for map projections

#### Documentation

- Complete docstring coverage for the entire Python library
- Automated reference documentation for BokehJS
- Specific Bokeh server deployment guidance for more scenarios
- Increase the number of examples in the main gallery
- Deploy more demos to [demo.bokehplots.com](//demo.bokehplots.com/)

#### Testing

- Improved unit test coverage to above 95 percent
- Add more Selenium tests to for interactive capabilities
- Require complete tests with all new PRs

### Infrastructure

- Automated Windows CI testing on [Appveyor](//www.appveyor.com)
- Implement code complexity and quality metrics
- Automatically generate reports to maintain API stability


Please [contact us](http://bokehplots.com/pages/contact.html) if you are interested
in contributing to Bokeh.
