Jesus College MCR site
====================

This theme is based on the [Agency bootstrap theme ](https://github.com/IronSummitMedia/startbootstrap-agency)

# How to use

### Committee members

Change this in the `_config.yaml`. The images go in `img/team`.

### Posts

The 'services', gradcon and 3mt entries are all just posts. Use the categories to tell Jekyll where in the site to put them.

### Font awesome icons

fa icons are used extensively. While usually the fa gives this away, in the `_config.yaml` the contact details icons are also fa icons with the fa stripped (meaning pretty much anything can be linked to).


# Live site

View this theme in action [here](https://mcr.jesus.cam.ac.uk)

# Updating the site

The site is compiled with Jekyll, and hosted on Zeus (student server).

#### Big updates

To update, fork the repo, make changes (and push the changes back), then cd to folder with site, and run `jekyll build`. You will likely have to edit the `_config.yaml` as the source of the code and destination for the compiled site are currently pre-specified for James' machine. You need ruby and to install some gems to run Jekyll. On unix (osx,linux) this will be `$ gem install jekyll`. Unsure what a windows workflow would be.

Once compiled, upload to the root of the `gradsoc/public_html` folder in zeus.

This can all be achived by running '_deploy.sh'.

#### Small non-urgent updates

These can be made directly to the github files (so no need to have Jekyll access), but changes won't appear in the site till someone else re-compiles.



