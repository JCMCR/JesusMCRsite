Jesus College MCR site
====================

This theme is based on the [Agency bootstrap theme ](http://startbootstrap.com/templates/agency/)

# How to use

### Committee members

Change this in the `_config.yaml`. The images go in `image/team`.

### Posts

The 'services', gradcon and 3mt entries are all just posts. Use the categories to tell Jekyll where in the site to put them.

### Font awesome icons

fa icons are used extensively. While usually the fa gives this away, in the `_config.yaml` the contact details icons are also fa iccons with the fa stripped (meaning pretty much anything can be linked to).


# Demo

View this theme in action [here](http://epijim.uk/MCRsite_test)

# Updating the site

**Currently this site is in development and has not been deployed to Zeus**

The site is compiled with Jekyll, and hosted on Zeus (student server).

To update, fork the repo, make changes (and push the changes back), then cd to folder with site, and run `jekyll build`. You will likely have to edit the `_config.yaml` as the source of the code and destination for the compiled site are currently pre-specified. You need ruby and to install some gems to run Jekyll. On unix (osx,linux) this will be `$ gem install jekyll`. Note jekyll and windows don't work well - but guessing this won't be an issue as it's unlikely the webmaster works in windows.

Once compiled - chuck up in the root of the `gradsoc` public folder in zeus.

