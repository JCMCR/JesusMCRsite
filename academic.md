---
layout: defaultPlain
subtitle: A subsite showcasing previous
title: MCR Academic Events
logoLink: /
menu2: Main Site
menu2Link: /
---

<div class="container">
    <div class="row">
        <div class="col-lg-12 text-center">
            <h2 class="section-heading">Gradcon</h2>
            <h3 class="section-subheading text-muted">Previous Graduate Conferences.</h3>
        </div>
    </div>
    <div class="row">
    {% for post in site.categories.gradcon %}
        <div class="col-md-4 col-sm-6 services-item">
            <div class="services-caption">
                <h4><a href="{{site.url}}{{site.baseurl}}{{ post.url }}">{{ post.title }}</a></h4>
            </div>
        </div>
    {% endfor %}
    </div>
</div>

<div class="container">
    <div class="row">
        <div class="col-lg-12 text-center">
            <h2 class="section-heading">3MT</h2>
            <h3 class="section-subheading text-muted">Previous three minute thesis talks.</h3>
        </div>
    </div>
    <div class="row">
    {% for post in site.categories.3mt %}
        <div class="col-md-4 col-sm-6 services-item">
            <div class="services-caption">
                <h4><a href="{{site.url}}{{site.baseurl}}{{ post.url }}">{{ post.title }}</a></h4>
            </div>
        </div>
    {% endfor %}
    </div>
</div>
