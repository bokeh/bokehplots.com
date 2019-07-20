
# *** THIS REPOSITORY IS OBSOLETE ***

New landing page is at bokeh.org

# bokehplots.com
Source code for bokeh landing site.

# Getting setup

  `$ conda env create`
  
  `$ source activate bokehplots_com`
  
  `$ npm install`

# Running locally

  `$ ./node_modules/grunt-cli/bin/grunt serve`

Grunt is then watching for changes.

**Edit the scss files not the css.**

# To deploy

Requires [s3cmd](http://s3tools.org/s3cmd-howto) and [optipng](http://optipng.sourceforge.net/) to be installed (both are `brew` installable on OSX) 

  `$ ./node_modules/grunt-cli/bin/grunt deploy` 
    
  `$ s3cmd put -r --force output/* s3://bokehplots.com`
